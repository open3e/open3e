"""Launcher — single entry point for the open3e web UI.

Starts the FastAPI web server with CAN engine and MQTT publisher.
Auto-connects CAN and MQTT if previously configured.
"""

from __future__ import annotations

import asyncio
import logging
import socket
import sys

import uvicorn

from open3e.web.can_engine import CanEngine
from open3e.web.config_store import ConfigStore
from open3e.web.mqtt_publisher import MqttPublisher
from open3e.web.server import create_app

DEFAULT_DB_PATH = "open3e_web.db"
DEFAULT_PORT = 8080
MAX_PORT_ATTEMPTS = 10

logger = logging.getLogger("open3e.web")


def _get_local_ip() -> str:
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.connect(("8.8.8.8", 80))
        ip = sock.getsockname()[0]
        sock.close()
        return ip
    except Exception:
        return "127.0.0.1"


def _port_available(port: int) -> bool:
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind(("0.0.0.0", port))
        sock.close()
        return True
    except OSError:
        return False


def _find_port(preferred: int) -> int:
    for offset in range(MAX_PORT_ATTEMPTS):
        candidate = preferred + offset
        if _port_available(candidate):
            return candidate
    return preferred


def main() -> None:
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(name)s %(levelname)s %(message)s")

    store = ConfigStore(DEFAULT_DB_PATH)
    loop = asyncio.new_event_loop()
    loop.run_until_complete(store.initialize())

    # Port
    preferred_port = loop.run_until_complete(store.get_setting("web_port", DEFAULT_PORT))
    try:
        preferred_port = int(preferred_port)
    except (ValueError, TypeError):
        preferred_port = DEFAULT_PORT
    port = _find_port(preferred_port)

    # Create app
    app = create_app(store)

    # Shared mutable state for the cross-thread bridge
    _main_loop = None

    def _bridge_to_ws(msg: dict) -> None:
        """Send a message from any thread to WebSocket clients on the uvicorn loop."""
        if _main_loop is None:
            return
        ws_mgr = getattr(app.state, "ws_manager", None)
        if ws_mgr is None:
            return
        if msg.get("type") == "did_value":
            coro = ws_mgr.broadcast_did_value(msg)
        else:
            coro = ws_mgr.broadcast_state(msg)
        try:
            asyncio.run_coroutine_threadsafe(coro, _main_loop)
        except RuntimeError:
            pass

    # --- CAN Engine ---

    engine = CanEngine(store)
    app.state.engine = engine

    def on_engine_data(msg: dict) -> None:
        _bridge_to_ws(msg)
        # Publish all DID values to MQTT — publisher handles its own change detection
        if msg.get("type") == "did_value":
            pub = getattr(app.state, "mqtt_publisher", None)
            if pub:
                pub.publish_did_value(
                    msg.get("ecu", 0), msg.get("did", 0),
                    msg.get("name", ""), msg.get("value")
                )

    engine._on_data = on_engine_data

    def start_engine(can_iface: str, can_bitrate: int, ecus: list, datapoints: dict,
                     poll_interval: float = 10.0) -> bool:
        """Start the CAN engine with given config. Thread-safe, no async."""
        if not can_iface or not ecus:
            logger.info("Cannot start engine: missing interface or ECUs")
            return False

        if engine._thread and engine._thread.is_alive():
            engine.stop()

        engine.start(
            can_interface=can_iface,
            can_bitrate=can_bitrate,
            datapoints=datapoints,
            ecus=ecus,
            poll_interval=poll_interval,
        )
        logger.info("CAN engine started on %s @ %d bps, %d ECUs, %d datapoints, interval=%ds",
                     can_iface, can_bitrate, len(ecus), len(datapoints), poll_interval)
        return True

    def start_engine_from_db_sync() -> bool:
        """Read CAN config from DB and start engine. Only safe at startup (sync context)."""
        can_iface = loop.run_until_complete(store.get_setting("can_interface"))
        if not can_iface:
            return False
        can_bitrate_str = loop.run_until_complete(store.get_setting("can_bitrate", "250000"))
        try:
            can_bitrate = int(can_bitrate_str)
        except (ValueError, TypeError):
            can_bitrate = 250000
        poll_interval_str = loop.run_until_complete(store.get_setting("poll_interval", "10"))
        try:
            poll_interval = float(poll_interval_str)
        except (ValueError, TypeError):
            poll_interval = 10.0
        ecus_rows = loop.run_until_complete(store.get_ecus())
        dp_rows = loop.run_until_complete(store.get_datapoints())
        if not ecus_rows:
            return False
        ecus = [dict(row) for row in ecus_rows]
        datapoints = {row["id"]: dict(row) for row in dp_rows}
        return start_engine(can_iface, can_bitrate, ecus, datapoints, poll_interval)

    # Expose the non-async start_engine for use from async server handlers
    app.state.start_engine = start_engine

    # --- MQTT Publisher ---

    publisher = MqttPublisher(store, on_status=lambda msg: _bridge_to_ws(msg))
    app.state.mqtt_publisher = publisher

    # Wire MQTT command handler to route HA writes to CAN engine
    def on_mqtt_command(did, value, sub=None):
        """Handle write commands from HA via MQTT."""
        # Default ECU is 0x680 (1664). For specific DIDs, use the correct ECU.
        ecu = 1664
        # DID 2214 (BackupBoxConfiguration) is on 0x6a1
        if did in (2214, 451, 1552, 1587, 1588, 1589, 1590, 1591):
            ecu = 0x6a1

        # Special handling for DID 1006 (TargetQuickMode) — switch on/off
        if did == 1006:
            if value in ("on", "ON", True, 1, "1"):
                value = {"OpMode": 2, "Required": "on", "Unknown": "0000"}
            else:
                value = {"OpMode": 0, "Required": "off", "Unknown": "0000"}
            sub = None  # write full object

        # DIDs with O3EByteVal sub-fields need text→int mapping
        # (O3EEnum DIDs like 1415/1416 accept text directly)
        if did in (531, 538) and sub == "Mode" and isinstance(value, str):
            _mode_map = {"Off": 0, "Heating": 1, "Cooling": 5}
            value = _mode_map.get(value, value)

        engine.send_command({
            "action": "write_did",
            "ecu": ecu,
            "did": did,
            "value": value,
            "sub": sub,
        })
        logger.info("HA MQTT write: ECU=%s DID=%s sub=%s val=%s", hex(ecu), did, sub, value)

    publisher.set_command_handler(on_mqtt_command)

    def start_mqtt_from_db() -> bool:
        """Read MQTT config from DB and start the publisher. Called at startup only."""
        configured = loop.run_until_complete(publisher.configure())
        if configured:
            publisher.start()
            logger.info("MQTT publisher started")
            return True
        else:
            logger.info("MQTT not configured — publisher not started")
            return False

    app.state.start_mqtt = start_mqtt_from_db

    # --- Auto-start ---

    engine_started = start_engine_from_db_sync()
    mqtt_started = start_mqtt_from_db()

    # --- Print startup info ---

    local_ip = _get_local_ip()
    print("open3e-web starting...")
    print(f"  Local:   http://127.0.0.1:{port}")
    print(f"  Network: http://{local_ip}:{port}")
    print(f"  CAN:     {'started' if engine_started else 'not started (configure via web UI)'}")
    print(f"  MQTT:    {'started' if mqtt_started else 'not configured'}")
    print()

    # --- Run uvicorn ---

    config = uvicorn.Config(app, host="0.0.0.0", port=port, log_level="warning")
    server = uvicorn.Server(config)

    async def _serve():
        nonlocal _main_loop
        _main_loop = asyncio.get_running_loop()

        # Emit initial status now that the loop is available for bridging
        async def _emit_initial_status():
            await asyncio.sleep(1)  # wait for first WebSocket clients
            ws_mgr = getattr(app.state, "ws_manager", None)
            if ws_mgr:
                if engine._state:
                    await ws_mgr.broadcast_state({"type": "engine_state", "state": engine._state.value})
                await ws_mgr.broadcast_state({"type": "mqtt_status", "connected": publisher.connected})

        _main_loop.create_task(_emit_initial_status())

        # Periodic HA discovery republish every 60 seconds
        async def _ha_discovery_loop():
            while True:
                await asyncio.sleep(60)
                try:
                    ha_enabled = await store.get_setting("ha_discovery_enabled")
                    if ha_enabled != "1":
                        continue
                    if not publisher.connected:
                        continue
                    entities = await store.get_ha_entities(enabled=1)
                    if not entities:
                        continue
                    ecus = await store.get_ecus()
                    tp = await store.get_setting("mqtt_topic_prefix", "vcal") or "vcal"
                    hp = await store.get_setting("ha_discovery_prefix", "homeassistant") or "homeassistant"
                    publisher.publish_ha_discovery(
                        [dict(e) for e in entities],
                        [dict(e) for e in ecus],
                        tp, hp,
                    )
                except Exception as exc:
                    logger.warning("HA discovery periodic publish failed: %s", exc)

        _main_loop.create_task(_ha_discovery_loop())

        await server.serve()

    asyncio.run(_serve())


if __name__ == "__main__":
    main()
