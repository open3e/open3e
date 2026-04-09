"""Home Assistant MQTT discovery — smart defaults and payload builder."""

import fnmatch
from typing import Optional

INFERENCE_RULES = [
    # (name_pattern, codec_types, ha_component, device_class, unit, icon)
    #
    # IMPORTANT: Order matters! More specific patterns must come before generic ones.
    # "CurrentPower" must match Power before Energy. "Percent" must match before generic.

    # --- Instantaneous power (W) — must come BEFORE energy rules ---
    ("*CurrentPower*", ["O3EInt16", "O3EInt32", "O3EComplexType"], "sensor", "power", "W", "mdi:flash"),
    ("*CurrentElectricalPower*", ["O3EInt16", "O3EInt32", "O3EComplexType"], "sensor", "power", "W", "mdi:flash"),
    ("*PowerAc*", ["O3EComplexType", "O3EInt32"], "sensor", "power", "W", "mdi:flash"),
    ("*PowerDc*", ["O3EComplexType", "O3EInt32"], "sensor", "power", "W", "mdi:flash"),
    ("*ThermalPower*", ["O3EComplexType"], "sensor", "power", "W", "mdi:fire"),
    ("*ThermalCapacity*", ["O3EComplexType", "O3EInt16", "O3EInt32"], "sensor", "power", "W", "mdi:fire"),
    ("*MaximumNominalPower*", ["O3EComplexType", "O3EInt32"], "sensor", "power", "W", "mdi:flash"),
    ("*CurrentMaximumPower*", ["O3EComplexType", "O3EInt32"], "sensor", "power", "W", "mdi:flash"),

    # --- Percent values ---
    ("*Percent*", ["O3EComplexType", "O3EInt8", "O3EByteVal", "O3EInt16"], "sensor", None, "%", "mdi:percent"),
    ("*StateOfCharge*", ["O3EInt8", "O3EByteVal", "O3EInt16", "O3EInt32"], "sensor", "battery", "%", "mdi:battery"),

    # --- Voltage ---
    ("*Voltage*", ["O3EComplexType", "O3EInt16", "O3EInt32", "RawCodec"], "sensor", "voltage", "V", "mdi:flash"),

    # --- Current (Ampere) ---
    ("*StringCurrent*", ["O3EComplexType"], "sensor", "current", "A", "mdi:current-ac"),
    ("*InverterCurrent*", ["O3EComplexType", "O3EInt16"], "sensor", "current", "A", "mdi:current-ac"),

    # --- Photovoltaic ---
    ("*Photovoltaic*Power*", ["O3EComplexType", "O3EInt32"], "sensor", "power", "W", "mdi:solar-panel"),
    ("*Photovoltaic*", ["O3EComplexType", "O3EInt32"], "sensor", None, None, "mdi:solar-panel"),

    # --- Flow rate ---
    # AllengraSensor has sub-fields: Actual=flow rate, Temperature=temp of flow sensor
    # The main entity uses Actual (flow rate). Temperature gets a separate entity via apply-defaults.
    ("*Allengra*", ["O3EComplexType"], "sensor", None, "L/h", "mdi:water-pump"),
    ("*FlowRate*", ["O3EComplexType", "O3EInt16", "O3EInt32"], "sensor", None, "L/h", "mdi:water-pump"),

    # --- Pressure ---
    ("*Pressure*", ["O3EComplexType", "O3EInt16"], "sensor", "pressure", "bar", "mdi:gauge"),

    # --- Temperature sensors ---
    ("*Temperature*", ["O3EComplexType", "O3EInt16"], "sensor", "temperature", "\u00b0C", "mdi:thermometer"),
    ("*TemperatureSensor*", ["O3EComplexType"], "sensor", "temperature", "\u00b0C", "mdi:thermometer"),
    ("*Sensor", ["O3EComplexType"], "sensor", "temperature", "\u00b0C", "mdi:thermometer"),

    # --- Energy (cumulative kWh) ---
    ("*EnergyConsumption*", ["O3EComplexType"], "sensor", "energy", "kWh", "mdi:lightning-bolt"),
    ("*GeneratedOutput*", ["O3EComplexType"], "sensor", "energy", "kWh", "mdi:solar-power"),
    ("*Generated*Output*", ["O3EComplexType"], "sensor", "energy", "kWh", "mdi:solar-power"),

    # --- Generic power (W) ---
    ("*Power*", ["O3EInt16", "O3EInt32", "O3EComplexType"], "sensor", "power", "W", "mdi:flash"),

    # --- Generic energy (kWh) — after power rules ---
    ("*Energy*", ["O3EInt32", "O3EInt64", "O3EComplexType"], "sensor", "energy", "kWh", "mdi:lightning-bolt"),

    # --- Flow and water ---
    ("*FlowMeter*", ["O3EInt32", "O3EComplexType"], "sensor", "water", "L", "mdi:water"),

    # --- Signal strength ---
    ("*SignalStrength*", ["O3EByteVal", "O3EInt8", "O3EInt16"], "sensor", "signal_strength", "dBm", "mdi:signal"),

    # --- Frequency ---
    ("*Frequency*", ["O3EInt16", "O3EInt32", "O3EComplexType"], "sensor", "frequency", "Hz", "mdi:sine-wave"),
    ("*Speed*", ["O3EInt16", "O3EInt32"], "sensor", None, "rpm", "mdi:fan"),

    # --- Fans ---
    ("*Fan*", ["O3EByteVal", "O3EInt8", "O3EInt16", "O3EComplexType"], "sensor", None, "%", "mdi:fan"),

    # --- Pumps ---
    ("*Pump*", ["O3EComplexType", "O3EBool", "O3EByteVal"], "sensor", None, None, "mdi:pump"),

    # --- Valves ---
    ("*Valve*", ["O3EComplexType", "O3EInt8", "O3EByteVal"], "sensor", None, "%", "mdi:valve"),

    # --- Setpoints ---
    ("*TemperatureSetpoint*", ["O3EComplexType", "O3EInt16"], "sensor", "temperature", "\u00b0C", "mdi:thermostat"),
    ("*Setpoint*", ["O3EComplexType", "O3EInt16"], "sensor", None, None, "mdi:thermostat"),
    ("*Hysteresis*", ["O3EComplexType"], "sensor", "temperature", "\u00b0C", "mdi:thermostat"),

    # --- Operation modes and states ---
    ("*OperationMode*", ["O3EEnum", "O3EComplexType"], "sensor", None, None, "mdi:cog"),
    ("*OperationState*", ["O3EEnum", "O3EComplexType"], "sensor", None, None, "mdi:toggle-switch"),
    ("*QuickMode*", ["O3EComplexType"], "sensor", None, None, "mdi:flash"),

    # --- Heating curves ---
    ("*HeatingCurve*", ["O3EComplexType"], "sensor", None, None, "mdi:chart-line"),
    ("*CurveAdaption*", ["O3EComplexType"], "sensor", None, None, "mdi:chart-line"),

    # --- Software/Hardware/Identity ---
    ("*Version*", ["O3ESoftVers"], "sensor", None, None, "mdi:information"),
    ("*MacAddress*", ["O3EMacAddr"], "sensor", None, None, "mdi:ethernet"),
    ("*Identification*", ["O3EComplexType", "O3EUtf8", "O3EByteVal"], "sensor", None, None, "mdi:card-account-details"),

    # --- Time and schedule ---
    ("*TimeSchedule*", ["O3EList"], "sensor", None, None, "mdi:clock-outline"),
    ("*Date*", ["O3ESdate"], "sensor", None, None, "mdi:calendar"),
    ("*Time*", ["O3EStime"], "sensor", None, None, "mdi:clock"),

    # --- Catch-all by codec type ---
    ("*", ["O3EEnum"], "sensor", None, None, "mdi:information"),
    ("*", ["O3EBool"], "binary_sensor", None, None, "mdi:toggle-switch"),
    ("*", ["O3EByteVal", "O3EInt8"], "sensor", None, None, "mdi:numeric"),
    ("*", ["O3EInt16", "O3EInt32", "O3EInt64"], "sensor", None, None, "mdi:numeric"),
]


# ---------------------------------------------------------------------------
# Writable entity definitions for HA (number, select, switch, button)
# Each entry: did -> {component, sub_field, min, max, step, options, icon, group}
# ---------------------------------------------------------------------------

# Enum mappings: text → numeric ID (for MQTT command handler reverse lookup)
# Corrected OpStates enum labels per open3e/open3e#145
OPSTATES_ID_TO_TEXT = {
    0: "Off", 1: "Heating Reduced", 2: "Heating Normal", 3: "Heating Comfort",
    4: "Fixed Flow Temperature", 5: "Frost Protection",
    6: "Energy Saving Reduced", 7: "Energy Saving Normal",
    8: "Energy Saving Comfort", 9: "Cooling Reduced",
    10: "Cooling Normal", 11: "Cooling Comfort", 255: "Unknown",
}


WRITABLE_ENTITIES = {
    # --- DHW Quick Action ---
    1006: {"component": "switch", "sub_field": "Required",
           "name": "One-Time DHW Heating",
           "icon": "mdi:water-boiler", "group": "Hot Water",
           "state_on": "on", "state_off": "off",
           "payload_on": "ON", "payload_off": "OFF"},

    # --- DHW Temperature ---
    396: {"component": "number", "device_class": "temperature", "unit": "\u00b0C",
          "min": 0, "max": 60, "step": 0.5, "icon": "mdi:water-thermometer", "group": "Hot Water"},
    2257: {"component": "number", "device_class": "temperature", "unit": "\u00b0C",
           "min": -10, "max": 10, "step": 0.5, "icon": "mdi:thermometer-plus", "group": "Hot Water"},
    1167: {"component": "number", "device_class": "temperature", "unit": "\u00b0C",
           "min": 0, "max": 60, "step": 0.5, "icon": "mdi:water-thermometer", "group": "Hot Water"},
    874: {"component": "number", "sub_field": "Setpoint", "device_class": "temperature", "unit": "\u00b0C",
          "min": 50, "max": 70, "step": 0.5, "icon": "mdi:shield-bug", "group": "Hot Water"},

    # --- Circuit Operation Mode (Heating / Off / Cooling) ---
    # Writing Mode to OperationState DIDs changes the heating mode directly.
    # State sub-field is read-only (computed from Mode + schedule).
    "1415_mode": {"did": 1415, "component": "select", "sub_field": "Mode",
                  "name": "Mixer 1 Operation Mode", "icon": "mdi:thermostat",
                  "options": ["Off", "Heating", "Cooling"],
                  "_id_to_text": {0: "Off", 1: "Heating", 5: "Cooling"},
                  "group": "Heating Circuit 1"},
    "1416_mode": {"did": 1416, "component": "select", "sub_field": "Mode",
                  "name": "Mixer 2 Operation Mode", "icon": "mdi:thermostat",
                  "options": ["Off", "Heating", "Cooling"],
                  "_id_to_text": {0: "Off", 1: "Heating", 5: "Cooling"},
                  "group": "Heating Circuit 2"},
    "531_mode": {"did": 531, "component": "select", "sub_field": "Mode",
                 "name": "DHW Operation Mode", "icon": "mdi:water-boiler",
                 "options": ["Off", "Heating"],
                 "_id_to_text": {0: "Off", 1: "Heating"},
                 "group": "Hot Water"},

    # --- External Target Operation Mode (enable/disable external control) ---
    "537_mode": {"did": 537, "component": "switch", "sub_field": "Mode",
                 "name": "Mixer 1 External Control", "icon": "mdi:thermostat",
                 "state_on": "1", "state_off": "0",
                 "payload_on": "1", "payload_off": "0",
                 "group": "Heating Circuit 1"},
    "538_mode": {"did": 538, "component": "switch", "sub_field": "Mode",
                 "name": "DHW External Control", "icon": "mdi:water-boiler",
                 "state_on": "1", "state_off": "0",
                 "payload_on": "1", "payload_off": "0",
                 "group": "Hot Water"},
    "1612_mode": {"did": 1612, "component": "switch", "sub_field": "Mode",
                  "name": "Mixer 2 External Control", "icon": "mdi:thermostat",
                  "state_on": "1", "state_off": "0",
                  "payload_on": "1", "payload_off": "0",
                  "group": "Heating Circuit 2"},

    # --- DHW Pump ---
    491: {"component": "select", "sub_field": "State", "icon": "mdi:pump",
          "options": ["0", "1"], "option_labels": {"0": "Off", "1": "On"}, "group": "Hot Water"},
    497: {"component": "select", "sub_field": "Mode", "icon": "mdi:pump",
          "options": ["0", "1", "2"], "option_labels": {"0": "Off", "1": "Eco", "2": "Comfort"}, "group": "Hot Water"},

    # --- DHW Pump Limits ---
    1101: {"component": "number", "sub_field": "Setpoint", "unit": "%",
           "min": 0, "max": 100, "step": 1, "icon": "mdi:pump", "group": "Hot Water"},

    # --- DHW Setpoint MetaData ---
    504: {"component": "number", "sub_field": "DefaultBufferTemperature", "device_class": "temperature", "unit": "\u00b0C",
          "min": 10, "max": 60, "step": 0.5, "icon": "mdi:water-thermometer", "group": "Hot Water"},

    # --- Heating Circuit 1 ---
    424: {"component": "number", "sub_field": "Comfort", "device_class": "temperature", "unit": "\u00b0C",
          "min": 5, "max": 30, "step": 0.5, "icon": "mdi:home-thermometer", "group": "Heating Circuit 1"},
    "424_standard": {"did": 424, "component": "number", "sub_field": "Standard", "device_class": "temperature", "unit": "\u00b0C",
                     "min": 5, "max": 30, "step": 0.5, "icon": "mdi:home-thermometer", "group": "Heating Circuit 1"},
    "424_reduced": {"did": 424, "component": "number", "sub_field": "Reduced", "device_class": "temperature", "unit": "\u00b0C",
                    "min": 5, "max": 30, "step": 0.5, "icon": "mdi:home-thermometer-outline", "group": "Heating Circuit 1"},
    1643: {"component": "number", "device_class": "temperature", "unit": "\u00b0C",
           "min": 5, "max": 30, "step": 0.5, "icon": "mdi:thermostat", "group": "Heating Circuit 1"},
    1102: {"component": "number", "sub_field": "Setpoint", "unit": "%",
           "min": 0, "max": 100, "step": 1, "icon": "mdi:pump", "group": "Heating Circuit 1"},
    2546: {"component": "number", "device_class": "temperature", "unit": "\u00b0C",
           "min": 18, "max": 30, "step": 0.5, "icon": "mdi:snowflake-thermometer", "group": "Heating Circuit 1"},

    # --- Heating Circuit 2 ---
    426: {"component": "number", "sub_field": "Comfort", "device_class": "temperature", "unit": "\u00b0C",
          "min": 5, "max": 30, "step": 0.5, "icon": "mdi:home-thermometer", "group": "Heating Circuit 2"},
    "426_standard": {"did": 426, "component": "number", "sub_field": "Standard", "device_class": "temperature", "unit": "\u00b0C",
                     "min": 5, "max": 30, "step": 0.5, "icon": "mdi:home-thermometer", "group": "Heating Circuit 2"},
    "426_reduced": {"did": 426, "component": "number", "sub_field": "Reduced", "device_class": "temperature", "unit": "\u00b0C",
                    "min": 5, "max": 30, "step": 0.5, "icon": "mdi:home-thermometer-outline", "group": "Heating Circuit 2"},
    1644: {"component": "number", "device_class": "temperature", "unit": "\u00b0C",
           "min": 5, "max": 30, "step": 0.5, "icon": "mdi:thermostat", "group": "Heating Circuit 2"},
    988: {"component": "number", "device_class": "temperature", "unit": "\u00b0C",
          "min": 20, "max": 60, "step": 0.5, "icon": "mdi:thermostat", "group": "Heating Circuit 2"},
    1103: {"component": "number", "sub_field": "Setpoint", "unit": "%",
           "min": 0, "max": 100, "step": 1, "icon": "mdi:pump", "group": "Heating Circuit 2"},
    2547: {"component": "number", "device_class": "temperature", "unit": "\u00b0C",
           "min": 18, "max": 30, "step": 0.5, "icon": "mdi:snowflake-thermometer", "group": "Heating Circuit 2"},

    # --- Heating Circuit 3 ---
    428: {"component": "number", "sub_field": "Comfort", "device_class": "temperature", "unit": "\u00b0C",
          "min": 5, "max": 30, "step": 0.5, "icon": "mdi:home-thermometer", "group": "Heating Circuit 3"},
    1104: {"component": "number", "sub_field": "Setpoint", "unit": "%",
           "min": 0, "max": 100, "step": 1, "icon": "mdi:pump", "group": "Heating Circuit 3"},
    2548: {"component": "number", "device_class": "temperature", "unit": "\u00b0C",
           "min": 18, "max": 30, "step": 0.5, "icon": "mdi:snowflake-thermometer", "group": "Heating Circuit 3"},

    # --- Heating Circuit 4 ---
    430: {"component": "number", "sub_field": "Comfort", "device_class": "temperature", "unit": "\u00b0C",
          "min": 5, "max": 30, "step": 0.5, "icon": "mdi:home-thermometer", "group": "Heating Circuit 4"},
    1105: {"component": "number", "sub_field": "Setpoint", "unit": "%",
           "min": 0, "max": 100, "step": 1, "icon": "mdi:pump", "group": "Heating Circuit 4"},
    2549: {"component": "number", "device_class": "temperature", "unit": "\u00b0C",
           "min": 18, "max": 30, "step": 0.5, "icon": "mdi:snowflake-thermometer", "group": "Heating Circuit 4"},

    # --- System ---
    1100: {"component": "number", "sub_field": "Setpoint", "unit": "%",
           "min": 0, "max": 100, "step": 1, "icon": "mdi:pump", "group": "System"},
    2543: {"component": "number", "sub_field": None, "device_class": "temperature", "unit": "\u00b0C",
           "min": -10, "max": 10, "step": 0.5, "icon": "mdi:transmission-tower", "group": "System"},
    2214: {"component": "number", "sub_field": "DischargeLimit", "unit": "%",
           "min": 0, "max": 100, "step": 1, "icon": "mdi:battery-charging", "group": "System"},

    # --- Flow Temperature Limits ---
    1192: {"component": "number", "sub_field": "Maximum", "device_class": "temperature", "unit": "\u00b0C",
           "min": 20, "max": 80, "step": 1, "icon": "mdi:thermometer-chevron-up", "group": "Heating Circuit 1"},
    1193: {"component": "number", "sub_field": "Maximum", "device_class": "temperature", "unit": "\u00b0C",
           "min": 20, "max": 80, "step": 1, "icon": "mdi:thermometer-chevron-up", "group": "Heating Circuit 2"},
}


def _humanize(name: str) -> str:
    """Convert CamelCase DID name to human-readable: 'FlowTemperatureSensor' -> 'Flow Temperature Sensor'."""
    import re
    return re.sub(r'(?<=[a-z])(?=[A-Z])', ' ', name)


def infer_ha_entity(dp_name: str, codec_type: str, is_writable: bool) -> Optional[dict]:
    """Infer HA entity config from datapoint name and codec type.

    Returns dict with: ha_component, device_class, unit, icon, sub_field, entity_name
    Returns None if no rule matches.
    """
    # RawCodec produces hex blobs that exceed HA's 255-char state limit — skip entirely
    if codec_type == "RawCodec":
        return None

    for pattern, codec_types, component, device_class, unit, icon in INFERENCE_RULES:
        if fnmatch.fnmatch(dp_name, pattern) and codec_type in codec_types:
            sub_field = "Actual" if codec_type == "O3EComplexType" else None
            if is_writable and component == "sensor":
                component = "number"
            return {
                "ha_component": component,
                "device_class": device_class,
                "unit": unit,
                "icon": icon,
                "sub_field": sub_field,
                "entity_name": _humanize(dp_name),
            }
    return None


def build_discovery_payload(
    entity: dict, ecu_address: int, ecu_name: str, ecu_prop: str,
    topic_prefix: str = "open3e", ha_prefix: str = "homeassistant",
    sw_version: str = ""
) -> tuple:
    """Build HA MQTT discovery topic and payload.

    Args:
        entity: dict with keys from ha_entities table (ha_component, device_class, unit, icon,
                entity_name, sub_field, did, dp_name, ecu_address)
        ecu_address: ECU address integer
        ecu_name: ECU name string
        ecu_prop: device property string (e.g., "HPMUMASTER")
        topic_prefix: MQTT topic prefix
        ha_prefix: HA discovery prefix
        sw_version: software version string

    Returns: (topic_str, payload_dict)
    """
    component = entity.get("ha_component") or entity.get("entity_type") or "sensor"
    did = entity["did"]
    sub = entity.get("sub_field") or ""
    ecu_hex = format(ecu_address, "03x")

    # Use unique_id from DB if available, otherwise build it
    object_id = entity.get("unique_id")
    if not object_id:
        obj_parts = ["o3e", ecu_hex, str(did)]
        if sub:
            obj_parts.append(sub.lower().replace(" ", "_"))
        object_id = "_".join(obj_parts)
    # Sanitize: MQTT topics must not contain spaces or special chars
    object_id = object_id.replace(" ", "_")

    # State topic — must match the actual MQTT data publish topic
    dp_name = entity.get("dp_name") or entity.get("name") or "DID_" + str(did)
    base_topic = "{}/{}_{}".format(topic_prefix, did, dp_name)

    # Use stored sub_field for the state topic path
    if sub:
        state_topic = base_topic + "/" + sub
    else:
        state_topic = base_topic

    # Discovery topic
    topic = "{}/{}/{}/config".format(ha_prefix, component, object_id)

    payload = {
        "name": entity.get("entity_name") or entity.get("name") or dp_name,
        "unique_id": object_id,
        "object_id": object_id,
        "state_topic": state_topic,
        "enabled_by_default": True,
        "device": {
            "identifiers": ["o3e_" + ecu_hex],
            "name": "{} ({})".format(ecu_name, "0x" + ecu_hex),
            "manufacturer": "Viessmann",
            "model": ecu_prop or "Unknown",
        },
        "origin": {
            "name": "open3e",
            "sw_version": sw_version or "0.5.10",
            "support_url": "https://github.com/open3e/open3e",
        },
        "availability": [{
            "topic": topic_prefix + "/LWT",
            "payload_available": "online",
            "payload_not_available": "offline",
        }],
    }
    if sw_version:
        payload["device"]["sw_version"] = sw_version
    if entity.get("device_class"):
        payload["device_class"] = entity["device_class"]
    if entity.get("unit"):
        payload["unit_of_measurement"] = entity["unit"]
    if entity.get("icon"):
        payload["icon"] = entity["icon"]

    # Writable entities — add command_topic and type-specific fields
    writable_cfg = entity.get("writable_cfg")
    if writable_cfg or component in ("number", "select", "switch", "button"):
        cmd_topic = state_topic + "/set"
        payload["command_topic"] = cmd_topic

        if component == "number":
            if writable_cfg:
                if "min" in writable_cfg:
                    payload["min"] = writable_cfg["min"]
                if "max" in writable_cfg:
                    payload["max"] = writable_cfg["max"]
                if "step" in writable_cfg:
                    payload["step"] = writable_cfg["step"]

        elif component == "select":
            if writable_cfg and "options" in writable_cfg:
                payload["options"] = writable_cfg["options"]
                # Add value_template to map integer enum values to text labels
                id_to_text = writable_cfg.get("_id_to_text")
                if id_to_text:
                    pairs = ", ".join(
                        "{}: '{}'".format(k, v.replace("'", "\\'"))
                        for k, v in sorted(id_to_text.items())
                    )
                    tpl = "{% set m = {" + pairs + "} %}{{ m.get(value | int(-1), value) }}"
                    payload["value_template"] = tpl

        elif component == "button":
            if writable_cfg and "payload_press" in writable_cfg:
                payload["payload_press"] = writable_cfg["payload_press"]

        elif component == "switch":
            payload["payload_on"] = writable_cfg.get("payload_on", "ON") if writable_cfg else "ON"
            payload["payload_off"] = writable_cfg.get("payload_off", "OFF") if writable_cfg else "OFF"
            if writable_cfg and "state_on" in writable_cfg:
                payload["state_on"] = writable_cfg["state_on"]
            if writable_cfg and "state_off" in writable_cfg:
                payload["state_off"] = writable_cfg["state_off"]

    return (topic, payload)


def build_removal_payload(entity: dict, ecu_address: int, ha_prefix: str = "homeassistant") -> tuple:
    """Build empty payload to remove entity from HA."""
    component = entity.get("ha_component") or entity.get("entity_type") or "sensor"
    did = entity["did"]
    sub = entity.get("sub_field") or ""
    ecu_hex = format(ecu_address, "03x")

    obj_parts = ["o3e", ecu_hex, str(did)]
    if sub:
        obj_parts.append(sub.lower())
    object_id = "_".join(obj_parts)

    topic = "{}/{}/{}/config".format(ha_prefix, component, object_id)
    return (topic, b"")
