import pytest
from open3e.web.ha_discovery import infer_ha_entity, build_discovery_payload, build_removal_payload


class TestInferHaEntity:
    def test_infer_temperature(self):
        result = infer_ha_entity("FlowTemperatureSensor", "O3EComplexType", False)
        assert result is not None
        assert result["ha_component"] == "sensor"
        assert result["device_class"] == "temperature"
        assert result["unit"] == "\u00b0C"
        assert result["sub_field"] == "Actual"
        assert "Flow Temperature Sensor" in result["entity_name"]

    def test_infer_pressure(self):
        result = infer_ha_entity("WaterPressureSensor", "O3EComplexType", False)
        assert result is not None
        assert result["ha_component"] == "sensor"
        assert result["device_class"] == "pressure"
        assert result["unit"] == "bar"

    def test_infer_setpoint_writable(self):
        result = infer_ha_entity("DomesticHotWaterTemperatureSetpoint", "O3EInt16", True)
        assert result is not None
        assert result["ha_component"] == "number"

    def test_infer_enum_operation_mode(self):
        result = infer_ha_entity("ExternalDomesticHotWaterTargetOperationMode", "O3EEnum", False)
        assert result is not None
        assert result["ha_component"] == "sensor"  # enums mapped as sensor

    def test_infer_pump(self):
        result = infer_ha_entity("DomesticHotWaterCirculationPump", "O3EBool", False)
        assert result is not None
        assert result["ha_component"] == "sensor"  # pumps mapped as sensor with pump icon

    def test_infer_unknown_returns_none(self):
        result = infer_ha_entity("SomeRandomDatapoint", "RawCodec", False)
        assert result is None

    def test_infer_energy(self):
        result = infer_ha_entity("EnergyConsumptionCentralHeating", "O3EComplexType", False)
        assert result is not None
        assert result["ha_component"] == "sensor"
        assert result["device_class"] == "energy"

    def test_infer_battery(self):
        result = infer_ha_entity("ElectricalEnergyStorageStateOfCharge", "O3EInt32", False)
        assert result is not None
        assert result["device_class"] == "battery"


class TestBuildDiscoveryPayload:
    def test_basic_payload(self):
        entity = {
            "ha_component": "sensor",
            "device_class": "temperature",
            "unit": "\u00b0C",
            "icon": "mdi:thermometer",
            "entity_name": "Flow Temperature Sensor",
            "sub_field": "Actual",
            "did": 268,
            "dp_name": "FlowTemperatureSensor",
        }
        topic, payload = build_discovery_payload(entity, 0x680, "vitocal", "HPMUMASTER")
        assert "homeassistant/sensor/o3e_680_268_actual/config" == topic
        assert payload["unique_id"] == "o3e_680_268_actual"
        assert payload["state_topic"] == "open3e/268_FlowTemperatureSensor/Actual"
        assert payload["device"]["manufacturer"] == "Viessmann"
        assert payload["device"]["identifiers"] == ["o3e_680"]
        assert payload["device_class"] == "temperature"
        assert payload["unit_of_measurement"] == "\u00b0C"

    def test_writable_has_command_topic(self):
        entity = {
            "ha_component": "number",
            "device_class": "temperature",
            "unit": "\u00b0C",
            "icon": "mdi:thermostat",
            "entity_name": "DHW Setpoint",
            "sub_field": None,
            "did": 396,
            "dp_name": "DomesticHotWaterTemperatureSetpoint",
        }
        topic, payload = build_discovery_payload(entity, 0x680, "vitocal", "HPMUMASTER")
        assert "command_topic" in payload
        assert payload["command_topic"].endswith("/set")


class TestBuildRemovalPayload:
    def test_removal(self):
        entity = {"ha_component": "sensor", "did": 268, "sub_field": "Actual"}
        topic, payload = build_removal_payload(entity, 0x680)
        assert "homeassistant/sensor/o3e_680_268_actual/config" == topic
        assert payload == b""
