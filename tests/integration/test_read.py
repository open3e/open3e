import subprocess
import time
import sys
import uuid

import pytest

import paho.mqtt.client as paho


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


@pytest.fixture
def open3e(open3e_arguments):
  open3e = subprocess.Popen(
    [sys.executable, "-m", "open3e.Open3Eclient"] + open3e_arguments,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True
  )

  yield open3e

  open3e.terminate()
  wait_for(lambda: open3e.poll() is not None)
  if open3e.poll() is None:
    open3e.kill()
  open3e.wait(timeout=5)


@pytest.mark.parametrize('open3e_arguments', [
  ["-c", "vcan0",
   "-r", "0x684.256"
  ]])
def test_read_cmd(open3e):
  # assert exit code
  wait_for(lambda: open3e.poll() is not None)
  assert open3e.poll() == 0

  # assert stdout output
  stdout, stderr = open3e.communicate(timeout=1)
  assert '' == stderr
  assert "{'BusAddress': 59," in stdout
  # TODO: valid json output?
  # result = json.loads(stdout)
  # assert result.get("BusAddress") == "59"
  # assert result.get('VIN') == "0000000000000815"


@pytest.mark.parametrize('open3e_arguments', [
  ["-c", "vcan0",
   "-l", "open3e/cmnd",
   "-m", "127.0.0.1:1883:open3e",
   "-mfstr", "{ecuAddr:03X}_{didNumber:04d}"
  ]])
def test_read_listen(mqtt, open3e):
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


def wait_for(predicate, timeout=5):
  """Waits for a condition to be met within a timeout."""
  start_time = time.time()
  while not predicate():
    if time.time() - start_time > timeout:
        raise TimeoutError("Timeout waiting for condition")
    time.sleep(0.1)