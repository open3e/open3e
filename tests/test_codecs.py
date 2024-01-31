from open3e.Open3Ecodecs import O3EByteVal, O3EComplexType, O3EInt8, O3EInt16, RawCodec, O3EUtf8, O3EDateTime, O3EList, O3EEnum, O3ESdate, \
    O3EStime, O3EUtc, O3ESoftVers, O3EMacAddr, O3EIp4Addr
import open3e.Open3Ecodecs

from open3e.Open3Edatapoints import dataIdentifiers
import random 

import pytest

open3e.Open3Ecodecs.flag_rawmode = False


def _check_supported_type(codec, unsupported):
    supported = True

    if type(codec) in unsupported:
        return False
    
    if hasattr(codec, "subTypes"):
        for sub in codec.subTypes:
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


if __name__ == "__main__":
    test_datapoints_length()
    test_complex_codec()
    test_datapoints_encode_decode()
    test_complex_code_raise_on_missing_key()
    test_list_code()