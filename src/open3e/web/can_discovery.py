"""CAN interface discovery via /sys/class/net scanning."""

import platform
from pathlib import Path
from typing import Optional

_CAN_ARPHRD = "280"  # CAN device type in /sys/class/net/<iface>/type


def _is_linux() -> bool:
    """Return True if the current platform is Linux."""
    return platform.system() == "Linux"


def _read_sys_net() -> dict:
    """Read /sys/class/net/ and return a dict of {name: {type, operstate}}."""
    base = Path("/sys/class/net")
    result = {}
    try:
        for entry in base.iterdir():
            name = entry.name
            try:
                iface_type = (entry / "type").read_text().strip()
                operstate = (entry / "operstate").read_text().strip()
            except OSError:
                continue
            result[name] = {"type": iface_type, "operstate": operstate}
    except OSError:
        pass
    return result


def _read_interface_stats(name: str) -> Optional[dict]:
    """Read statistics for a named interface from /sys/class/net/<name>/."""
    base = Path("/sys/class/net") / name
    try:
        operstate = (base / "operstate").read_text().strip()
        stats_dir = base / "statistics"
        rx_packets = int((stats_dir / "rx_packets").read_text().strip())
        tx_packets = int((stats_dir / "tx_packets").read_text().strip())
        rx_errors = int((stats_dir / "rx_errors").read_text().strip())
        tx_errors = int((stats_dir / "tx_errors").read_text().strip())
    except OSError:
        return None
    return {
        "operstate": operstate,
        "rx_packets": rx_packets,
        "tx_packets": tx_packets,
        "rx_errors": rx_errors,
        "tx_errors": tx_errors,
    }


def discover_can_interfaces() -> list:
    """Return a sorted list of dicts {name, state} for CAN interfaces.

    Returns an empty list on non-Linux platforms.
    """
    if not _is_linux():
        return []

    interfaces = []
    for name, info in _read_sys_net().items():
        if info.get("type") == _CAN_ARPHRD:
            interfaces.append({"name": name, "state": info.get("operstate", "UNKNOWN")})

    interfaces.sort(key=lambda x: x["name"])
    return interfaces


def get_can_status(interface: str) -> dict:
    """Return status dict for a CAN interface.

    Keys: available, interface, state, rx_packets, tx_packets, rx_errors, tx_errors.
    When not on Linux or stats are unreadable, available=False.
    """
    if not _is_linux():
        return {
            "available": False,
            "interface": interface,
            "state": None,
            "rx_packets": None,
            "tx_packets": None,
            "rx_errors": None,
            "tx_errors": None,
        }

    stats = _read_interface_stats(interface)
    if stats is None:
        return {
            "available": False,
            "interface": interface,
            "state": None,
            "rx_packets": None,
            "tx_packets": None,
            "rx_errors": None,
            "tx_errors": None,
        }

    return {
        "available": True,
        "interface": interface,
        "state": stats["operstate"],
        "rx_packets": stats["rx_packets"],
        "tx_packets": stats["tx_packets"],
        "rx_errors": stats["rx_errors"],
        "tx_errors": stats["tx_errors"],
    }
