"""Tests for the WebSocket connection manager."""

from __future__ import annotations

import asyncio
from unittest.mock import AsyncMock, MagicMock

import pytest


def run(coro):
    """Run a coroutine synchronously."""
    return asyncio.get_event_loop().run_until_complete(coro)


def make_ws():
    """Create a mock WebSocket."""
    ws = MagicMock()
    ws.accept = AsyncMock()
    ws.send_json = AsyncMock()
    return ws


class TestConnect:
    def test_add_client(self):
        from open3e.web.ws_manager import WebSocketManager

        mgr = WebSocketManager()
        ws = make_ws()

        run(mgr.connect(ws))

        ws.accept.assert_awaited_once()
        assert ws in mgr.clients

    def test_disconnect_removes_client(self):
        from open3e.web.ws_manager import WebSocketManager

        mgr = WebSocketManager()
        ws = make_ws()

        run(mgr.connect(ws))
        assert ws in mgr.clients

        mgr.disconnect(ws)
        assert ws not in mgr.clients
        assert ws not in mgr.subscriptions


class TestSubscribe:
    def test_default_subscribe_all(self):
        from open3e.web.ws_manager import WebSocketManager

        mgr = WebSocketManager()
        ws = make_ws()

        run(mgr.connect(ws))

        assert mgr.subscriptions[ws] == "*"

    def test_subscribe_specific_dids(self):
        from open3e.web.ws_manager import WebSocketManager

        mgr = WebSocketManager()
        ws = make_ws()

        run(mgr.connect(ws))
        mgr.subscribe(ws, [268, 300])

        assert mgr.subscriptions[ws] == {268, 300}

    def test_subscribe_all(self):
        from open3e.web.ws_manager import WebSocketManager

        mgr = WebSocketManager()
        ws = make_ws()

        run(mgr.connect(ws))
        mgr.subscribe(ws, [268, 300])
        mgr.subscribe(ws, "*")

        assert mgr.subscriptions[ws] == "*"


class TestBroadcast:
    def test_broadcast_to_subscribed(self):
        """ws1 subscribed to DID 268 receives it; ws2 subscribed to DID 300 does not."""
        from open3e.web.ws_manager import WebSocketManager

        mgr = WebSocketManager()
        ws1 = make_ws()
        ws2 = make_ws()

        run(mgr.connect(ws1))
        run(mgr.connect(ws2))
        mgr.subscribe(ws1, [268])
        mgr.subscribe(ws2, [300])

        msg = {"did": 268, "value": 42}
        run(mgr.broadcast_did_value(msg))

        ws1.send_json.assert_awaited_once_with(msg)
        ws2.send_json.assert_not_awaited()

    def test_broadcast_to_wildcard(self):
        """Wildcard subscriber receives all DIDs."""
        from open3e.web.ws_manager import WebSocketManager

        mgr = WebSocketManager()
        ws = make_ws()

        run(mgr.connect(ws))
        # default is already "*", but be explicit
        mgr.subscribe(ws, "*")

        msg = {"did": 999, "value": "hello"}
        run(mgr.broadcast_did_value(msg))

        ws.send_json.assert_awaited_once_with(msg)

    def test_broadcast_state(self):
        """broadcast_state sends to ALL clients regardless of subscription."""
        from open3e.web.ws_manager import WebSocketManager

        mgr = WebSocketManager()
        ws1 = make_ws()
        ws2 = make_ws()

        run(mgr.connect(ws1))
        run(mgr.connect(ws2))
        mgr.subscribe(ws1, [268])
        mgr.subscribe(ws2, [300])

        msg = {"state": "running"}
        run(mgr.broadcast_state(msg))

        ws1.send_json.assert_awaited_once_with(msg)
        ws2.send_json.assert_awaited_once_with(msg)

    def test_broken_client_removed(self):
        """A client that raises on send_json is removed from the pool."""
        from open3e.web.ws_manager import WebSocketManager

        mgr = WebSocketManager()
        ws_ok = make_ws()
        ws_bad = make_ws()
        ws_bad.send_json.side_effect = RuntimeError("connection closed")

        run(mgr.connect(ws_ok))
        run(mgr.connect(ws_bad))

        msg = {"did": 268, "value": 1}
        run(mgr.broadcast_did_value(msg))

        assert ws_bad not in mgr.clients
        assert ws_bad not in mgr.subscriptions
        # good client still present and received message
        assert ws_ok in mgr.clients
        ws_ok.send_json.assert_awaited_once_with(msg)
