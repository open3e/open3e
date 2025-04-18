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
def test_read_listen_json(open3e_mqtt_client, ecu, did, expected):
  with open3e_process.listen() as _:
    wait_for(lambda: open3e_mqtt_client.is_open3e_online())

    open3e_mqtt_client.subscribe(ecu, did)
    open3e_mqtt_client.publish_cmd("read-json", ecu, [did])

    wait_for(lambda: open3e_mqtt_client.received_messages_count() == 1)

    assert expected == open3e_mqtt_client.received_message_payload(ecu, did)