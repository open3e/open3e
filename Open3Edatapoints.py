"""
   Copyright 2023 abnoname
   
   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at
"),
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
    256 : RawCodec(36, "BusIdent"),
    268 : O3EInt16(9, "FlowTempSensor"),
    269 : O3EInt16(9, "ReturnTempSensor"),
    271 : O3EInt16(9, "DomesticHotWaterSensor"),
    274 : O3EInt16(9, "OutsideTempSensor"),
    318 : O3EInt16(9, "WaterPressureSensor"),
    320 : O3EInt16(9, "PrimaryHeatExchangerLiquidTempSensor"),
    321 : O3EInt16(9, "CompressorInletTempSensor"),
    324 : O3EInt16(9, "CompressorOutletTempSensor"),
    355 : O3EInt16(9, "SecondaryHeatExchangerLiquidTempSensor"),
    1043 : O3EInt16(5, "FlowMeterSensor"),
    377 : RawCodec(16, "IdentNumber"),
    424 : O3EInt16(9, "Mixer1TempSetpoint"),
    426 : O3EInt16(9, "Mixer2TempSetpoint"),
    428 : O3EInt16(9, "Mixer3TempSetpoint"),
    430 : O3EInt16(9, "Mixer4TempSetpoint"),

    # Reference: vibooks UK 6194799_Service_Intructions.pdf
    896 : RawCodec(2, "OutsideTempOffset"),
    919 : RawCodec(2, "OutsideTempDampingFactor"),
    897 : O3EInt8(1, "ScreedDryingProfileActivation"),
    933 : O3EInt16(9, "Mixer1Settings"),
    934 : O3EInt16(9, "Mixer2Settings"),
    935 : O3EInt16(9, "Mixer3Settings"),
    936 : O3EInt16(9, "Mixer4Settings"),
    1100 : RawCodec(3, "CentralHeaterPumpMinMaxLimit"),
    1192 : RawCodec(10, "Mixer1FlowTempMinMaxLimit"),
    1193 : RawCodec(10, "Mixer2FlowTempMinMaxLimit"),
    1194 : RawCodec(10, "Mixer3FlowTempMinMaxLimit"),
    1195 : RawCodec(10, "Mixer4FlowTempMinMaxLimit"),
    1240 : O3EInt8(1, "CentralHeaterPumpMode"),
    1395 : RawCodec(3, "Mixer1SummerSavingTempThresh"),
    1396 : RawCodec(3, "Mixer2SummerSavingTempThresh"),
    1397 : RawCodec(3, "Mixer3SummerSavingTempThresh"),
    1398 : RawCodec(3, "Mixer4SummerSavingTempThresh"),
    2405 : RawCodec(6, "Mixer1ConstantFlowSetTempCool"),
    2406 : RawCodec(6, "Mixer2ConstantFlowSetTempCool"),
    2407 : RawCodec(6, "Mixer3ConstantFlowSetTempCool"),
    2408 : RawCodec(6, "Mixer4ConstantFlowSetTempCool"),
    2409 : RawCodec(12, "Mixer1MinMaxFlowSetTempCool"),
    2410 : RawCodec(12, "Mixer2MinMaxFlowSetTempCool"),
    2411 : RawCodec(12, "Mixer3MinMaxFlowSetTempCool"),
    2412 : RawCodec(12, "Mixer4MinMaxFlowSetTempCool"),
    2426 : RawCodec(6, "Mixer1EcoSettings"),
    2427 : RawCodec(6, "Mixer2EcoSettings"),
    2428 : RawCodec(6, "Mixer3EcoSettings"),
    2429 : RawCodec(6, "Mixer4EcoSettings"),
    2452 : RawCodec(4, "Mixer1TempThreshCool"),
    2453 : RawCodec(4, "Mixer2TempThreshCool"),
    2454 : RawCodec(4, "Mixer3TempThreshCool"),
    2455 : RawCodec(4, "Mixer4TempThreshCool"),
    497 : RawCodec(5, "DomesticHotWaterCirculationPumpMode"),
    503 : RawCodec(2, "ScaldProtection"),
    504 : RawCodec(14, "DomesticHotWaterSetpoint"),
    874 : RawCodec(3, "Legi1llaProtectionTargetTempSetpoint"),
    1085 : RawCodec(4, "DomesticHotWaterHysteresis"),
    1087 : RawCodec(2, "MaxDomesticHotWaterLoadingTime"),
    1101 : RawCodec(3, "DomesticHotWaterPumpMinMaxLimit"),
    2540 : RawCodec(6, "NoiseReductionSettings"),
    2340 : RawCodec(2, "ElectricalHeaterConfiguration"),
    2544 : O3EInt8(1, "EnableElectricalHeaterSmartGridLock"),
    2545 : O3EInt8(1, "EnableElectricalHeaterSmartGridIncreaseMaxDemand"),
    2404 : RawCodec(6, "BivalenceControlMode"),
    2626 : RawCodec(4, "MaxPowerElectricalHeater"),
    2796 : RawCodec(2, "ExternalHeaterConfiguration"),
    2853 : RawCodec(2, "ExternalHeaterTimeIntegralThershold"),
    2940 : RawCodec(3, "ExternalHeaterDelayTimer"),
    2543 : RawCodec(10, "SmartGridTempOffsets"),
    2560 : O3EInt8(1, "SmartGridFeatureSelection")
}