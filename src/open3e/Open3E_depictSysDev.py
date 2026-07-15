"""
  Copyright 2026 MyHomeMyData

  Licensed under the Apache License, Version 2.0 (the "License");
  you may not use this file except in compliance with the License.
  You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License.
"""

#
# Fast, parallel ECU/DID discovery tool. Development tool, not used by open3e itself.
#
# Produces the same output files as Open3E_depictSystem.py (devices.json,
# Open3Edatapoints_<addr>.py, optionally virtdata_<addr>.txt) using the same UDS
# query method, but scans all addresses/ECUs in parallel instead of sequentially,
# with no artificial sleeps. Open3E_depictSystem.py itself is left untouched since
# the web UI subprocess-invokes it and parses its stdout.
#

import argparse
import binascii
import importlib.util
import json
import logging
import os
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass
from pathlib import Path
from threading import Lock
from typing import Callable, Optional

import udsoncan
from udsoncan.client import Client
from udsoncan.services import ReadDataByIdentifier
from udsoncan.connections import PythonIsoTpConnection

import can
from can.interfaces.socketcan import SocketcanBus
import isotp

from doipclient import DoIPClient
from doipclient.connectors import DoIPClientUDSConnector

from rich.console import Console
from rich.live import Live
from rich.table import Table

import open3e.Open3Edatapoints
import open3e.Open3Eenums


# NOTE: do not use logging.getLogger(__name__) here — this module is also invoked
# via "python -m open3e.Open3E_depictSysDev" (matching how the web UI invokes the
# original tool), which sets __name__ to "__main__" for the running module, not
# "open3e.Open3E_depictSysDev". That would make this logger a sibling of, not a
# child of, the "open3e" logger configured in configure_logging() below, so its
# records would never reach the configured handlers. Use a fixed name instead.
logger = logging.getLogger("open3e.depictSysDev")

DEFAULT_STARTCOB = 0x680
DEFAULT_LASTCOB = 0x6ff
DEFAULT_STARTDID = 256
DEFAULT_LASTDID = 4000
DEFAULT_LOG_FILE = "open3e_depictSysDev.log"
DEFAULT_MAX_WORKERS = 32
DEFAULT_DELAY_MS = 20


# ~~~~~~~~~~~~~~~~~~~~~~ data types ~~~~~~~~~~~~~~~~~~~~~~

@dataclass
class EcuInfo:
    tx: int
    devprop: str


@dataclass
class EcuScanState:
    tx: int
    devprop: str
    dids_queried: int = 0
    dids_found: int = 0
    status: str = "queued"   # queued -> scanning -> done / error
    error: Optional[str] = None


# ~~~~~~~~~~~~~~~~~~~~~~ CAN connection handling ~~~~~~~~~~~~~~~~~~~~~~

def get_isotp_params() -> dict:
    # Refer to isotp documentation for full details about parameters
    return {
        'stmin': 10,
        'blocksize': 0,
        'wftmax': 0,
        'tx_data_length': 8,
        'tx_data_min_length': 8,
        'tx_padding': 0,
        'rx_flowcontrol_timeout': 1000,
        'rx_consecutive_frame_timeout': 1000,
        'override_receiver_stmin': None,
        'max_frame_size': 4095,
        'can_fd': False,
        'bitrate_switch': False,
        'rate_limit_enable': False,
        'rate_limit_max_bitrate': 1000000,
        'rate_limit_window_size': 0.2,
        'listen_mode': False,
    }


class SharedCanContext:
    """One shared SocketcanBus + can.Notifier for all probed/scanned addresses.

    Avoids opening one raw socket per address; isotp.NotifierBasedCanStack
    registers/unregisters itself as a Notifier listener per address pair.
    """

    def __init__(self, channel: str):
        self.bus = SocketcanBus(channel=channel, bitrate=250000)
        self.notifier = can.Notifier(self.bus, listeners=[], timeout=1.0)
        self.channel = channel

    def open_stack(self, ecutx: int, ecurx: int) -> isotp.NotifierBasedCanStack:
        tp_addr = isotp.Address(isotp.AddressingMode.Normal_11bits, txid=ecutx, rxid=ecurx)
        stack = isotp.NotifierBasedCanStack(
            bus=self.bus, notifier=self.notifier, address=tp_addr, params=get_isotp_params()
        )
        return stack

    def close(self):
        self.notifier.stop()
        self.bus.shutdown()


def make_client_config(p2_timeout: Optional[float] = None) -> dict:
    config = dict(udsoncan.configs.default_client_config)
    if p2_timeout is not None:
        config['p2_timeout'] = p2_timeout
    return config


# ~~~~~~~~~~~~~~~~~~~~~~ scan workers ~~~~~~~~~~~~~~~~~~~~~~

def probe_ecu(shared: Optional[SharedCanContext], doip_ip: Optional[str], tx: int,
              e3_devices: dict) -> Optional[EcuInfo]:
    """Probe one ECU address for DID 256 (BusIdentification). Returns EcuInfo if it responds."""
    rx = tx + 0x10
    t0 = time.monotonic()
    try:
        if doip_ip is not None:
            conn = DoIPClientUDSConnector(DoIPClient(doip_ip, tx))
        else:
            stack = shared.open_stack(tx, rx)
            conn = PythonIsoTpConnection(stack)

        config = make_client_config()
        with Client(conn, config=config) as client:
            try:
                response = client.send_request(
                    udsoncan.Request(service=ReadDataByIdentifier, data=(256).to_bytes(2, byteorder='big'))
                )
            except udsoncan.exceptions.TimeoutException:
                logger.debug("probe %s: no response (%.3fs)", hex(tx), time.monotonic() - t0)
                return None

        if not response.positive:
            logger.debug("probe %s: negative response %s", hex(tx), response.code)
            return None
        try:
            iprop = response.data[2 + 2]   # PCI,DL, devprop is 3rd byte of diddata
        except IndexError:
            logger.warning("probe %s: malformed positive response (too short): %r", hex(tx), response.data)
            return None
        devprop = prop_str(iprop, e3_devices)
        logger.info("ECU found: %s : %s (%.3fs)", hex(tx), devprop, time.monotonic() - t0)
        return EcuInfo(tx=tx, devprop=devprop)
    except KeyboardInterrupt:
        raise
    except Exception as e:
        logger.warning("probe %s failed: %s", hex(tx), e)
        return None


def scan_ecu_dids(shared: Optional[SharedCanContext], doip_ip: Optional[str], tx: int,
                   startdid: int, lastdid: int,
                   progress_cb: Callable[[int, int, int], None], delay_ms: int = 0) -> list:
    """Scan DIDs startdid..lastdid on one ECU. Returns list of (did, dlen, data) tuples found.

    delay_ms is a pacing pause between consecutive DID requests, to avoid hammering a
    real ECU with thousands of back-to-back requests while it also runs live control logic.
    """
    rx = tx + 0x10
    lstfounds = []
    try:
        if doip_ip is not None:
            conn = DoIPClientUDSConnector(DoIPClient(doip_ip, tx))
        else:
            stack = shared.open_stack(tx, rx)
            conn = PythonIsoTpConnection(stack)

        config = make_client_config(p2_timeout=3)
        with Client(conn, config=config) as client:
            for did in range(startdid, lastdid + 1):
                t0 = time.monotonic()
                try:
                    response = client.send_request(
                        udsoncan.Request(service=ReadDataByIdentifier, data=did.to_bytes(2, byteorder='big'))
                    )
                    if response.positive:
                        dlen = len(response) - 3
                        if dlen > 0:
                            data = response.data[2:]
                            lstfounds.append((did, dlen, data))
                            logger.debug("DID %s/%d: found len=%d (%.3fs)", hex(tx), did, dlen, time.monotonic() - t0)
                        else:
                            # positive response with no payload: treat like "not present"
                            logger.debug("DID %s/%d: empty positive response, treated as not present (%.3fs)",
                                         hex(tx), did, time.monotonic() - t0)
                except udsoncan.exceptions.NegativeResponseException:
                    logger.debug("DID %s/%d: not present (%.3fs)", hex(tx), did, time.monotonic() - t0)
                except KeyboardInterrupt:
                    raise
                except Exception as e:
                    logger.warning("DID %s/%d: error %s", hex(tx), did, e)
                progress_cb(tx, did - startdid + 1, len(lstfounds))
                if delay_ms > 0:
                    time.sleep(delay_ms / 1000.0)
    except KeyboardInterrupt:
        raise
    except Exception as e:
        logger.error("ECU %s: scan setup failed: %s", hex(tx), e)
        return []
    logger.info("%d DIDs found on %s.", len(lstfounds), hex(tx))
    return lstfounds


# ~~~~~~~~~~~~~~~~~~~~~~ orchestration ~~~~~~~~~~~~~~~~~~~~~~

def run_discovery(startcob: int, lastcob: int, shared: Optional[SharedCanContext],
                   doip_ip: Optional[str], workers: int, e3_devices: dict,
                   status_cb: Optional[Callable[[int, int], None]] = None) -> list:
    addrs = list(range(startcob, lastcob + 1))
    found = []
    done_count = 0
    with ThreadPoolExecutor(max_workers=workers, thread_name_prefix="probe") as ex:
        futures = {ex.submit(probe_ecu, shared, doip_ip, tx, e3_devices): tx for tx in addrs}
        for fut in as_completed(futures):
            info = fut.result()
            done_count += 1
            if info is not None:
                found.append(info)
            if status_cb is not None:
                status_cb(done_count, len(addrs))
    found.sort(key=lambda e: e.tx)
    return found


def run_did_scans(ecus: list, shared: Optional[SharedCanContext], doip_ip: Optional[str],
                   startdid: int, lastdid: int, workers: int, dashboard: "DepictDashboard",
                   delay_ms: int = 0) -> dict:
    results = {}
    with ThreadPoolExecutor(max_workers=workers, thread_name_prefix="didscan") as ex:
        futures = {
            ex.submit(scan_ecu_dids, shared, doip_ip, e.tx, startdid, lastdid,
                      dashboard.make_callback(e.tx), delay_ms): e
            for e in ecus
        }
        for fut in as_completed(futures):
            e = futures[fut]
            try:
                results[e.tx] = fut.result()
                dashboard.mark_done(e.tx)
            except KeyboardInterrupt:
                raise
    return results


# ~~~~~~~~~~~~~~~~~~~~~~ dashboard ~~~~~~~~~~~~~~~~~~~~~~

class DepictDashboard:
    """Thread-safe sink for per-ECU scan progress, rendered as a rich table.

    Worker threads only call the closures returned by make_callback()/mark_done(),
    which update a lock-protected dict. render() (called only from rich.Live's own
    refresh) snapshots that state and builds the Table.
    """

    def __init__(self):
        self._lock = Lock()
        self._rows: dict = {}

    def add_ecu(self, tx: int, devprop: str):
        with self._lock:
            self._rows[tx] = EcuScanState(tx=tx, devprop=devprop)

    def make_callback(self, tx: int) -> Callable[[int, int, int], None]:
        def _cb(addr: int, queried: int, found: int):
            with self._lock:
                row = self._rows.get(addr)
                if row is not None:
                    row.dids_queried = queried
                    row.dids_found = found
                    row.status = "scanning"
        return _cb

    def mark_done(self, tx: int):
        with self._lock:
            row = self._rows.get(tx)
            if row is not None:
                row.status = "done"

    def render(self) -> Table:
        with self._lock:
            rows_snapshot = list(self._rows.values())
        table = Table(title="ECU DID scan")
        table.add_column("Address")
        table.add_column("Device")
        table.add_column("Queried", justify="right")
        table.add_column("Found", justify="right")
        table.add_column("Status")
        for r in sorted(rows_snapshot, key=lambda x: x.tx):
            table.add_row(hex(r.tx), r.devprop, str(r.dids_queried), str(r.dids_found), r.error or r.status)
        return table

    def live(self, console: Console) -> Live:
        return Live(self.render(), console=console, refresh_per_second=4, get_renderable=self.render)


def print_summary(console: Console, ecus: list, results: dict, elapsed: float):
    total_dids = sum(len(v) for v in results.values())
    table = Table(title="Summary")
    table.add_column("Metric")
    table.add_column("Value")
    table.add_row("Devices found", str(len(ecus)))
    table.add_row("Total DIDs found", str(total_dids))
    table.add_row("Elapsed time", f"{elapsed:.1f}s")
    console.print(table)


# ~~~~~~~~~~~~~~~~~~~~~~ utils ~~~~~~~~~~~~~~~~~~~~~~

def did_info(did: int, data_identifiers: dict, did_enums: dict) -> tuple:
    if did in data_identifiers:
        didlen = vars(data_identifiers[did])['string_len']
        idstr = vars(data_identifiers[did])['id']
        return (didlen, idstr)
    elif did in did_enums:
        return (0, did_enums[did])
    else:
        return (0, "Unknown")


def prop_str(devprop: int, e3_devices: dict) -> str:
    if devprop in e3_devices:
        return e3_devices[devprop]
    else:
        return str(devprop)


def shex(nbr: int) -> str:
    return format(nbr, '03x')


def read_didenums(path) -> dict:
    dicenums = {}
    lines = []
    logger.info("read DID enums ...")
    try:
        with open(path, 'r') as file:
            lines = file.readlines()
    except Exception as ex:
        logger.warning("could not read DID enums file %s: %s", path, ex)

    for line in lines:
        line = line.strip()
        if line:
            parts = line.split('(')
            if len(parts) == 2:
                name = parts[0].strip()
                num_str = parts[1].split(')')[0].strip()
                try:
                    num = int(num_str)
                    dicenums[num] = name
                except ValueError:
                    logger.debug("could not parse '%s' as an integer", num_str)
    logger.info("%d DIDs listed.", len(dicenums))
    return dicenums


def get_variants_dict(o3e_path) -> dict:
    module_name = "Open3EdatapointsVariants"
    source = Path(o3e_path, f"{module_name}.py")
    if not source.is_file():
        logger.info("no codec variants - %s.py not found", module_name)
        return {}
    try:
        spec = importlib.util.spec_from_file_location(module_name, source)
        variants_temp = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(variants_temp)
        return variants_temp.dataIdentifiers["dids"]
    except Exception as e:
        logger.error("ERROR getting DID variants: %s", e)
        return {}


# ~~~~~~~~~~~~~~~~~~~~~~ file writers ~~~~~~~~~~~~~~~~~~~~~~

def write_devices_json(ecus: list, path: str = 'devices.json'):
    logger.info("write %s ...", path)
    result_dict = {}
    for ecu in sorted(ecus, key=lambda e: e.tx):
        scob = hex(ecu.tx)
        sdplist = "Open3Edatapoints_" + shex(ecu.tx) + ".py"
        result_dict[scob] = {'tx': scob, 'dpList': sdplist, 'prop': ecu.devprop}
    with open(path, 'w') as json_file:
        json.dump(result_dict, json_file, indent=2)
    logger.info("done.")


def write_simul_datafile(lstdids: list, cobid: int, devprop: str, outdir: str = '.'):
    filename = os.path.join(outdir, "virtdata_" + shex(cobid) + ".txt")
    logger.info("write simulation data file %s ...", filename)
    with open(filename, "w") as file:
        file.write(f"# {hex(cobid)}:{devprop}\n")
        for did, dlen, data in lstdids:
            sdata = binascii.hexlify(data).decode('utf-8')
            file.write(str(did) + " " + sdata + "\n")
    logger.info("done.")


def write_datapoints_file(lstdids: list, cobid: int, devprop: str, dicvariants: dict,
                           data_identifiers: dict, did_enums: dict, outdir: str = '.'):
    filename = os.path.join(outdir, "Open3Edatapoints_" + shex(cobid) + ".py")
    logger.info("write datapoints file %s ...", filename)
    with open(filename, "w") as file:
        shead = 'from open3e.Open3Ecodecs import *\n\n'
        shead += 'dataIdentifiers = {\n'
        shead += '    \"name\": \"' + str(devprop) + '\",\n'
        shead += '    \"dids\" :\n'
        shead += '    {\n'
        file.write(shead)
        for did, dlen, data in lstdids:
            sline = '        ' + str(did) + " : "
            genlen, idstr = did_info(did, data_identifiers, did_enums)
            if dlen == genlen:
                sline += 'None,'
            elif (varitem := dicvariants.get(did, {}).get(dlen)):
                sline += varitem.getCodecString() + ','
            else:
                sline += 'RawCodec(' + str(dlen) + ', \"' + idstr + '\"),'
            file.write(sline + '\n')
        file.write('    }\n')
        file.write('}\n')
    logger.info("done.")


# ~~~~~~~~~~~~~~~~~~~~~~ logging setup ~~~~~~~~~~~~~~~~~~~~~~

def configure_logging(log_level: str, log_file: str):
    root = logging.getLogger("open3e")
    root.setLevel(logging.DEBUG)

    file_handler = logging.FileHandler(log_file, mode='w')
    file_handler.setLevel(getattr(logging, log_level.upper(), logging.INFO))
    file_handler.setFormatter(logging.Formatter("%(asctime)s %(name)s %(levelname)s %(message)s"))
    root.addHandler(file_handler)

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.WARNING)
    stream_handler.setFormatter(logging.Formatter("%(levelname)s %(message)s"))
    root.addHandler(stream_handler)

    # The isotp library logs under its own "isotp" logger (e.g. stray
    # ConsecutiveFrame warnings), unrelated to our "open3e" hierarchy above.
    # Without any handler attached anywhere in its ancestor chain, Python's
    # logging.lastResort prints such records straight to stderr, which
    # corrupts the rich Live dashboard. Route them into our log file instead.
    isotp_logger = logging.getLogger("isotp")
    isotp_logger.setLevel(logging.DEBUG)
    isotp_logger.addHandler(file_handler)
    isotp_logger.propagate = False


# ~~~~~~~~~~~~~~~~~~~~~~ CLI ~~~~~~~~~~~~~~~~~~~~~~

def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="open3e_depictSysDev")
    conn_group = parser.add_mutually_exclusive_group()
    conn_group.add_argument("-c", "--can", type=str, default=None, help="use CAN device, e.g. can0 (default: can0)")
    conn_group.add_argument("-d", "--doip", type=str, default=None, help="use DoIP access, e.g. 192.168.1.1")
    parser.add_argument("-s", "--simul", action='store_true', help="write simulation data files")
    parser.add_argument("--workers", type=int, default=None,
                         help="max concurrent scan threads (default: min(%d, address-range-size) for discovery; "
                              "min(workers, #ECUs found) for DID scan)" % DEFAULT_MAX_WORKERS)
    parser.add_argument("--delay-ms", type=int, default=DEFAULT_DELAY_MS,
                         help="pause in ms between consecutive DID requests within one ECU's scan, to avoid "
                              "flooding a real ECU's diagnostic handling (default: %d, use 0 to disable)"
                              % DEFAULT_DELAY_MS)
    parser.add_argument("--startcob", type=lambda x: int(x, 0), default=DEFAULT_STARTCOB, help=argparse.SUPPRESS)
    parser.add_argument("--lastcob", type=lambda x: int(x, 0), default=DEFAULT_LASTCOB, help=argparse.SUPPRESS)
    parser.add_argument("--startdid", type=int, default=DEFAULT_STARTDID, help=argparse.SUPPRESS)
    parser.add_argument("--lastdid", type=int, default=DEFAULT_LASTDID, help=argparse.SUPPRESS)
    parser.add_argument("--log-level", type=str, default="INFO",
                         choices=["DEBUG", "INFO", "WARNING", "ERROR"], help="file log verbosity (default: INFO)")
    parser.add_argument("--log-file", type=str, default=DEFAULT_LOG_FILE,
                         help=f"log file path (default: {DEFAULT_LOG_FILE} in CWD)")
    return parser


def main(argv=None):
    args = build_arg_parser().parse_args(argv)
    configure_logging(args.log_level, args.log_file)

    can_channel = args.can if args.can is not None else "can0"
    doip_ip = args.doip

    console = Console()
    t_start = time.monotonic()

    # ++ preparations +++++++
    data_identifiers = dict(open3e.Open3Edatapoints.dataIdentifiers["dids"])
    e3_devices = open3e.Open3Eenums.E3Enums['Devices']

    open3e_path = os.path.split(open3e.Open3Eenums.__file__)[0]
    did_enums = read_didenums(os.path.join(open3e_path, "DidEnums.txt"))
    did_variants = get_variants_dict(open3e_path)

    shared = SharedCanContext(can_channel) if doip_ip is None else None
    try:
        discovery_workers = args.workers if args.workers else min(DEFAULT_MAX_WORKERS,
                                                                    args.lastcob - args.startcob + 1)

        with console.status(f"Scanning COB-IDs {hex(args.startcob)} to {hex(args.lastcob)} ...") as status:
            def _discovery_status(done, total):
                status.update(f"Scanning COB-IDs {hex(args.startcob)} to {hex(args.lastcob)} ... ({done}/{total})")
            ecus = run_discovery(args.startcob, args.lastcob, shared, doip_ip, discovery_workers,
                                  e3_devices, status_cb=_discovery_status)

        console.print(f"{len(ecus)} responding ECUs found.")

        # devices.json reflects discovery results only, written before DID scan
        # (matches Open3E_depictSystem.py's behavior/timing)
        write_devices_json(ecus)

        did_workers = args.workers if args.workers else min(DEFAULT_MAX_WORKERS, max(len(ecus), 1))

        dashboard = DepictDashboard()
        for e in ecus:
            dashboard.add_ecu(e.tx, e.devprop)

        with dashboard.live(console):
            results = run_did_scans(ecus, shared, doip_ip, args.startdid, args.lastdid, did_workers, dashboard,
                                     delay_ms=args.delay_ms)

        for e in ecus:
            lstdids = results.get(e.tx, [])
            if args.simul:
                write_simul_datafile(lstdids, e.tx, e.devprop)
            write_datapoints_file(lstdids, e.tx, e.devprop, did_variants, data_identifiers, did_enums)

        elapsed = time.monotonic() - t_start
        print_summary(console, ecus, results, elapsed)
    finally:
        if shared is not None:
            shared.close()


if __name__ == "__main__":
    main()
