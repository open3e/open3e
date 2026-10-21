import open3e.Open3Ecodecs
from open3e.Open3Ecodecs import O3EComplexType, O3EInt16, RawCodec
from open3e.Open3Eclass import O3Eclass

import pytest


DID = 2085
SUB_DID_CODEC = O3EComplexType(13, "ZigBeeOneDeviceSetpoint", [RawCodec(2, "Prefix"), O3EInt16(2, "MaximumFlowTemperature", scale=10), RawCodec(9, "Unused")], acc="rw")
CURRENT_VALUE = bytes.fromhex("00032602000000000000000000")


class WrongLengthCodec(RawCodec):
    """Codec whose encode() returns one byte too many."""
    def encode(self, string_ascii):
        return bytes(self.string_len + 1)


def ecu_without_connection(write):
    """O3Eclass with readPure/_writeByDid replaced, no CAN or DoIP connection needed."""
    ecu = O3Eclass.__new__(O3Eclass)
    ecu.tx = 0x680
    ecu.dataIdentifiers = {DID: SUB_DID_CODEC}
    ecu.readPure = lambda did, binary=False: (CURRENT_VALUE, SUB_DID_CODEC.id)
    ecu._writeByDid = write
    return ecu


@pytest.fixture(autouse=True)
def restore_flags():
    # module wide flags, other test files rely on their own setting
    binary, rawmode = open3e.Open3Ecodecs.flag_binary, open3e.Open3Ecodecs.flag_rawmode
    yield
    open3e.Open3Ecodecs.flag_binary, open3e.Open3Ecodecs.flag_rawmode = binary, rawmode


def test_write_sub_replaces_only_sub_bytes():
    written = []
    ecu = ecu_without_connection(lambda did, val, raw, useService77=False: (written.append(bytes(val)), (True, 0))[1])

    assert ecu.writeByDid(DID, "45", raw=False, sub="MaximumFlowTemperature") == (True, 0)
    assert written == [bytes.fromhex("0003c201000000000000000000")]
    assert open3e.Open3Ecodecs.flag_binary is False


def test_write_sub_resets_flag_binary_on_error():
    def failing_write(did, val, raw, useService77=False):
        raise TimeoutError("no response")

    ecu = ecu_without_connection(failing_write)

    result = ecu.writeByDid(DID, "45", raw=False, sub="MaximumFlowTemperature")

    assert result == ("no response", "ERR/0x680.2085")
    assert open3e.Open3Ecodecs.flag_binary is False
    # reading afterwards must still return hex strings
    open3e.Open3Ecodecs.flag_rawmode = False
    assert SUB_DID_CODEC.decode(CURRENT_VALUE)["Prefix"] == "0003"


def test_write_sub_rejects_encoded_value_with_wrong_length():
    written = []
    ecu = ecu_without_connection(lambda did, val, raw, useService77=False: (written.append(val), (True, 0))[1])
    ecu.dataIdentifiers = {DID: O3EComplexType(13, "Test", [RawCodec(2, "Prefix"), WrongLengthCodec(2, "Broken"), RawCodec(9, "Unused")])}

    result = ecu.writeByDid(DID, "0000", raw=True, sub="Broken")

    assert "has 3 bytes, expected 2" in result[0]
    assert written == []
    assert open3e.Open3Ecodecs.flag_binary is False
