"""
Data points with variable length (codec length 0), refer to discussion #415:
read fallback and write checks in O3Eclass, no CAN or DoIP connection needed.
"""

from unittest.mock import MagicMock

import pytest
from udsoncan.exceptions import InvalidResponseException, UnexpectedResponseException

import open3e.Open3Ecodecs
from open3e.Open3Ecodecs import O3EUtf8
from open3e.Open3Eclass import O3Eclass


DID = 627
FIXED_CODEC = O3EUtf8(40, "CentralHeatingOneCircuitName", acc="rw")
VARIABLE_CODEC = O3EUtf8(0, "CentralHeatingOneCircuitName", acc="rw")


def ecu_without_connection(codec, read_error=None, pure_data=b""):
    ecu = O3Eclass.__new__(O3Eclass)
    ecu.tx = 0x680
    ecu.dataIdentifiers = {DID: codec}
    ecu.uds_client = MagicMock()
    if read_error is not None:
        ecu.uds_client.read_data_by_identifier.side_effect = read_error
    ecu.readPure = MagicMock(return_value=(pure_data, f"DID_{DID}"))
    ecu.written = []
    ecu._writeByDid = lambda did, val, raw, useService77=False: (ecu.written.append((did, val, useService77)), (True, 0))[1]
    return ecu


@pytest.fixture(autouse=True)
def restore_flags():
    binary, rawmode = open3e.Open3Ecodecs.flag_binary, open3e.Open3Ecodecs.flag_rawmode
    yield
    open3e.Open3Ecodecs.flag_binary, open3e.Open3Ecodecs.flag_rawmode = binary, rawmode


# ~~~~~~ reading ~~~~~~

@pytest.mark.parametrize("error", [
    InvalidResponseException(MagicMock(), "Value for data identifier 0x0273 was incomplete"),   # shorter than codec
    UnexpectedResponseException(MagicMock(), "Server returned values for data identifier 0x3100 that was not requested"),  # longer
])
def test_read_falls_back_to_variable_length_variant(error):
    ecu = ecu_without_connection(FIXED_CODEC, read_error=error, pure_data=bytes.fromhex("484b313100"))
    assert ecu.readByDid(DID, raw=False) == ("HK11", "CentralHeatingOneCircuitName", DID)
    ecu.readPure.assert_called_once_with(DID, binary=True)


def test_read_fallback_in_raw_mode_returns_hex():
    ecu = ecu_without_connection(FIXED_CODEC, read_error=InvalidResponseException(MagicMock(), "incomplete"),
                                 pure_data=bytes.fromhex("484b3100"))
    assert ecu.readByDid(DID, raw=True)[0] == "484b3100"


def test_read_no_fallback_for_dids_without_variable_variant():
    ecu = ecu_without_connection(FIXED_CODEC, read_error=InvalidResponseException(MagicMock(), "incomplete"))
    ecu.dataIdentifiers = {268: FIXED_CODEC}
    result = ecu.readByDid(268, raw=False)
    assert result[1] == "ERR/0x680.268"
    ecu.readPure.assert_not_called()


def test_read_no_fallback_if_codec_has_variable_length_already():
    ecu = ecu_without_connection(VARIABLE_CODEC, read_error=InvalidResponseException(MagicMock(), "No data in response"))
    result = ecu.readByDid(DID, raw=False)
    assert result[1] == f"ERR/0x680.{DID}"
    ecu.readPure.assert_not_called()


# ~~~~~~ writing ~~~~~~

def test_write_variable_length():
    ecu = ecu_without_connection(VARIABLE_CODEC)
    assert ecu.writeByDid(DID, "HK11", raw=False) == (True, 0)
    assert ecu.written == [(DID, "HK11", False)]


def test_write_variable_length_upper_limit_is_common_length():
    ecu = ecu_without_connection(VARIABLE_CODEC)
    ecu.writeByDid(DID, "x" * 39, raw=False)           # 39 bytes + NUL = 40, fits
    assert len(ecu.written) == 1
    result = ecu.writeByDid(DID, "x" * 40, raw=False)  # 41 bytes
    assert "too long" in result[0]
    assert len(ecu.written) == 1


def test_write_variable_length_rejects_service77():
    ecu = ecu_without_connection(VARIABLE_CODEC)
    result = ecu.writeByDid(DID, "HK11", raw=False, useService77=True)
    assert "service 77" in result[0]
    assert ecu.written == []


def test_write_variable_length_rejects_service77_with_separate_instance():
    # Open3Eclient uses a separate instance with the general table for service 77 and passes the device ecu as readecu
    ecu77 = ecu_without_connection(FIXED_CODEC)
    readecu = ecu_without_connection(VARIABLE_CODEC)
    result = ecu77.writeByDid(DID, "HK11", raw=False, useService77=True, readecu=readecu)
    assert "service 77" in result[0]
    assert ecu77.written == []


def test_read_fallback_prints_hint(capsys):
    ecu = ecu_without_connection(FIXED_CODEC, read_error=InvalidResponseException(MagicMock(), "incomplete"),
                                 pure_data=bytes.fromhex("484b3100"))
    ecu.readByDid(DID, raw=False)
    assert "open3e_depictSystem" in capsys.readouterr().out


def test_write_fixed_length_service77_still_allowed():
    ecu = ecu_without_connection(FIXED_CODEC)
    assert ecu.writeByDid(DID, "HK11", raw=False, useService77=True) == (True, 0)
    assert ecu.written == [(DID, "HK11", True)]
