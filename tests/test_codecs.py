from Open3Ecodecs import O3EByteVal, O3EComplexType, O3EInt16, RawCodec, O3EUtf8, O3EDateTime, O3EList, O3EEnum, O3ESdate, \
    O3EStime, O3EUtc, O3ESoftVers, O3EMacAddr, O3EIp4Addr, O3ECompStat, O3EAddElHeaterStat
import Open3Ecodecs

from Open3Edatapoints import dataIdentifiers
import random 


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

def test_complex_code():
    codec = O3EComplexType(9, "MixerOneCircuitRoomTemperatureSetpoint", [O3EInt16(2, "Comfort", signed=True), O3EInt16(2, "Standard", signed=True), 
                                                                 O3EInt16(2, "Reduced", signed=True), RawCodec(2, "Unknown2"), O3EByteVal(1, "Unknown1")])
    
    raw_input = bytes.fromhex("c800c900be00000000")
    decoded_input = codec.decode(raw_input)
    encoded_output = codec.encode(decoded_input)

    assert raw_input == encoded_output


def test_datapoints_encode_decode():

    PROBLEMATIC_DIDS = [405, 406, 407, 408, 417, 476, 874, 950, 1085, 1087, 1190, 1266, 1659, 1826, 1827, 1828, 1829, 1830, 1837, 1838,
                        2342, 2343, 2351, 2486, 2487, 2488, 2494, 2495, 2496, 2574, 2622, 2623, 2624, 2625, 2626, 2629, 2784, 2791, 
                        2792, 2793, 2794, 2795]

    for did, codec in dataIdentifiers["dids"].items():
        
        if not _check_supported_type(codec, unsupported=[O3EList, O3EUtf8, O3EDateTime, O3EEnum, O3ESdate, O3EStime, O3EUtc, O3ESoftVers, 
                                                         O3EMacAddr, O3EIp4Addr, O3ECompStat, O3ECompStat, O3EAddElHeaterStat]) or \
            (getattr(codec, "offset", 0) > 0) or \
                did in PROBLEMATIC_DIDS:
            continue 
        
        raw_input = random.randbytes(len(codec))
        decoded_input = codec.decode(raw_input)
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
    Open3Ecodecs.flag_rawmode = False

    test_datapoints_length()
    test_complex_code()
    test_datapoints_encode_decode()
    