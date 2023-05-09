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

    def __init__(self, string_len: int, idStr: str):
        self.string_len = string_len
        self.id = idStr

    def encode(self, string_ascii: float) -> bytes:
        raise Exception("not implemented yet")
        return ""

    def decode(self, string_bin: bytes) -> float:
        return ((int(string_bin[1]) << 8) + int(string_bin[0])) / 10;

    def __len__(self) -> int:
        return self.string_len

class O3EInt8(udsoncan.DidCodec):
    string_len: int

    def __init__(self, string_len: int, idStr: str):
        self.string_len = string_len
        self.id = idStr

    def encode(self, string_ascii: float) -> bytes:
        raise Exception("not implemented yet")
        return ""

    def decode(self, string_bin: bytes) -> float:
        return int(string_bin[0]);

    def __len__(self) -> int:
        return self.string_len
