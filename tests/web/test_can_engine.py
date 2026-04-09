"""Tests for CanEngine — CAN engine with priority scheduler and command queue."""

import queue
import threading
import time
from unittest.mock import MagicMock, patch, call

import pytest


# ---------------------------------------------------------------------------
# Helpers / fixtures
# ---------------------------------------------------------------------------

def make_store():
    """Return a mock ConfigStore with async-style methods."""
    store = MagicMock()
    store.get_ecus = MagicMock(return_value=[])
    store.get_datapoints = MagicMock(return_value=[])
    return store


# ---------------------------------------------------------------------------
# TestEngineState
# ---------------------------------------------------------------------------

class TestEngineState:
    def test_initial_state_idle(self):
        from open3e.web.can_engine import CanEngine, EngineState

        store = make_store()
        engine = CanEngine(store)
        assert engine.state == EngineState.IDLE

    def test_state_transitions(self):
        from open3e.web.can_engine import CanEngine, EngineState

        store = make_store()
        received = []

        def on_data(msg):
            received.append(msg)

        engine = CanEngine(store, on_data=on_data)

        # Transition to CONNECTING
        engine._set_state(EngineState.CONNECTING)
        assert engine.state == EngineState.CONNECTING

        # Transition to POLLING
        engine._set_state(EngineState.POLLING)
        assert engine.state == EngineState.POLLING

        # Transition to PAUSED
        engine._set_state(EngineState.PAUSED)
        assert engine.state == EngineState.PAUSED

        # Transition to EXECUTING_COMMAND
        engine._set_state(EngineState.EXECUTING_COMMAND)
        assert engine.state == EngineState.EXECUTING_COMMAND

        # Back to IDLE
        engine._set_state(EngineState.IDLE)
        assert engine.state == EngineState.IDLE

        # Check that engine_state messages were emitted (EXECUTING_COMMAND is suppressed)
        state_msgs = [m for m in received if m.get("type") == "engine_state"]
        assert len(state_msgs) == 4  # CONNECTING, POLLING, PAUSED, IDLE (no EXECUTING_COMMAND)

    def test_state_thread_safety(self):
        """Multiple threads reading/writing state should not deadlock or corrupt."""
        from open3e.web.can_engine import CanEngine, EngineState

        store = make_store()
        engine = CanEngine(store)

        errors = []

        def toggle():
            try:
                for _ in range(50):
                    engine._set_state(EngineState.POLLING)
                    _ = engine.state
                    engine._set_state(EngineState.IDLE)
            except Exception as exc:
                errors.append(exc)

        threads = [threading.Thread(target=toggle) for _ in range(4)]
        for t in threads:
            t.start()
        for t in threads:
            t.join(timeout=5)

        assert errors == []


# ---------------------------------------------------------------------------
# TestPriorityScheduler
# ---------------------------------------------------------------------------

class TestPriorityScheduler:
    """Tests for _build_poll_list — no real CAN hardware needed."""

    def _make_engine(self):
        from open3e.web.can_engine import CanEngine
        store = make_store()
        engine = CanEngine(store)
        return engine

    def _dp(self, ecu, did, priority, enabled=True):
        """Build a minimal datapoint dict."""
        return {
            "ecu_address": ecu,
            "did": did,
            "poll_priority": priority,
            "poll_enabled": 1 if enabled else 0,
        }

    def test_build_cycle_high_only(self):
        """Cycle 1: only high-priority (priority=3) DIDs should appear."""
        from open3e.web.can_engine import CanEngine, MEDIUM_INTERVAL, LOW_INTERVAL

        engine = self._make_engine()
        engine._datapoints = {
            1: self._dp(0x680, 100, 3),   # high
            2: self._dp(0x680, 200, 2),   # medium
            3: self._dp(0x680, 300, 1),   # low
        }

        # Cycle 1 is NOT divisible by MEDIUM_INTERVAL or LOW_INTERVAL
        result = engine._build_poll_list(1)
        dids = [item["did"] for item in result]

        assert 100 in dids
        assert 200 not in dids
        assert 300 not in dids

    def test_build_cycle_with_medium(self):
        """Cycle equal to MEDIUM_INTERVAL: high + medium DIDs should appear."""
        from open3e.web.can_engine import CanEngine, MEDIUM_INTERVAL

        engine = self._make_engine()
        engine._datapoints = {
            1: self._dp(0x680, 100, 3),   # high
            2: self._dp(0x680, 200, 2),   # medium
            3: self._dp(0x680, 300, 1),   # low
        }

        result = engine._build_poll_list(MEDIUM_INTERVAL)
        dids = [item["did"] for item in result]

        assert 100 in dids
        assert 200 in dids
        assert 300 not in dids

    def test_build_cycle_with_all(self):
        """Cycle 0 (divisible by everything): high + medium + low should appear."""
        from open3e.web.can_engine import CanEngine

        engine = self._make_engine()
        engine._datapoints = {
            1: self._dp(0x680, 100, 3),   # high
            2: self._dp(0x680, 200, 2),   # medium
            3: self._dp(0x680, 300, 1),   # low
        }

        result = engine._build_poll_list(0)
        dids = [item["did"] for item in result]

        assert 100 in dids
        assert 200 in dids
        assert 300 in dids

    def test_disabled_excluded(self):
        """Disabled DIDs (poll_enabled=0) should never appear regardless of cycle."""
        from open3e.web.can_engine import CanEngine

        engine = self._make_engine()
        engine._datapoints = {
            1: self._dp(0x680, 100, 3, enabled=False),  # high, disabled
            2: self._dp(0x680, 200, 2, enabled=False),  # medium, disabled
            3: self._dp(0x680, 300, 1, enabled=False),  # low, disabled
            4: self._dp(0x680, 400, 3, enabled=True),   # high, enabled
        }

        result = engine._build_poll_list(0)
        dids = [item["did"] for item in result]

        assert 100 not in dids
        assert 200 not in dids
        assert 300 not in dids
        assert 400 in dids

    def test_empty_datapoints(self):
        """An empty datapoints dict should produce an empty poll list."""
        from open3e.web.can_engine import CanEngine

        engine = self._make_engine()
        engine._datapoints = {}

        result = engine._build_poll_list(0)
        assert result == []

    def test_low_interval_boundary(self):
        """Cycle equal to LOW_INTERVAL: all tiers should appear."""
        from open3e.web.can_engine import CanEngine, LOW_INTERVAL

        engine = self._make_engine()
        engine._datapoints = {
            1: self._dp(0x680, 100, 3),   # high
            2: self._dp(0x680, 200, 2),   # medium
            3: self._dp(0x680, 300, 1),   # low
        }

        result = engine._build_poll_list(LOW_INTERVAL)
        dids = [item["did"] for item in result]
        assert 100 in dids
        assert 200 in dids
        assert 300 in dids


# ---------------------------------------------------------------------------
# TestCommandQueue
# ---------------------------------------------------------------------------

class TestCommandQueue:
    def test_enqueue_command(self):
        """send_command should put a dict on the internal queue."""
        from open3e.web.can_engine import CanEngine

        store = make_store()
        engine = CanEngine(store)

        cmd = {"type": "read_did", "ecu": 0x680, "did": 100}
        engine.send_command(cmd)

        assert not engine._cmd_queue.empty()

    def test_dequeue_command(self):
        """After enqueue, the exact dict should be retrievable from the queue."""
        from open3e.web.can_engine import CanEngine

        store = make_store()
        engine = CanEngine(store)

        cmd = {"type": "stop"}
        engine.send_command(cmd)

        item = engine._cmd_queue.get_nowait()
        assert item == cmd

    def test_multiple_commands_fifo(self):
        """Commands should come out in FIFO order."""
        from open3e.web.can_engine import CanEngine

        store = make_store()
        engine = CanEngine(store)

        cmds = [
            {"type": "stop"},
            {"type": "pause"},
            {"type": "resume"},
        ]
        for c in cmds:
            engine.send_command(c)

        received = []
        while not engine._cmd_queue.empty():
            received.append(engine._cmd_queue.get_nowait())

        assert received == cmds

    def test_thread_safe_enqueue(self):
        """Multiple threads enqueueing should not lose commands."""
        from open3e.web.can_engine import CanEngine

        store = make_store()
        engine = CanEngine(store)

        n = 100

        def enqueue():
            for i in range(n):
                engine.send_command({"type": "noop", "i": i})

        threads = [threading.Thread(target=enqueue) for _ in range(4)]
        for t in threads:
            t.start()
        for t in threads:
            t.join(timeout=5)

        count = 0
        while not engine._cmd_queue.empty():
            engine._cmd_queue.get_nowait()
            count += 1

        assert count == 4 * n


# ---------------------------------------------------------------------------
# TestDataCallback
# ---------------------------------------------------------------------------

class TestDataQueue:
    def test_data_callback(self):
        """_emit_data should invoke the on_data callback with the message."""
        from open3e.web.can_engine import CanEngine

        store = make_store()
        received = []

        engine = CanEngine(store, on_data=received.append)

        msg = {"type": "did_value", "ecu": 0x680, "did": 100, "value": 42}
        engine._emit_data(msg)

        assert len(received) == 1
        assert received[0] == msg

    def test_no_callback_no_error(self):
        """_emit_data without a callback should not raise."""
        from open3e.web.can_engine import CanEngine

        store = make_store()
        engine = CanEngine(store)  # no on_data

        # Should not raise
        engine._emit_data({"type": "did_value", "value": 1})

    def test_callback_receives_engine_state_on_set_state(self):
        """_set_state should deliver an engine_state message through on_data."""
        from open3e.web.can_engine import CanEngine, EngineState

        store = make_store()
        received = []
        engine = CanEngine(store, on_data=received.append)

        engine._set_state(EngineState.POLLING)

        assert any(
            m.get("type") == "engine_state" and m.get("state") == EngineState.POLLING.value
            for m in received
        )


# ---------------------------------------------------------------------------
# TestGetStatus
# ---------------------------------------------------------------------------

class TestGetStatus:
    def test_get_status_keys(self):
        """get_status() should return a dict with the required keys."""
        from open3e.web.can_engine import CanEngine, EngineState

        store = make_store()
        engine = CanEngine(store)

        status = engine.get_status()

        assert "state" in status
        assert "cycle" in status
        assert "ecus_connected" in status
        assert "datapoints_configured" in status
        assert "depict_running" in status

    def test_get_status_initial_values(self):
        """Fresh engine should report IDLE state and zero counts."""
        from open3e.web.can_engine import CanEngine, EngineState

        store = make_store()
        engine = CanEngine(store)

        status = engine.get_status()

        assert status["state"] == EngineState.IDLE.name
        assert status["ecus_connected"] == 0
        assert status["datapoints_configured"] == 0
        assert status["depict_running"] is False

    def test_depict_running_property(self):
        """depict_running property should be False initially."""
        from open3e.web.can_engine import CanEngine

        store = make_store()
        engine = CanEngine(store)

        assert engine.depict_running is False
