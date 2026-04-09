"""Tests for ConfigStore — SQLite persistence layer."""

import asyncio
import os
import pytest

DB_PATH = "/tmp/open3e_test.db"


def run(coro):
    """Run a coroutine synchronously."""
    return asyncio.get_event_loop().run_until_complete(coro)


@pytest.fixture
def store():
    """Create a fresh ConfigStore for each test and clean up afterward."""
    from open3e.web.config_store import ConfigStore

    # Remove any leftover db from a previous run
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)

    cs = ConfigStore(DB_PATH)
    run(cs.initialize())
    yield cs
    run(cs.close())

    # Clean up db file
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)

    # Clean up backup dir if created
    import pathlib
    backup_dir = pathlib.Path(DB_PATH).parent / "open3e_backups"
    if backup_dir.exists():
        import shutil
        shutil.rmtree(backup_dir)


# ---------------------------------------------------------------------------
# Settings
# ---------------------------------------------------------------------------

class TestSettings:
    def test_get_unset_returns_none(self, store):
        result = run(store.get_setting("missing_key"))
        assert result is None

    def test_get_unset_returns_default(self, store):
        result = run(store.get_setting("missing_key", default="fallback"))
        assert result == "fallback"

    def test_set_and_get(self, store):
        run(store.set_setting("my_key", "my_value"))
        result = run(store.get_setting("my_key"))
        assert result == "my_value"

    def test_overwrite(self, store):
        run(store.set_setting("key", "first"))
        run(store.set_setting("key", "second"))
        result = run(store.get_setting("key"))
        assert result == "second"

    def test_get_all_settings(self, store):
        run(store.set_setting("a", "1"))
        run(store.set_setting("b", "2"))
        all_settings = run(store.get_all_settings())
        assert all_settings["a"] == "1"
        assert all_settings["b"] == "2"


# ---------------------------------------------------------------------------
# ECUs
# ---------------------------------------------------------------------------

class TestEcus:
    def test_upsert_and_get(self, store):
        run(store.upsert_ecu(0x68, "Heater", '{"brand":"Viessmann"}', '[1,2,3]'))
        ecus = run(store.get_ecus())
        assert len(ecus) == 1
        assert ecus[0]["address"] == 0x68
        assert ecus[0]["name"] == "Heater"

    def test_upsert_overwrites(self, store):
        run(store.upsert_ecu(0x68, "Heater", '{}', '[]'))
        run(store.upsert_ecu(0x68, "Updated Heater", '{"v":2}', '[1]'))
        ecus = run(store.get_ecus())
        assert len(ecus) == 1
        assert ecus[0]["name"] == "Updated Heater"


# ---------------------------------------------------------------------------
# Datapoints
# ---------------------------------------------------------------------------

class TestDatapoints:
    def test_upsert_and_get(self, store):
        run(store.upsert_ecu(0x68, "Heater", '{}', '[]'))
        dp_id = run(store.upsert_datapoint(
            ecu_address=0x68,
            did=1,
            name="OutdoorTemp",
            codec="SensorTemperature",
            poll_priority=1,
            poll_enabled=1,
            unit="°C",
            description="Outdoor temperature sensor",
        ))
        assert dp_id is not None

        dps = run(store.get_datapoints())
        assert len(dps) == 1
        assert dps[0]["name"] == "OutdoorTemp"

    def test_update_priority(self, store):
        run(store.upsert_ecu(0x68, "Heater", '{}', '[]'))
        dp_id = run(store.upsert_datapoint(
            ecu_address=0x68,
            did=1,
            name="OutdoorTemp",
            codec="SensorTemperature",
            poll_priority=1,
            poll_enabled=1,
        ))
        run(store.update_datapoint(dp_id, poll_priority=5))
        dps = run(store.get_datapoints())
        assert dps[0]["poll_priority"] == 5

    def test_filter_by_priority(self, store):
        run(store.upsert_ecu(0x68, "Heater", '{}', '[]'))
        run(store.upsert_datapoint(
            ecu_address=0x68, did=1, name="DP1",
            codec="c", poll_priority=1, poll_enabled=1,
        ))
        run(store.upsert_datapoint(
            ecu_address=0x68, did=2, name="DP2",
            codec="c", poll_priority=5, poll_enabled=1,
        ))
        dps = run(store.get_datapoints(poll_priority=5))
        assert len(dps) == 1
        assert dps[0]["name"] == "DP2"


# ---------------------------------------------------------------------------
# HA Entities
# ---------------------------------------------------------------------------

class TestHaEntities:
    def _add_dp(self, store):
        run(store.upsert_ecu(0x68, "Heater", '{}', '[]'))
        return run(store.upsert_datapoint(
            ecu_address=0x68, did=1, name="OutdoorTemp",
            codec="SensorTemperature", poll_priority=1, poll_enabled=1,
        ))

    def test_upsert_and_get(self, store):
        dp_id = self._add_dp(store)
        ha_id = run(store.upsert_ha_entity(
            dp_id=dp_id,
            entity_type="sensor",
            unique_id="open3e_outdoor_temp",
            name="Outdoor Temperature",
            device_class="temperature",
            unit="°C",
            enabled=1,
        ))
        assert ha_id is not None
        entities = run(store.get_ha_entities())
        assert len(entities) == 1
        assert entities[0]["unique_id"] == "open3e_outdoor_temp"

    def test_enable_disable(self, store):
        dp_id = self._add_dp(store)
        ha_id = run(store.upsert_ha_entity(
            dp_id=dp_id,
            entity_type="sensor",
            unique_id="open3e_outdoor_temp",
            name="Outdoor Temperature",
            device_class="temperature",
            unit="°C",
            enabled=1,
        ))
        run(store.update_ha_entity(ha_id, enabled=0))
        enabled_entities = run(store.get_ha_entities(enabled=1))
        assert len(enabled_entities) == 0
        all_entities = run(store.get_ha_entities())
        assert len(all_entities) == 1


# ---------------------------------------------------------------------------
# MQTT Mappings
# ---------------------------------------------------------------------------

class TestMqttMappings:
    def _add_dp(self, store):
        run(store.upsert_ecu(0x68, "Heater", '{}', '[]'))
        return run(store.upsert_datapoint(
            ecu_address=0x68, did=1, name="OutdoorTemp",
            codec="SensorTemperature", poll_priority=1, poll_enabled=1,
        ))

    def test_upsert_and_get(self, store):
        dp_id = self._add_dp(store)
        run(store.upsert_mqtt_mapping(
            dp_id=dp_id,
            topic="open3e/outdoor_temp",
            enabled=1,
        ))
        mappings = run(store.get_mqtt_mappings())
        assert len(mappings) == 1
        assert mappings[0]["topic"] == "open3e/outdoor_temp"


# ---------------------------------------------------------------------------
# Backups
# ---------------------------------------------------------------------------

class TestBackup:
    def test_create_and_list(self, store):
        filename = run(store.create_backup())
        assert filename.endswith(".db")
        backups = run(store.list_backups())
        filenames = [b["filename"] for b in backups]
        assert filename in filenames

    def test_delete(self, store):
        filename = run(store.create_backup())
        run(store.delete_backup(filename))
        backups = run(store.list_backups())
        filenames = [b["filename"] for b in backups]
        assert filename not in filenames

    def test_backup_path(self, store):
        filename = run(store.create_backup())
        path = run(store.get_backup_path(filename))
        assert path.exists()
        assert path.name == filename

    def test_invalid_filename_rejected(self, store):
        with pytest.raises(ValueError):
            run(store.get_backup_path("bad filename!.db"))

    def test_path_traversal_rejected(self, store):
        with pytest.raises(ValueError):
            run(store.get_backup_path("../../etc/passwd"))


# ---------------------------------------------------------------------------
# Schema version
# ---------------------------------------------------------------------------

class TestSchemaVersion:
    def test_initial_version(self, store):
        version = run(store.get_schema_version())
        assert version == 2
