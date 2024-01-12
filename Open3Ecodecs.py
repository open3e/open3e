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
import datetime
import json
import Open3Eenums

flag_rawmode = True
flag_dev = "vcal"

class RawCodec(udsoncan.DidCodec):
    def __init__(self, string_len: int, idStr: str):
        self.string_len = string_len
        self.id = idStr

    def encode(self, string_ascii: Any) -> bytes:
        string_bin = bytes.fromhex(string_ascii)
        if len(string_bin) != self.string_len:
            raise ValueError('String must be %d long' % self.string_len)
        return string_bin

    def decode(self, string_bin: bytes) -> Any:
        string_ascii = string_bin.hex()
        return string_ascii

    def getCodecInfo(self):
        return ({"codec": self.__class__.__name__, "len": self.string_len, "id": self.id, "args": {}})

    def __len__(self) -> int:
        return self.string_len


class O3EInt(udsoncan.DidCodec):
    def __init__(self, string_len: int, idStr: str, byte_width: int, scale: float = 1.0, offset: int = 0, signed=False):
        self.string_len = string_len
        self.byte_width = byte_width
        self.id = idStr
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

    def getCodecInfo(self):
        return ({"codec": self.__class__.__name__, "len": self.string_len, "id": self.id, "args": {"scale":self.scale, "signed":self.signed, "offset":self.offset}})

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

class O3EByteVal(udsoncan.DidCodec):
    def __init__(self, string_len: int, idStr: str, offset: int = 0):
        self.string_len = string_len
        self.id = idStr
        self.offset = offset

    def encode(self, string_ascii: Any) -> bytes:        
        if(flag_rawmode == True): 
            return RawCodec.encode(self, string_ascii)
        string_bin = string_ascii.to_bytes(length=self.string_len,byteorder="little",signed=False)
        return string_bin

    def decode(self, string_bin: bytes) -> Any:
        if(flag_rawmode == True): 
            return RawCodec.decode(self, string_bin)
        return int.from_bytes(string_bin[self.offset:self.offset+self.string_len], byteorder="little", signed=False)

    def getCodecInfo(self):
        return ({"codec": self.__class__.__name__, "len": self.string_len, "id": self.id, "args": {"offset":self.offset}})

    def __len__(self) -> int:
        return self.string_len

class O3EBool(udsoncan.DidCodec):
    def __init__(self, string_len: int, idStr: str, offset: int = 0):
        self.string_len = string_len
        self.id = idStr
        self.offset = offset

    def encode(self, string_ascii: Any) -> bytes:        
        if(flag_rawmode == True): 
            return RawCodec.encode(self, string_ascii)
        raise Exception("not implemented yet")

    def decode(self, string_bin: bytes) -> Any:
        if(flag_rawmode == True): 
            return RawCodec.decode(self, string_bin)
        val = int(string_bin[self.offset])
        if(val==0):
            return "off"
        else:
            return "on"

    def getCodecInfo(self):
        return ({"codec": self.__class__.__name__, "len": self.string_len, "id": self.id, "args": {"offset":self.offset}})

    def __len__(self) -> int:
        return self.string_len

class O3EUtf8(udsoncan.DidCodec):
    def __init__(self, string_len: int, idStr: str, offset: int = 0):
        self.string_len = string_len
        self.id = idStr
        self.offset = offset

    def encode(self, string_ascii: Any) -> bytes:        
        if(flag_rawmode == True): 
            return RawCodec.encode(self, string_ascii)
        raise Exception("not implemented yet")

    def decode(self, string_bin: bytes) -> Any:
        if(flag_rawmode == True): 
            return RawCodec.decode(self, string_bin)
        mystr = string_bin[self.offset:self.offset+self.string_len].decode('utf-8')
        return mystr.replace('\x00', '')
       
    def getCodecInfo(self):
        return ({"codec": self.__class__.__name__, "len": self.string_len, "id": self.id, "args": {"offset":self.offset}})

    def __len__(self) -> int:
        return self.string_len


class O3ESoftVers(udsoncan.DidCodec):  # also working with hardware version
    def __init__(self, string_len: int, idStr: str):
        self.string_len = string_len
        self.id = idStr

    def encode(self, string_ascii: Any) -> bytes:        
        if(flag_rawmode == True): 
            return RawCodec.encode(self, string_ascii)
        raise Exception("not implemented yet")

    def decode(self, string_bin: bytes) -> Any:
        if(flag_rawmode == True): 
            return RawCodec.decode(self, string_bin)
        lstv = []
        for i in range(0, self.string_len, 2):
            lstv.append(str(int.from_bytes(string_bin[i:i+2], byteorder="little")))
        return ".".join(lstv)

    def getCodecInfo(self):
        return ({"codec": self.__class__.__name__, "len": self.string_len, "id": self.id, "args": {}})

    def __len__(self) -> int:
        return self.string_len

class O3EMacAddr(udsoncan.DidCodec):
    def __init__(self, string_len: int, idStr: str): #string_bin = bytes.fromhex(string_ascii)
        self.string_len = string_len
        self.id = idStr

    def encode(self, string_ascii: Any) -> bytes:        
        if(flag_rawmode == True): 
            return RawCodec.encode(self, string_ascii)
        raise Exception("not implemented yet")

    def decode(self, string_bin: bytes) -> Any:
        if(flag_rawmode == True): 
            return RawCodec.decode(self, string_bin)
        lstv = []
        for i in range(6):
            lstv.append(string_bin[i:i+1].hex().upper())
        return "-".join(lstv)

    def getCodecInfo(self):
        return ({"codec": self.__class__.__name__, "len": self.string_len, "id": self.id, "args": {}})

    def __len__(self) -> int:
        return self.string_len

class O3EIp4Addr(udsoncan.DidCodec):  # also working with Ip6
    def __init__(self, string_len: int, idStr: str):
        self.string_len = string_len
        self.id = idStr

    def encode(self, string_ascii: Any) -> bytes:        
        if(flag_rawmode == True): 
            return RawCodec.encode(self, string_ascii)
        raise Exception("not implemented yet")

    def decode(self, string_bin: bytes) -> Any:
        if(flag_rawmode == True): 
            return RawCodec.decode(self, string_bin)
        lstv = []
        for i in range(self.string_len):
            lstv.append(format(int(string_bin[i]), '03d'))
        return ".".join(lstv)

    def getCodecInfo(self):
        return ({"codec": self.__class__.__name__, "len": self.string_len, "id": self.id, "args": {}})

    def __len__(self) -> int:
        return self.string_len

class O3ESdate(udsoncan.DidCodec):
    def __init__(self, string_len: int, idStr: str):
        self.string_len = string_len
        self.id = idStr

    def encode(self, string_ascii: Any) -> bytes:        
        if(flag_rawmode == True): 
            return RawCodec.encode(self, string_ascii)
        raise Exception("not implemented yet")

    def decode(self, string_bin: bytes) -> Any:
        if(flag_rawmode == True): 
            return RawCodec.decode(self, string_bin)
        return f"{int(string_bin[0]):02d}.{int(string_bin[1]):02d}.{2000+int(string_bin[2])}"

    def getCodecInfo(self):
        return ({"codec": self.__class__.__name__, "len": self.string_len, "id": self.id, "args": {}})

    def __len__(self) -> int:
        return self.string_len

class O3EDateTime(udsoncan.DidCodec):
    def __init__(self, string_len: int, idStr: str, timeformat: str="VM"):
        self.string_len = string_len
        self.id = idStr
        self.timeformat = timeformat

    def encode(self, string_ascii: Any) -> bytes:        
        if(flag_rawmode == True): 
            return RawCodec.encode(self, string_ascii)
        raise Exception("not implemented yet")

    def decode(self, string_bin: bytes) -> Any:
        if(flag_rawmode == True): 
            return RawCodec.decode(self, string_bin)
        
        if self.timeformat == 'VM':
            dt = datetime.datetime(
                 string_bin[0]*100+string_bin[1], # year
                 string_bin[2],                   # month
                 string_bin[3],                   # day
                 string_bin[5],                   # hour
                 string_bin[6],                   # minute
                 string_bin[7]                    # second
                )
        if self.timeformat == 'ts':
            dt = datetime.datetime.fromtimestamp(int.from_bytes(string_bin[0:6], byteorder="little", signed=False))
        return { "DateTime": str(dt),
                 "Timestamp": int(dt.timestamp()*1000)
               }

    def getCodecInfo(self):
        return ({"codec": self.__class__.__name__, "len": self.string_len, "id": self.id, "args": {"timeformat":self.timeformat}})

    def __len__(self) -> int:
        return self.string_len

class O3EStime(udsoncan.DidCodec):
    def __init__(self, string_len: int, idStr: str):
        self.string_len = string_len
        self.id = idStr

    def encode(self, string_ascii: Any) -> bytes:        
        if(flag_rawmode == True): 
            return RawCodec.encode(self, string_ascii)
        raise Exception("not implemented yet")

    def decode(self, string_bin: bytes) -> Any:
        if(flag_rawmode == True): 
            return RawCodec.decode(self, string_bin)
        lstv = []
        for i in range(self.string_len):
            lstv.append(f"{(string_bin[i]):02d}")
        return ":".join(lstv)

    def getCodecInfo(self):
        return ({"codec": self.__class__.__name__, "len": self.string_len, "id": self.id, "args": {}})

    def __len__(self) -> int:
        return self.string_len

class O3EUtc(udsoncan.DidCodec):
    def __init__(self, string_len: int, idStr: str, offset: int = 0):
        self.string_len = string_len
        self.id = idStr
        self.offset = offset

    def encode(self, string_ascii: Any) -> bytes: 
        if(flag_rawmode == True): 
            return RawCodec.encode(self, string_ascii)
        raise Exception("not implemented yet")

    def decode(self, string_bin: bytes) -> Any:
        if(flag_rawmode == True): 
            return RawCodec.decode(self, string_bin)
        val = datetime.datetime.fromtimestamp(int.from_bytes(string_bin[0:4], byteorder="little", signed=False)).strftime('%Y-%m-%d %H:%M:%S')
        return str(val)

    def getCodecInfo(self):
        return ({"codec": self.__class__.__name__, "len": self.string_len, "id": self.id, "args": {"offset":self.offset}})

    def __len__(self) -> int:
        return self.string_len


class O3EEnum(udsoncan.DidCodec):
    def __init__(self, string_len: int, idStr: str, listStr:str):
        self.string_len = string_len
        self.id = idStr
        self.listStr = listStr

    def encode(self, string_ascii: Any) -> bytes:        
        if(flag_rawmode == True): 
            return RawCodec.encode(self, string_ascii)
        #raise Exception("not implemented yet")
        for key, value in Open3Eenums.E3Enums[self.listStr].items():
            if value.lower() == string_ascii.lower():
                string_bin = key.to_bytes(length=self.string_len,byteorder="little",signed=False)
                return string_bin
        raise Exception("not found")

    def decode(self, string_bin: bytes) -> str:
        if(flag_rawmode == True): 
            return RawCodec.decode(self, string_bin)
        try:
            val = int.from_bytes(string_bin[0:self.string_len], byteorder="little", signed=False)
            txt = Open3Eenums.E3Enums[self.listStr][val]
            return {"ID": val,
                    "Text": txt }
        except:
            return {"ID": val,
                    "Text": "not found in " + self.listStr}
        
    def getCodecInfo(self):
        return ({"codec": self.__class__.__name__, "len": self.string_len, "id": self.id, "args": {"listStr":self.listStr}})

    def __len__(self) -> int:
        return self.string_len
       
class O3EList(udsoncan.DidCodec):
    def __init__(self, string_len: int, idStr: str, subTypes: list, arraylength: int=0):
        self.string_len = string_len
        self.id = idStr
        self.subTypes = subTypes
        self.len = len

    def encode(self, string_ascii: Any) -> bytes:        
        raise Exception("not implemented yet")

    def decode(self, string_bin: bytes) -> Any:
        subTypes = self.subTypes
        idStr = self.id
        if(flag_rawmode == True): 
            return RawCodec.decode(self, string_bin)
        result = {}
        index = 0
        if(self.len == 0): 
            count = 0

        for subType in self.subTypes:
            # we expect a byte element with the name "Count" or "count"
            if subType.id.lower() == 'count':
                count = int(subType.decode(string_bin[index:index+subType.string_len]))
                result[subType.id]=count 
                index =+ subType.string_len 

            elif type(subType) is O3EComplexType:
                result[subType.id] = []
                for i in range(count):
                    result[subType.id].append(subType.decode(string_bin[index:index+subType.string_len]))
                    index+=subType.string_len

            else:
                result[subType.id]=subType.decode(string_bin[index:index+subType.string_len]) 
                index = index + subType.string_len

        return dict(result)
    
    def getCodecInfo(self):
        argsSubTypes = []
        for subType in self.subTypes:
            argsSubTypes.append(subType.getCodecInfo())
        return ({"codec": self.__class__.__name__, "len": self.string_len, "id": self.id, "args": {"subTypes":argsSubTypes}})

    def __len__(self) -> int:
        return self.string_len

class O3EArray(udsoncan.DidCodec):
    def __init__(self, string_len: int, idStr: str, subTypes: list, arraylength: int=0):
        self.string_len = string_len
        self.id = idStr
        self.subTypes = subTypes
        self.len = arraylength

    def encode(self, string_ascii: Any) -> bytes:        
        raise Exception("not implemented yet")

    def decode(self, string_bin: bytes) -> Any:
        subTypes = self.subTypes
        idStr = self.id
        if(flag_rawmode == True): 
            return RawCodec.decode(self, string_bin)
        result = {}
        index = 0
        count = self.len
        for subType in subTypes:
            result[subType.id]=[]
            for i in range(count):
                result[subType.id].append((subType.decode(string_bin[index:index+subType.string_len])))
                index+=subType.string_len
        return dict(result)
    
    def getCodecInfo(self):
        argsSubTypes = []
        for subType in self.subTypes:
            argsSubTypes.append(subType.getCodecInfo())
        return ({"codec": self.__class__.__name__, "len": self.string_len, "id": self.id, "args": {"subTypes":argsSubTypes, "arrayLength":self.len}})

    def __len__(self) -> int:
        return self.string_len

class O3EComplexType(udsoncan.DidCodec):
    def __init__(self, string_len: int, idStr: str, subTypes : list):
        self.string_len = string_len
        self.id = idStr
        self.subTypes = subTypes

    def encode(self, string_ascii: Any) -> bytes:        
        if(flag_rawmode == True): 
            return RawCodec.encode(self, string_ascii)
        else:
            try:
                string_bin = bytes()
                for subType in self.subTypes:
                    string_bin+=subType.encode(string_ascii[subType.id])
            except KeyError as e:
                raise ValueError(f"Cannot encode value due to missing key: {e}")
        return string_bin

    def decode(self, string_bin: bytes) -> Any:
        if(flag_rawmode == True): 
            return RawCodec.decode(self, string_bin)
        result = dict()
        index = 0
        for subType in self.subTypes:
            result[subType.id] = subType.decode(string_bin[index:index+subType.string_len])
            index+=subType.string_len
        return dict(result)
    
    def getCodecInfo(self):
        argsSubTypes = []
        for subType in self.subTypes:
            argsSubTypes.append(subType.getCodecInfo())
        return ({"codec": self.__class__.__name__, "len": self.string_len, "id": self.id, "args": {"subTypes":argsSubTypes}})

    def __len__(self) -> int:
        return self.string_len
