"""
  Copyright 2023 abnoname
  
  Licensed under the Apache License, Version 2.0 (the "License");
  you 05_may not use this file except in compliance with the License.
  You 05_may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License.
"""

import Open3Ecodecs
from Open3Ecodecs import *

# Datapoints sourced from ViGuide Demo Mode:
# https://viguide.viessmann.com/installations/10000017?gatewaySerial=7736170-gw-serial-17&deviceSerial=7720533-device-serial

dataIdentifiers = {
    "name": "general", 
    "dids" : 
    {
        256 : O3EComplexType(36, "BusIdentification", [O3EByteVal(1, "BusAddress"), O3EEnum(1, "BusType", "BusTypes"), O3EEnum(1, "DeviceProperty","Devices"), O3EEnum(1, "DeviceFunction","Devices"), O3ESoftVers(8, "SW-Version"), O3ESoftVers(8, "HW-Version"), O3EUtf8(16, "VIN")]),
        262 : O3EList(122, "ServiceDtcHistory", [O3EByteVal(2, "Count"), O3EComplexType(12, "ListEntries",[O3EEnum(2,"Service","Services"), O3EDateTime(8, "DateTime"),O3EByteVal(2, "Unknown")] )]),
        268 : O3EComplexType(9, "FlowTemperatureSensor", [O3EInt16(2, "Actual", signed=True), O3EInt16(2, "Minimum", signed=True), O3EInt16(2, "Maximum", signed=True), O3EInt16(2, "Average", signed=True), O3EByteVal(1, "Unknown")]),
        381 : O3EComplexType(4, "CentralHeatingPump", [O3EByteVal(1, "State"), O3EInt8(1, "TargetValue"), O3EInt8(1, "Actual"), RawCodec(1, "Unknown")]), # Unit %, MyHomeMyData, see discussion #212
        382 : O3EComplexType(5, "UnitsAndFormats", [O3EEnum(1, "Units", "Units"), O3EEnum(1, "DateFormat", "DateFormats"), O3EEnum(1, "TimeFormat", "TimeFormats"), O3EByteVal(1, "TimeZone"), O3EByteVal(1, "Unknown")]),
        396 : O3EInt16(2, "DomesticHotWaterTemperatureSetpoint", signed=True),
        505 : O3ESdate(3, "Date"),
        507 : O3EUtc(4, "UniversalTimeCoordinated"),
        548 : O3EComplexType(24, "EnergyConsumptionCentralHeating", [O3EInt32(4, "Today", scale=10), O3EInt32(4, "Past7Days", scale=10), O3EInt32(4, "CurrentMonth", scale=10), O3EInt32(4, "PastMonth", scale=10), O3EInt32(4, "CurrentYear", scale=10), O3EInt32(4, "PastYear", scale=10)]),  
        592 : O3EMacAddr(6, "MacAddressLan"),
        604 : O3EComplexType(76, "GatewayApDataSet", [O3EUtf8(32, "SSID_AccessPoint"), O3EUtf8(40, "Password_AccessPoint"), O3EIp4Addr(4, "IP-Address_AccessPoint")]),
        691 : O3EList(57, "DomesticHotWaterTimeScheduleMonday",[O3EByteVal(1, "Count"), O3EComplexType(7, "Schedules",[O3EStime(2, "Start"),O3EStime(2, "Stop"), RawCodec(2, "Unknown"), O3EByteVal(1, "Mode")])]),
        692 : O3EList(57, "DomesticHotWaterTimeScheduleTuesday",[O3EByteVal(1, "Count"), O3EComplexType(7, "Schedules",[O3EStime(2, "Start"),O3EStime(2, "Stop"), RawCodec(2, "Unknown"), O3EByteVal(1, "Mode")])]),
        875 : O3EStime(2, "LegionellaProtectionStartTime"),
        1006 : O3EComplexType(4, "TargetQuickMode", [O3EByteVal(1, "OpMode"), O3EBool(1, "Required"), RawCodec(2, "Unknown")]), # MyHomeMyData, ref. https://community.viessmann.de/viessmann/attachments/viessmann/customers-heatpump-hybrid/74546/1/6196307%20Kundendatenpunktliste%20Vitocal%20(1).pdf
        1007 : O3EComplexType(4, "CurrentQuickMode", [O3EByteVal(1, "OpMode"), O3EBool(1, "Required"), RawCodec(2, "Unknown")]), # MyHomeMyData, ref. did 1006
        1097 : O3EComplexType(20, "ElectricityPrice", [RawCodec(4, "Unknown1"), RawCodec(4, "Unknown2"), O3EInt32(4, "NormalRate", scale=100), O3EInt32(4, "LowRate", scale = 100), RawCodec(4, "Unknown3")]), # Unit ct
        1603 : O3EComplexType(4, "PointOfCommonCouplingPower", [O3EInt16(2, "ActivePower", scale=1.0, signed=True), O3EInt16(2, "ReactivePower", scale=1.0, signed=True)]),,
        2214 : O3EComplexType(2, "BackupBoxConfiguration", [O3EInt8(1, "DischargeLimit", scale=1, signed=False),O3EInt8(1, "Unknown", scale=1, signed=False)]),
    }
}
