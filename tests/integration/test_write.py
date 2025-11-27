import os

import pytest

import tests.util.open3e_cmd as open3e
from tests.util.dataset import dataset
from tests.util.wait import wait_for


WRITE_DATASET_FILE = os.path.join(os.path.dirname(__file__), "test_data/write.json")


@pytest.mark.parametrize("ecu, did, value_to_write", dataset(WRITE_DATASET_FILE).fixtures())
def test_write_json_cmd(ecu, did, value_to_write):
    # store initial value
    stdout, _ = open3e.read(ecu, [did])
    initial_value = stdout.strip()
    value_to_write = str(value_to_write)

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
    did = 1007
    sub_did = "Required"
    fq_did = f"{ecu}.{did}.{sub_did}"

    write_dataset = dataset(WRITE_DATASET_FILE)
    value_to_write = f'"{str(write_dataset.get(ecu, did, sub_did))}"'

    # store initial value
    stdout, _ = open3e.read_with_did_string(fq_did)
    initial_value = stdout.strip()

    try:
        # write new value
        stdout, stderr = open3e.write_with_did_string(fq_did, value_to_write)
        assert "" == stderr
        assert f"write: {int(ecu, 16)}.{did}.{sub_did} = {value_to_write}" == stdout.strip()

        # verify write of new value
        stdout, _ = open3e.read_with_did_string(fq_did)
        assert value_to_write == stdout.strip()
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


@pytest.mark.parametrize("ecu, did, value_to_write", dataset(WRITE_DATASET_FILE).fixtures())
def test_write_listen(open3e_mqtt_client, ecu, did, value_to_write):
    # store initial value
    stdout, _ = open3e.read(ecu, [did])
    initial_value = stdout.strip()

    value_to_write = str(value_to_write)
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
    ecus = ["0x680","0x680","0x6a1","0x680"]
    dids = [396, "1007.0", "0x6a1.2214", "0x680.382.Units"]
    dids_expect = [396, 1007, 2214, 382]
    sub_dids_expect = [None,"OpMode",None,"Units"]

    write_dataset = dataset(WRITE_DATASET_FILE)

    # store initial values
    initial_values = {}
    i = 0
    for did in dids_expect:
        stdout, _ = open3e.read(ecus[i], [did])
        initial_values[did] = stdout.strip()
        i += 1

    try:
        # start open3e process in listen mode
        with open3e.listen() as _:
            wait_for(lambda: open3e_mqtt_client.is_open3e_online())

            write_data = []
            i = 0
            for did in dids_expect:
                open3e_mqtt_client.subscribe(ecus[i], did)
                write_data.append([dids[i], str(write_dataset.get(ecus[i], did, sub_dids_expect[i]))])
                i += 1

            # write new value
            open3e_mqtt_client.publish_cmd("write", "0x680", write_data)

            # verify write of new value
            open3e_mqtt_client.publish_cmd("read-json", "0x680", dids)
            wait_for(lambda: open3e_mqtt_client.received_messages_count() == len(dids_expect))
            assert str(write_dataset.get(ecus[0], dids_expect[0], sub_dids_expect[0])) == open3e_mqtt_client.received_message_payload(ecus[0], dids_expect[0])
            assert str(write_dataset.get(ecus[1], dids_expect[1], sub_dids_expect[1])) == open3e_mqtt_client.received_message_payload(ecus[1], dids_expect[1])
            assert str(write_dataset.get(ecus[2], dids_expect[2], sub_dids_expect[2])) == open3e_mqtt_client.received_message_payload(ecus[2], dids_expect[2])
            assert str(write_dataset.get(ecus[3], dids_expect[3], sub_dids_expect[3])) == open3e_mqtt_client.received_message_payload(ecus[3], dids_expect[3])
    finally:
        # write initial value, to keep test data as expected
        i = 0
        for did in dids_expect:
            open3e.write(ecus[i], did, initial_values[did])
            i += 1


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
