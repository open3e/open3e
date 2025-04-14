import time
import uuid

import pytest

import paho.mqtt.client as paho

import tests.util.open3e_cmd_wrapper as open3e_process
from tests.util.wait import wait_for


@pytest.fixture
def mqtt():
  received_messages = []
  def on_message(client, userdata, msg):
    received_messages.append(msg.payload.decode())

  client = paho.Client(
    callback_api_version=paho.CallbackAPIVersion.VERSION2,
    client_id=f'IntegrationTest_{str(uuid.uuid4())}'
  )
  client.on_message = on_message
  client.connect("127.0.0.1")
  client.loop_start()

  yield client, received_messages

  client.loop_stop()
  client.disconnect()


def test_read_cmd():
  stdout, stderr = open3e_process.read("0x684.256")

  assert '' == stderr
  assert "{'BusAddress': 59," in stdout
  # TODO: valid json output?
  # result = json.loads(stdout)
  # assert result.get("BusAddress") == "59"
  # assert result.get('VIN') == "0000000000000815"


def test_read_listen(mqtt):
  with open3e_process.listen() as process:
    # wait for open3e to connect to mqtt
    # TODO: subscribe to LWT instead?
    time.sleep(1)

    client, received_messages = mqtt

    # subscribe on topic with expected read result
    client.subscribe("open3e/684_0256/BusAddress")

    # publish read command
    client.publish("open3e/cmnd", '{"mode":"read","addr":"0x684","data":[256]}')

    # wait for message on read result topic
    wait_for(lambda: len(received_messages) > 0)

    # assert message content
    assert len(received_messages) == 1
    assert received_messages[0] == '59'