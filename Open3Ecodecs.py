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

class RawCodec(udsoncan.DidCodec):
    string_len: int

    def __init__(self, string_len: int, idStr: str):
        self.string_len = string_len
        self.id = idStr
        self.complex = False

    def encode(self, string_ascii: Any) -> bytes:
        if len(string_ascii) != self.string_len:
            raise ValueError('String must be %d long' % self.string_len)
        return string_ascii

    def decode(self, string_bin: bytes) -> Any:
        string_ascii = string_bin.hex()
        return string_ascii

    def __len__(self) -> int:
        return self.string_len

class O3EInt16(udsoncan.DidCodec):
    string_len: int

    def __init__(self, string_len: int, idStr: str, scale: float = 10.0, offset: int = 0, signed=False):
        self.string_len = string_len
        self.id = idStr
        self.complex = False
        self.scale = scale
        self.offset = offset
        self.signed = signed

    def encode(self, string_ascii: float) -> bytes:
        raise Exception("not implemented yet")
        return ""

    def decode(self, string_bin: bytes) -> float:
        val = int.from_bytes([string_bin[self.offset + 1],string_bin[self.offset + 0]], byteorder="big", signed=self.signed)
        return val / self.scale;

    def __len__(self) -> int:
        return self.string_len

class O3EInt8(udsoncan.DidCodec):
    string_len: int

    def __init__(self, string_len: int, idStr: str, scale: float = 1.0, offset: int = 0, signed=False):
        self.string_len = string_len
        self.id = idStr
        self.complex = False
        self.scale = scale
        self.offset = offset
        self.signed = signed

    def encode(self, string_ascii: float) -> bytes:
        raise Exception("not implemented yet")
        return ""

    def decode(self, string_bin: bytes) -> float:
        val = int.from_bytes([string_bin[self.offset]], byteorder="big", signed=self.signed)
        return int(float(val) / self.scale);

    def __len__(self) -> int:
        return self.string_len


class O3ECompStat(udsoncan.DidCodec):
    string_len: int

    def __init__(self, string_len: int, idStr: str):
        self.string_len = string_len
        self.id = idStr
        self.complex = True

    def encode(self, string_ascii: float) -> bytes:
        raise Exception("not implemented yet")
        return ""

    def decode(self, string_bin: bytes): #-> int:
        return {
            "starts": int.from_bytes([string_bin[7],string_bin[6]], byteorder="big", signed=False),
            "hours": int.from_bytes([string_bin[11],string_bin[10]], byteorder="big", signed=False)
        }

    def __len__(self) -> int:
        return self.string_len

class O3EAddElHeaterStat(udsoncan.DidCodec):
    string_len: int

    def __init__(self, string_len: int, idStr: str):
        self.string_len = string_len
        self.id = idStr
        self.complex = True

    def encode(self, string_ascii: float) -> bytes:
        raise Exception("not implemented yet")
        return ""

    def decode(self, string_bin: bytes): #-> int:
        return {
            "starts": int.from_bytes([string_bin[4],string_bin[3]], byteorder="big", signed=False),
            "hours": int.from_bytes([string_bin[8],string_bin[7]], byteorder="big", signed=False)
        }

    def __len__(self) -> int:
        return self.string_len

class O3EHeatingCurve(udsoncan.DidCodec):
    string_len: int

    def __init__(self, string_len: int, idStr: str):
        self.string_len = string_len
        self.id = idStr
        self.complex = True

    def encode(self, string_ascii: float) -> bytes:
        raise Exception("not implemented yet")
        return ""

    def decode(self, string_bin: bytes): #-> int:
        return {
            "slope": float(string_bin[0]) / 10.0,
            "offset": int.from_bytes([string_bin[1]], byteorder="big", signed=True)
        }

    def __len__(self) -> int:
        return self.string_len