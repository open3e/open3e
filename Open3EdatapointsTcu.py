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

import Open3Ecodecs
from Open3Ecodecs import *

dataIdentifiers = {
    # VCMU Interner CAN-BUS: 54
    # Vapor Compression Management Unit
    "name": "VCMU", 
    "dids" : 
    {
        256 : None,
        265 : None,
        377 : None,
        505 : None,
        506 : None,
        507 : None,
        580 : None,
        581 : None,
        593 : None,
        602 : None,
        603 : None,
        604 : None,
        607 : None,
        616 : None,
        617 : None,
        618 : None,
        619 : None,
        620 : None,
        621 : None,
        625 : None,
        900 : None,
        924 : None,
        928 : None,
        954 : None,
        961 : None,
        964 : None,
        1165 : None,
        1233 : None,
        1234 : None,
        1235 : None,
        1236 : None,
        1237 : None,
        1286 : None,
        1287 : None,
        1288 : None,
        1289 : None,
        1494 : None,
        1538 : None,
        1539 : None,
        1540 : None,
        2375 : None,
        2376 : None,
        2377 : None,
        2378 : None,
        2379 : None,
        2380 : None,
#        2534 : O3EList(181, "BusTopologyMatrixSix", [O3EInt8(1, "Count"), O3EComplexType(36, "TopologyElement",[O3EByteVal(1, "NodeID"), O3EEnum(1, "BusType", "BusTypes"), O3EByteVal(1, "DeviceProperty"), O3EByteVal(1, "DeviceFunction"), O3ESoftVers(8, "SW-Version"), O3ESoftVers(8, "HW-Version"), O3EUtf8(16, "VIN")])]),
        2534 : RawCodec(181, "BusTopologyMatrixSix"),
        2535 : RawCodec(181, "BusTopologyMatrixSeven"),
        2536 : RawCodec(181, "BusTopologyMatrixEight"),
        2537 : RawCodec(181, "BusTopologyMatrixNine"),
        2538 : RawCodec(181, "BusTopologyMatrixTen"),
        2554 : None,
        3056 : None,
        3057 : None,
    }
}