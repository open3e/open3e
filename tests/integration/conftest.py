import paho.mqtt.client as paho
import pytest
import uuid

import tests.util.open3e_cmd_wrapper as open3e_process
from tests.util.Open3EMqttClient import Open3EMqttClient

@pytest.fixture
def open3e_mqtt_client():
  client = paho.Client(
    callback_api_version=paho.CallbackAPIVersion.VERSION2,
    client_id=f'IntegrationTest_{str(uuid.uuid4())}'
  )
  client.connect(open3e_process.MQTT_BROKER_ADDRESS, open3e_process.MQT_BROKER_PORT)
  client.loop_start()

  yield Open3EMqttClient(client)

  client.loop_stop()
  client.disconnect()