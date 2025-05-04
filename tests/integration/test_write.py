import os

import pytest

import tests.util.open3e_cmd_wrapper as open3e_process
from tests.util.json_device_dataset_loader import write_dataset
from tests.util.wait import wait_for


WRITE_DATASET_FILE = os.path.join(os.path.dirname(__file__), "test_data/write.json")


@pytest.mark.parametrize("ecu, did, initial_value, value_to_write", write_dataset(WRITE_DATASET_FILE))
def test_write_json_cmd(ecu, did, initial_value, value_to_write):
  # verify initial value
  stdout, _ = open3e_process.read(ecu, [did])
  assert initial_value == stdout.strip()

  # write new value
  stdout, stderr = open3e_process.write(ecu, did, value_to_write)
  assert '' == stderr
  assert f"write: {int(ecu, 16)}.{did} = {value_to_write}" == stdout.strip()

  # verify write of new value
  stdout, stderr = open3e_process.read(ecu, [did])
  assert '' == stderr
  assert value_to_write == stdout.strip()

  # write initial value, to keep test data as expected
  open3e_process.write(ecu, did, initial_value)


def test_write_json_cmd_sub_did():
  ecu = "0x680"
  sub_did = "1007.Required"
  fq_did = f"{ecu}.{sub_did}"

  initial_value = '"off"'
  value_to_write = '"on"'

  # verify initial value
  stdout, _ = open3e_process.read_with_did_string(fq_did)
  assert f'{initial_value}' == stdout.strip()

  # write new value
  stdout, stderr = open3e_process.write_with_did_string(fq_did, value_to_write)
  assert '' == stderr
  assert f'write: {int(ecu, 16)}.{sub_did} = {value_to_write}' == stdout.strip()

  # verify write of new value
  stdout, _ = open3e_process.read_with_did_string(fq_did)
  assert '"on"' == stdout.strip()

  # write initial value, to keep test data as expected
  open3e_process.write_with_did_string(fq_did, initial_value)


def test_write_raw_cmd():
  ecu = "0x680"
  did = 396

  initial_value = "45.0"
  value_to_write_raw = "D601" #47.0

  # verify initial value
  stdout, _ = open3e_process.read(ecu, [did])
  assert initial_value == stdout.strip()

  # write new value
  stdout, stderr = open3e_process.write_raw(ecu, did, value_to_write_raw)
  assert '' == stderr
  # TODO: quotes in write?
  assert f"write raw: {int(ecu, 16)}.{did} = \"{value_to_write_raw}\"" == stdout.strip()

  # verify write of new value
  stdout, _ = open3e_process.read(ecu, [did])
  assert '47.0' == stdout.strip()

  # write initial value, to keep test data as expected
  open3e_process.write(ecu, did, initial_value)


@pytest.mark.parametrize("ecu, did, initial_value, value_to_write", write_dataset(WRITE_DATASET_FILE))
def test_write_listen(open3e_mqtt_client, ecu, did, initial_value, value_to_write):
  # verify initial value
  stdout, _ = open3e_process.read(ecu, [did])
  assert initial_value == stdout.strip()

  # start open3e process in listen mode
  with open3e_process.listen() as _:
    wait_for(lambda: open3e_mqtt_client.is_open3e_online())

    open3e_mqtt_client.subscribe(ecu, did)

    # write new value
    open3e_mqtt_client.publish_cmd("write", ecu, [[did,value_to_write]])

    # verify write of new value
    open3e_mqtt_client.publish_cmd("read-json", ecu, [did])
    wait_for(lambda: open3e_mqtt_client.received_messages_count() == 1)
    assert value_to_write == open3e_mqtt_client.received_message_payload(ecu, did)

  # write initial value, to keep test data as expected
  open3e_process.write(ecu, did, initial_value)