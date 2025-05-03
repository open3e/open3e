import os

import pytest

import tests.util.open3e_cmd_wrapper as open3e_process
from tests.util.json_device_dataset_loader import device_dataset
from tests.util.wait import wait_for


WRITE_DATASET_FILE = os.path.join(os.path.dirname(__file__), "test_data/write.json")


@pytest.mark.parametrize("ecu, did, value_to_write", device_dataset(WRITE_DATASET_FILE))
def test_write_cmd(ecu, did, value_to_write):
  stdout, stderr = open3e_process.write(ecu, did, value_to_write)
  assert '' == stderr
  assert f"write: {int(ecu, 16)}.{did} = {value_to_write}" == stdout.strip()

  stdout, stderr = open3e_process.read(ecu, [did])
  assert '' == stderr
  assert value_to_write == stdout.strip()


@pytest.mark.parametrize("ecu, did, value_to_write", device_dataset(WRITE_DATASET_FILE))
def test_write_listen(open3e_mqtt_client, ecu, did, value_to_write):
  with open3e_process.listen() as _:
    wait_for(lambda: open3e_mqtt_client.is_open3e_online())

    open3e_mqtt_client.subscribe(ecu, did)

    open3e_mqtt_client.publish_cmd("write", ecu, [[did,value_to_write]])
    open3e_mqtt_client.publish_cmd("read-json", ecu, [did])

    wait_for(lambda: open3e_mqtt_client.received_messages_count() == 1)

    assert value_to_write == open3e_mqtt_client.received_message_payload(ecu, did)