"""WebSocket connection manager for the open3e web UI."""

from __future__ import annotations

from typing import Union


class WebSocketManager:
    """Tracks connected WebSocket clients and their DID subscriptions.

    Each client can subscribe to a specific set of DID integers or to "*"
    (wildcard) to receive every broadcast.  The default subscription after
    ``connect`` is "*".
    """

    def __init__(self) -> None:
        self.clients: set = set()
        # Maps WebSocket -> "*" | set[int]
        self.subscriptions: dict = {}

    # ------------------------------------------------------------------
    # Connection lifecycle
    # ------------------------------------------------------------------

    async def connect(self, ws) -> None:
        """Accept the WebSocket handshake and register the client."""
        await ws.accept()
        self.clients.add(ws)
        self.subscriptions[ws] = "*"

    def disconnect(self, ws) -> None:
        """Remove a client from the pool."""
        self.clients.discard(ws)
        self.subscriptions.pop(ws, None)

    # ------------------------------------------------------------------
    # Subscription management
    # ------------------------------------------------------------------

    def subscribe(self, ws, dids: Union[str, list]) -> None:
        """Update the DID subscription for *ws*.

        Parameters
        ----------
        ws:
            A connected WebSocket client.
        dids:
            Either the string ``"*"`` for a wildcard subscription, or a
            list of integer DID values to subscribe to.
        """
        if dids == "*":
            self.subscriptions[ws] = "*"
        else:
            self.subscriptions[ws] = set(dids)

    # ------------------------------------------------------------------
    # Broadcasting
    # ------------------------------------------------------------------

    async def broadcast_did_value(self, msg: dict) -> None:
        """Send *msg* to all clients whose subscription includes ``msg["did"]``.

        Dead clients (those that raise on ``send_json``) are removed.
        """
        did = msg["did"]
        dead: list = []
        for ws in list(self.clients):
            sub = self.subscriptions.get(ws)
            if sub == "*" or (isinstance(sub, set) and did in sub):
                try:
                    await ws.send_json(msg)
                except Exception:
                    dead.append(ws)
        for ws in dead:
            self.disconnect(ws)

    async def broadcast_state(self, msg: dict) -> None:
        """Send *msg* to ALL connected clients.

        Dead clients are removed.
        """
        dead: list = []
        for ws in list(self.clients):
            try:
                await ws.send_json(msg)
            except Exception:
                dead.append(ws)
        for ws in dead:
            self.disconnect(ws)
