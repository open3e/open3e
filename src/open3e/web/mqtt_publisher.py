"""MQTT publisher — connects to broker, publishes datapoint values and HA discovery."""

from __future__ import annotations

import base64
import json
import logging
import tempfile
import time
from typing import Any, Callable, Optional

import paho.mqtt.client as paho

logger = logging.getLogger(__name__)


class MqttPublisher:
    """Publishes CAN datapoint values to MQTT and manages HA discovery."""

    def __init__(self, store, on_status: Optional[Callable] = None):
        self.store = store
        self._on_status = on_status
        self._client: Optional[paho.Client] = None
        self._connected = False
        self._messages_published = 0
        self._topic_prefix = "open3e"
        self._format_string = "{didName}"
        self._mappings: dict = {}  # (ecu, did) -> mapping dict
        self._ca_cert_path: Optional[str] = None
        self._last_published: dict = {}  # (ecu, did) -> {"value": ..., "ts": ...}
        self._republish_interval = 60  # seconds

    @property
    def connected(self) -> bool:
        if self._client:
            return self._client.is_connected()
        return False

    @property
    def messages_published(self) -> int:
        return self._messages_published

    async def configure(self) -> bool:
        """Read MQTT settings from store. Returns False if host not configured."""
        host = await self.store.get_setting("mqtt_host")
        if not host:
            return False

        self._host = host
        self._port = int(await self.store.get_setting("mqtt_port", "1883"))
        self._user = await self.store.get_setting("mqtt_user")
        self._password = await self.store.get_setting("mqtt_password")
        self._tls_enabled = (await self.store.get_setting("mqtt_tls_enabled")) == "1"
        self._ca_cert_b64 = await self.store.get_setting("mqtt_ca_cert")
        self._topic_prefix = await self.store.get_setting("mqtt_topic_prefix", "vcal") or "vcal"
        self._format_string = await self.store.get_setting("mqtt_format_string", "{didNumber}_{didName}") or "{didNumber}_{didName}"
        self._client_id = await self.store.get_setting("mqtt_client_id") or ("open3e_" + str(int(time.time() * 1000)))
        self._publish_json = (await self.store.get_setting("mqtt_publish_json", "1")) != "0"

        # Load MQTT mappings
        mappings = await self.store.get_mqtt_mappings(enabled=True)
        self._mappings = {}
        for m in mappings:
            key = (m["ecu_address"], m["did"])
            self._mappings[key] = m

        return True

    def start(self) -> None:
        """Connect to MQTT broker and start the network loop."""
        if self._client:
            self.stop()

        self._client = paho.Client(paho.CallbackAPIVersion.VERSION2, self._client_id)

        if self._user:
            self._client.username_pw_set(self._user, self._password or "")

        if self._tls_enabled and self._ca_cert_b64:
            try:
                cert_bytes = base64.b64decode(self._ca_cert_b64)
                tmp = tempfile.NamedTemporaryFile(suffix=".pem", delete=False)
                tmp.write(cert_bytes)
                tmp.close()
                self._ca_cert_path = tmp.name
                self._client.tls_set(ca_certs=self._ca_cert_path)
            except Exception as e:
                logger.error("TLS setup failed: %s", e)

        self._client.on_connect = self._on_connect
        self._client.on_disconnect = self._on_disconnect
        self._client.on_message = self._on_message
        self._client.will_set(self._topic_prefix + "/LWT", "offline", qos=0, retain=True)
        self._client.reconnect_delay_set(min_delay=1, max_delay=30)

        try:
            self._client.connect(self._host, self._port)
            self._client.loop_start()
        except Exception as e:
            logger.error("MQTT connect failed: %s", e)
            self._emit_status(False)

    def stop(self) -> None:
        """Disconnect and stop the network loop."""
        if self._client:
            try:
                self._client.publish(self._topic_prefix + "/LWT", "offline", qos=0, retain=True)
                self._client.disconnect()
                self._client.loop_stop()
            except Exception:
                pass
            self._client = None
        self._connected = False
        self._emit_status(False)

    async def reconfigure(self) -> None:
        """Stop, reload settings, reconnect."""
        self.stop()
        if await self.configure():
            self.start()

    def _emit_status(self, connected: bool) -> None:
        if connected == self._connected:
            return  # no change, don't spam WebSocket
        self._connected = connected
        if self._on_status:
            try:
                self._on_status({"type": "mqtt_status", "connected": connected})
            except Exception:
                pass

    def _on_connect(self, client, userdata, flags, reason_code, properties):
        logger.info("MQTT connected")
        self._emit_status(True)
        client.publish(self._topic_prefix + "/LWT", "online", qos=0, retain=True)
        # Subscribe to command topics for writable entities
        # Subscribe to command topics for writable entities
        # +/set for direct DIDs, +/+/set for sub-field writes
        client.subscribe(self._topic_prefix + "/+/set")
        client.subscribe(self._topic_prefix + "/+/+/set")

    def _on_disconnect(self, client, userdata, flags, reason_code, properties):
        logger.warning("MQTT disconnected: reason_code=%s flags=%s", reason_code, flags)
        self._emit_status(False)

    def _on_message(self, client, userdata, msg):
        """Handle incoming MQTT commands from HA for writable entities."""
        topic = msg.topic
        payload_str = msg.payload.decode("utf-8", errors="replace").strip()
        logger.info("MQTT command: %s = %s", topic, payload_str[:100])

        if not self._command_handler:
            return

        # Parse topic: {prefix}/{did}_{name}/set or {prefix}/{did}_{name}/{sub}/set
        prefix = self._topic_prefix + "/"
        if not topic.startswith(prefix) or not topic.endswith("/set"):
            return

        # Strip prefix and /set
        path = topic[len(prefix):-4]  # e.g. "396_DomesticHotWaterTemperatureSetpoint" or "424_Mixer.../Comfort"
        parts = path.split("/")

        # Extract DID from first part: "396_Name" -> 396
        did_part = parts[0]
        try:
            did = int(did_part.split("_")[0])
        except (ValueError, IndexError):
            logger.warning("Cannot parse DID from topic: %s", topic)
            return

        # Sub-field if present
        sub = parts[1] if len(parts) > 1 else None

        # Parse value
        try:
            value = json.loads(payload_str)
        except (json.JSONDecodeError, ValueError):
            # Try as number
            try:
                value = float(payload_str)
                if value == int(value):
                    value = int(value)
            except ValueError:
                value = payload_str  # string (e.g., "on"/"off")

        logger.info("HA write: DID=%s sub=%s value=%s", did, sub, value)
        self._command_handler(did, value, sub)

    _command_handler: Optional[Callable] = None

    def set_command_handler(self, handler: Callable) -> None:
        """Set callback for handling HA write commands."""
        self._command_handler = handler

    def publish_did_value(self, ecu: int, did: int, name: str, value: Any) -> None:
        """Publish a datapoint value to MQTT.

        Only publishes if MQTT mappings exist for this datapoint,
        or if no mappings are configured (publishes all polled values).
        """
        if not self._client or not self._connected:
            return

        # Skip long hex strings (RawCodec diagnostic data) — useless for HA
        if isinstance(value, str) and len(value) > 255:
            return

        key = (ecu, did)
        # If explicit mappings exist, only publish mapped datapoints
        if self._mappings and key not in self._mappings:
            return

        # Change detection: only publish if value changed or republish interval passed
        now = time.time()
        prev = self._last_published.get(key)
        if prev is not None:
            if prev["value"] == value and (now - prev["ts"]) < self._republish_interval:
                return  # unchanged and not time to re-publish yet

        mapping = self._mappings.get(key, {})
        custom_topic = mapping.get("custom_topic")
        publish_json = self._publish_json

        if custom_topic:
            topic = custom_topic
        else:
            formatted = self._format_string.format(
                didName=name, didNumber=did,
                ecuAddr=ecu, device=format(ecu, "03x"),
            )
            topic = self._topic_prefix + "/" + formatted

        try:
            if publish_json:
                self._client.publish(topic, json.dumps(value), retain=True)
            else:
                self._publish_split(topic, value)
            self._messages_published += 1
            self._last_published[key] = {"value": value, "ts": now}
        except Exception as e:
            logger.warning("MQTT publish error: %s", e)

    def _publish_split(self, base_topic: str, value: Any) -> None:
        """Split complex values into scalar sub-topics (retained for HA state)."""
        if isinstance(value, dict):
            # Enum-like dicts {ID: x, Text: y} — publish Text at parent level for HA
            if "Text" in value and "ID" in value and len(value) <= 3:
                self._client.publish(base_topic, str(value["Text"]), retain=True)
            for k, v in value.items():
                self._publish_split(base_topic + "/" + str(k), v)
        elif isinstance(value, list):
            for i, v in enumerate(value):
                self._publish_split(base_topic + "/" + str(i), v)
        else:
            self._client.publish(base_topic, str(value), retain=True)

    def publish_ha_discovery(self, entities: list, ecus: list,
                             topic_prefix: str, ha_prefix: str) -> None:
        """Publish HA discovery config for all enabled entities."""
        if not self._client or not self._connected:
            return

        from open3e.web.ha_discovery import build_discovery_payload, WRITABLE_ENTITIES

        ecu_map = {e["address"]: e for e in ecus}

        # Build writable lookup by DID for quick matching
        writable_by_did = {}
        for key, cfg in WRITABLE_ENTITIES.items():
            did = cfg.get("did", key if isinstance(key, int) else None)
            if did is not None:
                writable_by_did.setdefault(did, []).append(cfg)

        published = 0
        for entity in entities:
            ecu_addr = entity.get("ecu_address", 0)
            ecu_info = ecu_map.get(ecu_addr, {})

            # Check if this entity has a writable config
            did = entity.get("did")
            entity_type = entity.get("entity_type", "sensor")
            writable_cfg = None
            if did in writable_by_did and entity_type in ("number", "select", "switch", "button"):
                for cfg in writable_by_did[did]:
                    sub = cfg.get("sub_field") or ""
                    # Match by sub_field if present
                    uid = entity.get("unique_id", "")
                    if sub and sub.lower() in uid:
                        writable_cfg = cfg
                        break
                    elif not sub:
                        writable_cfg = cfg
                        break

            # Attach writable config to entity for payload builder
            entity_with_cfg = dict(entity)
            if writable_cfg:
                entity_with_cfg["writable_cfg"] = writable_cfg

            try:
                topic, payload = build_discovery_payload(
                    entity_with_cfg, ecu_addr,
                    ecu_info.get("name", hex(ecu_addr)),
                    ecu_info.get("device_prop", ""),
                    topic_prefix, ha_prefix,
                )
                self._client.publish(topic, json.dumps(payload), retain=True)
                published += 1
            except Exception as e:
                logger.warning("HA discovery publish failed for entity %s: %s", entity.get("unique_id"), e)
        logger.info("Published %d HA discovery messages", published)

    def remove_ha_entity(self, entity: dict, ecu_address: int, ha_prefix: str = "homeassistant") -> None:
        """Remove an entity from HA by publishing empty payload."""
        if not self._client or not self._connected:
            return

        from open3e.web.ha_discovery import build_removal_payload
        topic, payload = build_removal_payload(entity, ecu_address, ha_prefix)
        self._client.publish(topic, payload, retain=True)
