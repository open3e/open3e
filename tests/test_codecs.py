from open3e.Open3Ecodecs import O3EByteVal, O3EComplexType, O3EInt8, O3EInt16, RawCodec, O3EUtf8, O3EDateTime, O3EList, O3EEnum, O3ESdate, \
    O3EStime, O3EUtc, O3ESoftVers, O3EMacAddr, O3EIp4Addr
import open3e.Open3Ecodecs
import udsoncan

from open3e.Open3Edatapoints import dataIdentifiers
import random 

import pytest

open3e.Open3Ecodecs.flag_rawmode = False


def _check_supported_type(codec, unsupported):
    if type(codec) in unsupported:
        return False

    if hasattr(codec, "subTypes"):
        for sub in codec.subTypes:
            if not _check_supported_type(sub, unsupported):
                return False

    if hasattr(codec, "cases"):  # O3ESwitch
        subcases = list(codec.cases.values())
        if codec.default is not None:
            subcases.append(codec.default)
        for sub in subcases:
            if not _check_supported_type(sub, unsupported):
                return False

    return True

def _calc_codec_length(codec):
    length = 0
    if hasattr(codec, "subTypes"):
        for sub in codec.subTypes:
            length += _calc_codec_length(sub)
    else:
        length = len(codec)
    
    return length

def test_complex_codec():
    codec = O3EComplexType(9, "MixerOneCircuitRoomTemperatureSetpoint", [O3EInt16(2, "Comfort", signed=True), O3EInt16(2, "Standard", signed=True), 
                                                                 O3EInt16(2, "Reduced", signed=True), RawCodec(2, "Unknown2"), O3EByteVal(1, "Unknown1")])
    
    raw_input = bytes.fromhex("c800c900be00000000")
    decoded_input = codec.decode(raw_input)
    encoded_output = codec.encode(decoded_input)

    assert raw_input == encoded_output

def test_complex_codec_raise_on_missing_key():
    codec = O3EComplexType(9, "MixerOneCircuitRoomTemperatureSetpoint", [O3EInt16(2, "Comfort", signed=True), O3EInt16(2, "Standard", signed=True), 
                                                                 O3EInt16(2, "Reduced", signed=True), RawCodec(2, "Unknown2"), O3EByteVal(1, "Unknown1")])
    
    decoded_input = {"Comfort": 21.0, "Standard": 20.0, "Reduced": 20.0, "Unknown2": "0000"}
    with pytest.raises(ValueError) as e_info:
        encoded_output = codec.encode(decoded_input)

def test_list_codec_raise_invalid_count():
    codec = O3EList(57, "MixerOneCircuitTimeScheduleMonday",[O3EByteVal(1, "Count"), 
                                                             O3EComplexType(7, "Schedules",[O3EStime(2, "Start"),O3EStime(2, "Stop"), RawCodec(2, "Unknown"), O3EByteVal(1, "Mode")])])
    
    decoded_input = {'Count': 4, 'Schedules': [{'Start': '09:00', 'Stop': '17:00', 'Unknown': '0000', 'Mode': 3}, 
                                               {'Start': '17:00', 'Stop': '20:00', 'Unknown': '0000', 'Mode': 4}, 
                                               {'Start': '20:00', 'Stop': '24:00', 'Unknown': '0000', 'Mode': 3}]}
    with pytest.raises(AssertionError) as e_info:
        encoded_output = codec.encode(decoded_input)

def test_list_codec():
    codec = O3EList(57, "MixerOneCircuitTimeScheduleMonday",[O3EByteVal(1, "Count"), 
                                                             O3EComplexType(7, "Schedules",[O3EStime(2, "Start"),O3EStime(2, "Stop"), RawCodec(2, "Unknown"), O3EByteVal(1, "Mode")])])
    
    raw_input = bytes.fromhex("030900110000000311001400000004140018000000030000000000000000000000000000000000000000000000000000000000000000000000")
    decoded_input = codec.decode(raw_input)
    encoded_output = codec.encode(decoded_input)

    assert raw_input == encoded_output

def test_list_codec_empty():
    codec = O3EList(57, "MixerOneCircuitTimeScheduleMonday",[O3EByteVal(1, "Count"), 
                                                             O3EComplexType(7, "Schedules",[O3EStime(2, "Start"),O3EStime(2, "Stop"), RawCodec(2, "Unknown"), O3EByteVal(1, "Mode")])])
    
    decoded_input = {'Count': 0, 'Schedules': []}
    encoded_output = codec.encode(decoded_input)

    assert encoded_output == bytes(len(codec))

def test_time_codec():
    codec = O3EStime(2, "Start")
    decoded_input = "17:00"
    encoded_output = codec.encode(decoded_input)
    decoded_output = codec.decode(encoded_output)
    assert decoded_input == decoded_output

def test_datapoints_encode_decode():
    for did, codec in dataIdentifiers["dids"].items():
        
        if not _check_supported_type(codec, unsupported=[O3EList, O3EUtf8, O3EDateTime, O3EEnum, O3ESdate, O3EUtc, O3ESoftVers, 
                                                         O3EMacAddr, O3EIp4Addr]) or \
            (getattr(codec, "offset", 0) > 0):
            continue 
        
        raw_input = codec.encode(codec.decode(random.randbytes(len(codec))))
        decoded_input = codec.decode(raw_input)
        encoded_output = codec.encode(decoded_input)

        assert raw_input == encoded_output, f"Did {did}: Input {raw_input.hex()} does not match output {encoded_output.hex()}" 

def test_datapoints_encode_decode_list():

    PROBLEMATIC_DIDS = []

    for did, codec in dataIdentifiers["dids"].items():

        if type(codec) != O3EList:
            continue
        
        if not _check_supported_type(codec, unsupported=[O3EUtf8, O3EDateTime, O3EEnum, O3ESdate, O3EUtc, O3ESoftVers, 
                                                         O3EMacAddr, O3EIp4Addr]) or \
                did in PROBLEMATIC_DIDS:
            continue

        subcodec_len_sum = _calc_codec_length(codec)
        max_list_length = int((len(codec)-1)/(subcodec_len_sum-1))
        
        raw_input = codec.subTypes[0].encode(max_list_length)+random.randbytes(len(codec)-1)
        decoded_input = codec.decode(raw_input)
        print(did, decoded_input)
        encoded_output = codec.encode(decoded_input)

        assert raw_input == encoded_output, f"Did {did}: Input {raw_input.hex()} does not match output {encoded_output.hex()}" 

def test_datapoints_length():

    for did, codec in dataIdentifiers["dids"].items():
        if not _check_supported_type(codec, unsupported=[O3EList]):
            continue 
        
        codec_len = len(codec)
        subcodec_len_sum = _calc_codec_length(codec)

        assert codec_len == subcodec_len_sum, f"Did {did}: Length {codec_len} does not match sum of subType lenghts {subcodec_len_sum}" 


@pytest.mark.parametrize("raw_hex, expected", [
    ("45472f4f470000000000000000000000000000000000000000000000000000000000000000000000", "EG/OG"),
    ("55470000ffffffff00000000010000005a360203a300007a495a360003a500007a495a3600000000", "UG"),
])
def test_utf8_ends_at_first_nul(monkeypatch, raw_hex, expected):
    monkeypatch.setattr(open3e.Open3Ecodecs, "flag_rawmode", False)
    assert O3EUtf8(40, "CircuitName").decode(bytes.fromhex(raw_hex)) == expected


# ~~~~~~ O3EUtf8 with variable length (string_len == 0), refer to discussion #415 ~~~~~~

@pytest.mark.parametrize("raw_hex, expected", [
    ("484b3100", "HK1"),                                  # 4 bytes
    ("484b313100", "HK11"),                               # 5 bytes, renamed in ViCare
    ("4865697a6b726569732031" + "00", "Heizkreis 1"),     # 12 bytes
    ("45472f4f47" + "00" * 35, "EG/OG"),                  # 40 bytes, padded like heat pumps
])
def test_utf8_variable_length_decode(monkeypatch, raw_hex, expected):
    monkeypatch.setattr(open3e.Open3Ecodecs, "flag_rawmode", False)
    assert O3EUtf8(0, "CentralHeatingOneCircuitName").decode(bytes.fromhex(raw_hex)) == expected


def test_utf8_variable_length_reads_all_remaining_data():
    with pytest.raises(udsoncan.DidCodec.ReadAllRemainingData):
        len(O3EUtf8(0, "CentralHeatingOneCircuitName"))
    assert len(O3EUtf8(40, "CentralHeatingOneCircuitName")) == 40


def test_utf8_variable_length_encode(monkeypatch):
    monkeypatch.setattr(open3e.Open3Ecodecs, "flag_rawmode", False)
    assert O3EUtf8(0, "CentralHeatingOneCircuitName").encode("HK11") == bytes.fromhex("484b313100")
    assert O3EUtf8(0, "CentralHeatingOneCircuitName").encode("Bäder") == "Bäder".encode("utf-8") + b"\x00"


def test_utf8_fixed_length_encode_pads_with_nul(monkeypatch):
    monkeypatch.setattr(open3e.Open3Ecodecs, "flag_rawmode", False)
    encoded = O3EUtf8(40, "CentralHeatingOneCircuitName").encode("EG/OG")
    assert encoded == b"EG/OG" + bytes(35)
    assert O3EUtf8(40, "CentralHeatingOneCircuitName").decode(encoded) == "EG/OG"


def test_utf8_fixed_length_encode_too_long(monkeypatch):
    monkeypatch.setattr(open3e.Open3Ecodecs, "flag_rawmode", False)
    O3EUtf8(12, "CentralHeatingOneCircuitName").encode("x" * 12)   # fits exactly, no NUL needed
    with pytest.raises(ValueError, match="too long"):
        O3EUtf8(12, "CentralHeatingOneCircuitName").encode("x" * 13)


def test_utf8_encode_rejects_nul(monkeypatch):
    monkeypatch.setattr(open3e.Open3Ecodecs, "flag_rawmode", False)
    with pytest.raises(ValueError, match="NUL"):
        O3EUtf8(0, "CentralHeatingOneCircuitName").encode("HK\x001")


def test_utf8_variable_length_raw_mode(monkeypatch):
    monkeypatch.setattr(open3e.Open3Ecodecs, "flag_rawmode", True)
    codec = O3EUtf8(0, "CentralHeatingOneCircuitName")
    assert codec.encode("484b3100") == bytes.fromhex("484b3100")
    assert codec.decode(bytes.fromhex("484b3100")) == "484b3100"


@pytest.mark.parametrize("payload_hex, expected", [
    ("484b3100", "HK1"),
    ("4865697a6b726569732031" + "00", "Heizkreis 1"),
])
def test_utf8_variable_length_via_udsoncan(monkeypatch, payload_hex, expected):
    # positive response 0x62 of ReadDataByIdentifier for DID 627 (0x0273), parsed by udsoncan
    monkeypatch.setattr(open3e.Open3Ecodecs, "flag_rawmode", False)
    didconfig = {627: O3EUtf8(0, "CentralHeatingOneCircuitName")}
    response = udsoncan.Response.from_payload(bytes.fromhex("620273" + payload_hex))
    udsoncan.services.ReadDataByIdentifier.interpret_response(response, didlist=[627], didconfig=didconfig)
    assert response.service_data.values[627] == expected


def test_variants_of_circuit_names():
    from open3e.Open3EdatapointsVariants import dataIdentifiers as variants
    for did in range(627, 635):
        assert list(variants["dids"][did].keys()) == [0]
        assert variants["dids"][did][0].getCodecInfo()["len"] == 0
        assert variants["dids"][did][0].acc == "rw"
        assert dataIdentifiers["dids"][did].string_len == 40
        assert dataIdentifiers["dids"][did].acc == "rw"
