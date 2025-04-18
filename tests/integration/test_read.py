import json
import os
import time

import pytest

import tests.util.open3e_cmd_wrapper as open3e_process
from tests.util.json_device_dataset_loader import device_dataset
from tests.util.wait import wait_for


READ_DATASET_FILE = os.path.join(os.path.dirname(__file__), "test_data/read.json")


@pytest.mark.parametrize("ecu, did, expected", device_dataset(READ_DATASET_FILE))
def test_read_cmd_json(ecu, did, expected):
  stdout, stderr = open3e_process.read(f"{ecu}.{did}")

  assert '' == stderr
  assert expected == stdout.strip()


@pytest.mark.parametrize("ecu, did, expected", device_dataset(READ_DATASET_FILE))
def test_read_listen_json(mqtt, ecu, did, expected):
  with open3e_process.listen() as _:
    # wait for open3e to connect to mqtt
    # TODO: subscribe to LWT instead?
    time.sleep(1)

    client, received_messages = mqtt

    # subscribe on expected topic
    expected_did_topic = open3e_process.MQTT_FORMAT_STRING.format(
      ecuAddr=int(ecu,16),
      didNumber=did
    )
    client.subscribe(f"{open3e_process.MQTT_BASE_TOPIC}/{expected_did_topic}")

    # publish read command
    read_payload = {
      "mode": "read-json",
      "addr": ecu,
      "data": [did]
    }
    client.publish("open3e/cmnd", json.dumps(read_payload))

    # wait for message on expected result topic
    wait_for(lambda: len(received_messages) > 0)

    # assert message content
    assert expected == received_messages[0].payload.decode()