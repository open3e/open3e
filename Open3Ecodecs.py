"""
   Copyright 2023 abnoname
   
   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""

import udsoncan 
from typing import Optional, Any

flag_rawmode = True

class RawCodec(udsoncan.DidCodec):
    def __init__(self, string_len: int, idStr: str):
        self.string_len = string_len
        self.id = idStr
        self.complex = False

    def encode(self, string_ascii: Any) -> bytes:
        string_bin = bytes.fromhex(string_ascii)
        if len(string_bin) != self.string_len:
            raise ValueError('String must be %d long' % self.string_len)
        return string_bin

    def decode(self, string_bin: bytes) -> Any:
        string_ascii = string_bin.hex()
        return string_ascii

    def __len__(self) -> int:
        return self.string_len


class O3EInt(udsoncan.DidCodec):
    def __init__(self, string_len: int, idStr: str, byte_width: int, scale: float = 1.0, offset: int = 0, signed=False):
        self.string_len = string_len
        self.byte_width = byte_width
        self.id = idStr
        self.complex = False
        self.scale = scale
        self.offset = offset
        self.signed = signed

    def encode(self, string_ascii: Any) -> bytes:        
        if(flag_rawmode == True): 
            return RawCodec.encode(self, string_ascii)
        else:
            if (self.offset != 0):
                raise("O3EInt.encode(): offset!=0 not implemented yet") 
            val = round(eval(str(string_ascii))*self.scale)    # convert submitted data to numeric value and apply scaling factor
            string_bin = val.to_bytes(length=self.byte_width,byteorder="little",signed=self.signed)
            return string_bin

    def decode(self, string_bin: bytes) -> Any:
        if(flag_rawmode == True): 
            return RawCodec.decode(self, string_bin)
        val = int.from_bytes(string_bin[self.offset:self.offset + self.byte_width], byteorder="little", signed=self.signed)
        return float(val) / self.scale

    def __len__(self) -> int:
        return self.string_len

class O3EInt8(O3EInt):
    def __init__(self, string_len: int, idStr: str, scale: float = 1.0, offset: int = 0, signed=False):
        O3EInt.__init__(self, string_len, idStr, byte_width=1, scale=scale, offset=offset, signed=signed)

class O3EInt16(O3EInt):
    def __init__(self, string_len: int, idStr: str, scale: float = 10.0, offset: int = 0, signed=False):
        O3EInt.__init__(self, string_len, idStr, byte_width=2, scale=scale, offset=offset, signed=signed)

class O3EInt32(O3EInt):
    def __init__(self, string_len: int, idStr: str, scale: float = 1.0, offset: int = 0, signed=False):
        O3EInt.__init__(self, string_len, idStr, byte_width=4, scale=scale, offset=offset, signed=signed)


class O3EBoolean(udsoncan.DidCodec):
    def __init__(self, string_len: int, idStr: str, offset: int = 0):
        self.string_len = string_len
        self.id = idStr
        self.offset = offset
        self.complex = False

    def encode(self, string_ascii: Any) -> bytes:        
        if(flag_rawmode == True): 
            return RawCodec.encode(self, string_ascii)
        raise Exception("not implemented yet")

    def decode(self, string_bin: bytes) -> Any:
        if(flag_rawmode == True): 
            return RawCodec.decode(self, string_bin)
        val = int.from_bytes(string_bin[self.offset:self.offset+1], byteorder="little", signed=False)
        if(val==0):
            return "off"
        else:
            return "on"

    def __len__(self) -> int:
        return self.string_len


class O3EUtf8(udsoncan.DidCodec):
    def __init__(self, string_len: int, idStr: str, offset: int = 0):
        self.string_len = string_len
        self.id = idStr
        self.offset = offset
        self.complex = False

    def encode(self, string_ascii: Any) -> bytes:        
        if(flag_rawmode == True): 
            return RawCodec.encode(self, string_ascii)
        raise Exception("not implemented yet")

    def decode(self, string_bin: bytes) -> Any:
        if(flag_rawmode == True): 
            return RawCodec.decode(self, string_bin)
        return string_bin[self.offset:self.string_len].decode('utf-8')

    def __len__(self) -> int:
        return self.string_len


class O3EComplexType(udsoncan.DidCodec):
    def __init__(self, string_len: int, idStr: str, subTypes : list):
        self.string_len = string_len
        self.id = idStr
        self.complex = True
        self.subTypes = subTypes

    def encode(self, string_ascii: Any) -> bytes:        
        if(flag_rawmode == True): 
            return RawCodec.encode(self, string_ascii)
        raise Exception("not implemented yet")

    def decode(self, string_bin: bytes) -> Any:
        if(flag_rawmode == True): 
            return RawCodec.decode(self, string_bin)
        result = dict()
        index = 0
        for subType in self.subTypes:
            result[subType.id] = subType.decode(string_bin[index:index+subType.string_len])
            index+=subType.string_len
        return dict(result)
    
    def __len__(self) -> int:
        return self.string_len


class O3ECompStat(udsoncan.DidCodec):
    def __init__(self, string_len: int, idStr: str):
        self.string_len = string_len
        self.id = idStr
        self.complex = True

    def encode(self, string_ascii: Any) -> bytes:        
        if(flag_rawmode == True): 
            return RawCodec.encode(self, string_ascii)
        raise Exception("not implemented yet")

    def decode(self, string_bin: bytes) -> Any:
        if(flag_rawmode == True): 
            return RawCodec.decode(self, string_bin)
        return {
            "starts": int.from_bytes([string_bin[7],string_bin[6]], byteorder="big", signed=False),
            "hours": int.from_bytes([string_bin[11],string_bin[10]], byteorder="big", signed=False)
        }

    def __len__(self) -> int:
        return self.string_len

class O3EAddElHeaterStat(udsoncan.DidCodec):
    def __init__(self, string_len: int, idStr: str):
        self.string_len = string_len
        self.id = idStr
        self.complex = True

    def encode(self, string_ascii: Any) -> bytes:        
        if(flag_rawmode == True): 
            return RawCodec.encode(self, string_ascii)
        raise Exception("not implemented yet")

    def decode(self, string_bin: bytes) -> Any:
        if(flag_rawmode == True): 
            return RawCodec.decode(self, string_bin)
        return {
            "starts": int.from_bytes([string_bin[4],string_bin[3]], byteorder="big", signed=False),
            "hours": int.from_bytes([string_bin[8],string_bin[7]], byteorder="big", signed=False)
        }

    def __len__(self) -> int:
        return self.string_len

class O3EHeatingCurve(udsoncan.DidCodec):
    def __init__(self, string_len: int, idStr: str):
        self.string_len = string_len
        self.id = idStr
        self.complex = True

    def encode(self, string_ascii: Any) -> bytes:        
        if(flag_rawmode == True): 
            return RawCodec.encode(self, string_ascii)
        raise Exception("not implemented yet")

    def decode(self, string_bin: bytes) -> Any:
        if(flag_rawmode == True): return RawCodec.decode(self, string_bin)
        return {
            "slope": float(string_bin[0]) / 10.0,
            "offset": int.from_bytes([string_bin[1]], byteorder="big", signed=True)
        }

    def __len__(self) -> int:
        return self.string_len
    
class O3EOperationState(udsoncan.DidCodec):
    def __init__(self, string_len: int, idStr: str):
        self.string_len = string_len
        self.id = idStr
        self.complex = True

    def encode(self, string_ascii: Any) -> bytes:        
        if(flag_rawmode == True): 
            return RawCodec.encode(self, string_ascii)
        raise Exception("not implemented yet")

    def decode(self, string_bin: bytes) -> Any:
        if(flag_rawmode == True): return RawCodec.decode(self, string_bin)
        return {
            "mode": int(string_bin[0]),
            "state": int(string_bin[1]),
        }

    def __len__(self) -> int:
        return self.string_len
