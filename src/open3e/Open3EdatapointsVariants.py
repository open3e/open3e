"""
    List of variants of data points having other lengths.
    Typically depends on device and/or Viessmann software version.
"""

from open3e.Open3Ecodecs import *

dataIdentifiers = {
    "name": "variants", 
    "Version": "20260114",
    "dids" : 
    {
        1603 : { 12: O3EComplexType(12, "PointOfCommonCouplingPower", [O3EInt16(2, "ActivePower", scale=1.0, signed=True), O3EInt16(2, "ReactivePower", scale=1.0, signed=True), O3EInt16(2, "ActivePowerDup", scale=1.0, signed=True), O3EInt16(2, "PadZeros", scale=1.0, signed=True), O3EInt16(2, "ReactivePowerDup", scale=1.0, signed=True), O3EInt16(2, "PadOnes", scale=1.0, signed=True),]), # MyHomeMyData, see discussion #315
            },
        1884 : { 85: O3EComplexType(85, "RoomOneProperty", [O3EUtf8(39, "Roomname"), RawCodec(4, "Unknown1"), O3EEnum(1, "Roomtype", "Roomtypes"), RawCodec(1, "Unknown2"), O3EEnum(1, "TemperatureControl", "TemperatureControlLevels"), RawCodec(29, "Unknown3"), O3EEnum(1, "WindowDetection", "WindowDetectionState"), RawCodec(9, "Unknown4")]), # (str, "name"); (o5cVar, "roomType"); (h5cVar, "lockMode"); (c5cVar, "roomControlAlgorithmType"); (list, "supplyChannel"); (list2, "roomDevices");
            },
        1887 : { 85: O3EComplexType(85, "RoomTwoProperty", [O3EUtf8(39, "Roomname"), RawCodec(4, "Unknown1"), O3EEnum(1, "Roomtype", "Roomtypes"), RawCodec(1, "Unknown2"), O3EEnum(1, "TemperatureControl", "TemperatureControlLevels"), RawCodec(29, "Unknown3"),  O3EEnum(1, "WindowDetection", "WindowDetectionState"), RawCodec(9, "Unknown4")]),
            },
        1890 : { 85: O3EComplexType(85, "RoomThreeProperty", [O3EUtf8(39, "Roomname"), RawCodec(4, "Unknown1"), O3EEnum(1, "Roomtype", "Roomtypes"), RawCodec(1, "Unknown2"), O3EEnum(1, "TemperatureControl", "TemperatureControlLevels"), RawCodec(29, "Unknown3"),  O3EEnum(1, "WindowDetection", "WindowDetectionState"), RawCodec(9, "Unknown4")]),
            },
        1893 : { 85: O3EComplexType(85, "RoomFourProperty", [O3EUtf8(39, "Roomname"), RawCodec(4, "Unknown1"), O3EEnum(1, "Roomtype", "Roomtypes"), RawCodec(1, "Unknown2"), O3EEnum(1, "TemperatureControl", "TemperatureControlLevels"), RawCodec(29, "Unknown3"),  O3EEnum(1, "WindowDetection", "WindowDetectionState"), RawCodec(9, "Unknown4")]),
            },
        1896 : { 85: O3EComplexType(85, "RoomFiveProperty", [O3EUtf8(39, "Roomname"), RawCodec(4, "Unknown1"), O3EEnum(1, "Roomtype", "Roomtypes"), RawCodec(1, "Unknown2"), O3EEnum(1, "TemperatureControl", "TemperatureControlLevels"), RawCodec(29, "Unknown3"),  O3EEnum(1, "WindowDetection", "WindowDetectionState"), RawCodec(9, "Unknown4")]),
            },
        1899 : { 85: O3EComplexType(85, "RoomSixProperty", [O3EUtf8(39, "Roomname"), RawCodec(4, "Unknown1"), O3EEnum(1, "Roomtype", "Roomtypes"), RawCodec(1, "Unknown2"), O3EEnum(1, "TemperatureControl", "TemperatureControlLevels"), RawCodec(29, "Unknown3"),  O3EEnum(1, "WindowDetection", "WindowDetectionState"), RawCodec(9, "Unknown4")]),
            },
        1902 : { 85: O3EComplexType(85, "RoomSevenProperty", [O3EUtf8(39, "Roomname"), RawCodec(4, "Unknown1"), O3EEnum(1, "Roomtype", "Roomtypes"), RawCodec(1, "Unknown2"), O3EEnum(1, "TemperatureControl", "TemperatureControlLevels"), RawCodec(29, "Unknown3"),  O3EEnum(1, "WindowDetection", "WindowDetectionState"), RawCodec(9, "Unknown4")]),
            },
        1905 : { 85: O3EComplexType(85, "RoomEightProperty", [O3EUtf8(39, "Roomname"), RawCodec(4, "Unknown1"), O3EEnum(1, "Roomtype", "Roomtypes"), RawCodec(1, "Unknown2"), O3EEnum(1, "TemperatureControl", "TemperatureControlLevels"), RawCodec(29, "Unknown3"),  O3EEnum(1, "WindowDetection", "WindowDetectionState"), RawCodec(9, "Unknown4")]),
            },
        1908 : { 85: O3EComplexType(85, "RoomNineProperty", [O3EUtf8(39, "Roomname"), RawCodec(4, "Unknown1"), O3EEnum(1, "Roomtype", "Roomtypes"), RawCodec(1, "Unknown2"), O3EEnum(1, "TemperatureControl", "TemperatureControlLevels"), RawCodec(29, "Unknown3"),  O3EEnum(1, "WindowDetection", "WindowDetectionState"), RawCodec(9, "Unknown4")]),
            },
        1911 : { 85: O3EComplexType(85, "RoomTenProperty", [O3EUtf8(39, "Roomname"), RawCodec(4, "Unknown1"), O3EEnum(1, "Roomtype", "Roomtypes"), RawCodec(1, "Unknown2"), O3EEnum(1, "TemperatureControl", "TemperatureControlLevels"), RawCodec(29, "Unknown3"),  O3EEnum(1, "WindowDetection", "WindowDetectionState"), RawCodec(9, "Unknown4")]),
            },
        1014 : { 85: O3EComplexType(85, "RoomElevenProperty", [O3EUtf8(39, "Roomname"), RawCodec(4, "Unknown1"), O3EEnum(1, "Roomtype", "Roomtypes"), RawCodec(1, "Unknown2"), O3EEnum(1, "TemperatureControl", "TemperatureControlLevels"), RawCodec(29, "Unknown3"),  O3EEnum(1, "WindowDetection", "WindowDetectionState"), RawCodec(9, "Unknown4")]),
            },
        1017 : { 85: O3EComplexType(85, "RoomTwelveProperty", [O3EUtf8(39, "Roomname"), RawCodec(4, "Unknown1"), O3EEnum(1, "Roomtype", "Roomtypes"), RawCodec(1, "Unknown2"), O3EEnum(1, "TemperatureControl", "TemperatureControlLevels"), RawCodec(29, "Unknown3"),  O3EEnum(1, "WindowDetection", "WindowDetectionState"), RawCodec(9, "Unknown4")]),
            },
        1920 : { 85: O3EComplexType(85, "RoomThirteenProperty", [O3EUtf8(39, "Roomname"), RawCodec(4, "Unknown1"), O3EEnum(1, "Roomtype", "Roomtypes"), RawCodec(1, "Unknown2"), O3EEnum(1, "TemperatureControl", "TemperatureControlLevels"), RawCodec(29, "Unknown3"),  O3EEnum(1, "WindowDetection", "WindowDetectionState"), RawCodec(9, "Unknown4")]),
            },
        1923 : { 85: O3EComplexType(85, "RoomFourteenProperty", [O3EUtf8(39, "Roomname"), RawCodec(4, "Unknown1"), O3EEnum(1, "Roomtype", "Roomtypes"), RawCodec(1, "Unknown2"), O3EEnum(1, "TemperatureControl", "TemperatureControlLevels"), RawCodec(29, "Unknown3"),  O3EEnum(1, "WindowDetection", "WindowDetectionState"), RawCodec(9, "Unknown4")]),
            },
        1926 : { 85: O3EComplexType(85, "RoomFifteenProperty", [O3EUtf8(39, "Roomname"), RawCodec(4, "Unknown1"), O3EEnum(1, "Roomtype", "Roomtypes"), RawCodec(1, "Unknown2"), O3EEnum(1, "TemperatureControl", "TemperatureControlLevels"), RawCodec(29, "Unknown3"),  O3EEnum(1, "WindowDetection", "WindowDetectionState"), RawCodec(9, "Unknown4")]),
            },
        1929 : { 85: O3EComplexType(85, "RoomSixteenProperty", [O3EUtf8(39, "Roomname"), RawCodec(4, "Unknown1"), O3EEnum(1, "Roomtype", "Roomtypes"), RawCodec(1, "Unknown2"), O3EEnum(1, "TemperatureControl", "TemperatureControlLevels"), RawCodec(29, "Unknown3"),  O3EEnum(1, "WindowDetection", "WindowDetectionState"), RawCodec(9, "Unknown4")]),
            },
        1932 : { 85: O3EComplexType(85, "RoomSeventeenProperty", [O3EUtf8(39, "Roomname"), RawCodec(4, "Unknown1"), O3EEnum(1, "Roomtype", "Roomtypes"), RawCodec(1, "Unknown2"), O3EEnum(1, "TemperatureControl", "TemperatureControlLevels"), RawCodec(29, "Unknown3"),  O3EEnum(1, "WindowDetection", "WindowDetectionState"), RawCodec(9, "Unknown4")]),
            },
        1935 : { 85: O3EComplexType(85, "RoomEightteenProperty", [O3EUtf8(39, "Roomname"), RawCodec(4, "Unknown1"), O3EEnum(1, "Roomtype", "Roomtypes"), RawCodec(1, "Unknown2"), O3EEnum(1, "TemperatureControl", "TemperatureControlLevels"), RawCodec(29, "Unknown3"),  O3EEnum(1, "WindowDetection", "WindowDetectionState"), RawCodec(9, "Unknown4")]),
            },
        1938 : { 85: O3EComplexType(85, "RoomNineteenProperty", [O3EUtf8(39, "Roomname"), RawCodec(4, "Unknown1"), O3EEnum(1, "Roomtype", "Roomtypes"), RawCodec(1, "Unknown2"), O3EEnum(1, "TemperatureControl", "TemperatureControlLevels"), RawCodec(29, "Unknown3"),  O3EEnum(1, "WindowDetection", "WindowDetectionState"), RawCodec(9, "Unknown4")]),
            },
        1941 : { 85: O3EComplexType(85, "RoomTwentyProperty", [O3EUtf8(39, "Roomname"), RawCodec(4, "Unknown1"), O3EEnum(1, "Roomtype", "Roomtypes"), RawCodec(1, "Unknown2"), O3EEnum(1, "TemperatureControl", "TemperatureControlLevels"), RawCodec(29, "Unknown3"),  O3EEnum(1, "WindowDetection", "WindowDetectionState"), RawCodec(9, "Unknown4")]),
            },
    }
}