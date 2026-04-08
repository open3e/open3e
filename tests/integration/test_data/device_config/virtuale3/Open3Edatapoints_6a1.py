from Open3Ecodecs import *

dataIdentifiers = {
    "name": "EMCUMASTER",
    "dids": {
        256: None,
        262: None,
        382: None,
        505: None,
        507: None,
        592: None,
        604: None,
        1603: O3EComplexType(4, "PointOfCommonCouplingPower", [O3EInt16(2, "ActivePower", scale=1.0, signed=True), O3EInt16(2, "ReactivePower", scale=1.0, signed=True)]),
        2214: None,
    },
}
