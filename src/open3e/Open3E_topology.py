"""
open3e_topology – read E3 bus topology from known devices and produce reports.

Data collection reads DID 256 (BusIdentification) and the topology matrix DIDs
defined in topology_analysis.TOPOLOGY_DIDS from every device listed in a
devices.json file.  Only DIDs that have a proper (non-Raw) codec in the device's
dataIdentifiers are read; others are silently skipped.

Output options:
  stdout      text table (default) or JSON (--json)
  -o STEM     write STEM.json + STEM.html

MQTT publishing is not yet implemented but the result dict returned by
build_topology_summary() is ready to be serialised and published.
"""

import argparse
import json
import os
import sys

import open3e.Open3Eclass
from open3e.Open3Ecodecs import RawCodec
from open3e.topology_analysis import TOPOLOGY_DIDS, build_topology_summary

_BUS_ID_DID = 256

_USAGE_HINT = (
    'Usage examples:\n'
    '  open3e_topology -c can0  -devices devices.json\n'
    '  open3e_topology -c can0  -devices devices.json -o topology -v\n'
    '  open3e_topology -c can0  -devices devices.json --json | jq .udsDevices\n'
    '  open3e_topology -d 192.168.1.1 -devices devices.json -o topology\n'
    '\n'
    'devices.json must be a JSON object with one entry per device:\n'
    '  {\n'
    '    "0x680": { "tx": "0x680", "dpList": "Open3Edatapoints_680.py", "prop": "HPMUMASTER" },\n'
    '    ...\n'
    '  }\n'
    'dpList paths are resolved relative to the devices.json directory.'
)


# ── devices.json loading ──────────────────────────────────────────────────────

def _load_devices(path: str) -> dict:
    if not os.path.exists(path):
        print(f"Error: devices file '{path}' not found.\n\n{_USAGE_HINT}", file=sys.stderr)
        sys.exit(1)

    try:
        with open(path) as f:
            devices = json.load(f)
    except json.JSONDecodeError as e:
        print(f"Error: cannot parse '{path}': {e}\n\n{_USAGE_HINT}", file=sys.stderr)
        sys.exit(1)

    if not isinstance(devices, dict) or not devices:
        print(f"Error: '{path}' contains no device entries.\n\n{_USAGE_HINT}", file=sys.stderr)
        sys.exit(1)

    for addr, dev in devices.items():
        if not isinstance(dev, dict) or 'tx' not in dev or 'dpList' not in dev:
            print(
                f"Error: entry '{addr}' in '{path}' is missing 'tx' or 'dpList'.\n\n{_USAGE_HINT}",
                file=sys.stderr,
            )
            sys.exit(1)

    return devices


def _resolve_dp_list(dp_list: str, devices_dir: str) -> str:
    if os.path.isabs(dp_list):
        return dp_list
    return os.path.join(devices_dir, dp_list)


# ── data collection ───────────────────────────────────────────────────────────

def _collect(devices: dict, devices_dir: str, args: argparse.Namespace, verbose: bool) -> dict:
    """Read BusIdentification and topology matrix DIDs from all listed devices."""
    topology_data = {}

    for can_addr, dev_cfg in devices.items():
        tx      = int(dev_cfg['tx'], 16)
        dp_list = _resolve_dp_list(dev_cfg['dpList'], devices_dir)
        prop    = dev_cfg.get('prop', '?')

        if verbose:
            print(f"  {can_addr} ({prop}) ... ", end='', flush=True)

        try:
            ecu = open3e.Open3Eclass.O3Eclass(
                ecutx=tx,
                can=args.can,
                doip=args.doip,
                dev=dp_list,
            )
        except Exception as e:
            if verbose:
                print(f"connection failed: {e}")
            continue

        # DID 256 – BusIdentification (always has a real codec in global datapoints)
        bus_id = None
        try:
            bus_id, _ = ecu._readByDid(_BUS_ID_DID, raw=False)
        except Exception:
            pass

        # Topology matrix DIDs – only those with a proper (non-Raw) codec
        matrices = []
        for did in sorted(TOPOLOGY_DIDS):
            codec = ecu.dataIdentifiers.get(did)
            if codec is None or isinstance(codec, RawCodec):
                continue
            try:
                val, _ = ecu._readByDid(did, raw=False)
                if isinstance(val, dict) and val.get('Count', 0) > 0:
                    matrices.append(val)
            except Exception:
                pass

        if bus_id is not None or matrices:
            topology_data[can_addr] = {
                'can_addr': can_addr,
                'bus_id':   bus_id,
                'matrices': matrices,
            }

        if verbose:
            n = sum(m.get('Count', 0) for m in matrices)
            plural = 'matrix' if len(matrices) == 1 else 'matrices'
            print(f"bus_id={'ok' if bus_id else 'n/a'}, {len(matrices)} {plural}, {n} elements")

    return topology_data


# ── entry point ───────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        prog='open3e_topology',
        description='Read E3 bus topology from known devices and produce JSON / HTML / text reports.',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=_USAGE_HINT,
    )

    conn = parser.add_mutually_exclusive_group(required=True)
    conn.add_argument('-c', '--can',  type=str, metavar='IFACE',
                      help='CAN interface, e.g. can0')
    conn.add_argument('-d', '--doip', type=str, metavar='IP',
                      help='DoIP IP address, e.g. 192.168.1.1')

    parser.add_argument('-devices', type=str, required=True, metavar='FILE',
                        help='Path to devices.json')
    parser.add_argument('-o', '--output', type=str, metavar='STEM',
                        help='Write STEM.json and STEM.html')
    parser.add_argument('--json', action='store_true',
                        help='Print JSON to stdout (instead of text table)')
    parser.add_argument('-v', '--verbose', action='store_true',
                        help='Show progress during data collection')

    args = parser.parse_args()

    devices     = _load_devices(args.devices)
    devices_dir = os.path.dirname(os.path.abspath(args.devices))

    if args.verbose:
        print(f"Collecting topology data from {len(devices)} device(s):")

    topology_data = _collect(devices, devices_dir, args, verbose=args.verbose)

    if not topology_data:
        print("No topology data collected — no devices responded.", file=sys.stderr)
        sys.exit(1)

    result = build_topology_summary(topology_data)

    # ── stdout ────────────────────────────────────────────────────────────────
    if args.json:
        print(json.dumps(result['json'], indent=2))
    else:
        print(result['text'])

    # ── file output ───────────────────────────────────────────────────────────
    if args.output:
        stem      = args.output
        json_path = f"{stem}.json"
        html_path = f"{stem}.html"

        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(result['json'], f, indent=2)
        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(result['html'])

        # When --json is active, stdout carries JSON → file notice goes to stderr
        out = sys.stderr if args.json else sys.stdout
        print(f"Written: {json_path}, {html_path}", file=out)


if __name__ == '__main__':
    main()
