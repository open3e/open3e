"""CAN engine with priority scheduler and command queue.

This module provides a CanEngine that runs ALL CAN/UDS communication in a
single dedicated background thread.  The web server communicates with it
exclusively through:

  - ``send_command(cmd)``  — web → engine (thread-safe queue)
  - ``on_data(msg)``       — engine → web (callback, never blocks engine)

The existing O3Eclass uses module-level global flags in Open3Ecodecs that are
NOT thread-safe; serialising every access through one thread makes it safe.
"""

from __future__ import annotations

import logging
import os
import queue
import subprocess
import threading
from enum import Enum
from typing import Any, Callable, Dict, List, Optional

logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Public constants (also importable by tests)
# ---------------------------------------------------------------------------

CYCLE_LENGTH: int = 12
MEDIUM_INTERVAL: int = 4
LOW_INTERVAL: int = 12
INTER_DID_DELAY: float = 0.05  # 50ms between UDS requests to avoid CAN bus saturation


# ---------------------------------------------------------------------------
# EngineState
# ---------------------------------------------------------------------------

class EngineState(Enum):
    IDLE = "idle"
    CONNECTING = "connecting"
    POLLING = "polling"
    PAUSED = "paused"
    EXECUTING_COMMAND = "executing_command"


# ---------------------------------------------------------------------------
# CanEngine
# ---------------------------------------------------------------------------

class CanEngine:
    """CAN communication engine that serialises all O3Eclass access.

    Parameters
    ----------
    store:
        ConfigStore reference (used to persist last values, etc.).
    on_data:
        Optional callback ``on_data(msg: dict)`` invoked by the engine
        thread whenever new data or state change messages are available.
        The callback must be non-blocking (the engine will not wait for it).
    """

    # -- class-level constants (also accessible via module) ------------------
    CYCLE_LENGTH = CYCLE_LENGTH
    MEDIUM_INTERVAL = MEDIUM_INTERVAL
    LOW_INTERVAL = LOW_INTERVAL
    INTER_DID_DELAY = INTER_DID_DELAY

    def __init__(self, store, on_data: Optional[Callable[[Dict], None]] = None):
        self._store = store
        self._on_data = on_data

        # Command queue: web → engine
        self._cmd_queue: queue.Queue = queue.Queue()

        # State protected by a lock
        self._state_lock = threading.Lock()
        self._state: EngineState = EngineState.IDLE

        # Runtime data
        self._ecus: Dict[int, Any] = {}           # address → O3Eclass instance
        self._datapoints: Dict[int, Dict] = {}    # dp_id  → datapoint dict
        self._last_values: Dict[str, Any] = {}    # "ecu:did" → last decoded value

        # Engine control
        self._running: bool = False
        self._thread: Optional[threading.Thread] = None
        self._poll_interval: float = 10.0  # seconds between poll cycles (default 10)
        self._cycle: int = 0

        # Depiction subprocess support
        self._depict_proc: Optional[subprocess.Popen] = None
        self._depict_lock = threading.Lock()
        self._depict_log: list[str] = []
        self._depict_returncode: Optional[int] = None

    # -----------------------------------------------------------------------
    # State property
    # -----------------------------------------------------------------------

    @property
    def state(self) -> EngineState:
        """Return current engine state (thread-safe read)."""
        with self._state_lock:
            return self._state

    def _set_state(self, state: EngineState) -> None:
        """Set engine state and emit an engine_state message."""
        with self._state_lock:
            prev = self._state
            self._state = state
        # Only broadcast meaningful state changes (skip transient EXECUTING_COMMAND)
        if state != EngineState.EXECUTING_COMMAND and state != prev:
            self._emit_data({"type": "engine_state", "state": state.value})

    # -----------------------------------------------------------------------
    # Data emission
    # -----------------------------------------------------------------------

    def _emit_data(self, msg: Dict) -> None:
        """Deliver *msg* to the on_data callback (if set)."""
        if self._on_data is not None:
            try:
                self._on_data(msg)
            except Exception:
                # Never let a misbehaving callback crash the engine
                pass

    # -----------------------------------------------------------------------
    # Command queue
    # -----------------------------------------------------------------------

    def send_command(self, cmd: Dict) -> None:
        """Enqueue *cmd* for the engine thread to process (thread-safe)."""
        self._cmd_queue.put(cmd)

    # -----------------------------------------------------------------------
    # Value cache
    # -----------------------------------------------------------------------

    def get_last_value(self, ecu: int, did: int) -> Any:
        """Return the most-recently cached decoded value for *ecu*/*did*."""
        return self._last_values.get(f"{ecu}:{did}")

    # -----------------------------------------------------------------------
    # Priority scheduler
    # -----------------------------------------------------------------------

    def _build_poll_list(self, cycle: int) -> List[Dict]:
        """Return the list of datapoint dicts to poll on *cycle*.

        Priority tiers
        ~~~~~~~~~~~~~~
        3 (high)   — polled every cycle
        2 (medium) — polled every MEDIUM_INTERVAL cycles (cycle % MEDIUM_INTERVAL == 0)
        1 (low)    — polled every LOW_INTERVAL cycles (cycle % LOW_INTERVAL == 0)
        0/disabled — never polled
        """
        poll = []
        include_medium = (cycle % MEDIUM_INTERVAL == 0)
        include_low = (cycle % LOW_INTERVAL == 0)

        for dp in self._datapoints.values():
            if not dp.get("poll_enabled", 1):
                continue
            priority = dp.get("poll_priority", 1)
            if priority == 3:
                poll.append(dp)
            elif priority == 2 and include_medium:
                poll.append(dp)
            elif priority == 1 and include_low:
                poll.append(dp)
            # priority == 0 or unknown → skip

        return poll

    # -----------------------------------------------------------------------
    # Lifecycle: start / stop
    # -----------------------------------------------------------------------

    def start(
        self,
        can_interface: str,
        can_bitrate: int,
        datapoints: Dict[int, Dict],
        ecus: List[Dict],
        poll_interval: float = 10.0,
    ) -> None:
        """Start the engine background thread."""
        if self._running:
            return

        self._running = True
        self._datapoints = dict(datapoints)
        self._poll_interval = max(1.0, float(poll_interval))

        self._thread = threading.Thread(
            target=self._run,
            args=(can_interface, can_bitrate, ecus),
            daemon=True,
            name="CanEngine",
        )
        self._thread.start()

    def stop(self) -> None:
        """Signal the engine to stop and wait for the thread to exit."""
        self._running = False
        self._cmd_queue.put({"type": "stop"})
        if self._thread is not None:
            self._thread.join(timeout=10)
            self._thread = None

    # -----------------------------------------------------------------------
    # Main engine loop
    # -----------------------------------------------------------------------

    def _run(self, can_interface: str, can_bitrate: int, ecus: List[Dict]) -> None:
        """Main engine loop — runs in the background daemon thread."""
        import time

        try:
            self._set_state(EngineState.CONNECTING)
            self._connect_ecus(can_interface, ecus)
            self._set_state(EngineState.POLLING)

            while self._running:
                # Check for pending commands first
                if self._process_commands():
                    break  # stop command received

                if self._state == EngineState.PAUSED:
                    time.sleep(0.1)
                    continue

                # Build the poll list for this cycle
                poll_list = self._build_poll_list(self._cycle)

                for dp in poll_list:
                    if not self._running:
                        break

                    # Check commands between every DID read
                    if self._process_commands():
                        self._cleanup()
                        return

                    if self._state == EngineState.PAUSED:
                        break

                    self._poll_did(dp)
                    time.sleep(INTER_DID_DELAY)

                self._cycle = (self._cycle + 1) % CYCLE_LENGTH

                # Pause between cycles — sleep in small increments to stay responsive to commands
                wait_until = time.time() + self._poll_interval
                while self._running and time.time() < wait_until:
                    if self._process_commands():
                        self._cleanup()
                        return
                    time.sleep(0.1)

        except Exception as exc:
            logger.error("Engine thread crashed: %s", exc, exc_info=True)
            self._emit_data({"type": "engine_error", "error": str(exc)})
        finally:
            logger.info("Engine thread exiting, running=%s", self._running)
            self._cleanup()
            self._set_state(EngineState.IDLE)

    def _connect_ecus(self, can_interface: str, ecus: List[Dict]) -> None:
        """Instantiate O3Eclass for each ECU in *ecus*."""
        from open3e.Open3Eclass import O3Eclass

        for ecu in ecus:
            address = ecu["address"]
            # O3Eclass expects dev= to be the datapoints file path (e.g., "Open3Edatapoints_680.py")
            dev = ecu.get("dp_list") or None
            try:
                o3e = O3Eclass(
                    ecutx=address,
                    can=can_interface,
                    dev=dev,
                )
                self._ecus[address] = o3e
                self._emit_data({"type": "ecu_connected", "ecu": address})
            except Exception as exc:
                self._emit_data({
                    "type": "ecu_error",
                    "ecu": address,
                    "error": str(exc),
                })

    def _poll_did(self, dp: Dict) -> None:
        """Read a single DID from its ECU and cache/emit the result."""
        ecu_addr = dp["ecu_address"]
        did = dp["did"]

        o3e = self._ecus.get(ecu_addr)
        if o3e is None:
            logger.warning("No ECU connection for address %s (did %s), connected ECUs: %s", ecu_addr, did, list(self._ecus.keys()))
            return

        try:
            value, idstr, _ = o3e.readByDid(did, raw=False)
            # Skip error strings from UDS exceptions (UnexpectedResponseException etc.)
            if isinstance(value, str) and ("service execution" in value or "ERR/" in idstr):
                return  # silently skip — will retry next cycle
            cache_key = f"{ecu_addr}:{did}"
            old_entry = self._last_values.get(cache_key)
            import time as _time
            now = int(_time.time())

            if old_entry is None:
                # First read — always publish
                changed = True
            elif old_entry.get("value") != value:
                # Value changed
                changed = True
            elif now - old_entry.get("ts", 0) >= 60:
                # Unchanged but 60 seconds since last publish — re-publish
                changed = True
            else:
                changed = False

            self._last_values[cache_key] = {"value": value, "ts": now}
            self._emit_data({
                "type": "did_value",
                "ecu": ecu_addr,
                "did": did,
                "name": dp.get("name", idstr),
                "value": value,
                "ts": now,
                "changed": changed,
            })
        except Exception as exc:
            self._emit_data({
                "type": "did_error",
                "ecu": ecu_addr,
                "did": did,
                "error": str(exc),
            })

    # -----------------------------------------------------------------------
    # Command processing
    # -----------------------------------------------------------------------

    def _process_commands(self) -> bool:
        """Drain pending commands.  Returns True if a *stop* was received."""
        while True:
            try:
                cmd = self._cmd_queue.get_nowait()
            except queue.Empty:
                return False

            cmd_type = cmd.get("action") or cmd.get("type")

            if cmd_type == "stop":
                return True
            elif cmd_type == "pause":
                self._set_state(EngineState.PAUSED)
            elif cmd_type == "resume":
                if self._state == EngineState.PAUSED:
                    self._set_state(EngineState.POLLING)
            elif cmd_type == "read_did":
                self._handle_read(cmd)
            elif cmd_type == "write_did":
                self._handle_write(cmd)
            elif cmd_type == "update_schedule":
                self._handle_update_schedule(cmd)

        # unreachable, but keeps linters happy
        return False  # pragma: no cover

    def _handle_read(self, cmd: Dict) -> None:
        """Execute an on-demand single DID read."""
        prev_state = self.state
        self._set_state(EngineState.EXECUTING_COMMAND)

        ecu_addr = cmd.get("ecu")
        did = cmd.get("did")
        o3e = self._ecus.get(ecu_addr)

        if o3e is None:
            self._emit_data({"type": "cmd_error", "cmd": cmd, "error": "ECU not connected"})
        else:
            try:
                value, idstr, _ = o3e.readByDid(did, raw=cmd.get("raw", False))
                self._last_values[f"{ecu_addr}:{did}"] = value
                self._emit_data({
                    "type": "did_value",
                    "ecu": ecu_addr,
                    "did": did,
                    "name": idstr,
                    "value": value,
                    "on_demand": True,
                })
            except Exception as exc:
                self._emit_data({"type": "cmd_error", "cmd": cmd, "error": str(exc)})

        self._set_state(prev_state)

    def _handle_write(self, cmd: Dict) -> None:
        """Execute a DID write via O3Eclass.writeByDid."""
        import time as _time
        prev_state = self.state
        self._set_state(EngineState.EXECUTING_COMMAND)

        ecu_addr = cmd.get("ecu")
        did = cmd.get("did")
        val = cmd.get("value")
        raw = cmd.get("raw", False)
        sub = cmd.get("sub")
        result_event = cmd.get("_result_event")  # threading.Event for sync callers
        result_holder = cmd.get("_result_holder")  # dict to store result
        o3e = self._ecus.get(ecu_addr)

        result = {"type": "write_result", "ecu": ecu_addr, "did": did,
                  "success": False, "error": None, "new_value": None}

        if o3e is None:
            result["error"] = "ECU not connected"
        else:
            _time.sleep(0.1)
            try:
                succ, code = o3e.writeByDid(did, val, raw, sub=sub)
                logger.info("Write DID %s on ECU %s: val=%s success=%s code=%s",
                            did, hex(ecu_addr), val, succ, code)
                result["success"] = succ
                result["code"] = str(code)
                # Read back the value to confirm
                _time.sleep(0.05)
                try:
                    new_val, idstr, _ = o3e.readByDid(did, raw=False)
                    result["new_value"] = new_val
                    cache_key = f"{ecu_addr}:{did}"
                    self._last_values[cache_key] = {"value": new_val, "ts": int(_time.time())}
                    self._emit_data({
                        "type": "did_value", "ecu": ecu_addr, "did": did,
                        "name": idstr, "value": new_val, "ts": int(_time.time()),
                        "changed": True,
                    })
                except Exception:
                    pass  # read-back failed, not critical
            except Exception as exc:
                logger.error("Write failed DID %s on ECU %s: %s", did, hex(ecu_addr), exc)
                result["error"] = str(exc)

        # Emit via WebSocket (for any listening clients)
        self._emit_data(result)

        # Signal synchronous caller if present
        if result_holder is not None:
            result_holder.update(result)
        if result_event is not None:
            result_event.set()

        self._set_state(prev_state)

    def _handle_update_schedule(self, cmd: Dict) -> None:
        """Replace the datapoints configuration (update polling schedule)."""
        new_datapoints = cmd.get("datapoints", {})
        self._datapoints = dict(new_datapoints)
        # Update poll interval if provided
        if "poll_interval" in cmd:
            self._poll_interval = max(1.0, float(cmd["poll_interval"]))
        active = [dp for dp in self._datapoints.values() if dp.get("poll_enabled") and dp.get("poll_priority", 0) > 0]
        logger.info("Schedule updated: %d total, %d active, interval=%.1fs",
                     len(self._datapoints), len(active), self._poll_interval)
        self._emit_data({"type": "schedule_updated", "count": len(self._datapoints)})

    # -----------------------------------------------------------------------
    # Cleanup
    # -----------------------------------------------------------------------

    def _cleanup(self) -> None:
        """Close all open ECU connections."""
        for address, o3e in list(self._ecus.items()):
            try:
                o3e.close()
            except Exception:
                pass
        self._ecus.clear()

    # -----------------------------------------------------------------------
    # Depiction support
    # -----------------------------------------------------------------------

    def start_depiction(self, can_interface: str, on_line: Optional[Callable[[str], None]] = None) -> None:
        """Run ``open3e_depictSystem`` as a subprocess.

        Reads stdout in a dedicated reader thread.  Emits:

        - ``depict_progress`` — for each output line
        - ``depict_complete`` — when the process exits
        """
        with self._depict_lock:
            if self._depict_proc is not None and self._depict_proc.poll() is None:
                # Already running
                return

            # Emit CAN status so sidebar updates
            self._emit_data({"type": "engine_state", "state": "paused"})
            self._emit_data({"type": "can_status", "interface": can_interface, "state": "scanning"})

            try:
                # Use sys.executable to ensure we run within the same venv
                # -u forces unbuffered stdout so lines stream in real time
                import sys as _sys
                env = dict(os.environ, PYTHONUNBUFFERED="1")
                proc = subprocess.Popen(
                    [_sys.executable, "-u", "-m", "open3e.Open3E_depictSystem", "-c", can_interface],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.STDOUT,
                    text=True,
                    bufsize=1,
                    env=env,
                )
                self._depict_proc = proc
            except Exception as exc:
                self._emit_data({"type": "depict_error", "error": str(exc)})
                return

        # Server-side log buffer for page refresh persistence
        self._depict_log: list[str] = []
        self._depict_returncode: Optional[int] = None
        self._depict_progress = {"phase": "starting", "percent": 0, "detail": "", "checklist": []}

        # Known scan ranges for progress calculation
        COB_START, COB_END = 0x680, 0x6ff
        COB_COUNT = COB_END - COB_START + 1
        DID_START, DID_END = 256, 3500
        DID_COUNT = DID_END - DID_START + 1

        import re
        _re_cob_scan = re.compile(r"^scan COB-IDs")
        _re_cob_addr = re.compile(r"^0x([0-9a-fA-F]+)\s*$")
        _re_cob_found = re.compile(r"^ECU found:\s*(0x[0-9a-fA-F]+)\s*:\s*(.*)")
        _re_cob_done = re.compile(r"(\d+) responding COB-IDs found")
        _re_did_scan = re.compile(r"^scan ([0-9a-fA-F]+) for DIDs (\d+) to (\d+)")
        _re_did_num = re.compile(r"^(\d+)\s*$")
        _re_did_found = re.compile(r"^found (\d+):(\d+):")
        _re_did_done = re.compile(r"(\d+) DIDs found on")
        _re_write_file = re.compile(r"^write (\S+ file \S+|devices\.json)")
        _re_done = re.compile(r"^done\.$")
        _re_read_enums = re.compile(r"^read DID enums")
        _re_configuration = re.compile(r"^configuration:")
        _re_run_open3e = re.compile(r"^run open3e")
        ecus_found_count = [0]  # mutable for closure
        ecus_scanned_count = [0]  # how many ECU DID scans completed
        current_ecu_hex = [""]

        def _parse_progress(text: str) -> None:
            """Parse depict output lines to update progress."""
            p = self._depict_progress
            cl = p["checklist"]

            if _re_read_enums.match(text):
                p["phase"] = "init"
                p["percent"] = 0
                p["detail"] = "Reading DID enums..."

            elif _re_cob_scan.match(text):
                p["phase"] = "cob_scan"
                p["percent"] = 1
                p["detail"] = "Phase 1/3: Scanning for ECUs on CAN bus..."

            elif _re_cob_addr.match(text):
                m = _re_cob_addr.match(text)
                addr = int(m.group(1), 16)
                done = addr - COB_START + 1
                # COB scan is 20% of total
                p["percent"] = max(p["percent"], int(20 * done / COB_COUNT))
                p["detail"] = "Phase 1/3: Scanning COB-ID 0x{:03x} ({}/{})".format(addr, done, COB_COUNT)

            elif _re_cob_found.match(text):
                ecus_found_count[0] += 1
                m = _re_cob_found.match(text)
                if m:
                    p["detail"] = "ECU found: {} ({})".format(m.group(1), m.group(2))

            elif _re_cob_done.match(text):
                p["phase"] = "cob_done"
                p["percent"] = 20
                p["detail"] = text
                # Add devices.json to checklist
                cl.append({"file": "devices.json", "done": False})

            elif _re_did_scan.match(text):
                m = _re_did_scan.match(text)
                ecu_hex = m.group(1)
                current_ecu_hex[0] = ecu_hex
                p["phase"] = "did_scan"
                p["detail"] = "Phase 2/3: Scanning DIDs on ECU 0x{} ...".format(ecu_hex)
                # Add datapoints file to checklist
                dp_file = "Open3Edatapoints_{}.py".format(ecu_hex)
                if not any(item["file"] == dp_file for item in cl):
                    cl.append({"file": dp_file, "done": False})

            elif _re_did_num.match(text):
                m = _re_did_num.match(text)
                did = int(m.group(1))
                done = did - DID_START + 1
                # DID scan is 60% of total (20-80%), split evenly across ECUs
                ecu_count = max(ecus_found_count[0], 1)
                base = 20 + int(60 * ecus_scanned_count[0] / ecu_count)
                per_ecu_range = 60 / ecu_count
                new_pct = min(80, base + int(per_ecu_range * done / DID_COUNT))
                p["percent"] = max(p["percent"], new_pct)  # never go backwards
                p["detail"] = "Phase 2/3: ECU 0x{} — DID {} ({}/{})".format(
                    current_ecu_hex[0], did, done, DID_COUNT)

            elif _re_did_found.match(text):
                pass  # don't update detail for individual finds, too noisy

            elif _re_did_done.match(text):
                ecus_scanned_count[0] += 1
                # Mark datapoints file as done
                dp_file = "Open3Edatapoints_{}.py".format(current_ecu_hex[0])
                for item in cl:
                    if item["file"] == dp_file:
                        item["done"] = True
                p["detail"] = text

            elif _re_write_file.match(text):
                p["phase"] = "writing"
                p["percent"] = max(p["percent"], 85)
                p["detail"] = "Phase 3/3: Writing files..."
                # Mark devices.json as done when written
                if "devices.json" in text:
                    for item in cl:
                        if item["file"] == "devices.json":
                            item["done"] = True

            elif _re_done.match(text):
                # "done." after a write — mark the last pending checklist item
                for item in reversed(cl):
                    if not item["done"]:
                        item["done"] = True
                        break
                p["percent"] = max(p["percent"], 90)

            elif _re_configuration.match(text):
                p["phase"] = "finishing"
                p["percent"] = 95
                p["detail"] = "Writing configuration summary..."

            elif _re_run_open3e.match(text):
                p["percent"] = 100
                p["phase"] = "complete"
                p["detail"] = "Scan complete"

        def _reader():
            assert proc.stdout is not None
            # Read character-by-character to handle \r as line separator
            buf = ""
            while True:
                ch = proc.stdout.read(1)
                if not ch:
                    break  # EOF
                if ch in ("\n", "\r"):
                    line = buf.strip()
                    buf = ""
                    if not line:
                        continue
                    _parse_progress(line)
                    self._depict_log.append(line)
                    if on_line is not None:
                        on_line(line)
                    self._emit_data({
                        "type": "depict_progress",
                        "line": line,
                        "progress": dict(self._depict_progress),
                    })
                else:
                    buf += ch
            # Flush remaining buffer
            if buf.strip():
                line = buf.strip()
                self._depict_log.append(line)
                self._emit_data({"type": "depict_progress", "line": line, "progress": dict(self._depict_progress)})

            proc.wait()
            self._depict_progress["percent"] = 100
            self._depict_progress["phase"] = "complete"
            self._depict_returncode = proc.returncode
            with self._depict_lock:
                self._depict_proc = None
            self._emit_data({"type": "depict_complete", "returncode": proc.returncode})
            self._emit_data({"type": "engine_state", "state": "idle"})

        reader_thread = threading.Thread(target=_reader, daemon=True, name="DepictReader")
        reader_thread.start()

    @property
    def depict_running(self) -> bool:
        """Return True if a depiction subprocess is currently running."""
        with self._depict_lock:
            return self._depict_proc is not None and self._depict_proc.poll() is None

    def cancel_depiction(self) -> bool:
        """Cancel a running depiction subprocess. Returns True if cancelled."""
        with self._depict_lock:
            if self._depict_proc is not None and self._depict_proc.poll() is None:
                self._depict_proc.terminate()
                self._depict_log.append("=== Scan cancelled by user ===")
                self._depict_progress["detail"] = "Cancelled by user"
                self._depict_progress["phase"] = "cancelled"
                self._emit_data({"type": "depict_progress", "line": "=== Scan cancelled by user ===", "progress": dict(self._depict_progress)})
                return True
        return False

    def get_depict_state(self) -> dict:
        """Return current depiction state including log buffer for page refresh."""
        return {
            "running": self.depict_running,
            "log": getattr(self, "_depict_log", []),
            "returncode": getattr(self, "_depict_returncode", None),
            "progress": getattr(self, "_depict_progress", {"phase": "idle", "percent": 0, "detail": ""}),
        }

    # -----------------------------------------------------------------------
    # Status
    # -----------------------------------------------------------------------

    def get_status(self) -> Dict:
        """Return a snapshot of engine status."""
        return {
            "state": self.state.name,
            "cycle": self._cycle,
            "ecus_connected": len(self._ecus),
            "datapoints_configured": len(self._datapoints),
            "depict_running": self.depict_running,
        }
