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
import Open3Eerrors 
import Open3EStatus, Open3EInfos, Open3EWarnings
import Open3Eenums

flag_rawmode = True
flag_dev = "vcal"

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


class O3EByteVal(udsoncan.DidCodec):
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
        return int(string_bin[self.offset])

    def __len__(self) -> int:
        return self.string_len

class O3EBool(udsoncan.DidCodec):
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
        mystr=""
        for i in range(self.offset, self.string_len):
            if(string_bin[i] == 0):
                break
            mystr += string_bin[i:i+1].decode('utf-8')
        return mystr

    def __len__(self) -> int:
        return self.string_len


class O3ESoftVers(udsoncan.DidCodec):
    def __init__(self, string_len: int, idStr: str):
        self.string_len = string_len
        self.id = idStr
        self.complex = False

    def encode(self, string_ascii: Any) -> bytes:        
        if(flag_rawmode == True): 
            return RawCodec.encode(self, string_ascii)
        raise Exception("not implemented yet")

    def decode(self, string_bin: bytes) -> Any:
        if(flag_rawmode == True): 
            return RawCodec.decode(self, string_bin)
        lstv = []
        for i in range(0, 7, 2):
            lstv.append(str(int.from_bytes(string_bin[i:i+2], byteorder="little")))
        return ".".join(lstv)

    def __len__(self) -> int:
        return self.string_len

class O3EMacAddr(udsoncan.DidCodec):
    def __init__(self, string_len: int, idStr: str): #string_bin = bytes.fromhex(string_ascii)
        self.string_len = string_len
        self.id = idStr
        self.complex = False

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

    def __len__(self) -> int:
        return self.string_len

class O3EIp4Addr(udsoncan.DidCodec):
    def __init__(self, string_len: int, idStr: str):
        self.string_len = string_len
        self.id = idStr
        self.complex = False

    def encode(self, string_ascii: Any) -> bytes:        
        if(flag_rawmode == True): 
            return RawCodec.encode(self, string_ascii)
        raise Exception("not implemented yet")

    def decode(self, string_bin: bytes) -> Any:
        if(flag_rawmode == True): 
            return RawCodec.decode(self, string_bin)
        return f"{int(string_bin[0]):03d}.{int(string_bin[1]):03d}.{int(string_bin[2]):03d}.{int(string_bin[3]):03d}"

    def __len__(self) -> int:
        return self.string_len

class O3ESdate(udsoncan.DidCodec):
    def __init__(self, string_len: int, idStr: str):
        self.string_len = string_len
        self.id = idStr
        self.complex = False

    def encode(self, string_ascii: Any) -> bytes:        
        if(flag_rawmode == True): 
            return RawCodec.encode(self, string_ascii)
        raise Exception("not implemented yet")

    def decode(self, string_bin: bytes) -> Any:
        if(flag_rawmode == True): 
            return RawCodec.decode(self, string_bin)
        return f"{int(string_bin[0]):02d}.{int(string_bin[1]):02d}.{2000+int(string_bin[2])}"

    def __len__(self) -> int:
        return self.string_len

class O3EStime(udsoncan.DidCodec):
    def __init__(self, string_len: int, idStr: str):
        self.string_len = string_len
        self.id = idStr
        self.complex = False

    def encode(self, string_ascii: Any) -> bytes:        
        if(flag_rawmode == True): 
            return RawCodec.encode(self, string_ascii)
        raise Exception("not implemented yet")

    def decode(self, string_bin: bytes) -> Any:
        if(flag_rawmode == True): 
            return RawCodec.decode(self, string_bin)
        return f"{int(string_bin[0]):02d}:{int(string_bin[1]):02d}:{int(string_bin[2]):02d}"

    def __len__(self) -> int:
        return self.string_len


class O3EUtc(udsoncan.DidCodec):
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
        val = datetime.datetime.fromtimestamp(int.from_bytes(string_bin[0:4], byteorder="little", signed=False)).strftime('%Y-%m-%d %H:%M:%S')
        return val

    def __len__(self) -> int:
        return self.string_len


class O3EEnum(udsoncan.DidCodec):
    def __init__(self, string_len: int, idStr: str, listStr:str):
        self.string_len = string_len
        self.id = idStr
        self.complex = False
        self.listStr = listStr

    def encode(self, string_ascii: Any) -> bytes:        
        raise Exception("not implemented yet")

    def decode(self, string_bin: bytes) -> str:
        if(flag_rawmode == True): 
            return RawCodec.decode(self, string_bin)
        try:
            val = int.from_bytes(string_bin[0:self.string_len], byteorder="little", signed=False)
            txt = Open3Eenums.E3Enums[self.listStr][val]
            return txt
        except:
            err = "Enum not found"
            return f"{err}: {self.listStr}.{val}"
        
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
            print(subType)
            result[subType.id] = subType.decode(string_bin[index:index+subType.string_len])
            index+=subType.string_len
        return dict(result)
    
    def __len__(self) -> int:
        return self.string_len

class O3EDtcList(udsoncan.DidCodec):
    def __init__(self, string_len: int, idStr: str, dtcType: str, subType: str="default"):
        self.string_len = string_len
        self.id = idStr
        self.complex = False
        self.dtcType = dtcType
        self.subType = subType

    def encode(self, string_ascii: Any) -> bytes:        
        raise Exception("not implemented yet")

    def decode(self, string_bin: bytes) -> Any:
        dtc = self.dtcType
        if(flag_rawmode == True): 
            return RawCodec.decode(self, string_bin)
        result = {
            "cntEvt": string_bin[0],
            dtc: []
            }
        for ofs in range(0,result["cntEvt"]):
            if self.subType == "History":
                result[dtc].append(toErrorEvent(string_bin[4+12*ofs:4+12+12*ofs],timeformat='VM',txt="eventDescription", type=dtc))
            else:
                result[dtc].append(toErrorEvent(string_bin[2+12*ofs:2+12+12*ofs],timeformat='VM',txt="eventDescription", type=dtc))
        return json.dumps(result)
    
    def __len__(self) -> int:
        return self.string_len


class O3EErrorDtcList(udsoncan.DidCodec):
    def __init__(self, string_len: int, idStr: str):
        self.string_len = string_len
        self.id = idStr
        self.complex = False

    def encode(self, string_ascii: Any) -> bytes:        
        raise Exception("not implemented yet")

    def decode(self, string_bin: bytes) -> Any:
        if(flag_rawmode == True): 
            return RawCodec.decode(self, string_bin)
        result = {
            "cntDtc": string_bin[0],
            "errors": []
            }
        for ofs in range(0,result["cntDtc"]):
            result["errors"].append(toErrorEvent(string_bin[2+12*ofs:2+12+12*ofs]))
        return json.dumps(result)
    
    def __len__(self) -> int:
        return self.string_len

class O3EErrorDtcHistory(udsoncan.DidCodec):
    def __init__(self, string_len: int, idStr: str):
        self.string_len = string_len
        self.id = idStr
        self.complex = False

    def encode(self, string_ascii: Any) -> bytes:        
        raise Exception("not implemented yet")

    def decode(self, string_bin: bytes) -> Any:
        if(flag_rawmode == True): 
            return RawCodec.decode(self, string_bin)
        result = {
            "cntDtc": string_bin[0],
            "totDtc": int.from_bytes(string_bin[2:4], byteorder="little", signed=False),
            "errors": []
            }
        for ofs in range(0,result["cntDtc"]):
            result["errors"].append(toErrorEvent(string_bin[4+12*ofs:4+12+12*ofs]))
        return json.dumps(result)
    
    def __len__(self) -> int:
        return self.string_len

class O3EEventLoggingHistory(udsoncan.DidCodec):
    def __init__(self, string_len: int, idStr: str):
        self.string_len = string_len
        self.id = idStr
        self.complex = False

    def encode(self, string_ascii: Any) -> bytes:        
        raise Exception("not implemented yet")

    def decode(self, string_bin: bytes) -> Any:
        if(flag_rawmode == True): 
            return RawCodec.decode(self, string_bin)
        result = {
            "cntEvt": string_bin[0],
            "events": []
            }
        for ofs in range(0,result["cntEvt"]):
            result["events"].append(toErrorEvent(string_bin[2+9*ofs:2+9+9*ofs],timeformat='ts',txt="event"))
        return json.dumps(result)
    
    def __len__(self) -> int:
        return self.string_len

def toErrorEvent(string_bin:bytes, timeformat='VM', txt="error", type="Info" ):
    id = int.from_bytes(string_bin[0:2], byteorder="little", signed=False)
    if timeformat == 'VM':
        dt = datetime.datetime(
                 string_bin[2]*100+string_bin[3], # year
                 string_bin[4],                   # month
                 string_bin[5],                   # day
                 string_bin[7],                   # hour
                 string_bin[8],                   # minute
                 string_bin[9]                    # second
                )
    if timeformat == 'ts':
        dt = datetime.datetime.fromtimestamp(int.from_bytes(string_bin[2:6], byteorder="little", signed=False))
    text = ""
    print(type)
    # load Errors for selected Eventtype
    try:
        if(type == "Error"):
            text = Open3Eerrors.E3errors[id]
        if(type == "Status"):
            text = Open3EStatus.E3Status[id]    
        if(type == "Info"):
            text = Open3EInfos.E3Infos[id]
        if(type == "Warning"):
            text = Open3EWarnings.E3Warnings[id]    
    except:
        text = "Description not found"
    
    
    event = {
        "id": id,
        txt : text,
        "dt": dt.strftime('%c'),            # Date & Time local format
        "ts": int(dt.timestamp()*1000)      # Unix timestamp (ms)
    }
    return event;

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
