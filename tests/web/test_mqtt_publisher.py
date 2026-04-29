import asyncio
import pytest
from unittest.mock import MagicMock, AsyncMock, patch

from open3e.web.mqtt_publisher import MqttPublisher


@pytest.fixture
def event_loop():
    loop = asyncio.new_event_loop()
    yield loop
    loop.close()


def run(coro):
    return asyncio.get_event_loop().run_until_complete(coro)


def make_store(host=None):
    store = MagicMock()
    settings = {
        "mqtt_host": host,
        "mqtt_port": "1883",
        "mqtt_user": "user",
        "mqtt_password": "pass",
        "mqtt_tls_enabled": "0",
        "mqtt_ca_cert": None,
        "mqtt_topic_prefix": "open3e",
        "mqtt_format_string": "{didName}",
        "mqtt_client_id": "test_client",
    }
    store.get_setting = AsyncMock(side_effect=lambda k, d=None: settings.get(k, d))
    store.get_mqtt_mappings = AsyncMock(return_value=[])
    return store


class TestConfigure:
    def test_no_host_returns_false(self):
        store = make_store(host=None)
        pub = MqttPublisher(store)
        assert run(pub.configure()) is False

    def test_with_host_returns_true(self):
        store = make_store(host="192.168.1.1")
        pub = MqttPublisher(store)
        assert run(pub.configure()) is True


class TestPublishDidValue:
    @patch("open3e.web.mqtt_publisher.paho.Client")
    def test_publish_formatted_topic(self, MockClient):
        store = make_store(host="192.168.1.1")
        pub = MqttPublisher(store)
        run(pub.configure())

        mock_client = MagicMock()
        pub._client = mock_client
        pub._connected = True

        pub.publish_did_value(0x680, 268, "FlowTemperatureSensor", {"Actual": 27.2})
        mock_client.publish.assert_called_once()
        topic = mock_client.publish.call_args[0][0]
        assert topic == "open3e/FlowTemperatureSensor"

    @patch("open3e.web.mqtt_publisher.paho.Client")
    def test_disabled_mapping_skipped(self, MockClient):
        store = make_store(host="192.168.1.1")
        pub = MqttPublisher(store)
        run(pub.configure())

        mock_client = MagicMock()
        pub._client = mock_client
        pub._connected = True
        # Set mappings that don't include DID 268
        pub._mappings = {(0x680, 999): {"enabled": True}}

        pub.publish_did_value(0x680, 268, "FlowTemp", 27.2)
        mock_client.publish.assert_not_called()

    @patch("open3e.web.mqtt_publisher.paho.Client")
    def test_json_mode(self, MockClient):
        store = make_store(host="192.168.1.1")
        pub = MqttPublisher(store)
        run(pub.configure())

        mock_client = MagicMock()
        pub._client = mock_client
        pub._connected = True

        pub.publish_did_value(0x680, 268, "FlowTemp", {"Actual": 27.2})
        payload = mock_client.publish.call_args[0][1]
        import json
        assert json.loads(payload) == {"Actual": 27.2}


class TestProperties:
    def test_connected_default_false(self):
        store = make_store()
        pub = MqttPublisher(store)
        assert pub.connected is False

    def test_messages_published_default_zero(self):
        store = make_store()
        pub = MqttPublisher(store)
        assert pub.messages_published == 0

    @patch("open3e.web.mqtt_publisher.paho.Client")
    def test_counter_increments(self, MockClient):
        store = make_store(host="192.168.1.1")
        pub = MqttPublisher(store)
        run(pub.configure())

        mock_client = MagicMock()
        pub._client = mock_client
        pub._connected = True

        pub.publish_did_value(0x680, 268, "FlowTemp", 27.2)
        pub.publish_did_value(0x680, 269, "ReturnTemp", 25.0)
        assert pub.messages_published == 2
