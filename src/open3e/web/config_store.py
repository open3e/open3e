"""ConfigStore — SQLite persistence layer for the open3e web UI.

Stores settings, ECU metadata, datapoints, HA entity mappings, MQTT topic
mappings, and provides a backup facility backed by SQLite's VACUUM INTO.
"""

from __future__ import annotations

import pathlib
import re
import time
from typing import Any

import aiosqlite

SCHEMA_VERSION = 2

# Only alphanumeric, hyphens, underscores and dots; must end with .db
_BACKUP_FILENAME_RE = re.compile(r'^[\w\-]+\.db$')


def _validate_backup_filename(filename: str) -> None:
    """Raise ValueError if *filename* is not a safe, plain filename."""
    if not _BACKUP_FILENAME_RE.match(filename):
        raise ValueError(
            f"Invalid backup filename {filename!r}. "
            "Must match [\\w\\-]+\\.db (no path separators or special chars)."
        )
    # Belt-and-suspenders: reject anything that looks like a path component
    if '/' in filename or '\\' in filename or filename.startswith('.'):
        raise ValueError(f"Path traversal detected in filename {filename!r}.")


_DDL = """
PRAGMA journal_mode=WAL;

CREATE TABLE IF NOT EXISTS settings (
    key   TEXT PRIMARY KEY,
    value TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS ecus (
    address     INTEGER PRIMARY KEY,
    name        TEXT    NOT NULL,
    device_prop TEXT,
    dp_list     TEXT
);

CREATE TABLE IF NOT EXISTS datapoints (
    id           INTEGER PRIMARY KEY AUTOINCREMENT,
    ecu_address  INTEGER NOT NULL REFERENCES ecus(address) ON DELETE CASCADE,
    did          INTEGER NOT NULL,
    name         TEXT    NOT NULL,
    codec        TEXT,
    poll_priority INTEGER NOT NULL DEFAULT 0,
    poll_enabled  INTEGER NOT NULL DEFAULT 0,
    unit         TEXT,
    description  TEXT,
    UNIQUE(ecu_address, did)
);

CREATE TABLE IF NOT EXISTS ha_entities (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    dp_id       INTEGER NOT NULL REFERENCES datapoints(id) ON DELETE CASCADE,
    entity_type TEXT    NOT NULL,
    unique_id   TEXT    NOT NULL UNIQUE,
    name        TEXT,
    device_class TEXT,
    unit        TEXT,
    enabled     INTEGER NOT NULL DEFAULT 1
);

CREATE TABLE IF NOT EXISTS mqtt_mappings (
    id      INTEGER PRIMARY KEY AUTOINCREMENT,
    dp_id   INTEGER NOT NULL REFERENCES datapoints(id) ON DELETE CASCADE,
    topic   TEXT    NOT NULL,
    enabled INTEGER NOT NULL DEFAULT 1,
    UNIQUE(dp_id)
);
"""

_ALLOWED_DATAPOINT_FIELDS = frozenset({
    "name", "codec", "poll_priority", "poll_enabled", "unit", "description",
})

_ALLOWED_HA_ENTITY_FIELDS = frozenset({
    "entity_type", "unique_id", "name", "device_class", "unit", "enabled", "sub_field",
})

_ALLOWED_MQTT_MAPPING_FIELDS = frozenset({
    "topic", "enabled",
})


class ConfigStore:
    """Async SQLite-backed configuration store."""

    def __init__(self, db_path: str | pathlib.Path) -> None:
        self._db_path = pathlib.Path(db_path)
        self._backup_dir = self._db_path.parent / "open3e_backups"
        self._db: aiosqlite.Connection | None = None

    # ------------------------------------------------------------------
    # Lifecycle
    # ------------------------------------------------------------------

    async def initialize(self) -> None:
        """Open the database, create schema and run migrations."""
        self._db = await aiosqlite.connect(self._db_path)
        self._db.row_factory = aiosqlite.Row
        await self._db.executescript(_DDL)
        await self._migrate()
        await self._db.execute(f"PRAGMA user_version = {SCHEMA_VERSION}")
        await self._db.commit()

    async def _migrate(self) -> None:
        """Run schema migrations based on current user_version."""
        cur = await self._db.execute("PRAGMA user_version")
        row = await cur.fetchone()
        version = row[0] if row else 0

        if version < 2:
            # Add sub_field column to ha_entities
            try:
                await self._db.execute("ALTER TABLE ha_entities ADD COLUMN sub_field TEXT")
            except Exception:
                pass  # column already exists

    async def close(self) -> None:
        """Close the database connection."""
        if self._db is not None:
            await self._db.close()
            self._db = None

    # ------------------------------------------------------------------
    # Settings
    # ------------------------------------------------------------------

    async def get_setting(self, key: str, default: Any = None) -> Any:
        async with self._db.execute(
            "SELECT value FROM settings WHERE key = ?", (key,)
        ) as cur:
            row = await cur.fetchone()
        return row["value"] if row is not None else default

    async def set_setting(self, key: str, value: Any) -> None:
        await self._db.execute(
            "INSERT INTO settings (key, value) VALUES (?, ?)"
            " ON CONFLICT(key) DO UPDATE SET value = excluded.value",
            (key, value),
        )
        await self._db.commit()

    async def get_all_settings(self) -> dict[str, Any]:
        async with self._db.execute("SELECT key, value FROM settings") as cur:
            rows = await cur.fetchall()
        return {row["key"]: row["value"] for row in rows}

    # ------------------------------------------------------------------
    # ECUs
    # ------------------------------------------------------------------

    async def upsert_ecu(
        self,
        address: int,
        name: str,
        device_prop: str | None = None,
        dp_list: str | None = None,
    ) -> None:
        await self._db.execute(
            "INSERT INTO ecus (address, name, device_prop, dp_list)"
            " VALUES (?, ?, ?, ?)"
            " ON CONFLICT(address) DO UPDATE SET"
            "   name = excluded.name,"
            "   device_prop = excluded.device_prop,"
            "   dp_list = excluded.dp_list",
            (address, name, device_prop, dp_list),
        )
        await self._db.commit()

    async def get_ecus(self) -> list[aiosqlite.Row]:
        async with self._db.execute("SELECT * FROM ecus ORDER BY address") as cur:
            return await cur.fetchall()

    # ------------------------------------------------------------------
    # Datapoints
    # ------------------------------------------------------------------

    async def upsert_datapoint(
        self,
        ecu_address: int,
        did: int,
        name: str,
        codec: str | None = None,
        poll_priority: int = 0,
        poll_enabled: int = 0,
        unit: str | None = None,
        description: str | None = None,
    ) -> int:
        async with self._db.execute(
            "INSERT INTO datapoints"
            "   (ecu_address, did, name, codec, poll_priority, poll_enabled, unit, description)"
            " VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
            " ON CONFLICT(ecu_address, did) DO UPDATE SET"
            "   name  = excluded.name,"
            "   codec = excluded.codec,"
            "   unit  = COALESCE(excluded.unit, unit),"
            "   description = COALESCE(excluded.description, description)",
            (ecu_address, did, name, codec, poll_priority, poll_enabled, unit, description),
        ) as cur:
            rowid = cur.lastrowid
        await self._db.commit()
        return rowid

    async def get_datapoints(
        self,
        ecu_address: int | None = None,
        poll_priority: int | None = None,
        poll_enabled: int | None = None,
    ) -> list[aiosqlite.Row]:
        query = "SELECT * FROM datapoints WHERE 1=1"
        params: list[Any] = []
        if ecu_address is not None:
            query += " AND ecu_address = ?"
            params.append(ecu_address)
        if poll_priority is not None:
            query += " AND poll_priority = ?"
            params.append(poll_priority)
        if poll_enabled is not None:
            query += " AND poll_enabled = ?"
            params.append(poll_enabled)
        query += " ORDER BY id"
        async with self._db.execute(query, params) as cur:
            return await cur.fetchall()

    async def update_datapoint(self, dp_id: int, **kwargs: Any) -> None:
        unknown = set(kwargs) - _ALLOWED_DATAPOINT_FIELDS
        if unknown:
            raise ValueError(f"Unknown datapoint fields: {unknown}")
        if not kwargs:
            return
        assignments = ", ".join(f"{k} = ?" for k in kwargs)
        values = list(kwargs.values()) + [dp_id]
        await self._db.execute(
            f"UPDATE datapoints SET {assignments} WHERE id = ?", values
        )
        await self._db.commit()

    # ------------------------------------------------------------------
    # HA Entities
    # ------------------------------------------------------------------

    async def upsert_ha_entity(
        self,
        dp_id: int,
        entity_type: str,
        unique_id: str,
        name: str | None = None,
        device_class: str | None = None,
        unit: str | None = None,
        enabled: int = 1,
        sub_field: str | None = None,
    ) -> int:
        async with self._db.execute(
            "INSERT INTO ha_entities"
            "   (dp_id, entity_type, unique_id, name, device_class, unit, enabled, sub_field)"
            " VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
            " ON CONFLICT(unique_id) DO UPDATE SET"
            "   dp_id        = excluded.dp_id,"
            "   entity_type  = excluded.entity_type,"
            "   name         = excluded.name,"
            "   device_class = excluded.device_class,"
            "   unit         = excluded.unit,"
            "   sub_field    = excluded.sub_field",
            (dp_id, entity_type, unique_id, name, device_class, unit, enabled, sub_field),
        ) as cur:
            rowid = cur.lastrowid
        await self._db.commit()
        return rowid

    async def get_ha_entities(
        self, enabled: int | None = None
    ) -> list[aiosqlite.Row]:
        query = (
            "SELECT ha_entities.*, datapoints.name AS dp_name,"
            " datapoints.ecu_address, datapoints.did"
            " FROM ha_entities"
            " JOIN datapoints ON datapoints.id = ha_entities.dp_id"
            " WHERE 1=1"
        )
        params: list[Any] = []
        if enabled is not None:
            query += " AND ha_entities.enabled = ?"
            params.append(enabled)
        query += " ORDER BY ha_entities.id"
        async with self._db.execute(query, params) as cur:
            return await cur.fetchall()

    async def update_ha_entity(self, ha_id: int, **kwargs: Any) -> None:
        unknown = set(kwargs) - _ALLOWED_HA_ENTITY_FIELDS
        if unknown:
            raise ValueError(f"Unknown ha_entity fields: {unknown}")
        if not kwargs:
            return
        assignments = ", ".join(f"{k} = ?" for k in kwargs)
        values = list(kwargs.values()) + [ha_id]
        await self._db.execute(
            f"UPDATE ha_entities SET {assignments} WHERE id = ?", values
        )
        await self._db.commit()

    # ------------------------------------------------------------------
    # MQTT Mappings
    # ------------------------------------------------------------------

    async def upsert_mqtt_mapping(
        self,
        dp_id: int,
        topic: str,
        enabled: int = 1,
    ) -> int:
        async with self._db.execute(
            "INSERT INTO mqtt_mappings (dp_id, topic, enabled)"
            " VALUES (?, ?, ?)"
            " ON CONFLICT(dp_id) DO UPDATE SET"
            "   topic   = excluded.topic,"
            "   enabled = excluded.enabled",
            (dp_id, topic, enabled),
        ) as cur:
            rowid = cur.lastrowid
        await self._db.commit()
        return rowid

    async def get_mqtt_mappings(
        self, enabled: int | None = None
    ) -> list[aiosqlite.Row]:
        query = (
            "SELECT mqtt_mappings.*, datapoints.name AS dp_name"
            " FROM mqtt_mappings"
            " JOIN datapoints ON datapoints.id = mqtt_mappings.dp_id"
            " WHERE 1=1"
        )
        params: list[Any] = []
        if enabled is not None:
            query += " AND mqtt_mappings.enabled = ?"
            params.append(enabled)
        query += " ORDER BY mqtt_mappings.id"
        async with self._db.execute(query, params) as cur:
            return await cur.fetchall()

    # ------------------------------------------------------------------
    # Schema version
    # ------------------------------------------------------------------

    async def get_schema_version(self) -> int:
        async with self._db.execute("PRAGMA user_version") as cur:
            row = await cur.fetchone()
        return row[0]

    # ------------------------------------------------------------------
    # Backups
    # ------------------------------------------------------------------

    async def create_backup(self) -> str:
        """Create a backup copy of the database; return filename."""
        import shutil
        self._backup_dir.mkdir(parents=True, exist_ok=True)
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        filename = f"open3e_backup_{timestamp}.db"
        dest = self._backup_dir / filename
        # Flush any pending writes
        await self._db.commit()
        # Use shutil.copy (not copy2) so the backup gets current mtime
        shutil.copy(self._db_path, str(dest))
        return filename

    async def list_backups(self) -> list:
        """Return sorted list of backup info dicts (newest first)."""
        if not self._backup_dir.exists():
            return []
        import datetime, re
        result = []
        for p in sorted(self._backup_dir.glob("*.db"), key=lambda x: x.name, reverse=True):
            st = p.stat()
            # Parse timestamp from filename: open3e_backup_YYYYMMDD_HHMMSS.db
            m = re.search(r"(\d{4})(\d{2})(\d{2})_(\d{2})(\d{2})(\d{2})", p.name)
            if m:
                created = "{}-{}-{} {}:{}:{}".format(*m.groups())
            else:
                created = datetime.datetime.fromtimestamp(st.st_mtime).strftime("%Y-%m-%d %H:%M:%S")
            result.append({
                "filename": p.name,
                "size": f"{st.st_size / 1024:.1f} KB",
                "created": created,
            })
        return result

    async def get_backup_path(self, filename: str) -> pathlib.Path:
        """Validate *filename* and return its absolute Path."""
        _validate_backup_filename(filename)
        return self._backup_dir / filename

    async def delete_backup(self, filename: str) -> None:
        """Delete a backup file after validating the filename."""
        path = await self.get_backup_path(filename)
        if path.exists():
            path.unlink()
