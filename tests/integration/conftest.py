import paho.mqtt.client as paho
import pytest
import uuid

import tests.util.open3e_cmd_wrapper as open3e_process

@pytest.fixture
def mqtt():
  received_messages = []
  def on_message(client, userdata, msg):
    received_messages.append(msg)

  client = paho.Client(
    callback_api_version=paho.CallbackAPIVersion.VERSION2,
    client_id=f'IntegrationTest_{str(uuid.uuid4())}'
  )
  client.on_message = on_message
  client.connect(open3e_process.MQTT_BROKER_ADDRESS, open3e_process.MQT_BROKER_PORT)
  client.loop_start()

  yield client, received_messages

  client.loop_stop()
  client.disconnect()