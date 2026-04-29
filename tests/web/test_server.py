"""Tests for the FastAPI server (server.py)."""

from __future__ import annotations

import asyncio
import os
import pathlib
import shutil

import pytest
import httpx

DB_PATH = "/tmp/open3e_test_server.db"


def run(coro):
    """Run a coroutine synchronously."""
    return asyncio.get_event_loop().run_until_complete(coro)


@pytest.fixture
def app():
    """Create a fresh ConfigStore and FastAPI app, clean up afterward."""
    from open3e.web.config_store import ConfigStore
    from open3e.web.server import create_app

    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)

    store = ConfigStore(DB_PATH)
    run(store.initialize())

    application = create_app(store)
    yield application

    run(store.close())

    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)

    backup_dir = pathlib.Path(DB_PATH).parent / "open3e_backups"
    if backup_dir.exists():
        shutil.rmtree(backup_dir)


def get(app, path, **kwargs):
    """Synchronous GET helper."""
    transport = httpx.ASGITransport(app=app)
    async def _req():
        async with httpx.AsyncClient(transport=transport, base_url="http://test") as client:
            return await client.get(path, **kwargs)
    return run(_req())


def post(app, path, **kwargs):
    """Synchronous POST helper."""
    transport = httpx.ASGITransport(app=app)
    async def _req():
        async with httpx.AsyncClient(transport=transport, base_url="http://test") as client:
            return await client.post(path, **kwargs)
    return run(_req())


def patch(app, path, **kwargs):
    """Synchronous PATCH helper."""
    transport = httpx.ASGITransport(app=app)
    async def _req():
        async with httpx.AsyncClient(transport=transport, base_url="http://test") as client:
            return await client.patch(path, **kwargs)
    return run(_req())


def delete(app, path, **kwargs):
    """Synchronous DELETE helper."""
    transport = httpx.ASGITransport(app=app)
    async def _req():
        async with httpx.AsyncClient(transport=transport, base_url="http://test") as client:
            return await client.delete(path, **kwargs)
    return run(_req())


# ---------------------------------------------------------------------------
# Page routes
# ---------------------------------------------------------------------------

class TestPages:
    def test_dashboard_loads(self, app):
        resp = get(app, "/")
        assert resp.status_code == 200
        assert "open3e" in resp.text

    def test_settings_loads(self, app):
        resp = get(app, "/settings")
        assert resp.status_code == 200
        assert "CAN" in resp.text


# ---------------------------------------------------------------------------
# Settings API
# ---------------------------------------------------------------------------

class TestSettingsApi:
    def test_get_settings(self, app):
        resp = get(app, "/api/settings")
        assert resp.status_code == 200
        assert isinstance(resp.json(), dict)

    def test_patch_settings(self, app):
        resp = patch(app, "/api/settings", json={"my_key": "my_value"})
        assert resp.status_code == 200
        # Verify it was saved
        resp2 = get(app, "/api/settings")
        assert resp2.json().get("my_key") == "my_value"


# ---------------------------------------------------------------------------
# CAN Interfaces API
# ---------------------------------------------------------------------------

class TestCanInterfacesApi:
    def test_list_interfaces(self, app):
        resp = get(app, "/api/can/interfaces")
        assert resp.status_code == 200
        assert isinstance(resp.json(), list)


# ---------------------------------------------------------------------------
# Backup API
# ---------------------------------------------------------------------------

class TestBackupApi:
    def test_create_and_list(self, app):
        # Create a backup
        resp = post(app, "/api/backup")
        assert resp.status_code == 200
        data = resp.json()
        assert "filename" in data

        # List backups
        resp2 = get(app, "/api/backups")
        assert resp2.status_code == 200
        backups = resp2.json()
        assert isinstance(backups, list)
        filenames = [b["filename"] for b in backups]
        assert data["filename"] in filenames

    def test_download(self, app):
        # Create a backup first
        resp = post(app, "/api/backup")
        filename = resp.json()["filename"]

        # Download it
        resp2 = get(app, f"/api/backup/{filename}")
        assert resp2.status_code == 200

    def test_delete(self, app):
        # Create a backup first
        resp = post(app, "/api/backup")
        filename = resp.json()["filename"]

        # Delete it
        resp2 = delete(app, f"/api/backup/{filename}")
        assert resp2.status_code == 200

        # Verify it's gone from the list
        resp3 = get(app, "/api/backups")
        assert filename not in resp3.json()


# ---------------------------------------------------------------------------
# Integration tests
# ---------------------------------------------------------------------------

class TestIntegration:
    def test_full_settings_roundtrip(self, app):
        """Save CAN + MQTT settings, reload settings page, verify values."""
        # Save settings via API
        resp = patch(app, "/api/settings", json={
            "can_interface": "can0",
            "can_bitrate": "250000",
            "mqtt_host": "192.168.1.100",
            "mqtt_port": "1883",
            "mqtt_topic_prefix": "open3e",
            "ha_discovery_enabled": "1",
            "ha_discovery_prefix": "homeassistant",
        })
        assert resp.status_code == 200

        # Read back via API
        resp = get(app, "/api/settings")
        data = resp.json()
        assert data["can_interface"] == "can0"
        assert data["mqtt_host"] == "192.168.1.100"
        assert data["ha_discovery_enabled"] == "1"

        # Load settings page — should render without error
        resp = get(app, "/settings")
        assert resp.status_code == 200
        assert "192.168.1.100" in resp.text
