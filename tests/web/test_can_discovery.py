"""Tests for CAN interface discovery module."""

import unittest
from unittest.mock import patch

from open3e.web.can_discovery import discover_can_interfaces, get_can_status


class TestDiscoverCanInterfaces(unittest.TestCase):
    def test_returns_list(self):
        result = discover_can_interfaces()
        self.assertIsInstance(result, list)

    def test_empty_on_non_linux(self):
        with patch("open3e.web.can_discovery._is_linux", return_value=False):
            result = discover_can_interfaces()
        self.assertEqual(result, [])

    def test_finds_can_interfaces(self):
        fake_sys_net = {
            "can0": {"type": "280", "operstate": "UP"},
            "can1": {"type": "280", "operstate": "DOWN"},
            "eth0": {"type": "1", "operstate": "UP"},
            "vcan0": {"type": "280", "operstate": "UNKNOWN"},
        }
        with patch("open3e.web.can_discovery._is_linux", return_value=True), \
             patch("open3e.web.can_discovery._read_sys_net", return_value=fake_sys_net):
            result = discover_can_interfaces()

        names = [iface["name"] for iface in result]
        self.assertIn("can0", names)
        self.assertIn("can1", names)
        self.assertIn("vcan0", names)
        self.assertNotIn("eth0", names)

    def test_includes_state(self):
        fake_sys_net = {
            "can0": {"type": "280", "operstate": "UP"},
        }
        with patch("open3e.web.can_discovery._is_linux", return_value=True), \
             patch("open3e.web.can_discovery._read_sys_net", return_value=fake_sys_net):
            result = discover_can_interfaces()

        self.assertEqual(len(result), 1)
        self.assertIn("state", result[0])


class TestGetCanStatus(unittest.TestCase):
    def test_unavailable_on_non_linux(self):
        with patch("open3e.web.can_discovery._is_linux", return_value=False):
            result = get_can_status("can0")
        self.assertFalse(result["available"])

    def test_reads_stats(self):
        fake_stats = {
            "operstate": "UP",
            "rx_packets": 42,
            "tx_packets": 17,
            "rx_errors": 0,
            "tx_errors": 1,
        }
        with patch("open3e.web.can_discovery._is_linux", return_value=True), \
             patch("open3e.web.can_discovery._read_interface_stats", return_value=fake_stats):
            result = get_can_status("can0")

        self.assertTrue(result["available"])
        self.assertEqual(result["interface"], "can0")
        self.assertEqual(result["state"], "UP")
        self.assertEqual(result["rx_packets"], 42)
        self.assertEqual(result["tx_packets"], 17)
        self.assertEqual(result["rx_errors"], 0)
        self.assertEqual(result["tx_errors"], 1)


if __name__ == "__main__":
    unittest.main()
