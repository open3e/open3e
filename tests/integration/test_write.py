import os

import pytest

import tests.util.open3e_cmd as open3e
from tests.util.dataset import dataset, dataset_dict
from tests.util.wait import wait_for


WRITE_DATASET_FILE = os.path.join(os.path.dirname(__file__), "test_data/write.json")


@pytest.mark.parametrize("ecu, did, value_to_write", dataset(WRITE_DATASET_FILE))
def test_write_json_cmd(ecu, did, value_to_write):
    # store initial value
    stdout, _ = open3e.read(ecu, [did])
    initial_value = stdout.strip()

    try:
        # write new value
        stdout, stderr = open3e.write(ecu, did, value_to_write)
        assert "" == stderr
        assert f"write: {int(ecu, 16)}.{did} = {value_to_write}" == stdout.strip()

        # verify write of new value
        stdout, stderr = open3e.read(ecu, [did])
        assert "" == stderr
        assert value_to_write == stdout.strip()
    finally:
        # write initial value, to keep test data as expected
        open3e.write(ecu, did, initial_value)


def test_write_json_cmd_sub_did():
    ecu = "0x680"
    sub_did = "1007.Required"
    fq_did = f"{ecu}.{sub_did}"
    value_to_write = '"on"'

    # store initial value
    stdout, _ = open3e.read_with_did_string(fq_did)
    initial_value = stdout.strip()

    try:
        # write new value
        stdout, stderr = open3e.write_with_did_string(fq_did, value_to_write)
        assert "" == stderr
        assert f"write: {int(ecu, 16)}.{sub_did} = {value_to_write}" == stdout.strip()

        # verify write of new value
        stdout, _ = open3e.read_with_did_string(fq_did)
        assert '"on"' == stdout.strip()
    finally:
        # write initial value, to keep test data as expected
        open3e.write_with_did_string(fq_did, initial_value)


def test_write_raw_cmd():
    ecu = "0x680"
    did = 396
    value_to_write_raw = "D601"  # 47.0

    # store initial value
    stdout, _ = open3e.read(ecu, [did])
    initial_value = stdout.strip()

    try:
        # write new value
        stdout, stderr = open3e.write_raw(ecu, did, value_to_write_raw)
        assert "" == stderr
        assert f'write raw: {int(ecu, 16)}.{did} = "{value_to_write_raw}"' == stdout.strip()

        # verify write of new value
        stdout, _ = open3e.read(ecu, [did])
        assert "47.0" == stdout.strip()
    finally:
        # write initial value, to keep test data as expected
        open3e.write(ecu, did, initial_value)


@pytest.mark.parametrize("ecu, did, value_to_write", dataset(WRITE_DATASET_FILE))
def test_write_listen(open3e_mqtt_client, ecu, did, value_to_write):
    # store initial value
    stdout, _ = open3e.read(ecu, [did])
    initial_value = stdout.strip()

    try:
        # start open3e process in listen mode
        with open3e.listen() as _:
            wait_for(lambda: open3e_mqtt_client.is_open3e_online())

            open3e_mqtt_client.subscribe(ecu, did)

            # write new value
            open3e_mqtt_client.publish_cmd("write", ecu, [[did, value_to_write]])

            # verify write of new value
            open3e_mqtt_client.publish_cmd("read-json", ecu, [did])
            wait_for(lambda: open3e_mqtt_client.received_messages_count() == 1)
            assert value_to_write == open3e_mqtt_client.received_message_payload(ecu, did)
    finally:
        # write initial value, to keep test data as expected
        open3e.write(ecu, did, initial_value)


def test_write_listen_multiple_dids(open3e_mqtt_client):
    ecu = "0x680"
    dids = [396, 1007]
    write_dataset = dataset_dict(WRITE_DATASET_FILE)

    # store initial values
    initial_values = {}
    for did in dids:
        stdout, _ = open3e.read(ecu, [did])
        initial_values[did] = stdout.strip()

    try:
        # start open3e process in listen mode
        with open3e.listen() as _:
            wait_for(lambda: open3e_mqtt_client.is_open3e_online())

            write_data = []
            for did in dids:
                open3e_mqtt_client.subscribe(ecu, did)
                write_data.append([did, write_dataset[ecu][did]])

            # write new value
            open3e_mqtt_client.publish_cmd("write", ecu, write_data)

            # verify write of new value
            open3e_mqtt_client.publish_cmd("read-json", ecu, dids)
            wait_for(lambda: open3e_mqtt_client.received_messages_count() == 2)
            assert write_dataset[ecu][dids[0]] == open3e_mqtt_client.received_message_payload(ecu, dids[0])
            assert write_dataset[ecu][dids[1]] == open3e_mqtt_client.received_message_payload(ecu, dids[1])
    finally:
        # write initial value, to keep test data as expected
        for did in dids:
            open3e.write(ecu, did, initial_values[did])


def test_write_listen_raw(open3e_mqtt_client):
    ecu = "0x680"
    did = 396

    value_to_write_raw = "D601"  # 47.0

    # store initial value
    stdout, _ = open3e.read(ecu, [did])
    initial_value = stdout.strip()

    try:
        with open3e.listen() as _:
            wait_for(lambda: open3e_mqtt_client.is_open3e_online())

            open3e_mqtt_client.subscribe(ecu, did)

            # write new value
            open3e_mqtt_client.publish_cmd("write-raw", ecu, [[did, value_to_write_raw]])

            # verify write of new value
            open3e_mqtt_client.publish_cmd("read-json", ecu, [did])
            wait_for(lambda: open3e_mqtt_client.received_messages_count() == 1)
            assert "47.0" == open3e_mqtt_client.received_message_payload(ecu, did)
    finally:
        # write initial value, to keep test data as expected
        open3e.write(ecu, did, initial_value)
