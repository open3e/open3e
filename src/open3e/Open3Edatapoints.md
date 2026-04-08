# Open3E - List of data points
- Version of general data points: 20260227
- Version of variant data points: 20260217

### Remarks
* Information on write access to data points (column Access) is based on documents of Viessmann
  * ro => data point is read only
  * rw => data point is read and write. However, device my reject or ignore write access anyway

### Table of contents
[Frequently used data points including subs](#frequently-used-data-points-including-subs)

[Frequently used data points as compact list](#frequently-used-data-points-in-compact-format)

[All presently known data points including subs](#all-presently-known-data-points-including-subs)

[All presently known data points as compact list](#all-presently-known-data-points-in-compact-format)

## Frequently used data points including subs
|  Did | ID   | Codec | Length | Unit  |   Access | Further info |
| ---: | :--- | :---  | ---:   | :---: |  :---:  | :---         |
|**256**|[**BusIdentification**](## "Device infos")|*O3EComplexType*|36||ro||
| |- BusAddress|O3EByteVal|1||||
| |- [BusType](## "{0: OwnBus, 1: PlusBus, 2: CanInternal, 3: CanExternal, 4: InternalUart, 5: Zigbee, 6: CanRaw, 7: Unkown, 8: ModBus, 9: EEBUS, 10: PlusBusTwo, 11: ISquaredCBus, 12: HEMS_Bus, 13: TL_SolarLogBus, 14: ServiceBus}")|O3EEnum|1||||
| |- [DeviceProperty](## "{0: NOTHING, 1: BACKENDGATEWAY, 2: HMUMASTER, 3: HMUSLAVE, 4: MCUMASTER, 5: MCUSLAVE, 6: HMI, 7: BCU, 8: GASAIRRATIOSYSTEM, 9: ADIO, 10: DIO, 11: KNXGATEWAY, 12: BACNETGATEWAY, 13: MODBUSGATEWAY, 14: MBUS, 15: FRIWASTATION, 16: FUELCELL, 17: CSC, 18: PHOTOVOLTAIC, 19: PRODUCTIONGATEWAY, 20: DIAGNOSTICGATEWAY, 21: SDIO, 22: MTWOIO, 23: REMOTECONTROLLOCAL, 24: CLIMASENSOR, 25: TEMPERATURERADIATORVALVE, 26: UNDERFLOORHEATINGVALVE, 27: ENERGYMETER, 28: EMCUMASTER, 29: EMCUSLAVE, 30: BMCU, 31: HPMUMASTER, 32: HPMUSLAVE, 33: VCMU, 34: EHCU, 35: MZIO, 36: PBE, 37: HBMU, 38: OSME, 39: TWOSTEPPERMOTOR, 40: INVERTER, 41: SMARTROOMCONTROL, 42: VCUMASTER, 43: VCUSLAVE, 44: CANOPENIOMODULE, 45: FAN, 46: ELECTRICALPREHEATER, 47: ELECTRICALPOSTHEATER, 48: GENERICHEATPUMP, 49: HOMEENERGYMANAGEMENTSYSTEM, 50: EEBUSHUB, 51: HIO, 52: BCUSLAVE, 53: UNDERFLOORHEATINGBOX, 54: ZIGBEERANGEEXTENDER, 55: AIRQUALITYSENSOR, 56: WATERSOFTENER, 57: AIRPURIFIER, 58: CONNECTIONADAPTERSTEPPERMOTOR, 59: REFRIGERATIONFURNITURETYPE, 60: SOLARLOGGATEWAY, 61: SYSTEMCONTROLLEREMBEDDED, 62: WALLBOX, 63: APARTMENTTRANSFERSTATION, 64: DHWTS, 65: VENTILATIONUNIT}")|O3EEnum|1||||
| |- [DeviceFunction](## "{0: NOTHING, 1: BACKENDGATEWAY, 2: HMUMASTER, 3: HMUSLAVE, 4: MCUMASTER, 5: MCUSLAVE, 6: HMI, 7: BCU, 8: GASAIRRATIOSYSTEM, 9: ADIO, 10: DIO, 11: KNXGATEWAY, 12: BACNETGATEWAY, 13: MODBUSGATEWAY, 14: MBUS, 15: FRIWASTATION, 16: FUELCELL, 17: CSC, 18: PHOTOVOLTAIC, 19: PRODUCTIONGATEWAY, 20: DIAGNOSTICGATEWAY, 21: SDIO, 22: MTWOIO, 23: REMOTECONTROLLOCAL, 24: CLIMASENSOR, 25: TEMPERATURERADIATORVALVE, 26: UNDERFLOORHEATINGVALVE, 27: ENERGYMETER, 28: EMCUMASTER, 29: EMCUSLAVE, 30: BMCU, 31: HPMUMASTER, 32: HPMUSLAVE, 33: VCMU, 34: EHCU, 35: MZIO, 36: PBE, 37: HBMU, 38: OSME, 39: TWOSTEPPERMOTOR, 40: INVERTER, 41: SMARTROOMCONTROL, 42: VCUMASTER, 43: VCUSLAVE, 44: CANOPENIOMODULE, 45: FAN, 46: ELECTRICALPREHEATER, 47: ELECTRICALPOSTHEATER, 48: GENERICHEATPUMP, 49: HOMEENERGYMANAGEMENTSYSTEM, 50: EEBUSHUB, 51: HIO, 52: BCUSLAVE, 53: UNDERFLOORHEATINGBOX, 54: ZIGBEERANGEEXTENDER, 55: AIRQUALITYSENSOR, 56: WATERSOFTENER, 57: AIRPURIFIER, 58: CONNECTIONADAPTERSTEPPERMOTOR, 59: REFRIGERATIONFURNITURETYPE, 60: SOLARLOGGATEWAY, 61: SYSTEMCONTROLLEREMBEDDED, 62: WALLBOX, 63: APARTMENTTRANSFERSTATION, 64: DHWTS, 65: VENTILATIONUNIT}")|O3EEnum|1||||
| |- [SW-Version](## "??.???.YYcw.ver")|O3ESoftVers|8||||
| |- HW-Version|O3ESoftVers|8||||
| |- VIN|O3EUtf8|16||||
|**257**|[**StatusDtcList**](## "List of active status messages")|*O3EList*|122||ro||
| |- [Count](## "Number of entries listed")|O3EByteVal|2||||
| |- - State|O3EEnum|2||||
| |- - [DateTime](## "Date of event")|O3EDateTime|8||||
| |- - Unknown|O3EByteVal|2||||
|**258**|[**StatusDtcHistory**](## "History of status messages")|*O3EList*|122||ro||
| |- [Count](## "Number of entries listed")|O3EByteVal|2||||
| |- - State|O3EEnum|2||||
| |- - [DateTime](## "Date of event")|O3EDateTime|8||||
| |- - Unknown|O3EByteVal|2||||
|**259**|[**InfoDtcList**](## "List of active info messages")|*O3EList*|122||ro||
| |- [Count](## "Number of entries listed")|O3EByteVal|2||||
| |- - Info|O3EEnum|2||||
| |- - [DateTime](## "Date of event")|O3EDateTime|8||||
| |- - Unknown|O3EByteVal|2||||
|**260**|[**InfoDtcHistory**](## "History of info messages")|*O3EList*|122||ro||
| |- [Count](## "Number of entries listed")|O3EByteVal|2||||
| |- - Info|O3EEnum|2||||
| |- - [DateTime](## "Date of event")|O3EDateTime|8||||
| |- - Unknown|O3EByteVal|2||||
|**261**|[**ServiceDtcList**](## "List of active service messages")|*O3EList*|122||ro||
| |- [Count](## "Number of entries listed")|O3EByteVal|2||||
| |- - [Service](## "{0: NoServiceRequired, 1: HoursTillServiceExpired, 2: ReplaceSacrificialAnode, 4: RefillWaterSystem, 5: RegularMaintenanceActive, 6: OverhaulActive, 7: DurationOfLife, 8: BurnerOperatingHoursTillServiceExpired, 9: ServiceFuelCellSixMonthsTillServiceExpired, 10: ServiceFuelCellFiveMonthsTillServiceExpired, 11: ServiceFuelCellFourMonthsTillServiceExpired, 12: ServiceFuelCellThreeMonthsTillServiceExpired, 13: ServiceFuelCellTwoMonthTillServiceExpired, 14: ServiceFuelCellFourtyfiveDaysTillServiceExpired, 15: ServiceFuelCellOneMonthTillServiceExpired, 16: ServiceFuelCellSixMonthsTillOverhaulExpired, 17: ServiceFuelCellFiveMonthsTillOverhaulExpired, 18: ServiceFuelCellFourMonthsTillOverhaulExpired, 19: ServiceFuelCellThreeMonthsTillOverhaulExpired, 20: ServiceFuelCellTwoMonthTillOverhaulExpired, 21: ServiceFuelCellFourtyfiveDaysTillOverhaulExpired, 22: ServiceFuelCellOneMonthTillOverhaulExpired, 23: ServiceFuelCellSixMonthsTillEndOfLife, 24: ServiceFuelCellFiveMonthsTillEndOfLife, 25: ServiceFuelCellFourMonthsTillEndOfLife, 26: ServiceFuelCellThreeMonthsTillEndOfLife, 27: ServiceFuelCellTwoMonthTillEndOfLife, 28: ServiceFuelCellFourtyfiveDaysTillEndOfLife, 29: ServiceFuelCellOneMonthTillEndOfLife, 30: BalancingInProgress, 31: BackupPowerFunctionActive, 32: BatteryLow, 33: BatteryDeviceTurnedOff, 34: MaintenanceIntervalHydraulicFilterExpired, 35: MaintenanceIntervalVentilationFilterExpired, 36: ContaminationAirFilter, 37: LagDeviceDtcReported, 65533: ViewedServiceList, 65534: ServiceDoneSuccessful}")|O3EEnum|2||||
| |- - [DateTime](## "Date of event")|O3EDateTime|8||||
| |- - Unknown|O3EByteVal|2||||
|**262**|[**ServiceDtcHistory**](## "History of service messages")|*O3EList*|122||ro||
| |- [Count](## "Number of entries listed")|O3EByteVal|2||||
| |- - [Service](## "{0: NoServiceRequired, 1: HoursTillServiceExpired, 2: ReplaceSacrificialAnode, 4: RefillWaterSystem, 5: RegularMaintenanceActive, 6: OverhaulActive, 7: DurationOfLife, 8: BurnerOperatingHoursTillServiceExpired, 9: ServiceFuelCellSixMonthsTillServiceExpired, 10: ServiceFuelCellFiveMonthsTillServiceExpired, 11: ServiceFuelCellFourMonthsTillServiceExpired, 12: ServiceFuelCellThreeMonthsTillServiceExpired, 13: ServiceFuelCellTwoMonthTillServiceExpired, 14: ServiceFuelCellFourtyfiveDaysTillServiceExpired, 15: ServiceFuelCellOneMonthTillServiceExpired, 16: ServiceFuelCellSixMonthsTillOverhaulExpired, 17: ServiceFuelCellFiveMonthsTillOverhaulExpired, 18: ServiceFuelCellFourMonthsTillOverhaulExpired, 19: ServiceFuelCellThreeMonthsTillOverhaulExpired, 20: ServiceFuelCellTwoMonthTillOverhaulExpired, 21: ServiceFuelCellFourtyfiveDaysTillOverhaulExpired, 22: ServiceFuelCellOneMonthTillOverhaulExpired, 23: ServiceFuelCellSixMonthsTillEndOfLife, 24: ServiceFuelCellFiveMonthsTillEndOfLife, 25: ServiceFuelCellFourMonthsTillEndOfLife, 26: ServiceFuelCellThreeMonthsTillEndOfLife, 27: ServiceFuelCellTwoMonthTillEndOfLife, 28: ServiceFuelCellFourtyfiveDaysTillEndOfLife, 29: ServiceFuelCellOneMonthTillEndOfLife, 30: BalancingInProgress, 31: BackupPowerFunctionActive, 32: BatteryLow, 33: BatteryDeviceTurnedOff, 34: MaintenanceIntervalHydraulicFilterExpired, 35: MaintenanceIntervalVentilationFilterExpired, 36: ContaminationAirFilter, 37: LagDeviceDtcReported, 65533: ViewedServiceList, 65534: ServiceDoneSuccessful}")|O3EEnum|2||||
| |- - [DateTime](## "Date of event")|O3EDateTime|8||||
| |- - Unknown|O3EByteVal|2||||
|**263**|[**WarningDtcList**](## "List of active warning messages")|*O3EList*|122||ro||
| |- [Count](## "Number of entries listed")|O3EByteVal|2||||
| |- - Warning|O3EEnum|2||||
| |- - [DateTime](## "Date of event")|O3EDateTime|8||||
| |- - Unknown|O3EByteVal|2||||
|**264**|[**WarningDtcHistory**](## "History of warning messages")|*O3EList*|124||ro||
| |- [Count](## "Number of entries listed")|O3EByteVal|2||||
| |- [GrandTotal](## "Total number of entries")|O3EByteVal|2||||
| |- - Warning|O3EEnum|2||||
| |- - [DateTime](## "Date of event")|O3EDateTime|8||||
| |- - Unknown|O3EByteVal|2||||
|**265**|[**ErrorDtcList**](## "List of active error messages")|*O3EList*|122||ro||
| |- [Count](## "Number of entries listed")|O3EByteVal|2||||
| |- - Error|O3EEnum|2||||
| |- - [DateTime](## "Date of event")|O3EDateTime|8||||
| |- - Unknown|O3EByteVal|2||||
|**266**|[**ErrorDtcHistory**](## "History of error messages")|*O3EList*|124||ro||
| |- [Count](## "Number of entries listed")|O3EByteVal|2||||
| |- [GrandTotal](## "Total number of entries")|O3EByteVal|2||||
| |- - Error|O3EEnum|2||||
| |- - [DateTime](## "Date of event")|O3EDateTime|8||||
| |- - Unknown|O3EByteVal|2||||
|**268**|[**FlowTemperatureSensor**](## "Flow temperature in the primary circuit downstream from the heat generator")|*O3EComplexType*|9||ro|[Link](https://github.com/open3e/open3e/wiki/036-DoI-%E2%80%90-Data-points-of-Interest/#data-points-of-vitocal-250)|
| |- Actual|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- Minimum|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- Maximum|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- Average|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- [SensorStatus](## "Actual state of sensor {0: no_error, 1: interruption, 2: short_circuit, 3: electrical_fault, 4: not_available, 5: invalidates}")|O3EEnum|1||||
|**269**|[**ReturnTemperatureSensor**](## "Flow temperature in the primary circuit upstream from the heat generator")|*O3EComplexType*|9||ro|[Link](https://github.com/open3e/open3e/wiki/036-DoI-%E2%80%90-Data-points-of-Interest/#data-points-of-vitocal-250)|
| |- Actual|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- Minimum|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- Maximum|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- Average|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- [SensorStatus](## "{0: no_error, 1: interruption, 2: short_circuit, 3: electrical_fault, 4: not_available, 5: invalidates}")|O3EEnum|1||||
|**271**|[**DomesticHotWaterSensor**](## "Actual temperature domestic hot water buffer")|*O3EComplexType*|9||ro|[Link](https://github.com/open3e/open3e/wiki/036-DoI-%E2%80%90-Data-points-of-Interest/#data-points-of-vitocal-250)|
| |- Actual|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- Minimum|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- Maximum|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- Average|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- [SensorStatus](## "{0: no_error, 1: interruption, 2: short_circuit, 3: electrical_fault, 4: not_available, 5: invalidates}")|O3EEnum|1||||
|**274**|[**OutsideTemperatureSensor**](## "Outside temperature value")|*O3EComplexType*|9||ro||
| |- Actual|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- Minimum|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- Maximum|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- Average|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- [SensorStatus](## "{0: no_error, 1: interruption, 2: short_circuit, 3: electrical_fault, 4: not_available, 5: invalidates}")|O3EEnum|1||||
|**282**|[**HydraulicSeparatorTemperatureSensor**](## "Actual flow temperature of the hydraulic switch")|*O3EComplexType*|9||ro||
| |- Actual|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- Minimum|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- Maximum|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- Average|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- [SensorStatus](## "{0: no_error, 1: interruption, 2: short_circuit, 3: electrical_fault, 4: not_available, 5: invalidates}")|O3EEnum|1||||
|**284**|[**MixerOneCircuitFlowTemperatureSensor**](## "Heating circuit 1: Actual flow temperature value")|*O3EComplexType*|9||ro||
| |- Actual|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- Minimum|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- Maximum|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- Average|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- [SensorStatus](## "{0: no_error, 1: interruption, 2: short_circuit, 3: electrical_fault, 4: not_available, 5: invalidates}")|O3EEnum|1||||
|**318**|[**WaterPressureSensor**](## "Actual pressure heat generator circulation")|*O3EComplexType*|9||ro||
| |- Actual|O3EInt16|2|hPa|||
| |- Minimum|O3EInt16|2|hPa|||
| |- Maximum|O3EInt16|2|hPa|||
| |- Average|O3EInt16|2|hPa|||
| |- [SensorStatus](## "{0: no_error, 1: interruption, 2: short_circuit, 3: electrical_fault, 4: not_available, 5: invalidates}")|O3EEnum|1||||
|**320**|[**PrimaryHeatExchangerLiquidTemperatureSensor**](## "Actual temperature primary heat exchanger inlet")|*O3EComplexType*|9||ro||
| |- Actual|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- Minimum|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- Maximum|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- Average|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- [SensorStatus](## "{0: no_error, 1: interruption, 2: short_circuit, 3: electrical_fault, 4: not_available, 5: invalidates}")|O3EEnum|1||||
|**321**|[**CompressorInletTemperatureSensor**](## "Actual temperature compressor inlet")|*O3EComplexType*|9||ro||
| |- Actual|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- Minimum|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- Maximum|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- Average|O3EInt16|2|hPa|||
| |- [SensorStatus](## "{0: no_error, 1: interruption, 2: short_circuit, 3: electrical_fault, 4: not_available, 5: invalidates}")|O3EEnum|1||||
|**322**|[**CompressorInletPressureSensor**](## "Actual pressure compressor inlet")|*O3EComplexType*|9||ro||
| |- Actual|O3EInt16|2|hPa|||
| |- Minimum|O3EInt16|2|hPa|||
| |- Maximum|O3EInt16|2|hPa|||
| |- Average|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- Unknown|O3EByteVal|1||||
|**324**|[**CompressorOutletTemperatureSensor**](## "Actual temperature compressor outlet")|*O3EComplexType*|9||ro||
| |- Actual|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- Minimum|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- Maximum|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- Average|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- [SensorStatus](## "{0: no_error, 1: interruption, 2: short_circuit, 3: electrical_fault, 4: not_available, 5: invalidates}")|O3EEnum|1||||
|**325**|[**CompressorOutletPressureSensor**](## "Actual pressure compressor outlet")|*O3EComplexType*|9||ro||
| |- Actual|O3EInt16|2|hPa|||
| |- Minimum|O3EInt16|2|hPa|||
| |- Maximum|O3EInt16|2|hPa|||
| |- Average|O3EInt16|2|hPa|||
| |- Unknown|O3EByteVal|1||||
|**355**|[**SecondaryHeatExchangerLiquidTemperatureSensor**](## "Actual temperature secondary heat exchanger outlet")|*O3EComplexType*|9||ro||
| |- Actual|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- Minimum|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- Maximum|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- Average|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- Error|O3EByteVal|1||||
|**381**|[**CentralHeatingPump**](## "Status of the primary circuit pump")|*O3EComplexType*|4||ro|[Link](https://github.com/open3e/open3e/discussions/212)|
| |- State|O3EByteVal|1||||
| |- TargetValue|O3EInt8|1||||
| |- Actual|O3EInt8|1||||
| |- Unknown|RawCodec|1||||
|**389**|[**ElectronicExpansionValveOneCurrentPositionPercent**](## "Actual position expansion valve one (secondary heat exchanger outlet)")|O3EInt8|1|%|ro||
|**391**|[**ElectronicExpansionValveTwoCurrentPositionPercent**](## "Actual position expansion valve two (evaporator outlet)")|O3EInt8|1|%|ro||
|**396**|[**DomesticHotWaterTemperatureSetpoint**](## "Temperature setpoint domestic hot water")|O3EInt16|2|[°C](## "°C or °F (system configuration)")|**rw**||
|**491**|[**DomesticHotWaterCirculationPump**](## "Request for domestic hot water circulation pump")|*O3EComplexType*|2||**rw**||
| |- State|O3EByteVal|1||||
| |- Unknown|O3EByteVal|1||||
|**497**|[**DomesticHotWaterCirculationPumpMode**](## "Operation Mode of domestic hot water circulation pump")|*O3EComplexType*|5||**rw**|[See page 22f](https://static.viessmann-climatesolutions.com/resources/technical_documents/DE/de/VSA/6179923VSA00001_1.pdf?)|
| |- Mode|O3EByteVal|1||||
| |- HygenieActive|O3EByteVal|1||||
| |- HeatingActive|O3EByteVal|1||||
| |- CyclesPerHour|O3EByteVal|1||||
| |- Cycles|O3EByteVal|1||||
|**531**|[**DomesticHotWaterOperationState**](## "Operation state of domestic hot water preparation")|*O3EComplexType*|2||**rw**||
| |- Mode|O3EByteVal|1||||
| |- [State](## "{0: Off, 1: Hot water, 2: Parallel operation, 3: Chimney sweep, 4: Test mode, 5: External temperature setpoint, 6: External modulation setpoint, 7: Hygiene function, 8: Automatic}")|O3EEnum|1||||
|**535**|[**ObjectElectricalEnergyStatistical**](## "Cumulative Grid Energy Statistics")|*O3EComplexType*|12||ro|[Link](https://github.com/open3e/open3e/wiki/036-DoI-%E2%80%90-Data-points-of-Interest/#data-points-of-vx3)|
| |- GridFeedInEnergy|O3EInt32|4|kWh|||
| |- GridSuppliedEnergy|O3EInt32|4|kWh|||
| |- ProducedEnergy|O3EInt32|4|kWh|||
|**902**|[**MalfunctionIdentification**](## "Indicates whether faults are present")|O3EByteVal|1||ro||
|**954**|[**BusTopologyMatrix**](## "Matrix of CAN bus topology")|*O3EList*|181||ro||
| |- [Count](## "Number of list entries")|O3EInt8|1||||
| |- TopologyElement|*O3EComplexType*|36||||
| |- - NodeID|O3EByteVal|1||||
| |- - [BusType](## "{0: OwnBus, 1: PlusBus, 2: CanInternal, 3: CanExternal, 4: InternalUart, 5: Zigbee, 6: CanRaw, 7: Unkown, 8: ModBus, 9: EEBUS, 10: PlusBusTwo, 11: ISquaredCBus, 12: HEMS_Bus, 13: TL_SolarLogBus, 14: ServiceBus}")|O3EEnum|1||||
| |- - DeviceProperty|O3EByteVal|1||||
| |- - DeviceFunction|O3EByteVal|1||||
| |- - SW-Version|O3ESoftVers|8||||
| |- - HW-Version|O3ESoftVers|8||||
| |- - VIN|O3EUtf8|16||||
|**987**|[**MixerOneCircuitFlowTemperatureTargetSetpoint**](## "Temperature setpoint heating curcuit 1")|O3EInt16|2|[°C](## "°C or °F (system configuration)")|**rw**||
|**1043**|[**AllengraSensor**](## "Flow rate and temperature in the primary circuit of the heat generator")|*O3EComplexType*|5||ro|[Link](https://github.com/open3e/open3e/wiki/036-DoI-%E2%80%90-Data-points-of-Interest/#data-points-of-vitocal-250)|
| |- Actual|O3EInt16|2|l/h|||
| |- Temperature|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- Unknown|RawCodec|1||||
|**1190**|[**ThermalPower**](## "Actual thermal power output of the system")|*O3EComplexType*|4||ro||
| |- Power|O3EInt16|2|kW|||
| |- Unknown|RawCodec|2||||
|**1294**|[**EnergyConsumptionCentralHeatingMonthMatrix**](## "Energy Consumption Central Heating Per Month")|*O3EComplexType*|124||ro||
| |- [CurrentMonth](## "Energy Consumption Central Heating Current Month")|*O3EList*|62||||
| |- - 01|O3EInt16|2|kWh|||
| |- - 02|O3EInt16|2|kWh|||
| |- - 03|O3EInt16|2|kWh|||
| |- - 04|O3EInt16|2|kWh|||
| |- - 05|O3EInt16|2|kWh|||
| |- - 06|O3EInt16|2|kWh|||
| |- - 07|O3EInt16|2|kWh|||
| |- - 08|O3EInt16|2|kWh|||
| |- - 09|O3EInt16|2|kWh|||
| |- - 10|O3EInt16|2|kWh|||
| |- - 11|O3EInt16|2|kWh|||
| |- - 12|O3EInt16|2|kWh|||
| |- - 13|O3EInt16|2|kWh|||
| |- - 14|O3EInt16|2|kWh|||
| |- - 15|O3EInt16|2|kWh|||
| |- - 16|O3EInt16|2|kWh|||
| |- - 17|O3EInt16|2|kWh|||
| |- - 18|O3EInt16|2|kWh|||
| |- - 19|O3EInt16|2|kWh|||
| |- - 20|O3EInt16|2|kWh|||
| |- - 21|O3EInt16|2|kWh|||
| |- - 22|O3EInt16|2|kWh|||
| |- - 23|O3EInt16|2|kWh|||
| |- - 24|O3EInt16|2|kWh|||
| |- - 25|O3EInt16|2|kWh|||
| |- - 26|O3EInt16|2|kWh|||
| |- - 27|O3EInt16|2|kWh|||
| |- - 28|O3EInt16|2|kWh|||
| |- - 29|O3EInt16|2|kWh|||
| |- - 30|O3EInt16|2|kWh|||
| |- - 31|O3EInt16|2|kWh|||
| |- [LastMonth](## "Energy Consumption Central Heating Previous Month")|*O3EList*|62||||
| |- - 01|O3EInt16|2|kWh|||
| |- - 02|O3EInt16|2|kWh|||
| |- - 03|O3EInt16|2|kWh|||
| |- - 04|O3EInt16|2|kWh|||
| |- - 05|O3EInt16|2|kWh|||
| |- - 06|O3EInt16|2|kWh|||
| |- - 07|O3EInt16|2|kWh|||
| |- - 08|O3EInt16|2|kWh|||
| |- - 09|O3EInt16|2|kWh|||
| |- - 10|O3EInt16|2|kWh|||
| |- - 11|O3EInt16|2|kWh|||
| |- - 12|O3EInt16|2|kWh|||
| |- - 13|O3EInt16|2|kWh|||
| |- - 14|O3EInt16|2|kWh|||
| |- - 15|O3EInt16|2|kWh|||
| |- - 16|O3EInt16|2|kWh|||
| |- - 17|O3EInt16|2|kWh|||
| |- - 18|O3EInt16|2|kWh|||
| |- - 19|O3EInt16|2|kWh|||
| |- - 20|O3EInt16|2|kWh|||
| |- - 21|O3EInt16|2|kWh|||
| |- - 22|O3EInt16|2|kWh|||
| |- - 23|O3EInt16|2|kWh|||
| |- - 24|O3EInt16|2|kWh|||
| |- - 25|O3EInt16|2|kWh|||
| |- - 26|O3EInt16|2|kWh|||
| |- - 27|O3EInt16|2|kWh|||
| |- - 28|O3EInt16|2|kWh|||
| |- - 29|O3EInt16|2|kWh|||
| |- - 30|O3EInt16|2|kWh|||
| |- - 31|O3EInt16|2|kWh|||
|**1311**|[**EnergyConsumptionDomesticHotWaterMonthMatrix**](## "Energy Consumption Domestic Hot Water Per Month")|*O3EComplexType*|124||ro||
| |- [CurrentMonth](## "Energy Consumption Domestic Hot Water Current Month")|*O3EList*|62||||
| |- - 01|O3EInt16|2|kWh|||
| |- - 02|O3EInt16|2|kWh|||
| |- - 03|O3EInt16|2|kWh|||
| |- - 04|O3EInt16|2|kWh|||
| |- - 05|O3EInt16|2|kWh|||
| |- - 06|O3EInt16|2|kWh|||
| |- - 07|O3EInt16|2|kWh|||
| |- - 08|O3EInt16|2|kWh|||
| |- - 09|O3EInt16|2|kWh|||
| |- - 10|O3EInt16|2|kWh|||
| |- - 11|O3EInt16|2|kWh|||
| |- - 12|O3EInt16|2|kWh|||
| |- - 13|O3EInt16|2|kWh|||
| |- - 14|O3EInt16|2|kWh|||
| |- - 15|O3EInt16|2|kWh|||
| |- - 16|O3EInt16|2|kWh|||
| |- - 17|O3EInt16|2|kWh|||
| |- - 18|O3EInt16|2|kWh|||
| |- - 19|O3EInt16|2|kWh|||
| |- - 20|O3EInt16|2|kWh|||
| |- - 21|O3EInt16|2|kWh|||
| |- - 22|O3EInt16|2|kWh|||
| |- - 23|O3EInt16|2|kWh|||
| |- - 24|O3EInt16|2|kWh|||
| |- - 25|O3EInt16|2|kWh|||
| |- - 26|O3EInt16|2|kWh|||
| |- - 27|O3EInt16|2|kWh|||
| |- - 28|O3EInt16|2|kWh|||
| |- - 29|O3EInt16|2|kWh|||
| |- - 30|O3EInt16|2|kWh|||
| |- - 31|O3EInt16|2|kWh|||
| |- [LastMonth](## "Energy Consumption Domestic Hot Water Previous Month")|*O3EList*|62||||
| |- - 01|O3EInt16|2|kWh|||
| |- - 02|O3EInt16|2|kWh|||
| |- - 03|O3EInt16|2|kWh|||
| |- - 04|O3EInt16|2|kWh|||
| |- - 05|O3EInt16|2|kWh|||
| |- - 06|O3EInt16|2|kWh|||
| |- - 07|O3EInt16|2|kWh|||
| |- - 08|O3EInt16|2|kWh|||
| |- - 09|O3EInt16|2|kWh|||
| |- - 10|O3EInt16|2|kWh|||
| |- - 11|O3EInt16|2|kWh|||
| |- - 12|O3EInt16|2|kWh|||
| |- - 13|O3EInt16|2|kWh|||
| |- - 14|O3EInt16|2|kWh|||
| |- - 15|O3EInt16|2|kWh|||
| |- - 16|O3EInt16|2|kWh|||
| |- - 17|O3EInt16|2|kWh|||
| |- - 18|O3EInt16|2|kWh|||
| |- - 19|O3EInt16|2|kWh|||
| |- - 20|O3EInt16|2|kWh|||
| |- - 21|O3EInt16|2|kWh|||
| |- - 22|O3EInt16|2|kWh|||
| |- - 23|O3EInt16|2|kWh|||
| |- - 24|O3EInt16|2|kWh|||
| |- - 25|O3EInt16|2|kWh|||
| |- - 26|O3EInt16|2|kWh|||
| |- - 27|O3EInt16|2|kWh|||
| |- - 28|O3EInt16|2|kWh|||
| |- - 29|O3EInt16|2|kWh|||
| |- - 30|O3EInt16|2|kWh|||
| |- - 31|O3EInt16|2|kWh|||
|**1315**|[**GeneratedCentralHeatingOutputMonthMatrix**](## "Generated Central Heating Output Per Month")|*O3EComplexType*|124||ro||
| |- [CurrentMonth](## "Generated Central Heating Output Current Month")|*O3EList*|62||||
| |- - 01|O3EInt16|2|kWh|||
| |- - 02|O3EInt16|2|kWh|||
| |- - 03|O3EInt16|2|kWh|||
| |- - 04|O3EInt16|2|kWh|||
| |- - 05|O3EInt16|2|kWh|||
| |- - 06|O3EInt16|2|kWh|||
| |- - 07|O3EInt16|2|kWh|||
| |- - 08|O3EInt16|2|kWh|||
| |- - 09|O3EInt16|2|kWh|||
| |- - 10|O3EInt16|2|kWh|||
| |- - 11|O3EInt16|2|kWh|||
| |- - 12|O3EInt16|2|kWh|||
| |- - 13|O3EInt16|2|kWh|||
| |- - 14|O3EInt16|2|kWh|||
| |- - 15|O3EInt16|2|kWh|||
| |- - 16|O3EInt16|2|kWh|||
| |- - 17|O3EInt16|2|kWh|||
| |- - 18|O3EInt16|2|kWh|||
| |- - 19|O3EInt16|2|kWh|||
| |- - 20|O3EInt16|2|kWh|||
| |- - 21|O3EInt16|2|kWh|||
| |- - 22|O3EInt16|2|kWh|||
| |- - 23|O3EInt16|2|kWh|||
| |- - 24|O3EInt16|2|kWh|||
| |- - 25|O3EInt16|2|kWh|||
| |- - 26|O3EInt16|2|kWh|||
| |- - 27|O3EInt16|2|kWh|||
| |- - 28|O3EInt16|2|kWh|||
| |- - 29|O3EInt16|2|kWh|||
| |- - 30|O3EInt16|2|kWh|||
| |- - 31|O3EInt16|2|kWh|||
| |- [LastMonth](## "Generated Central Heating Output Previous Month")|*O3EList*|62||||
| |- - 01|O3EInt16|2|kWh|||
| |- - 02|O3EInt16|2|kWh|||
| |- - 03|O3EInt16|2|kWh|||
| |- - 04|O3EInt16|2|kWh|||
| |- - 05|O3EInt16|2|kWh|||
| |- - 06|O3EInt16|2|kWh|||
| |- - 07|O3EInt16|2|kWh|||
| |- - 08|O3EInt16|2|kWh|||
| |- - 09|O3EInt16|2|kWh|||
| |- - 10|O3EInt16|2|kWh|||
| |- - 11|O3EInt16|2|kWh|||
| |- - 12|O3EInt16|2|kWh|||
| |- - 13|O3EInt16|2|kWh|||
| |- - 14|O3EInt16|2|kWh|||
| |- - 15|O3EInt16|2|kWh|||
| |- - 16|O3EInt16|2|kWh|||
| |- - 17|O3EInt16|2|kWh|||
| |- - 18|O3EInt16|2|kWh|||
| |- - 19|O3EInt16|2|kWh|||
| |- - 20|O3EInt16|2|kWh|||
| |- - 21|O3EInt16|2|kWh|||
| |- - 22|O3EInt16|2|kWh|||
| |- - 23|O3EInt16|2|kWh|||
| |- - 24|O3EInt16|2|kWh|||
| |- - 25|O3EInt16|2|kWh|||
| |- - 26|O3EInt16|2|kWh|||
| |- - 27|O3EInt16|2|kWh|||
| |- - 28|O3EInt16|2|kWh|||
| |- - 29|O3EInt16|2|kWh|||
| |- - 30|O3EInt16|2|kWh|||
| |- - 31|O3EInt16|2|kWh|||
|**1316**|[**EnergyConsumptionCentralHeatingYearMatrix**](## "Energy Consumption Central Heating Per Year")|*O3EComplexType*|96||ro||
| |- [CurrentYear](## "Energy Consumption Central Heating Current Year")|*O3EList*|48||||
| |- - 01_January|O3EInt32|4|kWh|||
| |- - 02_February|O3EInt32|4|kWh|||
| |- - 03_March|O3EInt32|4|kWh|||
| |- - 04_April|O3EInt32|4|kWh|||
| |- - 05_May|O3EInt32|4|kWh|||
| |- - 06_June|O3EInt32|4|kWh|||
| |- - 07_July|O3EInt32|4|kWh|||
| |- - 08_August|O3EInt32|4|kWh|||
| |- - 09_September|O3EInt32|4|kWh|||
| |- - 10_October|O3EInt32|4|kWh|||
| |- - 11_November|O3EInt32|4|kWh|||
| |- - 12_December|O3EInt32|4|kWh|||
| |- [LastYear](## "Energy Consumption Central Heating Last Year")|*O3EList*|48||||
| |- - 01_January|O3EInt32|4|kWh|||
| |- - 02_February|O3EInt32|4|kWh|||
| |- - 03_March|O3EInt32|4|kWh|||
| |- - 04_April|O3EInt32|4|kWh|||
| |- - 05_May|O3EInt32|4|kWh|||
| |- - 06_June|O3EInt32|4|kWh|||
| |- - 07_July|O3EInt32|4|kWh|||
| |- - 08_August|O3EInt32|4|kWh|||
| |- - 09_September|O3EInt32|4|kWh|||
| |- - 10_October|O3EInt32|4|kWh|||
| |- - 11_November|O3EInt32|4|kWh|||
| |- - 12_December|O3EInt32|4|kWh|||
|**1333**|[**EnergyConsumptionDomesticHotWaterYearMatrix**](## "Energy Consumption Domestic Hot Water Per Year")|*O3EComplexType*|96||ro||
| |- [CurrentYear](## "Energy Consumption Domestic Hot Water Current Year")|*O3EList*|48||||
| |- - 01_January|O3EInt32|4||||
| |- - 02_February|O3EInt32|4||||
| |- - 03_March|O3EInt32|4||||
| |- - 04_April|O3EInt32|4||||
| |- - 05_May|O3EInt32|4||||
| |- - 06_June|O3EInt32|4||||
| |- - 07_July|O3EInt32|4||||
| |- - 08_August|O3EInt32|4||||
| |- - 09_September|O3EInt32|4||||
| |- - 10_October|O3EInt32|4||||
| |- - 11_November|O3EInt32|4||||
| |- - 12_December|O3EInt32|4||||
| |- [LastYear](## "Energy Consumption Domestic Hot Water Last Year")|*O3EList*|48||||
| |- - 01_January|O3EInt32|4||||
| |- - 02_February|O3EInt32|4||||
| |- - 03_March|O3EInt32|4||||
| |- - 04_April|O3EInt32|4||||
| |- - 05_May|O3EInt32|4||||
| |- - 06_June|O3EInt32|4||||
| |- - 07_July|O3EInt32|4||||
| |- - 08_August|O3EInt32|4||||
| |- - 09_September|O3EInt32|4||||
| |- - 10_October|O3EInt32|4||||
| |- - 11_November|O3EInt32|4||||
| |- - 12_December|O3EInt32|4||||
|**1337**|[**GeneratedCentralHeatingOutputYearMatrix**](## "Generated Central Heating Output Per Year")|*O3EComplexType*|96||ro||
| |- [CurrentYear](## "Generated Central Heating Output Current Year")|*O3EList*|48||||
| |- - 01_January|O3EInt32|4||||
| |- - 02_February|O3EInt32|4||||
| |- - 03_March|O3EInt32|4||||
| |- - 04_April|O3EInt32|4||||
| |- - 05_May|O3EInt32|4||||
| |- - 06_June|O3EInt32|4||||
| |- - 07_July|O3EInt32|4||||
| |- - 08_August|O3EInt32|4||||
| |- - 09_September|O3EInt32|4||||
| |- - 10_October|O3EInt32|4||||
| |- - 11_November|O3EInt32|4||||
| |- - 12_December|O3EInt32|4||||
| |- [LastYear](## "Generated Central Heating Output Last Year")|*O3EList*|48||||
| |- - 01_January|O3EInt32|4||||
| |- - 02_February|O3EInt32|4||||
| |- - 03_March|O3EInt32|4||||
| |- - 04_April|O3EInt32|4||||
| |- - 05_May|O3EInt32|4||||
| |- - 06_June|O3EInt32|4||||
| |- - 07_July|O3EInt32|4||||
| |- - 08_August|O3EInt32|4||||
| |- - 09_September|O3EInt32|4||||
| |- - 10_October|O3EInt32|4||||
| |- - 11_November|O3EInt32|4||||
| |- - 12_December|O3EInt32|4||||
|**1391**|[**GeneratedDomesticHotWaterOutput**](## "Generated Domestic Hot Water Output per specific period")|*O3EComplexType*|24||ro||
| |- Today|O3EInt32|4|kWh|||
| |- Past7Days|O3EInt32|4|kWh|||
| |- CurrentMonth|O3EInt32|4|kWh|||
| |- PastMonth|O3EInt32|4|kWh|||
| |- CurrentYear|O3EInt32|4|kWh|||
| |- PastYear|O3EInt32|4|kWh|||
|**1392**|[**GeneratedDomesticHotWaterOutputMonthMatrix**](## "Generated Domestic Hot Water Output Per Month")|*O3EComplexType*|124||ro||
| |- [CurrentMonth](## "Generated Domestic Hot Water Output Current Month")|*O3EList*|62||||
| |- - 01|O3EInt16|2|kWh|||
| |- - 02|O3EInt16|2|kWh|||
| |- - 03|O3EInt16|2|kWh|||
| |- - 04|O3EInt16|2|kWh|||
| |- - 05|O3EInt16|2|kWh|||
| |- - 06|O3EInt16|2|kWh|||
| |- - 07|O3EInt16|2|kWh|||
| |- - 08|O3EInt16|2|kWh|||
| |- - 09|O3EInt16|2|kWh|||
| |- - 10|O3EInt16|2|kWh|||
| |- - 11|O3EInt16|2|kWh|||
| |- - 12|O3EInt16|2|kWh|||
| |- - 13|O3EInt16|2|kWh|||
| |- - 14|O3EInt16|2|kWh|||
| |- - 15|O3EInt16|2|kWh|||
| |- - 16|O3EInt16|2|kWh|||
| |- - 17|O3EInt16|2|kWh|||
| |- - 18|O3EInt16|2|kWh|||
| |- - 19|O3EInt16|2|kWh|||
| |- - 20|O3EInt16|2|kWh|||
| |- - 21|O3EInt16|2|kWh|||
| |- - 22|O3EInt16|2|kWh|||
| |- - 23|O3EInt16|2|kWh|||
| |- - 24|O3EInt16|2|kWh|||
| |- - 25|O3EInt16|2|kWh|||
| |- - 26|O3EInt16|2|kWh|||
| |- - 27|O3EInt16|2|kWh|||
| |- - 28|O3EInt16|2|kWh|||
| |- - 29|O3EInt16|2|kWh|||
| |- - 30|O3EInt16|2|kWh|||
| |- - 31|O3EInt16|2|kWh|||
| |- [LastMonth](## "Generated Domestic Hot Water Output Previous Month")|*O3EList*|62||||
| |- - 01|O3EInt16|2|kWh|||
| |- - 02|O3EInt16|2|kWh|||
| |- - 03|O3EInt16|2|kWh|||
| |- - 04|O3EInt16|2|kWh|||
| |- - 05|O3EInt16|2|kWh|||
| |- - 06|O3EInt16|2|kWh|||
| |- - 07|O3EInt16|2|kWh|||
| |- - 08|O3EInt16|2|kWh|||
| |- - 09|O3EInt16|2|kWh|||
| |- - 10|O3EInt16|2|kWh|||
| |- - 11|O3EInt16|2|kWh|||
| |- - 12|O3EInt16|2|kWh|||
| |- - 13|O3EInt16|2|kWh|||
| |- - 14|O3EInt16|2|kWh|||
| |- - 15|O3EInt16|2|kWh|||
| |- - 16|O3EInt16|2|kWh|||
| |- - 17|O3EInt16|2|kWh|||
| |- - 18|O3EInt16|2|kWh|||
| |- - 19|O3EInt16|2|kWh|||
| |- - 20|O3EInt16|2|kWh|||
| |- - 21|O3EInt16|2|kWh|||
| |- - 22|O3EInt16|2|kWh|||
| |- - 23|O3EInt16|2|kWh|||
| |- - 24|O3EInt16|2|kWh|||
| |- - 25|O3EInt16|2|kWh|||
| |- - 26|O3EInt16|2|kWh|||
| |- - 27|O3EInt16|2|kWh|||
| |- - 28|O3EInt16|2|kWh|||
| |- - 29|O3EInt16|2|kWh|||
| |- - 30|O3EInt16|2|kWh|||
| |- - 31|O3EInt16|2|kWh|||
|**1393**|[**GeneratedDomesticHotWaterOutputYearMatrix**](## "Generated Domestic Hot Water Output Per Year")|*O3EComplexType*|96||ro||
| |- [CurrentYear](## "Generated Domestic Hot Water Output Current Year")|*O3EList*|48||||
| |- - 01_January|O3EInt32|4|kWh|||
| |- - 02_February|O3EInt32|4|kWh|||
| |- - 03_March|O3EInt32|4|kWh|||
| |- - 04_April|O3EInt32|4|kWh|||
| |- - 05_May|O3EInt32|4|kWh|||
| |- - 06_June|O3EInt32|4|kWh|||
| |- - 07_July|O3EInt32|4|kWh|||
| |- - 08_August|O3EInt32|4|kWh|||
| |- - 09_September|O3EInt32|4|kWh|||
| |- - 10_October|O3EInt32|4|kWh|||
| |- - 11_November|O3EInt32|4|kWh|||
| |- - 12_December|O3EInt32|4|kWh|||
| |- [LastYear](## "Generated Domestic Hot Water Output Last Year")|*O3EList*|48||||
| |- - 01_January|O3EInt32|4|kWh|||
| |- - 02_February|O3EInt32|4|kWh|||
| |- - 03_March|O3EInt32|4|kWh|||
| |- - 04_April|O3EInt32|4|kWh|||
| |- - 05_May|O3EInt32|4|kWh|||
| |- - 06_June|O3EInt32|4|kWh|||
| |- - 07_July|O3EInt32|4|kWh|||
| |- - 08_August|O3EInt32|4|kWh|||
| |- - 09_September|O3EInt32|4|kWh|||
| |- - 10_October|O3EInt32|4|kWh|||
| |- - 11_November|O3EInt32|4|kWh|||
| |- - 12_December|O3EInt32|4|kWh|||
|**1415**|[**MixerOneCircuitOperationState**](## "Heating curcuit 1: Operating Mode")|*O3EComplexType*|2||**rw**||
| |- [Mode](## "Requested Operating Mode {0: Off, 1: Heating, 2: Parallel Operation: Heating HotWater, 3: Parallel Operation: Heating Cooling, 4: TestMode, 5: Cooling, 255: Automatic}")|O3EEnum|1||||
| |- [State](## "Actual Operating Mode {0: ShutDown, 1: Reduced, 2: Normal, 3: Comfort, 5: Fixed Value, 6: Antifreeze protection, 7: Energy Save: reduced, 8: Energy Save: normal, 9: Energy Save: comfort, 10: Cooling: normal, 11: Cooling: comfort, 12: No request}")|O3EEnum|1||||
|**1603**|[**PointOfCommonCouplingPower**](## "Actual Power at Point of Common Coupling")|*O3EComplexType*|4||ro|[Link](https://github.com/open3e/open3e/wiki/036-DoI-%E2%80%90-Data-points-of-Interest/#data-points-of-vx3)|
| |- [ActivePower](## "Active Power")|O3EInt16|2|W|||
| |- [ReactivePower](## "Reactive Power")|O3EInt16|2|VA|||
|**1603**|[**PointOfCommonCouplingPower**](## "Actual Power at Point of Common Coupling")|*O3EComplexType*|12||ro||
| |- [ActivePower](## "Active Power")|O3EInt16|2|W|||
| |- [ReactivePower](## "Reactive Power")|O3EInt16|2|VA|||
| |- [ActivePowerDup](## "Active Power Duplicate")|O3EInt16|2|W|||
| |- PadZeros|O3EInt16|2||||
| |- [ReactivePowerDup](## "Reactive Power Duplicate")|O3EInt16|2|VA|||
| |- PadOnes|O3EInt16|2||||
|**1643**|[**MixerOneCircuitCurrentTemperatureSetpoint**](## "Heating Circuit 1: Flow or Room Temperature Setpoint")|O3EInt16|2|[°C](## "°C or °F (system configuration)")|**rw**||
|**1664**|[**ElectricalEnergyStorageStateOfCharge**](## "SoC of Battery")|O3EInt8|1|%|ro|[Link](https://github.com/open3e/open3e/wiki/036-DoI-%E2%80%90-Data-points-of-Interest/#data-points-of-vx3)|
|**1684**|[**AmbientTemperatureSensor**](## "Actual Ambient Temperature")|*O3EComplexType*|9||ro||
| |- Actual|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- Minimum|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- Maximum|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- Average|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- [SensorStatus](## "{0: no_error, 1: interruption, 2: short_circuit, 3: electrical_fault, 4: not_available, 5: invalidates}")|O3EEnum|1||||
|**1690**|[**ElectricalEnergySystemPhotovoltaicStatus**](## "Actual Power of Photovoltaic")|*O3EComplexType*|17||ro|[Link](https://github.com/open3e/open3e/wiki/036-DoI-%E2%80%90-Data-points-of-Interest/#data-points-of-vx3)|
| |- ActivePower cumulated|O3EInt16|2|W|||
| |- RectivePower cumulated|O3EInt16|2|VA|||
| |- ActivePower String C|O3EInt16|2|W|||
| |- RectivePower String C|O3EInt16|2|VA|||
| |- ActivePower String B|O3EInt16|2|W|||
| |- RectivePower String B|O3EInt16|2|VA|||
| |- ActivePower String A|O3EInt16|2|W|||
| |- RectivePower String A|O3EInt16|2|VA|||
| |- OpMode|O3EInt8|1||||
|**1771**|[**EngineRoomTemperatureSensor**](## "Actual Temperature at Engine Room")|*O3EComplexType*|9||ro||
| |- Actual|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- Minimum|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- Maximum|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- Average|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- [SensorStatus](## "{0: no_error, 1: interruption, 2: short_circuit, 3: electrical_fault, 4: not_available, 5: invalidates}")|O3EEnum|1||||
|**1772**|[**CompressorOilTemperatureSensor**](## "Actual Compressor Oil Temperature")|*O3EComplexType*|9||ro|[Link](https://github.com/open3e/open3e/wiki/036-DoI-%E2%80%90-Data-points-of-Interest)|
| |- Actual|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- Minimum|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- Maximum|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- Average|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- [SensorStatus](## "{0: no_error, 1: interruption, 2: short_circuit, 3: electrical_fault, 4: not_available, 5: invalidates}")|O3EEnum|1||||
|**1775**|[**PrimaryCircuitFanOne**](## "Speed of Fan 1")|O3EByteVal|1|%|ro|[Link](https://github.com/open3e/open3e/wiki/036-DoI-%E2%80%90-Data-points-of-Interest)|
|**1776**|[**PrimaryCircuitFanTwo**](## "Speed of Fan 2")|O3EByteVal|1|%|ro|[Link](https://github.com/open3e/open3e/wiki/036-DoI-%E2%80%90-Data-points-of-Interest)|
|**1799**|[**PrimaryCircuitCurrentTemperatureSetpoint**](## "Heating Circuit 1: Temperature Setpoint")|O3EInt16|2|[°C](## "°C or °F (system configuration)")|**rw**||
|**1801**|[**ElectricalEnergyStorageEnergyTransferStatistic**](## "Statistics of Transfered Electrical Energy")|*O3EComplexType*|40||ro|[Link](https://github.com/open3e/open3e/wiki/036-DoI-%E2%80%90-Data-points-of-Interest/#data-points-of-vx3)|
| |- BatteryChargeToday|O3EInt32|4|Wh|||
| |- BatteryChargeWeek|O3EInt32|4|Wh|||
| |- BatteryChargeMonth|O3EInt32|4|Wh|||
| |- BatteryChargeYear|O3EInt32|4|Wh|||
| |- BatteryChargeTotal|O3EInt32|4|Wh|||
| |- BatteryDischargeToday|O3EInt32|4|Wh|||
| |- BatteryDischargeWeek|O3EInt32|4|Wh|||
| |- BatteryDischargeMonth|O3EInt32|4|Wh|||
| |- BatteryDischargeYear|O3EInt32|4|Wh|||
| |- BatteryDischargeTotal|O3EInt32|4|Wh|||
|**1802**|[**EnergyProductionPhotovoltaic**](## "Statistics of Photovoltaic Production")|*O3EComplexType*|80||ro|[Link](https://github.com/open3e/open3e/wiki/036-DoI-%E2%80%90-Data-points-of-Interest/#data-points-of-vx3)|
| |- PhotovoltaicProductionToday|O3EInt32|4|Wh|||
| |- PhotovoltaicProductionWeek|O3EInt32|4|Wh|||
| |- PhotovoltaicProductionMonth|O3EInt32|4|Wh|||
| |- PhotovoltaicProductionYear|O3EInt32|4|Wh|||
| |- PhotovoltaicProductionTotal|O3EInt32|4|Wh|||
| |- PhotovoltaicProductionToday1|O3EInt32|4|Wh|||
| |- PhotovoltaicProductionWeek1|O3EInt32|4|Wh|||
| |- PhotovoltaicProductionMonth1|O3EInt32|4|Wh|||
| |- PhotovoltaicProductionYear1|O3EInt32|4|Wh|||
| |- PhotovoltaicProductionTotal1|O3EInt32|4|Wh|||
| |- PhotovoltaicProductionToday2|O3EInt32|4|Wh|||
| |- PhotovoltaicProductionWeek2|O3EInt32|4|Wh|||
| |- PhotovoltaicProductionMonth2|O3EInt32|4|Wh|||
| |- PhotovoltaicProductionYear2|O3EInt32|4|Wh|||
| |- PhotovoltaicProductionTotal2|O3EInt32|4|Wh|||
| |- PhotovoltaicProductionToday3|O3EInt32|4|Wh|||
| |- PhotovoltaicProductionWeek3|O3EInt32|4|Wh|||
| |- PhotovoltaicProductionMonth3|O3EInt32|4|Wh|||
| |- PhotovoltaicProductionYear3|O3EInt32|4|Wh|||
| |- PhotovoltaicProductionTotal3|O3EInt32|4|Wh|||
|**1828**|[**InverterElectricalEnergyStorageCurrentMaximumlChargePower**](## "Maximum Electrical Power of Inverter for Charging")|*O3EComplexType*|4||ro||
| |- Power|O3EInt16|2|W|||
| |- Unknown|RawCodec|2||||
|**1830**|[**InverterElectricalEnergyStorageCurrentMaximumlDishargePower**](## "Maximum Electrical Power of Inverter for Discharging")|*O3EComplexType*|4||ro||
| |- Power|O3EInt16|2|W|||
| |- Unknown|RawCodec|2||||
|**1831**|[**PhotovoltaicCurrentStringPower**](## "Current Photovoltaic Power per String")|*O3EComplexType*|12||ro||
| |- String1|O3EInt32|4|W|||
| |- String2|O3EInt32|4|W|||
| |- String3|O3EInt32|4|W|||
|**1832**|[**PhotovoltaicStringCurrent**](## "Current Photovoltaic Current per String (resolution is 1 Ampere)")|*O3EComplexType*|12||ro||
| |- String1|O3EInt32|4|A|||
| |- String2|O3EInt32|4|A|||
| |- String3|O3EInt32|4|V|||
|**1833**|[**PhotovoltaicStringVoltage**](## "Current Photovoltaic Voltage per String")|*O3EComplexType*|12||ro|[Link](https://github.com/open3e/open3e/wiki/036-DoI-%E2%80%90-Data-points-of-Interest/#data-points-of-vx3)|
| |- String1|O3EInt32|4|V|||
| |- String2|O3EInt32|4|V|||
| |- String3|O3EInt32|4|V|||
|**1834**|[**ElectricalEnergyStorageStateOfEnergy**](## "SoC of Battery")|*O3EComplexType*|4||ro||
| |- StateOfEnergy|O3EInt16|2|Wh|||
| |- Unknown|O3EInt16|2||||
|**1836**|[**ElectricalEnergyStorageCurrentPower**](## "Current Power for Battery Discharging (positive values) and Charging (negative values)")|O3EInt32|4|W|ro||
|**1842**|[**SecondaryCircuitFourThreeWayValve**](## "Circuit 2: Position of Four Three Way Valve")|*O3EComplexType*|2||ro||
| |- Setpoint|O3EInt8|1|%|||
| |- CurrentPosition|O3EInt8|1|%|||
|**2214**|[**BackupBoxConfiguration**](## "Configuration for Backup Box")|*O3EComplexType*|2||**rw**||
| |- [DischargeLimit](## "Discharge limit of battery")|O3EInt8|1|%|||
| |- Unknown|O3EInt8|1||||
|**2256**|[**DesiredThermalEnergyDefrost**](## "Target value of thermal energy to perform next defrosting")|O3EInt16|2|Wh|ro||
|**2320**|[**DomesticHotWaterStatus**](## "Status of domestic hot water preparation {0: Idle, 1: Active, 2: Postrun}")|O3EEnum|1||ro||
|**2333**|[**EconomizerLiquidTemperatureSensor**](## "Actual temperature economizer inlet")|*O3EComplexType*|9||ro|[Link](https://github.com/open3e/open3e/wiki/036-DoI-%E2%80%90-Data-points-of-Interest/#data-points-of-vitocal-250)|
| |- Actual|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- Minimum|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- Maximum|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- Average|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- [SensorStatus](## "{0: no_error, 1: interruption, 2: short_circuit, 3: electrical_fault, 4: not_available, 5: invalidates}")|O3EEnum|1||||
|**2334**|[**EvaporatorVaporTemperatureSensor**](## "Actual temperature avaporator inlet")|*O3EComplexType*|9||ro|[Link](https://github.com/open3e/open3e/wiki/036-DoI-%E2%80%90-Data-points-of-Interest/#data-points-of-vitocal-250)|
| |- Actual|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- Minimum|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- Maximum|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- Average|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- [SensorStatus](## "{0: no_error, 1: interruption, 2: short_circuit, 3: electrical_fault, 4: not_available, 5: invalidates}")|O3EEnum|1||||
|**2346**|[**CompressorSpeedPercent**](## "Actual speed of heat pump compressor")|O3EInt8|1|%|ro|[Link](https://github.com/open3e/open3e/wiki/036-DoI-%E2%80%90-Data-points-of-Interest/#data-points-of-vitocal-250)|
|**2351**|[**HeatPumpCompressor**](## "Actual state of the heat pump compressor")|*O3EComplexType*|2||ro||
| |- [PowerState](## "{0: Off, 1: On, 2: Out of range}")|O3EEnum|1||||
| |- ErrorState|O3EByteVal|1||||
|**2352**|[**AdditionalElectricHeater**](## "Actual state of the electric auxiliary heating")|*O3EComplexType*|2||ro||
| |- [PowerState](## "{0: Off, 1: On, 2: Out of range}")|O3EEnum|1||||
| |- ErrorState|O3EByteVal|1||||
|**2369**|[**HeatPumpCompressorStatistical**](## "Statistics for heat pump compressor starts")|*O3EComplexType*|14||ro||
| |- Unknown1|RawCodec|6||||
| |- [starts](## "Number of starts")|O3EInt16|2||||
| |- Unknown2|RawCodec|2||||
| |- [hours](## "Operating hours")|O3EInt16|2|h|||
| |- Unknown3|RawCodec|2||||
|**2486**|[**CurrentElectricalPowerConsumptionRefrigerantCircuit**](## "Actual electrical power consumption of the refrigeration circuit")|O3EInt32|4|W|ro||
|**2487**|[**CurrentElectricalPowerConsumptionElectricHeater**](## "Actual electrical power consumption of the auxiliary heater")|O3EInt32|4|W|ro||
|**2488**|[**CurrentElectricalPowerConsumptionSystem**](## "Actual total electrical power consumption of the system")|O3EInt32|4|W|ro||
|**2494**|[**CurrentThermalCapacityRefrigerantCircuit**](## "Actual thermal power output of the refrigeration circuit")|O3EInt32|4|W|ro||
|**2495**|[**CurrentThermalCapacityElectricHeater**](## "Actual thermal power output of the auxiliary heater")|O3EInt32|4|W|ro||
|**2496**|[**CurrentThermalCapacitySystem**](## "Actual thermal power output of the system")|O3EInt32|4|W|ro||
|**2569**|[**CompressorSpeedRps**](## "Actual speed of the heat pump compressor")|O3EInt16|2|rps|ro||
|**2735**|[**FourThreeWayValveValveCurrentPosition**](## "Current position of the four/three-way valve {0: Heating/Cooling, 1: Internal Buffer, 2: Domestic Hot Water, 3: Heating/Cooling and Internal Buffer, 4: Domestic Hot Water and Internal Buffer}")|O3EEnum|1||ro||
|**2760**|[**EnergyOwnConsumption**](## "Own Energy Consumption")|*O3EComplexType*|24||ro||
| |- Today|O3EInt32|4|kWh|||
| |- Past7Days|O3EInt32|4|kWh|||
| |- CurrentMonth|O3EInt32|4|kWh|||
| |- PastMonth|O3EInt32|4|kWh|||
| |- CurrentYear|O3EInt32|4|kWh|||
| |- PastYear|O3EInt32|4|kWh|||
|**2806**|[**RefrigerationCircuitOperationMode**](## "Actual operating mode of the refrigeration circuit")|*O3EComplexType*|2||ro||
| |- Mode|O3EByteVal|1||||
| |- [State](## "{0: Off, 1: ShutDown, 2: Heating, 3: Cooling, 4: Manual, 5: De-icing, 6: Grid-lock}")|O3EEnum|1||||
|**3016**|[**HeatingBufferTemperatureSensor**](## "Actual temperature of the heating buffer")|*O3EComplexType*|9||ro||
| |- Actual|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- Minimum|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- Maximum|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- Average|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- [SensorStatus](## "{0: no_error, 1: interruption, 2: short_circuit, 3: electrical_fault, 4: not_available, 5: invalidates}")|O3EEnum|1||||
## Frequently used data points in compact format

[Back to table of contents](#table-of-contents)

|  Did | ID   | Codec | Length | Unit  |   Access | Further info |
| ---: | :--- | :---  | ---:   | :---: |  :---:  | :---         |
|**256**|[**BusIdentification**](## "Device infos")|*O3EComplexType*|36||ro||
|**257**|[**StatusDtcList**](## "List of active status messages")|*O3EList*|122||ro||
|**258**|[**StatusDtcHistory**](## "History of status messages")|*O3EList*|122||ro||
|**259**|[**InfoDtcList**](## "List of active info messages")|*O3EList*|122||ro||
|**260**|[**InfoDtcHistory**](## "History of info messages")|*O3EList*|122||ro||
|**261**|[**ServiceDtcList**](## "List of active service messages")|*O3EList*|122||ro||
|**262**|[**ServiceDtcHistory**](## "History of service messages")|*O3EList*|122||ro||
|**263**|[**WarningDtcList**](## "List of active warning messages")|*O3EList*|122||ro||
|**264**|[**WarningDtcHistory**](## "History of warning messages")|*O3EList*|124||ro||
|**265**|[**ErrorDtcList**](## "List of active error messages")|*O3EList*|122||ro||
|**266**|[**ErrorDtcHistory**](## "History of error messages")|*O3EList*|124||ro||
|**268**|[**FlowTemperatureSensor**](## "Flow temperature in the primary circuit downstream from the heat generator")|*O3EComplexType*|9||ro|[Link](https://github.com/open3e/open3e/wiki/036-DoI-%E2%80%90-Data-points-of-Interest/#data-points-of-vitocal-250)|
|**269**|[**ReturnTemperatureSensor**](## "Flow temperature in the primary circuit upstream from the heat generator")|*O3EComplexType*|9||ro|[Link](https://github.com/open3e/open3e/wiki/036-DoI-%E2%80%90-Data-points-of-Interest/#data-points-of-vitocal-250)|
|**271**|[**DomesticHotWaterSensor**](## "Actual temperature domestic hot water buffer")|*O3EComplexType*|9||ro|[Link](https://github.com/open3e/open3e/wiki/036-DoI-%E2%80%90-Data-points-of-Interest/#data-points-of-vitocal-250)|
|**274**|[**OutsideTemperatureSensor**](## "Outside temperature value")|*O3EComplexType*|9||ro||
|**282**|[**HydraulicSeparatorTemperatureSensor**](## "Actual flow temperature of the hydraulic switch")|*O3EComplexType*|9||ro||
|**284**|[**MixerOneCircuitFlowTemperatureSensor**](## "Heating circuit 1: Actual flow temperature value")|*O3EComplexType*|9||ro||
|**318**|[**WaterPressureSensor**](## "Actual pressure heat generator circulation")|*O3EComplexType*|9||ro||
|**320**|[**PrimaryHeatExchangerLiquidTemperatureSensor**](## "Actual temperature primary heat exchanger inlet")|*O3EComplexType*|9||ro||
|**321**|[**CompressorInletTemperatureSensor**](## "Actual temperature compressor inlet")|*O3EComplexType*|9||ro||
|**322**|[**CompressorInletPressureSensor**](## "Actual pressure compressor inlet")|*O3EComplexType*|9||ro||
|**324**|[**CompressorOutletTemperatureSensor**](## "Actual temperature compressor outlet")|*O3EComplexType*|9||ro||
|**325**|[**CompressorOutletPressureSensor**](## "Actual pressure compressor outlet")|*O3EComplexType*|9||ro||
|**355**|[**SecondaryHeatExchangerLiquidTemperatureSensor**](## "Actual temperature secondary heat exchanger outlet")|*O3EComplexType*|9||ro||
|**381**|[**CentralHeatingPump**](## "Status of the primary circuit pump")|*O3EComplexType*|4||ro|[Link](https://github.com/open3e/open3e/discussions/212)|
|**389**|[**ElectronicExpansionValveOneCurrentPositionPercent**](## "Actual position expansion valve one (secondary heat exchanger outlet)")|O3EInt8|1|%|ro||
|**391**|[**ElectronicExpansionValveTwoCurrentPositionPercent**](## "Actual position expansion valve two (evaporator outlet)")|O3EInt8|1|%|ro||
|**396**|[**DomesticHotWaterTemperatureSetpoint**](## "Temperature setpoint domestic hot water")|O3EInt16|2|[°C](## "°C or °F (system configuration)")|**rw**||
|**491**|[**DomesticHotWaterCirculationPump**](## "Request for domestic hot water circulation pump")|*O3EComplexType*|2||**rw**||
|**497**|[**DomesticHotWaterCirculationPumpMode**](## "Operation Mode of domestic hot water circulation pump")|*O3EComplexType*|5||**rw**|[See page 22f](https://static.viessmann-climatesolutions.com/resources/technical_documents/DE/de/VSA/6179923VSA00001_1.pdf?)|
|**531**|[**DomesticHotWaterOperationState**](## "Operation state of domestic hot water preparation")|*O3EComplexType*|2||**rw**||
|**535**|[**ObjectElectricalEnergyStatistical**](## "Cumulative Grid Energy Statistics")|*O3EComplexType*|12||ro|[Link](https://github.com/open3e/open3e/wiki/036-DoI-%E2%80%90-Data-points-of-Interest/#data-points-of-vx3)|
|**902**|[**MalfunctionIdentification**](## "Indicates whether faults are present")|O3EByteVal|1||ro||
|**954**|[**BusTopologyMatrix**](## "Matrix of CAN bus topology")|*O3EList*|181||ro||
|**987**|[**MixerOneCircuitFlowTemperatureTargetSetpoint**](## "Temperature setpoint heating curcuit 1")|O3EInt16|2|[°C](## "°C or °F (system configuration)")|**rw**||
|**1043**|[**AllengraSensor**](## "Flow rate and temperature in the primary circuit of the heat generator")|*O3EComplexType*|5||ro|[Link](https://github.com/open3e/open3e/wiki/036-DoI-%E2%80%90-Data-points-of-Interest/#data-points-of-vitocal-250)|
|**1190**|[**ThermalPower**](## "Actual thermal power output of the system")|*O3EComplexType*|4||ro||
|**1294**|[**EnergyConsumptionCentralHeatingMonthMatrix**](## "Energy Consumption Central Heating Per Month")|*O3EComplexType*|124||ro||
|**1311**|[**EnergyConsumptionDomesticHotWaterMonthMatrix**](## "Energy Consumption Domestic Hot Water Per Month")|*O3EComplexType*|124||ro||
|**1315**|[**GeneratedCentralHeatingOutputMonthMatrix**](## "Generated Central Heating Output Per Month")|*O3EComplexType*|124||ro||
|**1316**|[**EnergyConsumptionCentralHeatingYearMatrix**](## "Energy Consumption Central Heating Per Year")|*O3EComplexType*|96||ro||
|**1333**|[**EnergyConsumptionDomesticHotWaterYearMatrix**](## "Energy Consumption Domestic Hot Water Per Year")|*O3EComplexType*|96||ro||
|**1337**|[**GeneratedCentralHeatingOutputYearMatrix**](## "Generated Central Heating Output Per Year")|*O3EComplexType*|96||ro||
|**1391**|[**GeneratedDomesticHotWaterOutput**](## "Generated Domestic Hot Water Output per specific period")|*O3EComplexType*|24||ro||
|**1392**|[**GeneratedDomesticHotWaterOutputMonthMatrix**](## "Generated Domestic Hot Water Output Per Month")|*O3EComplexType*|124||ro||
|**1393**|[**GeneratedDomesticHotWaterOutputYearMatrix**](## "Generated Domestic Hot Water Output Per Year")|*O3EComplexType*|96||ro||
|**1415**|[**MixerOneCircuitOperationState**](## "Heating curcuit 1: Operating Mode")|*O3EComplexType*|2||**rw**||
|**1603**|[**PointOfCommonCouplingPower**](## "Actual Power at Point of Common Coupling")|*O3EComplexType*|4||ro|[Link](https://github.com/open3e/open3e/wiki/036-DoI-%E2%80%90-Data-points-of-Interest/#data-points-of-vx3)|
|**1603**|[**PointOfCommonCouplingPower**](## "Actual Power at Point of Common Coupling")|*O3EComplexType*|12||ro||
|**1643**|[**MixerOneCircuitCurrentTemperatureSetpoint**](## "Heating Circuit 1: Flow or Room Temperature Setpoint")|O3EInt16|2|[°C](## "°C or °F (system configuration)")|**rw**||
|**1664**|[**ElectricalEnergyStorageStateOfCharge**](## "SoC of Battery")|O3EInt8|1|%|ro|[Link](https://github.com/open3e/open3e/wiki/036-DoI-%E2%80%90-Data-points-of-Interest/#data-points-of-vx3)|
|**1684**|[**AmbientTemperatureSensor**](## "Actual Ambient Temperature")|*O3EComplexType*|9||ro||
|**1690**|[**ElectricalEnergySystemPhotovoltaicStatus**](## "Actual Power of Photovoltaic")|*O3EComplexType*|17||ro|[Link](https://github.com/open3e/open3e/wiki/036-DoI-%E2%80%90-Data-points-of-Interest/#data-points-of-vx3)|
|**1771**|[**EngineRoomTemperatureSensor**](## "Actual Temperature at Engine Room")|*O3EComplexType*|9||ro||
|**1772**|[**CompressorOilTemperatureSensor**](## "Actual Compressor Oil Temperature")|*O3EComplexType*|9||ro|[Link](https://github.com/open3e/open3e/wiki/036-DoI-%E2%80%90-Data-points-of-Interest)|
|**1775**|[**PrimaryCircuitFanOne**](## "Speed of Fan 1")|O3EByteVal|1|%|ro|[Link](https://github.com/open3e/open3e/wiki/036-DoI-%E2%80%90-Data-points-of-Interest)|
|**1776**|[**PrimaryCircuitFanTwo**](## "Speed of Fan 2")|O3EByteVal|1|%|ro|[Link](https://github.com/open3e/open3e/wiki/036-DoI-%E2%80%90-Data-points-of-Interest)|
|**1799**|[**PrimaryCircuitCurrentTemperatureSetpoint**](## "Heating Circuit 1: Temperature Setpoint")|O3EInt16|2|[°C](## "°C or °F (system configuration)")|**rw**||
|**1801**|[**ElectricalEnergyStorageEnergyTransferStatistic**](## "Statistics of Transfered Electrical Energy")|*O3EComplexType*|40||ro|[Link](https://github.com/open3e/open3e/wiki/036-DoI-%E2%80%90-Data-points-of-Interest/#data-points-of-vx3)|
|**1802**|[**EnergyProductionPhotovoltaic**](## "Statistics of Photovoltaic Production")|*O3EComplexType*|80||ro|[Link](https://github.com/open3e/open3e/wiki/036-DoI-%E2%80%90-Data-points-of-Interest/#data-points-of-vx3)|
|**1828**|[**InverterElectricalEnergyStorageCurrentMaximumlChargePower**](## "Maximum Electrical Power of Inverter for Charging")|*O3EComplexType*|4||ro||
|**1830**|[**InverterElectricalEnergyStorageCurrentMaximumlDishargePower**](## "Maximum Electrical Power of Inverter for Discharging")|*O3EComplexType*|4||ro||
|**1831**|[**PhotovoltaicCurrentStringPower**](## "Current Photovoltaic Power per String")|*O3EComplexType*|12||ro||
|**1832**|[**PhotovoltaicStringCurrent**](## "Current Photovoltaic Current per String (resolution is 1 Ampere)")|*O3EComplexType*|12||ro||
|**1833**|[**PhotovoltaicStringVoltage**](## "Current Photovoltaic Voltage per String")|*O3EComplexType*|12||ro|[Link](https://github.com/open3e/open3e/wiki/036-DoI-%E2%80%90-Data-points-of-Interest/#data-points-of-vx3)|
|**1834**|[**ElectricalEnergyStorageStateOfEnergy**](## "SoC of Battery")|*O3EComplexType*|4||ro||
|**1836**|[**ElectricalEnergyStorageCurrentPower**](## "Current Power for Battery Discharging (positive values) and Charging (negative values)")|O3EInt32|4|W|ro||
|**1842**|[**SecondaryCircuitFourThreeWayValve**](## "Circuit 2: Position of Four Three Way Valve")|*O3EComplexType*|2||ro||
|**2214**|[**BackupBoxConfiguration**](## "Configuration for Backup Box")|*O3EComplexType*|2||**rw**||
|**2256**|[**DesiredThermalEnergyDefrost**](## "Target value of thermal energy to perform next defrosting")|O3EInt16|2|Wh|ro||
|**2320**|[**DomesticHotWaterStatus**](## "Status of domestic hot water preparation {0: Idle, 1: Active, 2: Postrun}")|O3EEnum|1||ro||
|**2333**|[**EconomizerLiquidTemperatureSensor**](## "Actual temperature economizer inlet")|*O3EComplexType*|9||ro|[Link](https://github.com/open3e/open3e/wiki/036-DoI-%E2%80%90-Data-points-of-Interest/#data-points-of-vitocal-250)|
|**2334**|[**EvaporatorVaporTemperatureSensor**](## "Actual temperature avaporator inlet")|*O3EComplexType*|9||ro|[Link](https://github.com/open3e/open3e/wiki/036-DoI-%E2%80%90-Data-points-of-Interest/#data-points-of-vitocal-250)|
|**2346**|[**CompressorSpeedPercent**](## "Actual speed of heat pump compressor")|O3EInt8|1|%|ro|[Link](https://github.com/open3e/open3e/wiki/036-DoI-%E2%80%90-Data-points-of-Interest/#data-points-of-vitocal-250)|
|**2351**|[**HeatPumpCompressor**](## "Actual state of the heat pump compressor")|*O3EComplexType*|2||ro||
|**2352**|[**AdditionalElectricHeater**](## "Actual state of the electric auxiliary heating")|*O3EComplexType*|2||ro||
|**2369**|[**HeatPumpCompressorStatistical**](## "Statistics for heat pump compressor starts")|*O3EComplexType*|14||ro||
|**2486**|[**CurrentElectricalPowerConsumptionRefrigerantCircuit**](## "Actual electrical power consumption of the refrigeration circuit")|O3EInt32|4|W|ro||
|**2487**|[**CurrentElectricalPowerConsumptionElectricHeater**](## "Actual electrical power consumption of the auxiliary heater")|O3EInt32|4|W|ro||
|**2488**|[**CurrentElectricalPowerConsumptionSystem**](## "Actual total electrical power consumption of the system")|O3EInt32|4|W|ro||
|**2494**|[**CurrentThermalCapacityRefrigerantCircuit**](## "Actual thermal power output of the refrigeration circuit")|O3EInt32|4|W|ro||
|**2495**|[**CurrentThermalCapacityElectricHeater**](## "Actual thermal power output of the auxiliary heater")|O3EInt32|4|W|ro||
|**2496**|[**CurrentThermalCapacitySystem**](## "Actual thermal power output of the system")|O3EInt32|4|W|ro||
|**2569**|[**CompressorSpeedRps**](## "Actual speed of the heat pump compressor")|O3EInt16|2|rps|ro||
|**2735**|[**FourThreeWayValveValveCurrentPosition**](## "Current position of the four/three-way valve {0: Heating/Cooling, 1: Internal Buffer, 2: Domestic Hot Water, 3: Heating/Cooling and Internal Buffer, 4: Domestic Hot Water and Internal Buffer}")|O3EEnum|1||ro||
|**2760**|[**EnergyOwnConsumption**](## "Own Energy Consumption")|*O3EComplexType*|24||ro||
|**2806**|[**RefrigerationCircuitOperationMode**](## "Actual operating mode of the refrigeration circuit")|*O3EComplexType*|2||ro||
|**3016**|[**HeatingBufferTemperatureSensor**](## "Actual temperature of the heating buffer")|*O3EComplexType*|9||ro||
## All presently known data points including subs

[Back to table of contents](#table-of-contents)

|  Did | ID   | Codec | Length | Unit  |   Access | Further info |
| ---: | :--- | :---  | ---:   | :---: |  :---:  | :---         |
|**256**|[**BusIdentification**](## "Device infos")|*O3EComplexType*|36||ro||
| |- BusAddress|O3EByteVal|1||||
| |- [BusType](## "{0: OwnBus, 1: PlusBus, 2: CanInternal, 3: CanExternal, 4: InternalUart, 5: Zigbee, 6: CanRaw, 7: Unkown, 8: ModBus, 9: EEBUS, 10: PlusBusTwo, 11: ISquaredCBus, 12: HEMS_Bus, 13: TL_SolarLogBus, 14: ServiceBus}")|O3EEnum|1||||
| |- [DeviceProperty](## "{0: NOTHING, 1: BACKENDGATEWAY, 2: HMUMASTER, 3: HMUSLAVE, 4: MCUMASTER, 5: MCUSLAVE, 6: HMI, 7: BCU, 8: GASAIRRATIOSYSTEM, 9: ADIO, 10: DIO, 11: KNXGATEWAY, 12: BACNETGATEWAY, 13: MODBUSGATEWAY, 14: MBUS, 15: FRIWASTATION, 16: FUELCELL, 17: CSC, 18: PHOTOVOLTAIC, 19: PRODUCTIONGATEWAY, 20: DIAGNOSTICGATEWAY, 21: SDIO, 22: MTWOIO, 23: REMOTECONTROLLOCAL, 24: CLIMASENSOR, 25: TEMPERATURERADIATORVALVE, 26: UNDERFLOORHEATINGVALVE, 27: ENERGYMETER, 28: EMCUMASTER, 29: EMCUSLAVE, 30: BMCU, 31: HPMUMASTER, 32: HPMUSLAVE, 33: VCMU, 34: EHCU, 35: MZIO, 36: PBE, 37: HBMU, 38: OSME, 39: TWOSTEPPERMOTOR, 40: INVERTER, 41: SMARTROOMCONTROL, 42: VCUMASTER, 43: VCUSLAVE, 44: CANOPENIOMODULE, 45: FAN, 46: ELECTRICALPREHEATER, 47: ELECTRICALPOSTHEATER, 48: GENERICHEATPUMP, 49: HOMEENERGYMANAGEMENTSYSTEM, 50: EEBUSHUB, 51: HIO, 52: BCUSLAVE, 53: UNDERFLOORHEATINGBOX, 54: ZIGBEERANGEEXTENDER, 55: AIRQUALITYSENSOR, 56: WATERSOFTENER, 57: AIRPURIFIER, 58: CONNECTIONADAPTERSTEPPERMOTOR, 59: REFRIGERATIONFURNITURETYPE, 60: SOLARLOGGATEWAY, 61: SYSTEMCONTROLLEREMBEDDED, 62: WALLBOX, 63: APARTMENTTRANSFERSTATION, 64: DHWTS, 65: VENTILATIONUNIT}")|O3EEnum|1||||
| |- [DeviceFunction](## "{0: NOTHING, 1: BACKENDGATEWAY, 2: HMUMASTER, 3: HMUSLAVE, 4: MCUMASTER, 5: MCUSLAVE, 6: HMI, 7: BCU, 8: GASAIRRATIOSYSTEM, 9: ADIO, 10: DIO, 11: KNXGATEWAY, 12: BACNETGATEWAY, 13: MODBUSGATEWAY, 14: MBUS, 15: FRIWASTATION, 16: FUELCELL, 17: CSC, 18: PHOTOVOLTAIC, 19: PRODUCTIONGATEWAY, 20: DIAGNOSTICGATEWAY, 21: SDIO, 22: MTWOIO, 23: REMOTECONTROLLOCAL, 24: CLIMASENSOR, 25: TEMPERATURERADIATORVALVE, 26: UNDERFLOORHEATINGVALVE, 27: ENERGYMETER, 28: EMCUMASTER, 29: EMCUSLAVE, 30: BMCU, 31: HPMUMASTER, 32: HPMUSLAVE, 33: VCMU, 34: EHCU, 35: MZIO, 36: PBE, 37: HBMU, 38: OSME, 39: TWOSTEPPERMOTOR, 40: INVERTER, 41: SMARTROOMCONTROL, 42: VCUMASTER, 43: VCUSLAVE, 44: CANOPENIOMODULE, 45: FAN, 46: ELECTRICALPREHEATER, 47: ELECTRICALPOSTHEATER, 48: GENERICHEATPUMP, 49: HOMEENERGYMANAGEMENTSYSTEM, 50: EEBUSHUB, 51: HIO, 52: BCUSLAVE, 53: UNDERFLOORHEATINGBOX, 54: ZIGBEERANGEEXTENDER, 55: AIRQUALITYSENSOR, 56: WATERSOFTENER, 57: AIRPURIFIER, 58: CONNECTIONADAPTERSTEPPERMOTOR, 59: REFRIGERATIONFURNITURETYPE, 60: SOLARLOGGATEWAY, 61: SYSTEMCONTROLLEREMBEDDED, 62: WALLBOX, 63: APARTMENTTRANSFERSTATION, 64: DHWTS, 65: VENTILATIONUNIT}")|O3EEnum|1||||
| |- [SW-Version](## "??.???.YYcw.ver")|O3ESoftVers|8||||
| |- HW-Version|O3ESoftVers|8||||
| |- VIN|O3EUtf8|16||||
|**257**|[**StatusDtcList**](## "List of active status messages")|*O3EList*|122||ro||
| |- [Count](## "Number of entries listed")|O3EByteVal|2||||
| |- - State|O3EEnum|2||||
| |- - [DateTime](## "Date of event")|O3EDateTime|8||||
| |- - Unknown|O3EByteVal|2||||
|**258**|[**StatusDtcHistory**](## "History of status messages")|*O3EList*|122||ro||
| |- [Count](## "Number of entries listed")|O3EByteVal|2||||
| |- - State|O3EEnum|2||||
| |- - [DateTime](## "Date of event")|O3EDateTime|8||||
| |- - Unknown|O3EByteVal|2||||
|**259**|[**InfoDtcList**](## "List of active info messages")|*O3EList*|122||ro||
| |- [Count](## "Number of entries listed")|O3EByteVal|2||||
| |- - Info|O3EEnum|2||||
| |- - [DateTime](## "Date of event")|O3EDateTime|8||||
| |- - Unknown|O3EByteVal|2||||
|**260**|[**InfoDtcHistory**](## "History of info messages")|*O3EList*|122||ro||
| |- [Count](## "Number of entries listed")|O3EByteVal|2||||
| |- - Info|O3EEnum|2||||
| |- - [DateTime](## "Date of event")|O3EDateTime|8||||
| |- - Unknown|O3EByteVal|2||||
|**261**|[**ServiceDtcList**](## "List of active service messages")|*O3EList*|122||ro||
| |- [Count](## "Number of entries listed")|O3EByteVal|2||||
| |- - [Service](## "{0: NoServiceRequired, 1: HoursTillServiceExpired, 2: ReplaceSacrificialAnode, 4: RefillWaterSystem, 5: RegularMaintenanceActive, 6: OverhaulActive, 7: DurationOfLife, 8: BurnerOperatingHoursTillServiceExpired, 9: ServiceFuelCellSixMonthsTillServiceExpired, 10: ServiceFuelCellFiveMonthsTillServiceExpired, 11: ServiceFuelCellFourMonthsTillServiceExpired, 12: ServiceFuelCellThreeMonthsTillServiceExpired, 13: ServiceFuelCellTwoMonthTillServiceExpired, 14: ServiceFuelCellFourtyfiveDaysTillServiceExpired, 15: ServiceFuelCellOneMonthTillServiceExpired, 16: ServiceFuelCellSixMonthsTillOverhaulExpired, 17: ServiceFuelCellFiveMonthsTillOverhaulExpired, 18: ServiceFuelCellFourMonthsTillOverhaulExpired, 19: ServiceFuelCellThreeMonthsTillOverhaulExpired, 20: ServiceFuelCellTwoMonthTillOverhaulExpired, 21: ServiceFuelCellFourtyfiveDaysTillOverhaulExpired, 22: ServiceFuelCellOneMonthTillOverhaulExpired, 23: ServiceFuelCellSixMonthsTillEndOfLife, 24: ServiceFuelCellFiveMonthsTillEndOfLife, 25: ServiceFuelCellFourMonthsTillEndOfLife, 26: ServiceFuelCellThreeMonthsTillEndOfLife, 27: ServiceFuelCellTwoMonthTillEndOfLife, 28: ServiceFuelCellFourtyfiveDaysTillEndOfLife, 29: ServiceFuelCellOneMonthTillEndOfLife, 30: BalancingInProgress, 31: BackupPowerFunctionActive, 32: BatteryLow, 33: BatteryDeviceTurnedOff, 34: MaintenanceIntervalHydraulicFilterExpired, 35: MaintenanceIntervalVentilationFilterExpired, 36: ContaminationAirFilter, 37: LagDeviceDtcReported, 65533: ViewedServiceList, 65534: ServiceDoneSuccessful}")|O3EEnum|2||||
| |- - [DateTime](## "Date of event")|O3EDateTime|8||||
| |- - Unknown|O3EByteVal|2||||
|**262**|[**ServiceDtcHistory**](## "History of service messages")|*O3EList*|122||ro||
| |- [Count](## "Number of entries listed")|O3EByteVal|2||||
| |- - [Service](## "{0: NoServiceRequired, 1: HoursTillServiceExpired, 2: ReplaceSacrificialAnode, 4: RefillWaterSystem, 5: RegularMaintenanceActive, 6: OverhaulActive, 7: DurationOfLife, 8: BurnerOperatingHoursTillServiceExpired, 9: ServiceFuelCellSixMonthsTillServiceExpired, 10: ServiceFuelCellFiveMonthsTillServiceExpired, 11: ServiceFuelCellFourMonthsTillServiceExpired, 12: ServiceFuelCellThreeMonthsTillServiceExpired, 13: ServiceFuelCellTwoMonthTillServiceExpired, 14: ServiceFuelCellFourtyfiveDaysTillServiceExpired, 15: ServiceFuelCellOneMonthTillServiceExpired, 16: ServiceFuelCellSixMonthsTillOverhaulExpired, 17: ServiceFuelCellFiveMonthsTillOverhaulExpired, 18: ServiceFuelCellFourMonthsTillOverhaulExpired, 19: ServiceFuelCellThreeMonthsTillOverhaulExpired, 20: ServiceFuelCellTwoMonthTillOverhaulExpired, 21: ServiceFuelCellFourtyfiveDaysTillOverhaulExpired, 22: ServiceFuelCellOneMonthTillOverhaulExpired, 23: ServiceFuelCellSixMonthsTillEndOfLife, 24: ServiceFuelCellFiveMonthsTillEndOfLife, 25: ServiceFuelCellFourMonthsTillEndOfLife, 26: ServiceFuelCellThreeMonthsTillEndOfLife, 27: ServiceFuelCellTwoMonthTillEndOfLife, 28: ServiceFuelCellFourtyfiveDaysTillEndOfLife, 29: ServiceFuelCellOneMonthTillEndOfLife, 30: BalancingInProgress, 31: BackupPowerFunctionActive, 32: BatteryLow, 33: BatteryDeviceTurnedOff, 34: MaintenanceIntervalHydraulicFilterExpired, 35: MaintenanceIntervalVentilationFilterExpired, 36: ContaminationAirFilter, 37: LagDeviceDtcReported, 65533: ViewedServiceList, 65534: ServiceDoneSuccessful}")|O3EEnum|2||||
| |- - [DateTime](## "Date of event")|O3EDateTime|8||||
| |- - Unknown|O3EByteVal|2||||
|**263**|[**WarningDtcList**](## "List of active warning messages")|*O3EList*|122||ro||
| |- [Count](## "Number of entries listed")|O3EByteVal|2||||
| |- - Warning|O3EEnum|2||||
| |- - [DateTime](## "Date of event")|O3EDateTime|8||||
| |- - Unknown|O3EByteVal|2||||
|**264**|[**WarningDtcHistory**](## "History of warning messages")|*O3EList*|124||ro||
| |- [Count](## "Number of entries listed")|O3EByteVal|2||||
| |- [GrandTotal](## "Total number of entries")|O3EByteVal|2||||
| |- - Warning|O3EEnum|2||||
| |- - [DateTime](## "Date of event")|O3EDateTime|8||||
| |- - Unknown|O3EByteVal|2||||
|**265**|[**ErrorDtcList**](## "List of active error messages")|*O3EList*|122||ro||
| |- [Count](## "Number of entries listed")|O3EByteVal|2||||
| |- - Error|O3EEnum|2||||
| |- - [DateTime](## "Date of event")|O3EDateTime|8||||
| |- - Unknown|O3EByteVal|2||||
|**266**|[**ErrorDtcHistory**](## "History of error messages")|*O3EList*|124||ro||
| |- [Count](## "Number of entries listed")|O3EByteVal|2||||
| |- [GrandTotal](## "Total number of entries")|O3EByteVal|2||||
| |- - Error|O3EEnum|2||||
| |- - [DateTime](## "Date of event")|O3EDateTime|8||||
| |- - Unknown|O3EByteVal|2||||
|**268**|[**FlowTemperatureSensor**](## "Flow temperature in the primary circuit downstream from the heat generator")|*O3EComplexType*|9||ro|[Link](https://github.com/open3e/open3e/wiki/036-DoI-%E2%80%90-Data-points-of-Interest/#data-points-of-vitocal-250)|
| |- Actual|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- Minimum|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- Maximum|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- Average|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- [SensorStatus](## "Actual state of sensor {0: no_error, 1: interruption, 2: short_circuit, 3: electrical_fault, 4: not_available, 5: invalidates}")|O3EEnum|1||||
|**269**|[**ReturnTemperatureSensor**](## "Flow temperature in the primary circuit upstream from the heat generator")|*O3EComplexType*|9||ro|[Link](https://github.com/open3e/open3e/wiki/036-DoI-%E2%80%90-Data-points-of-Interest/#data-points-of-vitocal-250)|
| |- Actual|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- Minimum|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- Maximum|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- Average|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- [SensorStatus](## "{0: no_error, 1: interruption, 2: short_circuit, 3: electrical_fault, 4: not_available, 5: invalidates}")|O3EEnum|1||||
|**271**|[**DomesticHotWaterSensor**](## "Actual temperature domestic hot water buffer")|*O3EComplexType*|9||ro|[Link](https://github.com/open3e/open3e/wiki/036-DoI-%E2%80%90-Data-points-of-Interest/#data-points-of-vitocal-250)|
| |- Actual|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- Minimum|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- Maximum|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- Average|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- [SensorStatus](## "{0: no_error, 1: interruption, 2: short_circuit, 3: electrical_fault, 4: not_available, 5: invalidates}")|O3EEnum|1||||
|**272**|**DomesticHotWaterFlowSensor**|RawCodec|10||ro||
|**273**|[**SolarRoofTemperatureSensor**](## "Actual collector temperature value")|*O3EComplexType*|9||ro||
| |- Actual|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- Minimum|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- Maximum|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- Average|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- [SensorStatus](## "{0: no_error, 1: interruption, 2: short_circuit, 3: electrical_fault, 4: not_available, 5: invalidates}")|O3EEnum|1||||
|**274**|[**OutsideTemperatureSensor**](## "Outside temperature value")|*O3EComplexType*|9||ro||
| |- Actual|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- Minimum|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- Maximum|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- Average|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- [SensorStatus](## "{0: no_error, 1: interruption, 2: short_circuit, 3: electrical_fault, 4: not_available, 5: invalidates}")|O3EEnum|1||||
|**275**|[**SolarBottomTemperatureSensor**](## "Actual collector return temperature value")|*O3EComplexType*|9||ro||
| |- Actual|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- Minimum|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- Maximum|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- Average|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- [SensorStatus](## "{0: no_error, 1: interruption, 2: short_circuit, 3: electrical_fault, 4: not_available, 5: invalidates}")|O3EEnum|1||||
|**277**|[**BufferBottomTemperatureSensor**](## "Actual buffer bottom temperature value")|*O3EComplexType*|9||ro||
| |- Actual|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- Minimum|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- Maximum|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- Average|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- [SensorStatus](## "{0: no_error, 1: interruption, 2: short_circuit, 3: electrical_fault, 4: not_available, 5: invalidates}")|O3EEnum|1||||
|**278**|[**BufferMidBottomTemperatureSensor**](## "Actual buffer mid bottom temperature value")|*O3EComplexType*|9||ro||
| |- Actual|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- Minimum|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- Maximum|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- Average|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- [SensorStatus](## "{0: no_error, 1: interruption, 2: short_circuit, 3: electrical_fault, 4: not_available, 5: invalidates}")|O3EEnum|1||||
|**279**|[**BufferMidTemperatureSensor**](## "Actual buffer mid temperature value")|*O3EComplexType*|9||ro||
| |- [Actual](## "°C")|O3EInt16|2||||
| |- Minimum|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- Maximum|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- Average|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- [SensorStatus](## "{0: no_error, 1: interruption, 2: short_circuit, 3: electrical_fault, 4: not_available, 5: invalidates}")|O3EEnum|1||||
|**281**|[**BufferTopTemperatureSensor**](## "Actual buffer top temperature value")|*O3EComplexType*|9||ro||
| |- [Actual](## "°C")|O3EInt16|2||||
| |- Minimum|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- Maximum|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- Average|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- [SensorStatus](## "{0: no_error, 1: interruption, 2: short_circuit, 3: electrical_fault, 4: not_available, 5: invalidates}")|O3EEnum|1||||
|**282**|[**HydraulicSeparatorTemperatureSensor**](## "Actual flow temperature of the hydraulic switch")|*O3EComplexType*|9||ro||
| |- Actual|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- Minimum|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- Maximum|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- Average|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- [SensorStatus](## "{0: no_error, 1: interruption, 2: short_circuit, 3: electrical_fault, 4: not_available, 5: invalidates}")|O3EEnum|1||||
|**283**|[**HydraulicSeparatorReturnTemperatureSensor**](## "Actual return temperature of the hydraulic switch")|*O3EComplexType*|9||ro||
| |- Actual|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- Minimum|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- Maximum|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- Average|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- [SensorStatus](## "{0: no_error, 1: interruption, 2: short_circuit, 3: electrical_fault, 4: not_available, 5: invalidates}")|O3EEnum|1||||
|**284**|[**MixerOneCircuitFlowTemperatureSensor**](## "Heating circuit 1: Actual flow temperature value")|*O3EComplexType*|9||ro||
| |- Actual|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- Minimum|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- Maximum|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- Average|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- [SensorStatus](## "{0: no_error, 1: interruption, 2: short_circuit, 3: electrical_fault, 4: not_available, 5: invalidates}")|O3EEnum|1||||
|**285**|[**MixerOneCircuitReturnTemperatureSensor**](## "Heating circuit 1: Actual return temperature value")|*O3EComplexType*|9||ro||
| |- Actual|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- Minimum|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- Maximum|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- Average|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- [SensorStatus](## "{0: no_error, 1: interruption, 2: short_circuit, 3: electrical_fault, 4: not_available, 5: invalidates}")|O3EEnum|1||||
|**286**|[**MixerTwoCircuitFlowTemperatureSensor**](## "Heating circuit 2: Actual flow temperature value")|*O3EComplexType*|9||ro||
| |- Actual|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- Minimum|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- Maximum|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- Average|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- [SensorStatus](## "{0: no_error, 1: interruption, 2: short_circuit, 3: electrical_fault, 4: not_available, 5: invalidates}")|O3EEnum|1||||
|**287**|[**MixerTwoCircuitReturnTemperatureSensor**](## "Heating circuit 2: Actual return temperature value")|*O3EComplexType*|9||ro||
| |- Actual|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- Minimum|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- Maximum|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- Average|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- [SensorStatus](## "{0: no_error, 1: interruption, 2: short_circuit, 3: electrical_fault, 4: not_available, 5: invalidates}")|O3EEnum|1||||
|**288**|[**MixerThreeCircuitFlowTemperatureSensor**](## "Heating circuit 3: Actual flow temperature value")|*O3EComplexType*|9||ro||
| |- Actual|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- Minimum|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- Maximum|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- Average|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- [SensorStatus](## "{0: no_error, 1: interruption, 2: short_circuit, 3: electrical_fault, 4: not_available, 5: invalidates}")|O3EEnum|1||||
|**289**|[**MixerThreeCircuitReturnTemperatureSensor**](## "Heating circuit 3: Actual return temperature value")|*O3EComplexType*|9||ro||
| |- Actual|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- Minimum|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- Maximum|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- Average|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- [SensorStatus](## "{0: no_error, 1: interruption, 2: short_circuit, 3: electrical_fault, 4: not_available, 5: invalidates}")|O3EEnum|1||||
|**290**|[**MixerFourCircuitFlowTemperatureSensor**](## "Heating circuit 4: Actual flow temperature value")|*O3EComplexType*|9||ro||
| |- Actual|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- Minimum|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- Maximum|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- Average|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- [SensorStatus](## "{0: no_error, 1: interruption, 2: short_circuit, 3: electrical_fault, 4: not_available, 5: invalidates}")|O3EEnum|1||||
|**291**|[**MixerFourCircuitReturnTemperatureSensor**](## "Heating circuit 4: Actual return temperature value")|*O3EComplexType*|9||ro||
| |- Actual|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- Minimum|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- Maximum|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- Average|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- [SensorStatus](## "{0: no_error, 1: interruption, 2: short_circuit, 3: electrical_fault, 4: not_available, 5: invalidates}")|O3EEnum|1||||
|**318**|[**WaterPressureSensor**](## "Actual pressure heat generator circulation")|*O3EComplexType*|9||ro||
| |- Actual|O3EInt16|2|hPa|||
| |- Minimum|O3EInt16|2|hPa|||
| |- Maximum|O3EInt16|2|hPa|||
| |- Average|O3EInt16|2|hPa|||
| |- [SensorStatus](## "{0: no_error, 1: interruption, 2: short_circuit, 3: electrical_fault, 4: not_available, 5: invalidates}")|O3EEnum|1||||
|**320**|[**PrimaryHeatExchangerLiquidTemperatureSensor**](## "Actual temperature primary heat exchanger inlet")|*O3EComplexType*|9||ro||
| |- Actual|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- Minimum|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- Maximum|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- Average|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- [SensorStatus](## "{0: no_error, 1: interruption, 2: short_circuit, 3: electrical_fault, 4: not_available, 5: invalidates}")|O3EEnum|1||||
|**321**|[**CompressorInletTemperatureSensor**](## "Actual temperature compressor inlet")|*O3EComplexType*|9||ro||
| |- Actual|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- Minimum|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- Maximum|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- Average|O3EInt16|2|hPa|||
| |- [SensorStatus](## "{0: no_error, 1: interruption, 2: short_circuit, 3: electrical_fault, 4: not_available, 5: invalidates}")|O3EEnum|1||||
|**322**|[**CompressorInletPressureSensor**](## "Actual pressure compressor inlet")|*O3EComplexType*|9||ro||
| |- Actual|O3EInt16|2|hPa|||
| |- Minimum|O3EInt16|2|hPa|||
| |- Maximum|O3EInt16|2|hPa|||
| |- Average|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- Unknown|O3EByteVal|1||||
|**324**|[**CompressorOutletTemperatureSensor**](## "Actual temperature compressor outlet")|*O3EComplexType*|9||ro||
| |- Actual|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- Minimum|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- Maximum|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- Average|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- [SensorStatus](## "{0: no_error, 1: interruption, 2: short_circuit, 3: electrical_fault, 4: not_available, 5: invalidates}")|O3EEnum|1||||
|**325**|[**CompressorOutletPressureSensor**](## "Actual pressure compressor outlet")|*O3EComplexType*|9||ro||
| |- Actual|O3EInt16|2|hPa|||
| |- Minimum|O3EInt16|2|hPa|||
| |- Maximum|O3EInt16|2|hPa|||
| |- Average|O3EInt16|2|hPa|||
| |- Unknown|O3EByteVal|1||||
|**327**|**OutdoorAirTemperatureSensor**|*O3EComplexType*|9||ro||
| |- Actual|O3EInt16|2||||
| |- Minimum|O3EInt16|2||||
| |- Maximum|O3EInt16|2||||
| |- Average|O3EInt16|2||||
| |- Error|O3EByteVal|1||||
|**328**|**SupplyAirTemperatureSensor**|*O3EComplexType*|9||ro||
| |- Actual|O3EInt16|2||||
| |- Minimum|O3EInt16|2||||
| |- Maximum|O3EInt16|2||||
| |- Average|O3EInt16|2||||
| |- Error|O3EByteVal|1||||
|**329**|**ExtractAirTemperatureSensor**|*O3EComplexType*|9||ro||
| |- Actual|O3EInt16|2||||
| |- Minimum|O3EInt16|2||||
| |- Maximum|O3EInt16|2||||
| |- Average|O3EInt16|2||||
| |- Error|O3EByteVal|1||||
|**330**|**ExhaustAirTemperatureSensor**|*O3EComplexType*|9||ro||
| |- Actual|O3EInt16|2||||
| |- Minimum|O3EInt16|2||||
| |- Maximum|O3EInt16|2||||
| |- Average|O3EInt16|2||||
| |- Error|O3EByteVal|1||||
|**331**|**FlueGasTemperatureSensor**|*O3EComplexType*|9||ro||
| |- Actual|O3EInt16|2||||
| |- Minimum|O3EInt16|2||||
| |- Maximum|O3EInt16|2||||
| |- Average|O3EInt16|2||||
| |- [SensorStatus](## "{0: no_error, 1: interruption, 2: short_circuit, 3: electrical_fault, 4: not_available, 5: invalidates}")|O3EEnum|1||||
|**323**|**EnhancedVapourInjectionTemperatureSensor**|RawCodec|9||ro||
|**334**|**MixerOneCircuitRoomTemperatureSensor**|*O3EComplexType*|9||ro||
| |- Actual|O3EInt16|2||||
| |- Minimum|O3EInt16|2||||
| |- Maximum|O3EInt16|2||||
| |- Average|O3EInt16|2||||
| |- Error|O3EByteVal|1||||
|**335**|**MixerTwoCircuitRoomTemperatureSensor**|*O3EComplexType*|9||ro||
| |- Actual|O3EInt16|2||||
| |- Minimum|O3EInt16|2||||
| |- Maximum|O3EInt16|2||||
| |- Average|O3EInt16|2||||
| |- Error|O3EByteVal|1||||
|**336**|**MixerThreeCircuitRoomTemperatureSensor**|*O3EComplexType*|9||ro||
| |- Actual|O3EInt16|2||||
| |- Minimum|O3EInt16|2||||
| |- Maximum|O3EInt16|2||||
| |- Average|O3EInt16|2||||
| |- Error|O3EByteVal|1||||
|**337**|**MixerFourCircuitRoomTemperatureSensor**|*O3EComplexType*|9||ro||
| |- Actual|O3EInt16|2||||
| |- Minimum|O3EInt16|2||||
| |- Maximum|O3EInt16|2||||
| |- Average|O3EInt16|2||||
| |- Error|O3EByteVal|1||||
|**354**|**PrimaryHeatExchangerBaseHeater**|O3EByteVal|1||ro||
|**355**|[**SecondaryHeatExchangerLiquidTemperatureSensor**](## "Actual temperature secondary heat exchanger outlet")|*O3EComplexType*|9||ro||
| |- Actual|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- Minimum|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- Maximum|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- Average|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- Error|O3EByteVal|1||||
|**356**|**MainPowerSupplyValue**|O3EInt16|2||ro||
|**360**|**DomesticHotWaterOutletSensor**|*O3EComplexType*|9||ro||
| |- Actual|O3EInt16|2||||
| |- Minimum|O3EInt16|2||||
| |- Maximum|O3EInt16|2||||
| |- Average|O3EInt16|2||||
| |- Error|O3EByteVal|1||||
|**364**|**Flame**|*O3EComplexType*|6||ro||
| |- State|O3EByteVal|1||||
| |- Unknown|RawCodec|2||||
| |- IonizationCurrent|O3EInt16|2||||
| |- Unknown2|RawCodec|1||||
|**365**|**FlameStatistical**|*O3EComplexType*|42||ro||
| |- Unknown1|RawCodec|38||||
| |- BurnerStarts|O3EInt16|2||||
| |- Unknown2|RawCodec|2||||
|**373**|**FanTargetSpeed**|O3EInt16|2||**rw**||
|**374**|**FanCurrentSpeed**|O3EInt16|2||ro||
|**376**|**MassFlowSensor**|*O3EComplexType*|9||ro||
| |- CurrentValue|O3EInt16|2||||
| |- Min|O3EInt16|2||||
| |- Max|O3EInt16|2||||
| |- DeltaT|O3EInt16|2||||
| |- State|O3EByteVal|1||||
|**377**|**ViessmannIdentificationNumber**|O3EUtf8|16||ro||
|**378**|**PointOfCommonCouplingPhaseOne**|*O3EComplexType*|4||ro||
| |- ActivePower|O3EInt16|2||||
| |- ReactivePower|O3EInt16|2||||
|**379**|**PointOfCommonCouplingPhaseTwo**|*O3EComplexType*|4||ro||
| |- ActivePower|O3EInt16|2||||
| |- ReactivePower|O3EInt16|2||||
|**380**|**PointOfCommonCouplingPhaseThree**|*O3EComplexType*|4||ro||
| |- ActivePower|O3EInt16|2||||
| |- ReactivePower|O3EInt16|2||||
|**381**|[**CentralHeatingPump**](## "Status of the primary circuit pump")|*O3EComplexType*|4||ro|[Link](https://github.com/open3e/open3e/discussions/212)|
| |- State|O3EByteVal|1||||
| |- TargetValue|O3EInt8|1||||
| |- Actual|O3EInt8|1||||
| |- Unknown|RawCodec|1||||
|**382**|**UnitsAndFormats**|*O3EComplexType*|5||ro||
| |- [Units](## "{0: Metric, 1: Imperial}")|O3EEnum|1||||
| |- [DateFormat](## "{0: DayMonthYear, 1: MonthDayYear, 2: YearMonthDay}")|O3EEnum|1||||
| |- [TimeFormat](## "{0: TwentyFourHours, 1: TwelveHours}")|O3EEnum|1||||
| |- TimeZone|O3EByteVal|1||||
| |- Unknown|O3EByteVal|1||||
|**386**|**DiverterValveTargetPosition**|O3EByteVal|1||**rw**||
|**388**|[**ElectronicExpansionValveOneTargetPositionPercent**](## "Target position expansion valve one (secondary heat exchanger outlet)")|O3EInt8|1|%|**rw**||
|**389**|[**ElectronicExpansionValveOneCurrentPositionPercent**](## "Actual position expansion valve one (secondary heat exchanger outlet)")|O3EInt8|1|%|ro||
|**390**|[**ElectronicExpansionValveTwoTargetPositionPercent**](## "Target position expansion valve two (evaporator outlet)")|O3EInt8|1|%|**rw**||
|**391**|[**ElectronicExpansionValveTwoCurrentPositionPercent**](## "Actual position expansion valve two (evaporator outlet)")|O3EInt8|1|%|ro||
|**392**|**DomesticHotWaterPump**|RawCodec|4||ro||
|**395**|[**CentralHeatingTemperatureSetpoint**](## "Temperature setpoint central heating")|O3EInt16|2|[°C](## "°C or °F (system configuration)")|**rw**||
|**396**|[**DomesticHotWaterTemperatureSetpoint**](## "Temperature setpoint domestic hot water")|O3EInt16|2|[°C](## "°C or °F (system configuration)")|**rw**||
|**401**|**MixerOneCircuitPump**|*O3EComplexType*|5||ro||
| |- TargetPowerState|O3EByteVal|1||||
| |- TargetValue|O3EInt8|1||||
| |- PowerState|O3EByteVal|1||||
| |- ErrorState|O3EByteVal|1||||
| |- ActualValue|O3EInt8|1||||
|**402**|**MixerTwoCircuitPump**|*O3EComplexType*|5||ro||
| |- TargetPowerState|O3EByteVal|1||||
| |- TargetValue|O3EInt8|1||||
| |- PowerState|O3EByteVal|1||||
| |- ErrorState|O3EByteVal|1||||
| |- ActualValue|O3EInt8|1||||
|**403**|**MixerThreeCircuitPump**|*O3EComplexType*|5||ro||
| |- TargetPowerState|O3EByteVal|1||||
| |- TargetValue|O3EInt8|1||||
| |- PowerState|O3EByteVal|1||||
| |- ErrorState|O3EByteVal|1||||
| |- ActualValue|O3EInt8|1||||
|**404**|**MixerFourCircuitPump**|*O3EComplexType*|5||ro||
| |- TargetPowerState|O3EByteVal|1||||
| |- TargetValue|O3EInt8|1||||
| |- PowerState|O3EByteVal|1||||
| |- ErrorState|O3EByteVal|1||||
| |- ActualValue|O3EInt8|1||||
|**405**|**MixerFiveCircuitPump**|*O3EComplexType*|5||ro||
| |- TargetPowerState|O3EByteVal|1||||
| |- TargetValue|O3EInt8|1||||
| |- PowerState|O3EByteVal|1||||
| |- ErrorState|O3EByteVal|1||||
| |- ActualValue|O3EInt8|1||||
|**406**|**MixerSixCircuitPump**|*O3EComplexType*|5||ro||
| |- TargetPowerState|O3EByteVal|1||||
| |- TargetValue|O3EInt8|1||||
| |- PowerState|O3EByteVal|1||||
| |- ErrorState|O3EByteVal|1||||
| |- ActualValue|O3EInt8|1||||
|**407**|**MixerSevenCircuitPump**|*O3EComplexType*|5||ro||
| |- TargetPowerState|O3EByteVal|1||||
| |- TargetValue|O3EInt8|1||||
| |- PowerState|O3EByteVal|1||||
| |- ErrorState|O3EByteVal|1||||
| |- ActualValue|O3EInt8|1||||
|**408**|**MixerEightCircuitPump**|*O3EComplexType*|5||ro||
| |- TargetPowerState|O3EByteVal|1||||
| |- TargetValue|O3EInt8|1||||
| |- PowerState|O3EByteVal|1||||
| |- ErrorState|O3EByteVal|1||||
| |- ActualValue|O3EInt8|1||||
|**417**|**SolarCircuitPump**|*O3EComplexType*|5||ro||
| |- SolarCircuitPump|O3EInt8|1||||
| |- Unknown|RawCodec|4||||
|**419**|**OutdoorAirHumiditySensor**|*O3EComplexType*|5||ro||
| |- Actual|O3EByteVal|1||||
| |- Minimum|O3EByteVal|1||||
| |- Maximum|O3EByteVal|1||||
| |- Average|O3EByteVal|1||||
| |- Error|O3EByteVal|1||||
|**420**|**SupplyAirHumiditySensor**|*O3EComplexType*|5||ro||
| |- Actual|O3EByteVal|1||||
| |- Minimum|O3EByteVal|1||||
| |- Maximum|O3EByteVal|1||||
| |- Average|O3EByteVal|1||||
| |- Error|O3EByteVal|1||||
|**421**|**ExtractAirHumiditySensor**|*O3EComplexType*|5||ro||
| |- Actual|O3EByteVal|1||||
| |- Minimum|O3EByteVal|1||||
| |- Maximum|O3EByteVal|1||||
| |- Average|O3EByteVal|1||||
| |- Error|O3EByteVal|1||||
|**422**|**ExhaustAirHumiditySensor**|*O3EComplexType*|5||ro||
| |- Actual|O3EByteVal|1||||
| |- Minimum|O3EByteVal|1||||
| |- Maximum|O3EByteVal|1||||
| |- Average|O3EByteVal|1||||
| |- Error|O3EByteVal|1||||
|**424**|**MixerOneCircuitRoomTemperatureSetpoint**|*O3EComplexType*|9||**rw**||
| |- Comfort|O3EInt16|2||||
| |- Standard|O3EInt16|2||||
| |- Reduced|O3EInt16|2||||
| |- Increased|O3EInt16|2||||
| |- Duration|O3EByteVal|1||||
|**426**|**MixerTwoCircuitRoomTemperatureSetpoint**|*O3EComplexType*|9||**rw**||
| |- Comfort|O3EInt16|2||||
| |- Standard|O3EInt16|2||||
| |- Reduced|O3EInt16|2||||
| |- Increased|O3EInt16|2||||
| |- Duration|O3EByteVal|1||||
|**428**|**MixerThreeCircuitRoomTemperatureSetpoint**|*O3EComplexType*|9||**rw**||
| |- Comfort|O3EInt16|2||||
| |- Standard|O3EInt16|2||||
| |- Reduced|O3EInt16|2||||
| |- Increased|O3EInt16|2||||
| |- Duration|O3EByteVal|1||||
|**429**|**ElectricalPreHeater**|RawCodec|4||ro||
|**430**|**MixerFourCircuitRoomTemperatureSetpoint**|*O3EComplexType*|9||**rw**||
| |- Comfort|O3EInt16|2||||
| |- Standard|O3EInt16|2||||
| |- Reduced|O3EInt16|2||||
| |- Increased|O3EInt16|2||||
| |- Duration|O3EByteVal|1||||
|**431**|**SupplyAirVolumeFlowSensor**|*O3EComplexType*|9||ro||
| |- Zuluftvolumenstrom|O3EInt16|2||||
| |- Minimum|O3EInt16|2||||
| |- Maximum|O3EInt16|2||||
| |- Average|O3EInt16|2||||
| |- Error|O3EByteVal|1||||
|**432**|**MixerFiveCircuitRoomTemperatureSetpoint**|*O3EComplexType*|9||**rw**||
| |- Comfort|O3EInt16|2||||
| |- Standard|O3EInt16|2||||
| |- Reduced|O3EInt16|2||||
| |- Increased|O3EInt16|2||||
| |- Duration|O3EByteVal|1||||
|**433**|**ExhaustAirVolumeFlowSensor**|*O3EComplexType*|9||ro||
| |- Abluftvolumenstrom|O3EInt16|2||||
| |- Minimum|O3EInt16|2||||
| |- Maximum|O3EInt16|2||||
| |- Average|O3EInt16|2||||
| |- Error|O3EByteVal|1||||
|**434**|**MixerSixCircuitRoomTemperatureSetpoint**|*O3EComplexType*|9||**rw**||
| |- Comfort|O3EInt16|2||||
| |- Standard|O3EInt16|2||||
| |- Reduced|O3EInt16|2||||
| |- Increased|O3EInt16|2||||
| |- Duration|O3EByteVal|1||||
|**435**|**VentilationStageTargetVolumeFlow**|*O3EComplexType*|8||**rw**||
| |- Stage1|O3EInt16|2||||
| |- Stage2|O3EInt16|2||||
| |- Stage3|O3EInt16|2||||
| |- Stage4|O3EInt16|2||||
|**436**|**MixerSevenCircuitRoomTemperatureSetpoint**|*O3EComplexType*|9||**rw**||
| |- Comfort|O3EInt16|2||||
| |- Standard|O3EInt16|2||||
| |- Reduced|O3EInt16|2||||
| |- Increased|O3EInt16|2||||
| |- Duration|O3EByteVal|1||||
|**437**|**BypassOperationState**|*O3EComplexType*|2||**rw**||
| |- BypassStatus|O3EByteVal|1||||
| |- Unknown1|O3EByteVal|1||||
|**438**|**MixerEightCircuitRoomTemperatureSetpoint**|*O3EComplexType*|9||**rw**||
| |- Comfort|O3EInt16|2||||
| |- Standard|O3EInt16|2||||
| |- Reduced|O3EInt16|2||||
| |- Increased|O3EInt16|2||||
| |- Duration|O3EByteVal|1||||
|**439**|**BypassAvailableModes**|O3EByteVal|1||ro||
|**449**|**ElectricalEnergyMatrix**|RawCodec|141||ro||
|**451**|**ExternalAlternatingCurrentPowerSetpoint**|RawCodec|4||**rw**||
|**475**|**MixerOneCircuitThreeWayValvePositionPercent**|*O3EComplexType*|2||ro||
| |- Setpoint|O3EInt8|1||||
| |- Actual|O3EInt8|1||||
|**476**|**MixerTwoCircuitThreeWayValvePositionPercent**|*O3EComplexType*|2||ro||
| |- Setpoint|O3EInt8|1||||
| |- Actual|O3EInt8|1||||
|**477**|**MixerThreeCircuitThreeWayValvePositionPercent**|*O3EComplexType*|2||ro||
| |- Setpoint|O3EInt8|1||||
| |- Actual|O3EInt8|1||||
|**478**|**MixerFourCircuitThreeWayValvePositionPercent**|*O3EComplexType*|2||ro||
| |- Setpoint|O3EInt8|1||||
| |- Actual|O3EInt8|1||||
|**491**|[**DomesticHotWaterCirculationPump**](## "Request for domestic hot water circulation pump")|*O3EComplexType*|2||**rw**||
| |- State|O3EByteVal|1||||
| |- Unknown|O3EByteVal|1||||
|**497**|[**DomesticHotWaterCirculationPumpMode**](## "Operation Mode of domestic hot water circulation pump")|*O3EComplexType*|5||**rw**|[See page 22f](https://static.viessmann-climatesolutions.com/resources/technical_documents/DE/de/VSA/6179923VSA00001_1.pdf?)|
| |- Mode|O3EByteVal|1||||
| |- HygenieActive|O3EByteVal|1||||
| |- HeatingActive|O3EByteVal|1||||
| |- CyclesPerHour|O3EByteVal|1||||
| |- Cycles|O3EByteVal|1||||
|**500**|**CentralHeatDemandExternalAc**|RawCodec|2||ro||
|**503**|**ScaldProtection**|RawCodec|2||ro||
|**504**|**DomesticHotWaterSetpointMetaData**|*O3EComplexType*|14||**rw**||
| |- LowerBufferLimitTemperature|O3EInt16|2||||
| |- MinimumBufferTemperature|O3EInt16|2||||
| |- DefaultBufferTemperature|O3EInt16|2||||
| |- MaximumBufferTemperature|O3EInt16|2||||
| |- UpperBufferLimitTemperature|O3EInt16|2||||
| |- EfficiencyLowerLimit|O3EInt16|2||||
| |- EfficiencyUpperLimit|O3EInt16|2||||
|**505**|**Date**|O3ESdate|3||ro||
|**506**|**Time**|O3EStime|3||ro||
|**507**|**UniversalTimeCoordinated**|O3EUtc|4||ro||
|**508**|**UniversalTimeCoordinatedOffset**|O3EByteVal|1||**rw**||
|**510**|**Language**|O3EByteVal|1||ro||
|**511**|**HolidayPhase**|*O3EComplexType*|8||ro||
| |- PhaseBegin|O3ESdate|3||||
| |- PhaseEnd|O3ESdate|3||||
| |- Planned|O3EByteVal|1||||
| |- Active|O3EByteVal|1||||
|**512**|**HolidayAtHomePhase**|*O3EComplexType*|8||ro||
| |- PhaseBegin|O3ESdate|3||||
| |- PhaseEnd|O3ESdate|3||||
| |- Planned|O3EByteVal|1||||
| |- Active|O3EByteVal|1||||
|**513**|**HolidayPhaseCircuitOne**|*O3EComplexType*|8||ro||
| |- PhaseBegin|O3ESdate|3||||
| |- PhaseEnd|O3ESdate|3||||
| |- Planned|O3EByteVal|1||||
| |- Active|O3EByteVal|1||||
|**514**|**HolidayAtHomePhaseCircuitOne**|*O3EComplexType*|8||ro||
| |- PhaseBegin|O3ESdate|3||||
| |- PhaseEnd|O3ESdate|3||||
| |- Planned|O3EByteVal|1||||
| |- Active|O3EByteVal|1||||
|**515**|**HolidayPhaseCircuitTwo**|*O3EComplexType*|8||ro||
| |- PhaseBegin|O3ESdate|3||||
| |- PhaseEnd|O3ESdate|3||||
| |- Planned|O3EByteVal|1||||
| |- Active|O3EByteVal|1||||
|**516**|**HolidayAtHomePhaseCircuitTwo**|*O3EComplexType*|8||ro||
| |- PhaseBegin|O3ESdate|3||||
| |- PhaseEnd|O3ESdate|3||||
| |- Planned|O3EByteVal|1||||
| |- Active|O3EByteVal|1||||
|**517**|**HolidayPhaseCircuitThree**|*O3EComplexType*|8||ro||
| |- PhaseBegin|O3ESdate|3||||
| |- PhaseEnd|O3ESdate|3||||
| |- Planned|O3EByteVal|1||||
| |- Active|O3EByteVal|1||||
|**518**|**HolidayAtHomePhaseCircuitThree**|*O3EComplexType*|8||ro||
| |- PhaseBegin|O3ESdate|3||||
| |- PhaseEnd|O3ESdate|3||||
| |- Planned|O3EByteVal|1||||
| |- Active|O3EByteVal|1||||
|**519**|**HolidayPhaseCircuitFour**|*O3EComplexType*|8||ro||
| |- PhaseBegin|O3ESdate|3||||
| |- PhaseEnd|O3ESdate|3||||
| |- Planned|O3EByteVal|1||||
| |- Active|O3EByteVal|1||||
|**520**|**HolidayAtHomePhaseCircuitFour**|*O3EComplexType*|8||ro||
| |- PhaseBegin|O3ESdate|3||||
| |- PhaseEnd|O3ESdate|3||||
| |- Planned|O3EByteVal|1||||
| |- Active|O3EByteVal|1||||
|**521**|**OperatingHoursTillService**|O3EInt16|2||ro||
|**522**|**ServiceDateNext**|*O3EComplexType*|4||ro||
| |- Date|O3ESdate|3||||
| |- Status|O3EByteVal|1||||
|**523**|**ServiceDateLast**|O3ESdate|3||ro||
|**524**|**ModulationTargetSetpoint**|O3EInt16|2||**rw**||
|**525**|**ExternalModulationSetpoint**|O3EInt16|2||**rw**||
|**526**|**ModulationCurrentValue**|O3EInt16|2||ro||
|**527**|**FlowTemperatureTargetSetpoint**|O3EInt16|2||**rw**||
|**528**|**ExternalTargetFlowTemperatureSetpoint**|O3EInt16|2||**rw**||
|**531**|[**DomesticHotWaterOperationState**](## "Operation state of domestic hot water preparation")|*O3EComplexType*|2||**rw**||
| |- Mode|O3EByteVal|1||||
| |- [State](## "{0: Off, 1: Hot water, 2: Parallel operation, 3: Chimney sweep, 4: Test mode, 5: External temperature setpoint, 6: External modulation setpoint, 7: Hygiene function, 8: Automatic}")|O3EEnum|1||||
|**533**|**VentilationTargetOperationLevel**|*O3EComplexType*|2||**rw**||
| |- Acutual|O3EByteVal|1||||
| |- Unknown1|O3EByteVal|1||||
|**534**|**DomesticHotWaterPumpPostRunTime**|RawCodec|2||ro||
|**535**|[**ObjectElectricalEnergyStatistical**](## "Cumulative Grid Energy Statistics")|*O3EComplexType*|12||ro|[Link](https://github.com/open3e/open3e/wiki/036-DoI-%E2%80%90-Data-points-of-Interest/#data-points-of-vx3)|
| |- GridFeedInEnergy|O3EInt32|4|kWh|||
| |- GridSuppliedEnergy|O3EInt32|4|kWh|||
| |- ProducedEnergy|O3EInt32|4|kWh|||
|**537**|**ExternalMixerOneCircuitTargetOperationMode**|*O3EComplexType*|2||**rw**||
| |- Mode|O3EByteVal|1||||
| |- State|O3EByteVal|1||||
|**538**|**ExternalDomesticHotWaterTargetOperationMode**|*O3EComplexType*|2||**rw**||
| |- Mode|O3EByteVal|1||||
| |- State|O3EByteVal|1||||
|**543**|**SmartGridReadyConsolidator**|*O3EComplexType*|4||ro||
| |- Unknown1|O3EByteVal|1||||
| |- OperatingStatus|O3EByteVal|1||||
| |- Unknown2|O3EByteVal|1||||
| |- Unknown3|O3EByteVal|1||||
|**544**|**GasConsumptionCentralHeating**|*O3EComplexType*|12||ro||
| |- Today|O3EInt16|2||||
| |- Past7Days|O3EInt16|2||||
| |- CurrentMonth|O3EInt16|2||||
| |- PastMonth|O3EInt16|2||||
| |- CurrentYear|O3EInt16|2||||
| |- PastYear|O3EInt16|2||||
|**545**|**GasConsumptionDomesticHotWater**|*O3EComplexType*|12||ro||
| |- Today|O3EInt16|2||||
| |- Past7Days|O3EInt16|2||||
| |- CurrentMonth|O3EInt16|2||||
| |- PastMonth|O3EInt16|2||||
| |- CurrentYear|O3EInt16|2||||
| |- PastYear|O3EInt16|2||||
|**548**|**EnergyConsumptionCentralHeating**|*O3EComplexType*|24||ro||
| |- Today|O3EInt32|4||||
| |- Past7Days|O3EInt32|4||||
| |- CurrentMonth|O3EInt32|4||||
| |- PastMonth|O3EInt32|4||||
| |- CurrentYear|O3EInt32|4||||
| |- PastYear|O3EInt32|4||||
|**565**|**EnergyConsumptionDomesticHotWater**|*O3EComplexType*|24||ro||
| |- Today|O3EInt32|4||||
| |- Past7Days|O3EInt32|4||||
| |- CurrentMonth|O3EInt32|4||||
| |- PastMonth|O3EInt32|4||||
| |- CurrentYear|O3EInt32|4||||
| |- PastYear|O3EInt32|4||||
|**566**|**EnergyConsumptionCooling**|*O3EComplexType*|24||ro||
| |- Today|O3EInt32|4||||
| |- Past7Days|O3EInt32|4||||
| |- CurrentMonth|O3EInt32|4||||
| |- PastMonth|O3EInt32|4||||
| |- CurrentYear|O3EInt32|4||||
| |- PastYear|O3EInt32|4||||
|**567**|**GeneratedElectricity**|*O3EComplexType*|24||ro||
| |- Today|O3EInt32|4||||
| |- Past7Days|O3EInt32|4||||
| |- CurrentMonth|O3EInt32|4||||
| |- PastMonth|O3EInt32|4||||
| |- CurrentYear|O3EInt32|4||||
| |- PastYear|O3EInt32|4||||
|**568**|**CoTwoSavings**|RawCodec|24||ro||
|**569**|**ResetSensorMinMaxAverageStatistics**|O3EByteVal|1||ro||
|**570**|**ResetStatistics**|RawCodec|1||ro||
|**572**|**SetDefaultValuesDate**|RawCodec|3||ro||
|**573**|**RemoteReset**|RawCodec|2||ro||
|**575**|**SetDeliveryStatus**|O3EByteVal|1||ro||
|**576**|**SetDeliveryStatusDate**|O3ESdate|3||ro||
|**580**|**SoftwareVersion**|O3ESoftVers|8||ro||
|**581**|**HardwareVersion**|O3ESoftVers|8||ro||
|**589**|**VentilationOperationHours**|O3EInt32|4||ro||
|**592**|**MacAddressLan**|O3EMacAddr|6||ro||
|**593**|**GatewayMac**|O3EMacAddr|6||ro||
|**596**|**CentralHeatingPartLoadPercent**|O3EByteVal|1||ro||
|**597**|**DomesticHotWaterPartLoadPercent**|O3EByteVal|1||ro||
|**600**|**FuelCellReset**|RawCodec|3||ro||
|**602**|**GatewayRemoteLocalNetworkStatus**|O3EByteVal|1||ro||
|**603**|**GatewayApEnable**|O3EByteVal|1||ro||
|**604**|**GatewayApDataSet**|*O3EComplexType*|76||ro||
| |- SSID_AccessPoint|O3EUtf8|32||||
| |- Password_AccessPoint|O3EUtf8|40||||
| |- IP-Address_AccessPoint|O3EIp4Addr|4||||
|**607**|**GatewayRemoteIp**|*O3EComplexType*|20||ro||
| |- WLAN_IP-Address|O3EIp4Addr|4||||
| |- SubnetMask|O3EIp4Addr|4||||
| |- Gateway_IP-Address|O3EIp4Addr|4||||
| |- DNSServer1|O3EIp4Addr|4||||
| |- DNSServer2|O3EIp4Addr|4||||
|**609**|**ProxyServer**|RawCodec|40||ro||
|**610**|**ProxyPort**|RawCodec|2||ro||
|**611**|**ProxyUser**|O3EUtf8|40||ro||
|**613**|**ProxyEnabled**|O3EByteVal|1||ro||
|**616**|**GatewayRemoteEnable**|O3EByteVal|1||ro||
|**617**|**GatewayRemoteSsid**|O3EUtf8|72||ro||
|**618**|**GatewayRemoteIpStatic**|O3EByteVal|1||ro||
|**619**|**GatewayRemoteScanNetwork**|RawCodec|2||ro||
|**620**|**DiagnosticServiceConnectionStatus**|O3EByteVal|1||ro||
|**621**|**ObjectContactDetails**|*O3EComplexType*|181||ro||
| |- Name|O3EUtf8|20||||
| |- PreName|O3EUtf8|15||||
| |- Street|O3EUtf8|20||||
| |- StreetExtension|O3EUtf8|10||||
| |- ZipCode|O3EUtf8|7||||
| |- Region|O3EUtf8|15||||
| |- City|O3EUtf8|15||||
| |- Phone|O3EUtf8|16||||
| |- Mobile|O3EUtf8|16||||
| |- Email|O3EUtf8|30||||
| |- [Country](## "{0: Germany, 1: Austria, 2: France, 3: UnitedKingdom, 4: Afghanistan, 5: Albania, 6: Algeria, 7: Andorra, 8: Angola, 9: Antigua and Barbuda, 10: Argentina, 11: Armenia, 12: Australia, 13: Azerbaijan, 14: Bahamas, 15: Bahrain, 16: Bangladesh, 17: Barbados, 18: Belarus, 19: Belgium, 20: Belize, 21: Benin, 22: Bhutan, 23: Bolivia, 24: Bosnia and Herzegovina, 25: Botswana, 26: Brazil, 27: Brunei Darussalam, 28: Bulgaria, 29: Burkina Faso, 30: Burundi, 31: Cabo Verde, 32: Cambodia, 33: Cameroon, 34: Canada, 35: Central African Republic, 36: Chad, 37: Chile, 38: China, 39: Colombia, 40: Comoros, 41: Congo, 42: Antarcitc, 43: Costa Rica, 44: IvoryCoast, 45: Croatia, 46: Cuba, 47: Cyprus, 48: Czechia, 49: Denmark, 50: Djibouti, 51: Dominica, 52: Dominican Republic, 53: Ecuador, 54: Egypt, 55: El Salvador, 56: Equatorial Guinea, 57: Eritrea, 58: Estonia, 59: Eswatini, 60: Ethiopia, 61: Fiji, 62: Finland, 63: Gabon, 64: Gambia, 65: Georgia, 66: Ghana, 67: Greece, 68: Grenada, 69: Guatemala, 70: Guinea, 71: Guinea-Bissau, 72: Guyana, 73: Haiti, 74: Holy See, 75: Honduras, 76: Hungary, 77: Iceland, 78: India, 79: Indonesia, 80: Iran, 81: Iraq, 82: Ireland, 83: Israel, 84: Italy, 85: Jamaica, 86: Japan, 87: Jordan, 88: Kazakhstan, 89: Kenya, 90: Kiribati, 91: NorthKorea, 92: Korea, 93: Kuwait, 94: Kyrgyzstan, 95: Lao People's Democratic Republic, 96: Latvia, 97: Lebanon, 98: Lesotho, 99: Liberia, 100: Libya, 101: Liechtenstein, 102: Lithuania, 103: Luxembourg, 104: Macedonia, 105: Madagascar, 106: Malawi, 107: Malaysia, 108: Maldives, 109: Mali, 110: Malta, 111: Marshall Islands, 112: Mauritania, 113: Mauritius, 114: Mexico, 115: Micronesia, 116: Moldova, 117: Monaco, 118: Mongolia, 119: Montenegro, 120: Morocco, 121: Mozambique, 122: Myanmar, 123: Namibia, 124: Nauru, 125: Nepal, 126: Netherlands, 127: New Zealand, 128: Nicaragua, 129: Niger, 130: Nigeria, 131: Norway, 132: Oman, 133: Pakistan, 134: Palau, 135: Panama, 136: Papua New Guinea, 137: Paraguay, 138: Peru, 139: Philippines, 140: Poland, 141: Portugal, 142: Qatar, 143: Romania, 144: Russian Federation, 145: Rwanda, 146: Saint Kitts and Nevis, 147: Saint Lucia, 148: Saint Vincent and the Grenadines, 149: Samoa, 150: San Marino, 151: Sao Tome and Principe, 152: Saudi Arabia, 153: Senegal, 154: Serbia, 155: Seychelles, 156: Sierra Leone, 157: Singapore, 158: Slovakia, 159: Slovenia, 160: Solomon Islands, 161: Somalia, 162: South Africa, 163: South Sudan, 164: Spain, 165: Sri Lanka, 166: Sudan, 167: Suriname, 168: Sweden, 169: Switzerland, 170: Syrian Arab Republic, 171: Tajikistan, 172: Tanzania, 173: Thailand, 174: TimorLeste, 175: Togo, 176: Tonga, 177: Trinidad and Tobago, 178: Tunisia, 179: Turkey, 180: Turkmenistan, 181: Tuvalu, 182: Uganda, 183: Ukraine, 184: United Arab Emirates, 185: United States of America, 186: Uruguay, 187: Uzbekistan, 188: Vanuatu, 189: Venezuela, 190: Viet Nam, 191: Yemen, 192: Zambia, 193: Zimbabwe}")|O3EEnum|1||||
| |- IdentificationNumber|O3EUtf8|16||||
|**622**|**CustomerDetails**|*O3EComplexType*|181||ro||
| |- Name|O3EUtf8|20||||
| |- PreName|O3EUtf8|15||||
| |- Street|O3EUtf8|20||||
| |- StreetExtension|O3EUtf8|10||||
| |- ZipCode|O3EUtf8|7||||
| |- Region|O3EUtf8|15||||
| |- City|O3EUtf8|15||||
| |- Phone|O3EUtf8|16||||
| |- Mobile|O3EUtf8|16||||
| |- Email|O3EUtf8|30||||
| |- [Country](## "{0: Germany, 1: Austria, 2: France, 3: UnitedKingdom, 4: Afghanistan, 5: Albania, 6: Algeria, 7: Andorra, 8: Angola, 9: Antigua and Barbuda, 10: Argentina, 11: Armenia, 12: Australia, 13: Azerbaijan, 14: Bahamas, 15: Bahrain, 16: Bangladesh, 17: Barbados, 18: Belarus, 19: Belgium, 20: Belize, 21: Benin, 22: Bhutan, 23: Bolivia, 24: Bosnia and Herzegovina, 25: Botswana, 26: Brazil, 27: Brunei Darussalam, 28: Bulgaria, 29: Burkina Faso, 30: Burundi, 31: Cabo Verde, 32: Cambodia, 33: Cameroon, 34: Canada, 35: Central African Republic, 36: Chad, 37: Chile, 38: China, 39: Colombia, 40: Comoros, 41: Congo, 42: Antarcitc, 43: Costa Rica, 44: IvoryCoast, 45: Croatia, 46: Cuba, 47: Cyprus, 48: Czechia, 49: Denmark, 50: Djibouti, 51: Dominica, 52: Dominican Republic, 53: Ecuador, 54: Egypt, 55: El Salvador, 56: Equatorial Guinea, 57: Eritrea, 58: Estonia, 59: Eswatini, 60: Ethiopia, 61: Fiji, 62: Finland, 63: Gabon, 64: Gambia, 65: Georgia, 66: Ghana, 67: Greece, 68: Grenada, 69: Guatemala, 70: Guinea, 71: Guinea-Bissau, 72: Guyana, 73: Haiti, 74: Holy See, 75: Honduras, 76: Hungary, 77: Iceland, 78: India, 79: Indonesia, 80: Iran, 81: Iraq, 82: Ireland, 83: Israel, 84: Italy, 85: Jamaica, 86: Japan, 87: Jordan, 88: Kazakhstan, 89: Kenya, 90: Kiribati, 91: NorthKorea, 92: Korea, 93: Kuwait, 94: Kyrgyzstan, 95: Lao People's Democratic Republic, 96: Latvia, 97: Lebanon, 98: Lesotho, 99: Liberia, 100: Libya, 101: Liechtenstein, 102: Lithuania, 103: Luxembourg, 104: Macedonia, 105: Madagascar, 106: Malawi, 107: Malaysia, 108: Maldives, 109: Mali, 110: Malta, 111: Marshall Islands, 112: Mauritania, 113: Mauritius, 114: Mexico, 115: Micronesia, 116: Moldova, 117: Monaco, 118: Mongolia, 119: Montenegro, 120: Morocco, 121: Mozambique, 122: Myanmar, 123: Namibia, 124: Nauru, 125: Nepal, 126: Netherlands, 127: New Zealand, 128: Nicaragua, 129: Niger, 130: Nigeria, 131: Norway, 132: Oman, 133: Pakistan, 134: Palau, 135: Panama, 136: Papua New Guinea, 137: Paraguay, 138: Peru, 139: Philippines, 140: Poland, 141: Portugal, 142: Qatar, 143: Romania, 144: Russian Federation, 145: Rwanda, 146: Saint Kitts and Nevis, 147: Saint Lucia, 148: Saint Vincent and the Grenadines, 149: Samoa, 150: San Marino, 151: Sao Tome and Principe, 152: Saudi Arabia, 153: Senegal, 154: Serbia, 155: Seychelles, 156: Sierra Leone, 157: Singapore, 158: Slovakia, 159: Slovenia, 160: Solomon Islands, 161: Somalia, 162: South Africa, 163: South Sudan, 164: Spain, 165: Sri Lanka, 166: Sudan, 167: Suriname, 168: Sweden, 169: Switzerland, 170: Syrian Arab Republic, 171: Tajikistan, 172: Tanzania, 173: Thailand, 174: TimorLeste, 175: Togo, 176: Tonga, 177: Trinidad and Tobago, 178: Tunisia, 179: Turkey, 180: Turkmenistan, 181: Tuvalu, 182: Uganda, 183: Ukraine, 184: United Arab Emirates, 185: United States of America, 186: Uruguay, 187: Uzbekistan, 188: Vanuatu, 189: Venezuela, 190: Viet Nam, 191: Yemen, 192: Zambia, 193: Zimbabwe}")|O3EEnum|1||||
| |- Identification Number|O3EUtf8|16||||
|**623**|**ServiceEngineer**|*O3EComplexType*|181||ro||
| |- Name|O3EUtf8|20||||
| |- PreName|O3EUtf8|15||||
| |- Street|O3EUtf8|20||||
| |- StreetExtension|O3EUtf8|10||||
| |- ZipCode|O3EUtf8|7||||
| |- Region|O3EUtf8|15||||
| |- City|O3EUtf8|15||||
| |- Phone|O3EUtf8|16||||
| |- Mobile|O3EUtf8|16||||
| |- Email|O3EUtf8|30||||
| |- [Country](## "{0: Germany, 1: Austria, 2: France, 3: UnitedKingdom, 4: Afghanistan, 5: Albania, 6: Algeria, 7: Andorra, 8: Angola, 9: Antigua and Barbuda, 10: Argentina, 11: Armenia, 12: Australia, 13: Azerbaijan, 14: Bahamas, 15: Bahrain, 16: Bangladesh, 17: Barbados, 18: Belarus, 19: Belgium, 20: Belize, 21: Benin, 22: Bhutan, 23: Bolivia, 24: Bosnia and Herzegovina, 25: Botswana, 26: Brazil, 27: Brunei Darussalam, 28: Bulgaria, 29: Burkina Faso, 30: Burundi, 31: Cabo Verde, 32: Cambodia, 33: Cameroon, 34: Canada, 35: Central African Republic, 36: Chad, 37: Chile, 38: China, 39: Colombia, 40: Comoros, 41: Congo, 42: Antarcitc, 43: Costa Rica, 44: IvoryCoast, 45: Croatia, 46: Cuba, 47: Cyprus, 48: Czechia, 49: Denmark, 50: Djibouti, 51: Dominica, 52: Dominican Republic, 53: Ecuador, 54: Egypt, 55: El Salvador, 56: Equatorial Guinea, 57: Eritrea, 58: Estonia, 59: Eswatini, 60: Ethiopia, 61: Fiji, 62: Finland, 63: Gabon, 64: Gambia, 65: Georgia, 66: Ghana, 67: Greece, 68: Grenada, 69: Guatemala, 70: Guinea, 71: Guinea-Bissau, 72: Guyana, 73: Haiti, 74: Holy See, 75: Honduras, 76: Hungary, 77: Iceland, 78: India, 79: Indonesia, 80: Iran, 81: Iraq, 82: Ireland, 83: Israel, 84: Italy, 85: Jamaica, 86: Japan, 87: Jordan, 88: Kazakhstan, 89: Kenya, 90: Kiribati, 91: NorthKorea, 92: Korea, 93: Kuwait, 94: Kyrgyzstan, 95: Lao People's Democratic Republic, 96: Latvia, 97: Lebanon, 98: Lesotho, 99: Liberia, 100: Libya, 101: Liechtenstein, 102: Lithuania, 103: Luxembourg, 104: Macedonia, 105: Madagascar, 106: Malawi, 107: Malaysia, 108: Maldives, 109: Mali, 110: Malta, 111: Marshall Islands, 112: Mauritania, 113: Mauritius, 114: Mexico, 115: Micronesia, 116: Moldova, 117: Monaco, 118: Mongolia, 119: Montenegro, 120: Morocco, 121: Mozambique, 122: Myanmar, 123: Namibia, 124: Nauru, 125: Nepal, 126: Netherlands, 127: New Zealand, 128: Nicaragua, 129: Niger, 130: Nigeria, 131: Norway, 132: Oman, 133: Pakistan, 134: Palau, 135: Panama, 136: Papua New Guinea, 137: Paraguay, 138: Peru, 139: Philippines, 140: Poland, 141: Portugal, 142: Qatar, 143: Romania, 144: Russian Federation, 145: Rwanda, 146: Saint Kitts and Nevis, 147: Saint Lucia, 148: Saint Vincent and the Grenadines, 149: Samoa, 150: San Marino, 151: Sao Tome and Principe, 152: Saudi Arabia, 153: Senegal, 154: Serbia, 155: Seychelles, 156: Sierra Leone, 157: Singapore, 158: Slovakia, 159: Slovenia, 160: Solomon Islands, 161: Somalia, 162: South Africa, 163: South Sudan, 164: Spain, 165: Sri Lanka, 166: Sudan, 167: Suriname, 168: Sweden, 169: Switzerland, 170: Syrian Arab Republic, 171: Tajikistan, 172: Tanzania, 173: Thailand, 174: TimorLeste, 175: Togo, 176: Tonga, 177: Trinidad and Tobago, 178: Tunisia, 179: Turkey, 180: Turkmenistan, 181: Tuvalu, 182: Uganda, 183: Ukraine, 184: United Arab Emirates, 185: United States of America, 186: Uruguay, 187: Uzbekistan, 188: Vanuatu, 189: Venezuela, 190: Viet Nam, 191: Yemen, 192: Zambia, 193: Zimbabwe}")|O3EEnum|1||||
| |- Identification Number|O3EUtf8|16||||
|**624**|**TechnicalSupport**|*O3EComplexType*|181||ro||
| |- Name|O3EUtf8|20||||
| |- PreName|O3EUtf8|15||||
| |- Street|O3EUtf8|20||||
| |- StreetExtension|O3EUtf8|10||||
| |- ZipCode|O3EUtf8|7||||
| |- Region|O3EUtf8|15||||
| |- City|O3EUtf8|15||||
| |- Phone|O3EUtf8|16||||
| |- Mobile|O3EUtf8|16||||
| |- Email|O3EUtf8|30||||
| |- [Country](## "{0: Germany, 1: Austria, 2: France, 3: UnitedKingdom, 4: Afghanistan, 5: Albania, 6: Algeria, 7: Andorra, 8: Angola, 9: Antigua and Barbuda, 10: Argentina, 11: Armenia, 12: Australia, 13: Azerbaijan, 14: Bahamas, 15: Bahrain, 16: Bangladesh, 17: Barbados, 18: Belarus, 19: Belgium, 20: Belize, 21: Benin, 22: Bhutan, 23: Bolivia, 24: Bosnia and Herzegovina, 25: Botswana, 26: Brazil, 27: Brunei Darussalam, 28: Bulgaria, 29: Burkina Faso, 30: Burundi, 31: Cabo Verde, 32: Cambodia, 33: Cameroon, 34: Canada, 35: Central African Republic, 36: Chad, 37: Chile, 38: China, 39: Colombia, 40: Comoros, 41: Congo, 42: Antarcitc, 43: Costa Rica, 44: IvoryCoast, 45: Croatia, 46: Cuba, 47: Cyprus, 48: Czechia, 49: Denmark, 50: Djibouti, 51: Dominica, 52: Dominican Republic, 53: Ecuador, 54: Egypt, 55: El Salvador, 56: Equatorial Guinea, 57: Eritrea, 58: Estonia, 59: Eswatini, 60: Ethiopia, 61: Fiji, 62: Finland, 63: Gabon, 64: Gambia, 65: Georgia, 66: Ghana, 67: Greece, 68: Grenada, 69: Guatemala, 70: Guinea, 71: Guinea-Bissau, 72: Guyana, 73: Haiti, 74: Holy See, 75: Honduras, 76: Hungary, 77: Iceland, 78: India, 79: Indonesia, 80: Iran, 81: Iraq, 82: Ireland, 83: Israel, 84: Italy, 85: Jamaica, 86: Japan, 87: Jordan, 88: Kazakhstan, 89: Kenya, 90: Kiribati, 91: NorthKorea, 92: Korea, 93: Kuwait, 94: Kyrgyzstan, 95: Lao People's Democratic Republic, 96: Latvia, 97: Lebanon, 98: Lesotho, 99: Liberia, 100: Libya, 101: Liechtenstein, 102: Lithuania, 103: Luxembourg, 104: Macedonia, 105: Madagascar, 106: Malawi, 107: Malaysia, 108: Maldives, 109: Mali, 110: Malta, 111: Marshall Islands, 112: Mauritania, 113: Mauritius, 114: Mexico, 115: Micronesia, 116: Moldova, 117: Monaco, 118: Mongolia, 119: Montenegro, 120: Morocco, 121: Mozambique, 122: Myanmar, 123: Namibia, 124: Nauru, 125: Nepal, 126: Netherlands, 127: New Zealand, 128: Nicaragua, 129: Niger, 130: Nigeria, 131: Norway, 132: Oman, 133: Pakistan, 134: Palau, 135: Panama, 136: Papua New Guinea, 137: Paraguay, 138: Peru, 139: Philippines, 140: Poland, 141: Portugal, 142: Qatar, 143: Romania, 144: Russian Federation, 145: Rwanda, 146: Saint Kitts and Nevis, 147: Saint Lucia, 148: Saint Vincent and the Grenadines, 149: Samoa, 150: San Marino, 151: Sao Tome and Principe, 152: Saudi Arabia, 153: Senegal, 154: Serbia, 155: Seychelles, 156: Sierra Leone, 157: Singapore, 158: Slovakia, 159: Slovenia, 160: Solomon Islands, 161: Somalia, 162: South Africa, 163: South Sudan, 164: Spain, 165: Sri Lanka, 166: Sudan, 167: Suriname, 168: Sweden, 169: Switzerland, 170: Syrian Arab Republic, 171: Tajikistan, 172: Tanzania, 173: Thailand, 174: TimorLeste, 175: Togo, 176: Tonga, 177: Trinidad and Tobago, 178: Tunisia, 179: Turkey, 180: Turkmenistan, 181: Tuvalu, 182: Uganda, 183: Ukraine, 184: United Arab Emirates, 185: United States of America, 186: Uruguay, 187: Uzbekistan, 188: Vanuatu, 189: Venezuela, 190: Viet Nam, 191: Yemen, 192: Zambia, 193: Zimbabwe}")|O3EEnum|1||||
| |- Identification Number|O3EUtf8|16||||
|**625**|**ObjectDetails**|*O3EComplexType*|26||ro||
| |- Latitude|O3EInt32|4||||
| |- Longitude|O3EInt32|4||||
| |- Altitude|O3EInt16|2||||
| |- OrientationHorizontally|O3EInt16|2||||
| |- OrientationVertically|O3EInt16|2||||
| |- HeatingLoadPerSquareMeterPerYear|O3EInt16|2||||
| |- CentralHeatingCylinderSize|O3EInt16|2||||
| |- DomesticHotWaterCylinderSize|O3EInt16|2||||
| |- BufferCylinderSize|O3EInt16|2||||
| |- InstallationRoomSize|O3EInt16|2||||
| |- NitrogenOxide|O3EInt16|2||||
|**627**|**CentralHeatingOneCircuitName**|O3EUtf8|40||ro||
|**627**|**CentralHeatingOneCircuitName**|O3EUtf8|12||ro||
|**628**|**CentralHeatingTwoCircuitName**|O3EUtf8|40||ro||
|**628**|**CentralHeatingTwoCircuitName**|O3EUtf8|12||ro||
|**629**|**CentralHeatingThreeCircuitName**|O3EUtf8|40||ro||
|**629**|**CentralHeatingThreeCircuitName**|O3EUtf8|12||ro||
|**630**|**CentralHeatingFourCircuitName**|O3EUtf8|40||ro||
|**630**|**CentralHeatingFourCircuitName**|O3EUtf8|12||ro||
|**631**|**CentralHeatingFiveCircuitName**|O3EUtf8|12||ro||
|**632**|**CentralHeatingSixCircuitName**|O3EUtf8|12||ro||
|**633**|**CentralHeatingSevenCircuitName**|O3EUtf8|12||ro||
|**634**|**CentralHeatingEightCircuitName**|O3EUtf8|12||ro||
|**645**|**GenericAnalogDigitalAccessoryOneModulFunction**|O3EByteVal|1||ro||
|**646**|**GenericAnalogDigitalAccessoryTwoModulFunction**|O3EByteVal|1||ro||
|**647**|**GenericAnalogDigitalAccessoryThreeModulFunction**|O3EByteVal|1||ro||
|**648**|**GenericAnalogDigitalAccessoryFourModulFunction**|O3EByteVal|1||ro||
|**649**|**GenericAnalogDigitalAccessoryFiveModulFunction**|O3EByteVal|1||ro||
|**650**|**GenericDigitalAccessoryOneModulFunction**|O3EByteVal|1||ro||
|**651**|**GenericDigitalAccessoryTwoModulFunction**|O3EByteVal|1||ro||
|**652**|**GenericDigitalAccessoryThreeModulFunction**|O3EByteVal|1||ro||
|**653**|**GenericDigitalAccessoryFourModulFunction**|O3EByteVal|1||ro||
|**654**|**GenericDigitalAccessoryFiveModulFunction**|O3EByteVal|1||ro||
|**680**|**EnergyMeter**|RawCodec|123||ro||
|**691**|**DomesticHotWaterTimeScheduleMonday**|*O3EList*|57||**rw**||
| |- Count|O3EByteVal|1||||
| |- Schedules|*O3EComplexType*|7||||
| |- - Start|O3EStime|2||||
| |- - Stop|O3EStime|2||||
| |- - Unknown|RawCodec|2||||
| |- - Mode|O3EByteVal|1||||
|**692**|**DomesticHotWaterTimeScheduleTuesday**|*O3EList*|57||**rw**||
| |- Count|O3EByteVal|1||||
| |- Schedules|*O3EComplexType*|7||||
| |- - Start|O3EStime|2||||
| |- - Stop|O3EStime|2||||
| |- - Unknown|RawCodec|2||||
| |- - Mode|O3EByteVal|1||||
|**693**|**DomesticHotWaterTimeScheduleWednesday**|*O3EList*|57||**rw**||
| |- Count|O3EByteVal|1||||
| |- Schedules|*O3EComplexType*|7||||
| |- - Start|O3EStime|2||||
| |- - Stop|O3EStime|2||||
| |- - Unknown|RawCodec|2||||
| |- - Mode|O3EByteVal|1||||
|**694**|**DomesticHotWaterTimeScheduleThursday**|*O3EList*|57||**rw**||
| |- Count|O3EByteVal|1||||
| |- Schedules|*O3EComplexType*|7||||
| |- - Start|O3EStime|2||||
| |- - Stop|O3EStime|2||||
| |- - Unknown|RawCodec|2||||
| |- - Mode|O3EByteVal|1||||
|**695**|**DomesticHotWaterTimeScheduleFriday**|*O3EList*|57||**rw**||
| |- Count|O3EByteVal|1||||
| |- Schedules|*O3EComplexType*|7||||
| |- - Start|O3EStime|2||||
| |- - Stop|O3EStime|2||||
| |- - Unknown|RawCodec|2||||
| |- - Mode|O3EByteVal|1||||
|**696**|**DomesticHotWaterTimeScheduleSaturday**|*O3EList*|57||**rw**||
| |- Count|O3EByteVal|1||||
| |- Schedules|*O3EComplexType*|7||||
| |- - Start|O3EStime|2||||
| |- - Stop|O3EStime|2||||
| |- - Unknown|RawCodec|2||||
| |- - Mode|O3EByteVal|1||||
|**697**|**DomesticHotWaterTimeScheduleSunday**|*O3EList*|57||**rw**||
| |- Count|O3EByteVal|1||||
| |- Schedules|*O3EComplexType*|7||||
| |- - Start|O3EStime|2||||
| |- - Stop|O3EStime|2||||
| |- - Unknown|RawCodec|2||||
| |- - Mode|O3EByteVal|1||||
|**726**|**DomesticHotWaterCirculationTimeScheduleMonday**|*O3EList*|57||**rw**||
| |- Count|O3EByteVal|1||||
| |- Schedules|*O3EComplexType*|7||||
| |- - Start|O3EStime|2||||
| |- - Stop|O3EStime|2||||
| |- - Unknown|RawCodec|2||||
| |- - Mode|O3EByteVal|1||||
|**727**|**DomesticHotWaterCirculationTimeScheduleTuesday**|*O3EList*|57||**rw**||
| |- Count|O3EByteVal|1||||
| |- Schedules|*O3EComplexType*|7||||
| |- - Start|O3EStime|2||||
| |- - Stop|O3EStime|2||||
| |- - Unknown|RawCodec|2||||
| |- - Mode|O3EByteVal|1||||
|**728**|**DomesticHotWaterCirculationTimeScheduleWednesday**|*O3EList*|57||**rw**||
| |- Count|O3EByteVal|1||||
| |- Schedules|*O3EComplexType*|7||||
| |- - Start|O3EStime|2||||
| |- - Stop|O3EStime|2||||
| |- - Unknown|RawCodec|2||||
| |- - Mode|O3EByteVal|1||||
|**729**|**DomesticHotWaterCirculationTimeScheduleThursday**|*O3EList*|57||**rw**||
| |- Count|O3EByteVal|1||||
| |- Schedules|*O3EComplexType*|7||||
| |- - Start|O3EStime|2||||
| |- - Stop|O3EStime|2||||
| |- - Unknown|RawCodec|2||||
| |- - Mode|O3EByteVal|1||||
|**730**|**DomesticHotWaterCirculationTimeScheduleFriday**|*O3EList*|57||**rw**||
| |- Count|O3EByteVal|1||||
| |- Schedules|*O3EComplexType*|7||||
| |- - Start|O3EStime|2||||
| |- - Stop|O3EStime|2||||
| |- - Unknown|RawCodec|2||||
| |- - Mode|O3EByteVal|1||||
|**731**|**DomesticHotWaterCirculationTimeScheduleSaturday**|*O3EList*|57||**rw**||
| |- Count|O3EByteVal|1||||
| |- Schedules|*O3EComplexType*|7||||
| |- - Start|O3EStime|2||||
| |- - Stop|O3EStime|2||||
| |- - Unknown|RawCodec|2||||
| |- - Mode|O3EByteVal|1||||
|**732**|**DomesticHotWaterCirculationTimeScheduleSunday**|*O3EList*|57||**rw**||
| |- Count|O3EByteVal|1||||
| |- Schedules|*O3EComplexType*|7||||
| |- - Start|O3EStime|2||||
| |- - Stop|O3EStime|2||||
| |- - Unknown|RawCodec|2||||
| |- - Mode|O3EByteVal|1||||
|**761**|**MixerOneCircuitTimeScheduleMonday**|*O3EList*|57||**rw**||
| |- Count|O3EByteVal|1||||
| |- Schedules|*O3EComplexType*|7||||
| |- - Start|O3EStime|2||||
| |- - Stop|O3EStime|2||||
| |- - Unknown|RawCodec|2||||
| |- - Mode|O3EByteVal|1||||
|**762**|**MixerOneCircuitTimeScheduleTuesday**|*O3EList*|57||**rw**||
| |- Count|O3EByteVal|1||||
| |- Schedules|*O3EComplexType*|7||||
| |- - Start|O3EStime|2||||
| |- - Stop|O3EStime|2||||
| |- - Unknown|RawCodec|2||||
| |- - Mode|O3EByteVal|1||||
|**763**|**MixerOneCircuitTimeScheduleWednesday**|*O3EList*|57||**rw**||
| |- Count|O3EByteVal|1||||
| |- Schedules|*O3EComplexType*|7||||
| |- - Start|O3EStime|2||||
| |- - Stop|O3EStime|2||||
| |- - Unknown|RawCodec|2||||
| |- - Mode|O3EByteVal|1||||
|**764**|**MixerOneCircuitTimeScheduleThursday**|*O3EList*|57||**rw**||
| |- Count|O3EByteVal|1||||
| |- Schedules|*O3EComplexType*|7||||
| |- - Start|O3EStime|2||||
| |- - Stop|O3EStime|2||||
| |- - Unknown|RawCodec|2||||
| |- - Mode|O3EByteVal|1||||
|**765**|**MixerOneCircuitTimeScheduleFriday**|*O3EList*|57||**rw**||
| |- Count|O3EByteVal|1||||
| |- Schedules|*O3EComplexType*|7||||
| |- - Start|O3EStime|2||||
| |- - Stop|O3EStime|2||||
| |- - Unknown|RawCodec|2||||
| |- - Mode|O3EByteVal|1||||
|**766**|**MixerOneCircuitTimeScheduleSaturday**|*O3EList*|57||**rw**||
| |- Count|O3EByteVal|1||||
| |- Schedules|*O3EComplexType*|7||||
| |- - Start|O3EStime|2||||
| |- - Stop|O3EStime|2||||
| |- - Unknown|RawCodec|2||||
| |- - Mode|O3EByteVal|1||||
|**767**|**MixerOneCircuitTimeScheduleSunday**|*O3EList*|57||**rw**||
| |- Count|O3EByteVal|1||||
| |- Schedules|*O3EComplexType*|7||||
| |- - Start|O3EStime|2||||
| |- - Stop|O3EStime|2||||
| |- - Unknown|RawCodec|2||||
| |- - Mode|O3EByteVal|1||||
|**768**|**MixerTwoCircuitTimeScheduleMonday**|*O3EList*|57||**rw**||
| |- Count|O3EByteVal|1||||
| |- Schedules|*O3EComplexType*|7||||
| |- - Start|O3EStime|2||||
| |- - Stop|O3EStime|2||||
| |- - Unknown|RawCodec|2||||
| |- - Mode|O3EByteVal|1||||
|**769**|**MixerTwoCircuitTimeScheduleTuesday**|*O3EList*|57||**rw**||
| |- Count|O3EByteVal|1||||
| |- Schedules|*O3EComplexType*|7||||
| |- - Start|O3EStime|2||||
| |- - Stop|O3EStime|2||||
| |- - Unknown|RawCodec|2||||
| |- - Mode|O3EByteVal|1||||
|**770**|**MixerTwoCircuitTimeScheduleWednesday**|*O3EList*|57||**rw**||
| |- Count|O3EByteVal|1||||
| |- Schedules|*O3EComplexType*|7||||
| |- - Start|O3EStime|2||||
| |- - Stop|O3EStime|2||||
| |- - Unknown|RawCodec|2||||
| |- - Mode|O3EByteVal|1||||
|**771**|**MixerTwoCircuitTimeScheduleThursday**|*O3EList*|57||**rw**||
| |- Count|O3EByteVal|1||||
| |- Schedules|*O3EComplexType*|7||||
| |- - Start|O3EStime|2||||
| |- - Stop|O3EStime|2||||
| |- - Unknown|RawCodec|2||||
| |- - Mode|O3EByteVal|1||||
|**772**|**MixerTwoCircuitTimeScheduleFriday**|*O3EList*|57||**rw**||
| |- Count|O3EByteVal|1||||
| |- Schedules|*O3EComplexType*|7||||
| |- - Start|O3EStime|2||||
| |- - Stop|O3EStime|2||||
| |- - Unknown|RawCodec|2||||
| |- - Mode|O3EByteVal|1||||
|**773**|**MixerTwoCircuitTimeScheduleSaturday**|*O3EList*|57||**rw**||
| |- Count|O3EByteVal|1||||
| |- Schedules|*O3EComplexType*|7||||
| |- - Start|O3EStime|2||||
| |- - Stop|O3EStime|2||||
| |- - Unknown|RawCodec|2||||
| |- - Mode|O3EByteVal|1||||
|**774**|**MixerTwoCircuitTimeScheduleSunday**|*O3EList*|57||**rw**||
| |- Count|O3EByteVal|1||||
| |- Schedules|*O3EComplexType*|7||||
| |- - Start|O3EStime|2||||
| |- - Stop|O3EStime|2||||
| |- - Unknown|RawCodec|2||||
| |- - Mode|O3EByteVal|1||||
|**775**|**MixerThreeCircuitTimeScheduleMonday**|*O3EList*|57||**rw**||
| |- Count|O3EByteVal|1||||
| |- Schedules|*O3EComplexType*|7||||
| |- - Start|O3EStime|2||||
| |- - Stop|O3EStime|2||||
| |- - Unknown|RawCodec|2||||
| |- - Mode|O3EByteVal|1||||
|**776**|**MixerThreeCircuitTimeScheduleTuesday**|*O3EList*|57||**rw**||
| |- Count|O3EByteVal|1||||
| |- Schedules|*O3EComplexType*|7||||
| |- - Start|O3EStime|2||||
| |- - Stop|O3EStime|2||||
| |- - Unknown|RawCodec|2||||
| |- - Mode|O3EByteVal|1||||
|**777**|**MixerThreeCircuitTimeScheduleWednesday**|*O3EList*|57||**rw**||
| |- Count|O3EByteVal|1||||
| |- Schedules|*O3EComplexType*|7||||
| |- - Start|O3EStime|2||||
| |- - Stop|O3EStime|2||||
| |- - Unknown|RawCodec|2||||
| |- - Mode|O3EByteVal|1||||
|**778**|**MixerThreeCircuitTimeScheduleThursday**|*O3EList*|57||**rw**||
| |- Count|O3EByteVal|1||||
| |- Schedules|*O3EComplexType*|7||||
| |- - Start|O3EStime|2||||
| |- - Stop|O3EStime|2||||
| |- - Unknown|RawCodec|2||||
| |- - Mode|O3EByteVal|1||||
|**779**|**MixerThreeCircuitTimeScheduleFriday**|*O3EList*|57||**rw**||
| |- Count|O3EByteVal|1||||
| |- Schedules|*O3EComplexType*|7||||
| |- - Start|O3EStime|2||||
| |- - Stop|O3EStime|2||||
| |- - Unknown|RawCodec|2||||
| |- - Mode|O3EByteVal|1||||
|**780**|**MixerThreeCircuitTimeScheduleSaturday**|*O3EList*|57||**rw**||
| |- Count|O3EByteVal|1||||
| |- Schedules|*O3EComplexType*|7||||
| |- - Start|O3EStime|2||||
| |- - Stop|O3EStime|2||||
| |- - Unknown|RawCodec|2||||
| |- - Mode|O3EByteVal|1||||
|**781**|**MixerThreeCircuitTimeScheduleSunday**|*O3EList*|57||**rw**||
| |- Count|O3EByteVal|1||||
| |- Schedules|*O3EComplexType*|7||||
| |- - Start|O3EStime|2||||
| |- - Stop|O3EStime|2||||
| |- - Unknown|RawCodec|2||||
| |- - Mode|O3EByteVal|1||||
|**782**|**MixerFourCircuitTimeScheduleMonday**|*O3EList*|57||**rw**||
| |- Count|O3EByteVal|1||||
| |- Schedules|*O3EComplexType*|7||||
| |- - Start|O3EStime|2||||
| |- - Stop|O3EStime|2||||
| |- - Unknown|RawCodec|2||||
| |- - Mode|O3EByteVal|1||||
|**783**|**MixerFourCircuitTimeScheduleTuesday**|*O3EList*|57||**rw**||
| |- Count|O3EByteVal|1||||
| |- Schedules|*O3EComplexType*|7||||
| |- - Start|O3EStime|2||||
| |- - Stop|O3EStime|2||||
| |- - Unknown|RawCodec|2||||
| |- - Mode|O3EByteVal|1||||
|**784**|**MixerFourCircuitTimeScheduleWednesday**|*O3EList*|57||**rw**||
| |- Count|O3EByteVal|1||||
| |- Schedules|*O3EComplexType*|7||||
| |- - Start|O3EStime|2||||
| |- - Stop|O3EStime|2||||
| |- - Unknown|RawCodec|2||||
| |- - Mode|O3EByteVal|1||||
|**785**|**MixerFourCircuitTimeScheduleThursday**|*O3EList*|57||**rw**||
| |- Count|O3EByteVal|1||||
| |- Schedules|*O3EComplexType*|7||||
| |- - Start|O3EStime|2||||
| |- - Stop|O3EStime|2||||
| |- - Unknown|RawCodec|2||||
| |- - Mode|O3EByteVal|1||||
|**786**|**MixerFourCircuitTimeScheduleFriday**|*O3EList*|57||**rw**||
| |- Count|O3EByteVal|1||||
| |- Schedules|*O3EComplexType*|7||||
| |- - Start|O3EStime|2||||
| |- - Stop|O3EStime|2||||
| |- - Unknown|RawCodec|2||||
| |- - Mode|O3EByteVal|1||||
|**787**|**MixerFourCircuitTimeScheduleSaturday**|*O3EList*|57||**rw**||
| |- Count|O3EByteVal|1||||
| |- Schedules|*O3EComplexType*|7||||
| |- - Start|O3EStime|2||||
| |- - Stop|O3EStime|2||||
| |- - Unknown|RawCodec|2||||
| |- - Mode|O3EByteVal|1||||
|**788**|**MixerFourCircuitTimeScheduleSunday**|*O3EList*|57||**rw**||
| |- Count|O3EByteVal|1||||
| |- Schedules|*O3EComplexType*|7||||
| |- - Start|O3EStime|2||||
| |- - Stop|O3EStime|2||||
| |- - Unknown|RawCodec|2||||
| |- - Mode|O3EByteVal|1||||
|**873**|**LegionellaProtectionActivation**|*O3EComplexType*|2||ro||
| |- Mode|O3EByteVal|1||||
| |- State|O3EByteVal|1||||
|**874**|**LegionellaProtectionTargetTemperatureSetpoint**|*O3EComplexType*|3||**rw**||
| |- Setpoint|O3EInt16|2||||
| |- Unknown|RawCodec|1||||
|**875**|**LegionellaProtectionStartTime**|O3EStime|2||ro||
|**876**|**LegionellaProtectionWeekday**|O3EByteVal|1||ro||
|**877**|**LegionellaProtectionLastSuccessfulStartTime**|O3EStime|3||ro||
|**878**|**LegionellaProtectionLastSuccessfulWeekday**|O3EByteVal|1||ro||
|**880**|**MixerOneCircuitCentralHeatingCurve**|*O3EComplexType*|4||ro||
| |- Gradient|O3EInt8|1||||
| |- Level|O3EInt8|1||||
| |- BasePoint|O3EInt16|2||||
|**881**|**MixerTwoCircuitCentralHeatingCurve**|*O3EComplexType*|4||ro||
| |- Gradient|O3EInt8|1||||
| |- Level|O3EInt8|1||||
| |- BasePoint|O3EInt16|2||||
|**882**|**MixerThreeCircuitCentralHeatingCurve**|*O3EComplexType*|4||ro||
| |- Gradient|O3EInt8|1||||
| |- Level|O3EInt8|1||||
| |- BasePoint|O3EInt16|2||||
|**883**|**MixerFourCircuitCentralHeatingCurve**|*O3EComplexType*|4||ro||
| |- Gradient|O3EInt8|1||||
| |- Level|O3EInt8|1||||
| |- BasePoint|O3EInt16|2||||
|**884**|**MixerFiveCircuitCentralHeatingCurve**|*O3EComplexType*|4||ro||
| |- Gradient|O3EInt8|1||||
| |- Level|O3EInt8|1||||
| |- BasePoint|O3EInt16|2||||
|**885**|**MixerSixCircuitCentralHeatingCurve**|*O3EComplexType*|4||ro||
| |- Gradient|O3EInt8|1||||
| |- Level|O3EInt8|1||||
| |- BasePoint|O3EInt16|2||||
|**886**|**MixerSevenCircuitCentralHeatingCurve**|*O3EComplexType*|4||ro||
| |- Gradient|O3EInt8|1||||
| |- Level|O3EInt8|1||||
| |- BasePoint|O3EInt16|2||||
|**887**|**MixerEightCircuitCentralHeatingCurve**|*O3EComplexType*|4||ro||
| |- Gradient|O3EInt8|1||||
| |- Level|O3EInt8|1||||
| |- BasePoint|O3EInt16|2||||
|**896**|**OutsideTemperatureOffset**|O3EInt16|2||**rw**||
|**897**|**ScreedDryingProfileActivation**|O3EByteVal|1||ro||
|**898**|**RemainingFloorDryingDays**|O3EByteVal|1||ro||
|**900**|**GatewayRemoteSignalStrength**|O3EByteVal|1||ro||
|**901**|**ServiceManagerIsRequired**|O3EByteVal|1||ro||
|**902**|[**MalfunctionIdentification**](## "Indicates whether faults are present")|O3EByteVal|1||ro||
|**903**|**DisplaySettings**|RawCodec|4||ro||
|**905**|**ElectricalPostHeater**|RawCodec|4||ro||
|**906**|**ExhaustFlap**|RawCodec|3||ro||
|**907**|**UserInterfaceDefaultHomeScreen**|O3EByteVal|1||ro||
|**908**|**ExternalFaultSignal**|O3EByteVal|1||ro||
|**909**|**ExternalFaultSignalInput**|O3EByteVal|1||ro||
|**912**|**DaylightSavingTimeActive**|RawCodec|5||ro||
|**915**|**LastBackupDate**|O3ESdate|3||ro||
|**917**|**RemoteWeatherService**|RawCodec|20||ro||
|**918**|**TradeFairMode**|O3EByteVal|1||ro||
|**919**|**OutsideTemperatureDampingFactor**|O3EInt16|2||ro||
|**920**|**ThreeAxisAccelerationSensor**|RawCodec|36||ro||
|**921**|**ExternalAccessInProgress**|*O3EComplexType*|2||ro||
| |- Mode|O3EByteVal|1||||
| |- State|O3EByteVal|1||||
|**922**|**ProductionTraceabilityByte**|O3EInt16|2||ro||
|**923**|**RealTimeClockStatus**|RawCodec|8||ro||
|**924**|**StartUpWizard**|O3EByteVal|1||ro||
|**925**|**FillingVenting**|RawCodec|5||ro||
|**927**|[**BuildingType**](## "Type of building {0: OneFamily, 1: MultiFamilyOnlyHeating, 2: MultiFamilyHeatingDomesticHotWater, 3: TownHouse}")|O3EEnum|1||ro||
|**928**|**ElectronicTraceabilityNumber**|O3EUtf8|16||ro||
|**929**|[**GasType**](## "{1: LLGas, 2: EGas, 3: LiquidGas}")|O3EEnum|1||ro||
|**930**|**ExternalTargetCentralHeatingFlowSetpointMetaData**|RawCodec|10||**rw**||
|**931**|**DomesticHotWaterFlowSetpointMetaData**|RawCodec|10||**rw**||
|**933**|**MixerOneCircuitProperty**|*O3EComplexType*|9||ro||
| |- [MixerCircuitType](## "{0: NormalCentralHeating, 1: UnderFloorCentralHeating, 2: SwimmingPool, 3: Baseboard, 4: Radiator, 5: RadiantUnderfloorHeating, 6: Snowmelt, 7: AirHandler, 8: FanCoil}")|O3EEnum|1||||
| |- [BusType](## "{0: OwnBus, 1: PlusBus, 2: CanInternal, 3: CanExternal, 4: InternalUart, 5: Zigbee, 6: CanRaw, 7: Unkown, 8: ModBus, 9: EEBUS, 10: PlusBusTwo, 11: ISquaredCBus, 12: HEMS_Bus, 13: TL_SolarLogBus, 14: ServiceBus}")|O3EEnum|1||||
| |- [RemoteControl](## "{0: Nothing, 48: RemoteControlOne, 49: RemoteControlTwo, 50: RemoteControlThree, 51: RemoteControlFour}")|O3EEnum|1||||
| |- [Priority](## "{0: Off, 1: DomesticHotWater}")|O3EEnum|1||||
| |- BusAddress|O3EByteVal|1||||
| |- FlowTemperatureOffset|O3EInt16|2||||
| |- [RegulationType](## "{0: Nothing, 1: ConstantControlled, 4: WeatherByOutsideSensorControlled, 7: WeatherByOutsideSensorAndRoomCorrectionControlled, 10: ConstantControlledWithExternalThermostat, 13: WeatherByOutsideAndZones, 15: WeatherByOutsideSensorAndAutomaticAdaptationControlled}")|O3EEnum|1||||
| |- RoomTemperatureCorrectionFactor|O3EByteVal|1||||
|**934**|**MixerTwoCircuitProperty**|*O3EComplexType*|9||ro||
| |- [MixerCircuitType](## "{0: NormalCentralHeating, 1: UnderFloorCentralHeating, 2: SwimmingPool, 3: Baseboard, 4: Radiator, 5: RadiantUnderfloorHeating, 6: Snowmelt, 7: AirHandler, 8: FanCoil}")|O3EEnum|1||||
| |- [BusType](## "{0: OwnBus, 1: PlusBus, 2: CanInternal, 3: CanExternal, 4: InternalUart, 5: Zigbee, 6: CanRaw, 7: Unkown, 8: ModBus, 9: EEBUS, 10: PlusBusTwo, 11: ISquaredCBus, 12: HEMS_Bus, 13: TL_SolarLogBus, 14: ServiceBus}")|O3EEnum|1||||
| |- [RemoteControl](## "{0: Nothing, 48: RemoteControlOne, 49: RemoteControlTwo, 50: RemoteControlThree, 51: RemoteControlFour}")|O3EEnum|1||||
| |- [Priority](## "{0: Off, 1: DomesticHotWater}")|O3EEnum|1||||
| |- BusAddress|O3EByteVal|1||||
| |- FlowTemperatureOffset|O3EInt16|2||||
| |- [RegulationType](## "{0: Nothing, 1: ConstantControlled, 4: WeatherByOutsideSensorControlled, 7: WeatherByOutsideSensorAndRoomCorrectionControlled, 10: ConstantControlledWithExternalThermostat, 13: WeatherByOutsideAndZones, 15: WeatherByOutsideSensorAndAutomaticAdaptationControlled}")|O3EEnum|1||||
| |- RoomTemperatureCorrectionFactor|O3EByteVal|1||||
|**935**|**MixerThreeCircuitProperty**|*O3EComplexType*|9||ro||
| |- [MixerCircuitType](## "{0: NormalCentralHeating, 1: UnderFloorCentralHeating, 2: SwimmingPool, 3: Baseboard, 4: Radiator, 5: RadiantUnderfloorHeating, 6: Snowmelt, 7: AirHandler, 8: FanCoil}")|O3EEnum|1||||
| |- [BusType](## "{0: OwnBus, 1: PlusBus, 2: CanInternal, 3: CanExternal, 4: InternalUart, 5: Zigbee, 6: CanRaw, 7: Unkown, 8: ModBus, 9: EEBUS, 10: PlusBusTwo, 11: ISquaredCBus, 12: HEMS_Bus, 13: TL_SolarLogBus, 14: ServiceBus}")|O3EEnum|1||||
| |- [RemoteControl](## "{0: Nothing, 48: RemoteControlOne, 49: RemoteControlTwo, 50: RemoteControlThree, 51: RemoteControlFour}")|O3EEnum|1||||
| |- [Priority](## "{0: Off, 1: DomesticHotWater}")|O3EEnum|1||||
| |- BusAddress|O3EByteVal|1||||
| |- FlowTemperatureOffset|O3EInt16|2||||
| |- [RegulationType](## "{0: Nothing, 1: ConstantControlled, 4: WeatherByOutsideSensorControlled, 7: WeatherByOutsideSensorAndRoomCorrectionControlled, 10: ConstantControlledWithExternalThermostat, 13: WeatherByOutsideAndZones, 15: WeatherByOutsideSensorAndAutomaticAdaptationControlled}")|O3EEnum|1||||
| |- RoomTemperatureCorrectionFactor|O3EByteVal|1||||
|**936**|**MixerFourCircuitProperty**|*O3EComplexType*|9||ro||
| |- [MixerCircuitType](## "{0: NormalCentralHeating, 1: UnderFloorCentralHeating, 2: SwimmingPool, 3: Baseboard, 4: Radiator, 5: RadiantUnderfloorHeating, 6: Snowmelt, 7: AirHandler, 8: FanCoil}")|O3EEnum|1||||
| |- [BusType](## "{0: OwnBus, 1: PlusBus, 2: CanInternal, 3: CanExternal, 4: InternalUart, 5: Zigbee, 6: CanRaw, 7: Unkown, 8: ModBus, 9: EEBUS, 10: PlusBusTwo, 11: ISquaredCBus, 12: HEMS_Bus, 13: TL_SolarLogBus, 14: ServiceBus}")|O3EEnum|1||||
| |- [RemoteControl](## "{0: Nothing, 48: RemoteControlOne, 49: RemoteControlTwo, 50: RemoteControlThree, 51: RemoteControlFour}")|O3EEnum|1||||
| |- [Priority](## "{0: Off, 1: DomesticHotWater}")|O3EEnum|1||||
| |- BusAddress|O3EByteVal|1||||
| |- FlowTemperatureOffset|O3EInt16|2||||
| |- [RegulationType](## "{0: Nothing, 1: ConstantControlled, 4: WeatherByOutsideSensorControlled, 7: WeatherByOutsideSensorAndRoomCorrectionControlled, 10: ConstantControlledWithExternalThermostat, 13: WeatherByOutsideAndZones, 15: WeatherByOutsideSensorAndAutomaticAdaptationControlled}")|O3EEnum|1||||
| |- RoomTemperatureCorrectionFactor|O3EByteVal|1||||
|**937**|**MixerFiveCircuitProperty**|*O3EComplexType*|9||ro||
| |- [MixerCircuitType](## "{0: NormalCentralHeating, 1: UnderFloorCentralHeating, 2: SwimmingPool, 3: Baseboard, 4: Radiator, 5: RadiantUnderfloorHeating, 6: Snowmelt, 7: AirHandler, 8: FanCoil}")|O3EEnum|1||||
| |- [BusType](## "{0: OwnBus, 1: PlusBus, 2: CanInternal, 3: CanExternal, 4: InternalUart, 5: Zigbee, 6: CanRaw, 7: Unkown, 8: ModBus, 9: EEBUS, 10: PlusBusTwo, 11: ISquaredCBus, 12: HEMS_Bus, 13: TL_SolarLogBus, 14: ServiceBus}")|O3EEnum|1||||
| |- [RemoteControl](## "{0: Nothing, 48: RemoteControlOne, 49: RemoteControlTwo, 50: RemoteControlThree, 51: RemoteControlFour}")|O3EEnum|1||||
| |- [Priority](## "{0: Off, 1: DomesticHotWater}")|O3EEnum|1||||
| |- BusAddress|O3EByteVal|1||||
| |- FlowTemperatureOffset|O3EInt16|2||||
| |- [RegulationType](## "{0: Nothing, 1: ConstantControlled, 4: WeatherByOutsideSensorControlled, 7: WeatherByOutsideSensorAndRoomCorrectionControlled, 10: ConstantControlledWithExternalThermostat, 13: WeatherByOutsideAndZones, 15: WeatherByOutsideSensorAndAutomaticAdaptationControlled}")|O3EEnum|1||||
| |- RoomTemperatureCorrectionFactor|O3EByteVal|1||||
|**938**|**MixerSixCircuitProperty**|*O3EComplexType*|9||ro||
| |- [MixerCircuitType](## "{0: NormalCentralHeating, 1: UnderFloorCentralHeating, 2: SwimmingPool, 3: Baseboard, 4: Radiator, 5: RadiantUnderfloorHeating, 6: Snowmelt, 7: AirHandler, 8: FanCoil}")|O3EEnum|1||||
| |- [BusType](## "{0: OwnBus, 1: PlusBus, 2: CanInternal, 3: CanExternal, 4: InternalUart, 5: Zigbee, 6: CanRaw, 7: Unkown, 8: ModBus, 9: EEBUS, 10: PlusBusTwo, 11: ISquaredCBus, 12: HEMS_Bus, 13: TL_SolarLogBus, 14: ServiceBus}")|O3EEnum|1||||
| |- [RemoteControl](## "{0: Nothing, 48: RemoteControlOne, 49: RemoteControlTwo, 50: RemoteControlThree, 51: RemoteControlFour}")|O3EEnum|1||||
| |- [Priority](## "{0: Off, 1: DomesticHotWater}")|O3EEnum|1||||
| |- BusAddress|O3EByteVal|1||||
| |- FlowTemperatureOffset|O3EInt16|2||||
| |- [RegulationType](## "{0: Nothing, 1: ConstantControlled, 4: WeatherByOutsideSensorControlled, 7: WeatherByOutsideSensorAndRoomCorrectionControlled, 10: ConstantControlledWithExternalThermostat, 13: WeatherByOutsideAndZones, 15: WeatherByOutsideSensorAndAutomaticAdaptationControlled}")|O3EEnum|1||||
| |- RoomTemperatureCorrectionFactor|O3EByteVal|1||||
|**939**|**MixerSevenCircuitProperty**|*O3EComplexType*|9||ro||
| |- [MixerCircuitType](## "{0: NormalCentralHeating, 1: UnderFloorCentralHeating, 2: SwimmingPool, 3: Baseboard, 4: Radiator, 5: RadiantUnderfloorHeating, 6: Snowmelt, 7: AirHandler, 8: FanCoil}")|O3EEnum|1||||
| |- [BusType](## "{0: OwnBus, 1: PlusBus, 2: CanInternal, 3: CanExternal, 4: InternalUart, 5: Zigbee, 6: CanRaw, 7: Unkown, 8: ModBus, 9: EEBUS, 10: PlusBusTwo, 11: ISquaredCBus, 12: HEMS_Bus, 13: TL_SolarLogBus, 14: ServiceBus}")|O3EEnum|1||||
| |- [RemoteControl](## "{0: Nothing, 48: RemoteControlOne, 49: RemoteControlTwo, 50: RemoteControlThree, 51: RemoteControlFour}")|O3EEnum|1||||
| |- [Priority](## "{0: Off, 1: DomesticHotWater}")|O3EEnum|1||||
| |- BusAddress|O3EByteVal|1||||
| |- FlowTemperatureOffset|O3EInt16|2||||
| |- [RegulationType](## "{0: Nothing, 1: ConstantControlled, 4: WeatherByOutsideSensorControlled, 7: WeatherByOutsideSensorAndRoomCorrectionControlled, 10: ConstantControlledWithExternalThermostat, 13: WeatherByOutsideAndZones, 15: WeatherByOutsideSensorAndAutomaticAdaptationControlled}")|O3EEnum|1||||
| |- RoomTemperatureCorrectionFactor|O3EByteVal|1||||
|**940**|**MixerEightCircuitProperty**|*O3EComplexType*|9||ro||
| |- [MixerCircuitType](## "{0: NormalCentralHeating, 1: UnderFloorCentralHeating, 2: SwimmingPool, 3: Baseboard, 4: Radiator, 5: RadiantUnderfloorHeating, 6: Snowmelt, 7: AirHandler, 8: FanCoil}")|O3EEnum|1||||
| |- [BusType](## "{0: OwnBus, 1: PlusBus, 2: CanInternal, 3: CanExternal, 4: InternalUart, 5: Zigbee, 6: CanRaw, 7: Unkown, 8: ModBus, 9: EEBUS, 10: PlusBusTwo, 11: ISquaredCBus, 12: HEMS_Bus, 13: TL_SolarLogBus, 14: ServiceBus}")|O3EEnum|1||||
| |- [RemoteControl](## "{0: Nothing, 48: RemoteControlOne, 49: RemoteControlTwo, 50: RemoteControlThree, 51: RemoteControlFour}")|O3EEnum|1||||
| |- [Priority](## "{0: Off, 1: DomesticHotWater}")|O3EEnum|1||||
| |- BusAddress|O3EByteVal|1||||
| |- FlowTemperatureOffset|O3EInt16|2||||
| |- [RegulationType](## "{0: Nothing, 1: ConstantControlled, 4: WeatherByOutsideSensorControlled, 7: WeatherByOutsideSensorAndRoomCorrectionControlled, 10: ConstantControlledWithExternalThermostat, 13: WeatherByOutsideAndZones, 15: WeatherByOutsideSensorAndAutomaticAdaptationControlled}")|O3EEnum|1||||
| |- RoomTemperatureCorrectionFactor|O3EByteVal|1||||
|**950**|**SolarCircuitWaterFlowRate**|*O3EComplexType*|4||ro||
| |- FlowRate|O3EInt8|1||||
| |- Unknown|RawCodec|3||||
|**951**|**SolarCircuitExtendedFunctions**|RawCodec|8||ro||
|**952**|**HydraulicMatrix**|RawCodec|51||ro||
|**953**|**SolarEnergyYield**|RawCodec|24||ro||
|**954**|[**BusTopologyMatrix**](## "Matrix of CAN bus topology")|*O3EList*|181||ro||
| |- [Count](## "Number of list entries")|O3EInt8|1||||
| |- TopologyElement|*O3EComplexType*|36||||
| |- - NodeID|O3EByteVal|1||||
| |- - [BusType](## "{0: OwnBus, 1: PlusBus, 2: CanInternal, 3: CanExternal, 4: InternalUart, 5: Zigbee, 6: CanRaw, 7: Unkown, 8: ModBus, 9: EEBUS, 10: PlusBusTwo, 11: ISquaredCBus, 12: HEMS_Bus, 13: TL_SolarLogBus, 14: ServiceBus}")|O3EEnum|1||||
| |- - DeviceProperty|O3EByteVal|1||||
| |- - DeviceFunction|O3EByteVal|1||||
| |- - SW-Version|O3ESoftVers|8||||
| |- - HW-Version|O3ESoftVers|8||||
| |- - VIN|O3EUtf8|16||||
|**960**|**ExhaustPipeType**|O3EByteVal|1||ro||
|**961**|**SecurityAlgorithmNumber**|RawCodec|2||ro||
|**962**|**BootLoaderVersion**|O3ESoftVers|8||ro||
|**963**|**SparePartNumber**|O3EUtf8|16||ro||
|**964**|[**ActiveDiagnosticSession**](## "{0: NotSet, 1: Default, 2: ProgrammingSession, 3: ExtendedDiagnosticSession, 4: SafetySystemDiagnosticSession, 64: ManufacturerProgramming, 65: ManufacturerDiagnostic, 96: SystemSupplier(VEG)Programming, 97: SystemSupplier(VEG)Diagnostic}")|O3EEnum|1||ro||
|**987**|[**MixerOneCircuitFlowTemperatureTargetSetpoint**](## "Temperature setpoint heating curcuit 1")|O3EInt16|2|[°C](## "°C or °F (system configuration)")|**rw**||
|**988**|[**MixerTwoCircuitFlowTemperatureTargetSetpoint**](## "Temperature setpoint heating curcuit 2")|O3EInt16|2|[°C](## "°C or °F (system configuration)")|**rw**||
|**989**|[**MixerThreeCircuitFlowTemperatureTargetSetpoint**](## "Temperature setpoint heating curcuit 3")|O3EInt16|2|[°C](## "°C or °F (system configuration)")|**rw**||
|**990**|[**MixerFourCircuitFlowTemperatureTargetSetpoint**](## "Temperature setpoint heating curcuit 4")|O3EInt16|2|[°C](## "°C or °F (system configuration)")|**rw**||
|**1004**|[**CentralHeatingRegulationMode**](## "{0: Nothing, 1: ConstantControlled, 4: WeatherByOutsideSensorControlled, 7: WeatherByOutsideSensorAndRoomCorrectionControlled, 10: ConstantControlledWithExternalThermostat, 13: WeatherByOutsideAndZones, 15: WeatherByOutsideSensorAndAutomaticAdaptationControlled}")|O3EEnum|1||ro||
|**1006**|[**TargetQuickMode**](## "External request for one-time charging of domestic hot water (0: off, 2: one-time request)")|*O3EComplexType*|4||**rw**|[Link](https://github.com/open3e/open3e/discussions/318)|
| |- OpMode|O3EByteVal|1||||
| |- Required|O3EBool|1||||
| |- Unknown|RawCodec|2||||
|**1006**|[**TargetQuickMode**](## "External request for one-time charging of domestic hot water (0: off, 2: one-time request)")|*O3EComplexType*|3||**rw**|[Link](https://github.com/open3e/open3e/discussions/318)|
| |- SetModeOneTimesHotWater|O3EByteVal|1||||
| |- State|O3EByteVal|1||||
| |- Unknown|RawCodec|1||||
|**1007**|[**CurrentQuickMode**](## "State of external request for one-time charging of domestic hot water (0: off, 2: on)")|*O3EComplexType*|4||ro|[Link](https://github.com/open3e/open3e/discussions/318)|
| |- OpMode|O3EByteVal|1||||
| |- Required|O3EBool|1||||
| |- Unknown|RawCodec|2||||
|**1007**|[**CurrentQuickMode**](## "State of external request for one-time charging of domestic hot water (0: off, 2: on)")|*O3EComplexType*|3||ro|[Link](https://github.com/open3e/open3e/discussions/318)|
| |- ModeOneTimesHotWater|O3EByteVal|1||||
| |- State|O3EByteVal|1||||
| |- Unknown|RawCodec|1||||
|**1008**|**MixerOneCircuitTargetQuickMode**|RawCodec|4||**rw**||
|**1008**|**MixerOneCircuitTargetQuickMode**|*O3EComplexType*|3||**rw**||
| |- SetModeParty|O3EByteVal|1||||
| |- State|O3EByteVal|1||||
| |- Unknown|RawCodec|1||||
|**1009**|**MixerTwoCircuitTargetQuickMode**|RawCodec|4||**rw**||
|**1009**|**MixerTwoCircuitTargetQuickMode**|*O3EComplexType*|3||**rw**||
| |- SetModeParty|O3EByteVal|1||||
| |- State|O3EByteVal|1||||
| |- Unknown|RawCodec|1||||
|**1010**|**MixerThreeCircuitTargetQuickMode**|RawCodec|4||**rw**||
|**1010**|**MixerThreeCircuitTargetQuickMode**|*O3EComplexType*|3||**rw**||
| |- SetModeParty|O3EByteVal|1||||
| |- State|O3EByteVal|1||||
| |- Unknown|RawCodec|1||||
|**1011**|**MixerFourCircuitTargetQuickMode**|RawCodec|4||**rw**||
|**1011**|**MixerFourCircuitTargetQuickMode**|*O3EComplexType*|3||**rw**||
| |- SetModeParty|O3EByteVal|1||||
| |- State|O3EByteVal|1||||
| |- Unknown|RawCodec|1||||
|**1024**|**MixerOneCircuitCurrentQuickMode**|RawCodec|4||ro||
|**1024**|**MixerOneCircuitCurrentQuickMode**|*O3EComplexType*|3||ro||
| |- ModeParty|O3EByteVal|1||||
| |- State|O3EByteVal|1||||
| |- Unknown|RawCodec|1||||
|**1025**|**MixerTwoCircuitCurrentQuickMode**|RawCodec|4||ro||
|**1025**|**MixerTwoCircuitCurrentQuickMode**|*O3EComplexType*|3||ro||
| |- ModeParty|O3EByteVal|1||||
| |- State|O3EByteVal|1||||
| |- Unknown|RawCodec|1||||
|**1026**|**MixerThreeCircuitCurrentQuickMode**|RawCodec|4||ro||
|**1026**|**MixerThreeCircuitCurrentQuickMode**|*O3EComplexType*|3||ro||
| |- ModeParty|O3EByteVal|1||||
| |- State|O3EByteVal|1||||
| |- Unknown|RawCodec|1||||
|**1027**|**MixerFourCircuitCurrentQuickMode**|RawCodec|4||ro||
|**1027**|**MixerFourCircuitCurrentQuickMode**|*O3EComplexType*|3||ro||
| |- ModeParty|O3EByteVal|1||||
| |- State|O3EByteVal|1||||
| |- Unknown|RawCodec|1||||
|**1040**|**SupplyAirFan**|*O3EComplexType*|6||ro||
| |- Unknown1|RawCodec|3||||
| |- Actual|O3EInt16|2||||
| |- Unknown2|RawCodec|1||||
|**1041**|**ExhaustAirFan**|*O3EComplexType*|6||ro||
| |- Unknown1|RawCodec|3||||
| |- Actual|O3EInt16|2||||
| |- Unknown2|RawCodec|1||||
|**1042**|**PrimaryHeatExchangerTemperatureSensor**|RawCodec|9||ro||
|**1043**|[**AllengraSensor**](## "Flow rate and temperature in the primary circuit of the heat generator")|*O3EComplexType*|5||ro|[Link](https://github.com/open3e/open3e/wiki/036-DoI-%E2%80%90-Data-points-of-Interest/#data-points-of-vitocal-250)|
| |- Actual|O3EInt16|2|l/h|||
| |- Temperature|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- Unknown|RawCodec|1||||
|**1044**|**SecondaryCentralHeatingPump**|RawCodec|2||ro||
|**1047**|**TimeSeriesRecordedFlowTemperatureSensor**|RawCodec|11||ro||
|**1084**|**FlowTemperatureMinimumMaximumLimit**|RawCodec|4||**rw**||
|**1085**|**DomesticHotWaterHysteresis**|*O3EComplexType*|4||ro||
| |- SetpointSwitchOn|O3EInt16|2||||
| |- SetpointSwitchOff|O3EInt16|2||||
|**1087**|**MaximumDomesticHotWaterLoadingTime**|*O3EComplexType*|2||ro||
| |- SetpointMaxOn|O3EInt8|1||||
| |- SetpointMinOff|O3EInt8|1||||
|**1088**|**OutsideAirBypass**|O3EByteVal|1||ro||
|**1089**|**InsideAirBypass**|O3EByteVal|1||ro||
|**1090**|**EnvironmentAirQuality**|RawCodec|9||ro||
|**1093**|**ExhaustPipeLength**|RawCodec|2||ro||
|**1096**|**ResetEnergyManagerDataCollector**|O3EByteVal|1||ro||
|**1097**|**ElectricityPrice**|*O3EComplexType*|20||ro||
| |- Unknown1|RawCodec|4||||
| |- Unknown2|RawCodec|4||||
| |- NormalRate|O3EInt32|4||||
| |- LowRate|O3EInt32|4||||
| |- Unknown3|RawCodec|4||||
|**1098**|**GasProperties**|*O3EComplexType*|20||ro||
| |- Rate|O3EInt32|4||||
| |- Unknown|RawCodec|10||||
| |- VolumeCorrectionFactor|O3EInt16|2||||
| |- CalorificValue|O3EInt32|4||||
|**1100**|**CentralHeatingPumpMinimumMaximumLimit**|*O3EComplexType*|3||**rw**||
| |- MinSpeed|O3EInt8|1||||
| |- MaxSpeed|O3EInt8|1||||
| |- Setpoint|O3EInt8|1||||
|**1101**|**DomesticHotWaterPumpMinimumMaximumLimit**|*O3EComplexType*|3||**rw**||
| |- MinSpeed|O3EInt8|1||||
| |- MaxSpeed|O3EInt8|1||||
| |- Setpoint|O3EInt8|1||||
|**1102**|**MixerOneCircuitPumpMinimumMaximumLimit**|*O3EComplexType*|3||**rw**||
| |- MinSpeed|O3EInt8|1||||
| |- MaxSpeed|O3EInt8|1||||
| |- Setpoint|O3EInt8|1||||
|**1103**|**MixerTwoCircuitPumpMinimumMaximumLimit**|*O3EComplexType*|3||**rw**||
| |- MinSpeed|O3EInt8|1||||
| |- MaxSpeed|O3EInt8|1||||
| |- Setpoint|O3EInt8|1||||
|**1104**|**MixerThreeCircuitPumpMinimumMaximumLimit**|*O3EComplexType*|3||**rw**||
| |- MinSpeed|O3EInt8|1||||
| |- MaxSpeed|O3EInt8|1||||
| |- Setpoint|O3EInt8|1||||
|**1105**|**MixerFourCircuitPumpMinimumMaximumLimit**|*O3EComplexType*|3||**rw**||
| |- MinSpeed|O3EInt8|1||||
| |- MaxSpeed|O3EInt8|1||||
| |- Setpoint|O3EInt8|1||||
|**1118**|**SolarCircuitPumpMinimumMaximumLimit**|*O3EComplexType*|3||**rw**||
| |- MinSpeed|O3EInt8|1||||
| |- MaxSpeed|O3EInt8|1||||
| |- Setpoint|O3EInt8|1||||
|**1125**|**SolarMaximumLoadingTemperature**|O3EInt16|2||ro||
|**1128**|**SolarStagnationHours**|O3EInt16|2||ro||
|**1132**|**ViessmannIdentificationNumberListInternal**|*O3EComplexType*|97||ro||
| |- Count|O3EByteVal|1||||
| |- VIN1|O3EUtf8|16||||
| |- VIN2|O3EUtf8|16||||
| |- VIN3|O3EUtf8|16||||
| |- VIN4|O3EUtf8|16||||
| |- VIN5|O3EUtf8|16||||
| |- VIN6|O3EUtf8|16||||
|**1136**|**SolarProperty**|RawCodec|4||ro||
|**1137**|**ServiceModeActivation**|O3EByteVal|1||ro||
|**1138**|**AccentLedBar**|RawCodec|1||ro||
|**1139**|**CentralHeatingCurveAdaptionParameter**|*O3EComplexType*|7||ro||
| |- TemperatureHigh|O3EInt16|2||||
| |- TemperatureLow|O3EInt16|2||||
| |- Unknown|RawCodec|3||||
|**1165**|**BackendConnectionStatus**|O3EByteVal|1||ro||
|**1166**|**ResetDtcHistory**|RawCodec|5||ro||
|**1167**|**ExternalDomesticHotWaterTemperatureSetpoint**|O3EInt16|2||**rw**||
|**1172**|**SolarCircuitPumpStatistical**|RawCodec|14||ro||
|**1175**|**AcknowledgeInfoAlarmMessage**|O3EByteVal|1||ro||
|**1176**|**AcknowledgeWarningAlarmMessage**|O3EByteVal|1||ro||
|**1177**|**AcknowledgeServiceAlarmMessage**|O3EByteVal|1||ro||
|**1178**|**AcknowledgeErrorAlarmMessage**|O3EByteVal|1||ro||
|**1181**|**DisplayTestMode**|O3EInt8|1||ro||
|**1190**|[**ThermalPower**](## "Actual thermal power output of the system")|*O3EComplexType*|4||ro||
| |- Power|O3EInt16|2|kW|||
| |- Unknown|RawCodec|2||||
|**1191**|**FuelCellStatus**|RawCodec|1||ro||
|**1192**|**MixerOneCircuitFlowTemperatureMinimumMaximumLimit**|*O3EComplexType*|10||**rw**||
| |- Minimum|O3EInt16|2||||
| |- Maximum|O3EInt16|2||||
| |- Unknown|RawCodec|6||||
|**1193**|**MixerTwoCircuitFlowTemperatureMinimumMaximumLimit**|*O3EComplexType*|10||**rw**||
| |- Minimum|O3EInt16|2||||
| |- Maximum|O3EInt16|2||||
| |- Unknown|RawCodec|6||||
|**1194**|**MixerThreeCircuitFlowTemperatureMinimumMaximumLimit**|*O3EComplexType*|10||**rw**||
| |- Minimum|O3EInt16|2||||
| |- Maximum|O3EInt16|2||||
| |- Unknown|RawCodec|6||||
|**1195**|**MixerFourCircuitFlowTemperatureMinimumMaximumLimit**|*O3EComplexType*|10||**rw**||
| |- Minimum|O3EInt16|2||||
| |- Maximum|O3EInt16|2||||
| |- Unknown|RawCodec|6||||
|**1196**|**MixerFiveCircuitFlowTemperatureMinimumMaximumLimit**|*O3EComplexType*|10||**rw**||
| |- Minimum|O3EInt16|2||||
| |- Maximum|O3EInt16|2||||
| |- Unknown|RawCodec|6||||
|**1197**|**MixerSixCircuitFlowTemperatureMinimumMaximumLimit**|*O3EComplexType*|10||**rw**||
| |- Minimum|O3EInt16|2||||
| |- Maximum|O3EInt16|2||||
| |- Unknown|RawCodec|6||||
|**1198**|**MixerSevenCircuitFlowTemperatureMinimumMaximumLimit**|*O3EComplexType*|10||**rw**||
| |- Minimum|O3EInt16|2||||
| |- Maximum|O3EInt16|2||||
| |- Unknown|RawCodec|6||||
|**1199**|**MixerEightCircuitFlowTemperatureMinimumMaximumLimit**|*O3EComplexType*|10||**rw**||
| |- Minimum|O3EInt16|2||||
| |- Maximum|O3EInt16|2||||
| |- Unknown|RawCodec|6||||
|**1210**|**FuelCellStatistical**|RawCodec|13||ro||
|**1211**|**GeneratedCentralHeatingOutput**|*O3EComplexType*|24||ro||
| |- Today|O3EInt32|4||||
| |- Past7Days|O3EInt32|4||||
| |- CurrentMonth|O3EInt32|4||||
| |- PastMonth|O3EInt32|4||||
| |- CurrentYear|O3EInt32|4||||
| |- PastYear|O3EInt32|4||||
|**1214**|**ElectricalPowerOutput**|O3EInt16|2||ro||
|**1215**|**FuelCellState**|RawCodec|1||ro||
|**1216**|**FuelCellStateTwo**|RawCodec|1||ro||
|**1217**|**FuelCellGenerationMode**|RawCodec|1||ro||
|**1218**|**FuelCellInstruction**|RawCodec|1||ro||
|**1220**|**FuelCellMode**|RawCodec|1||ro||
|**1221**|**FuelCellModeResult**|RawCodec|1||ro||
|**1222**|**FuelCellRunRequest**|RawCodec|1||ro||
|**1223**|**FuelCellRunRequestResult**|RawCodec|1||ro||
|**1224**|**FuelCellStopRequest**|RawCodec|1||ro||
|**1226**|**FuelCellProcessNumber**|RawCodec|1||ro||
|**1227**|**FuelCellRequestAction**|RawCodec|1||ro||
|**1228**|**FuelCellCompletionNotification**|RawCodec|1||ro||
|**1229**|**FuelCellGasTypeSetting**|RawCodec|1||ro||
|**1230**|**FuelCellCountrySetting**|RawCodec|1||ro||
|**1231**|**FuelCellPrimaryPump**|RawCodec|4||ro||
|**1232**|[**GenericDigitalInputConfigurationOnBoardOne**](## "{0: Nothing, 1: FaultSignal, 2: DhwCirculation, 3: FaultSignalAndLocked, 4: ExternalHeatDemand, 5: ExternalLocked, 6: ExternalThermostat, 7: RoomTemperatureLimiter, 8: CallForHeat, 9: SmartGridReadyInputOne, 10: SmartGridReadyInputTwo, 11: PowerSupplierLock, 12: ExternalCoolingDemand, 13: PrioritizedDemandDeactivationOtherCircuits, 14: LockCircuitOne, 15: LockCircuitTwo, 16: ExternalDemandAutomatic, 17: FanControl, 18: FanRpmControl, 19: DefrostHeaterControlOne, 20: DefrostHeaterControlTwo, 21: DayNigthOperation, 22: DayNigthOperationPlusDirectControlDigitalOutputOne, 23: PermanentHeating, 24: DirectControlDryContactOne, 25: DirectControlDryContactTwo, 26: DirectControlDryContactThree, 27: DirectControlDigitalOutputTwentyFourVolt}")|O3EEnum|1||ro||
|**1233**|**GatewayRemoteVisibleOneTwo**|RawCodec|68||ro||
|**1234**|**GatewayRemoteVisibleThreeFour**|RawCodec|68||ro||
|**1235**|**GatewayRemoteVisibleFiveSix**|RawCodec|68||ro||
|**1236**|**GatewayRemoteVisibleSevenEight**|RawCodec|68||ro||
|**1237**|**GatewayRemoteVisibleNineTen**|RawCodec|68||ro||
|**1238**|**AvailableActorSensorComponents**|RawCodec|31||ro||
|**1239**|**ActorSensorTest**|RawCodec|2||ro||
|**1240**|**CentralHeatingPumpMode**|O3EByteVal|1||ro||
|**1241**|**MixerOneCircuitPumpMode**|O3EByteVal|1||ro||
|**1242**|**MixerTwoCircuitPumpMode**|O3EByteVal|1||ro||
|**1243**|**MixerThreeCircuitPumpMode**|O3EByteVal|1||ro||
|**1244**|**MixerFourCircuitPumpMode**|O3EByteVal|1||ro||
|**1263**|**DiverterValveBoilerHydraulicTower**|RawCodec|2||ro||
|**1264**|**DiverterValveFuelCellHydraulicTower**|RawCodec|2||ro||
|**1265**|**FanTargetSpeedMeta**|RawCodec|8||**rw**||
|**1266**|**DiverterValveStatistical**|*O3EComplexType*|8||ro||
| |- Value1|O3EInt16|2||||
| |- Unknown|RawCodec|6||||
|**1286**|**BusTopologyMatrixTwo**|*O3EList*|181||ro||
| |- Count|O3EInt8|1||||
| |- TopologyElement|*O3EComplexType*|36||||
| |- - NodeID|O3EByteVal|1||||
| |- - [BusType](## "{0: OwnBus, 1: PlusBus, 2: CanInternal, 3: CanExternal, 4: InternalUart, 5: Zigbee, 6: CanRaw, 7: Unkown, 8: ModBus, 9: EEBUS, 10: PlusBusTwo, 11: ISquaredCBus, 12: HEMS_Bus, 13: TL_SolarLogBus, 14: ServiceBus}")|O3EEnum|1||||
| |- - DeviceProperty|O3EByteVal|1||||
| |- - DeviceFunction|O3EByteVal|1||||
| |- - SW-Version|O3ESoftVers|8||||
| |- - HW-Version|O3ESoftVers|8||||
| |- - VIN|O3EUtf8|16||||
|**1287**|**BusTopologyMatrixThree**|*O3EList*|181||ro||
| |- Count|O3EInt8|1||||
| |- TopologyElement|*O3EComplexType*|36||||
| |- - NodeID|O3EByteVal|1||||
| |- - [BusType](## "{0: OwnBus, 1: PlusBus, 2: CanInternal, 3: CanExternal, 4: InternalUart, 5: Zigbee, 6: CanRaw, 7: Unkown, 8: ModBus, 9: EEBUS, 10: PlusBusTwo, 11: ISquaredCBus, 12: HEMS_Bus, 13: TL_SolarLogBus, 14: ServiceBus}")|O3EEnum|1||||
| |- - DeviceProperty|O3EByteVal|1||||
| |- - DeviceFunction|O3EByteVal|1||||
| |- - SW-Version|O3ESoftVers|8||||
| |- - HW-Version|O3ESoftVers|8||||
| |- - VIN|O3EUtf8|16||||
|**1288**|**BusTopologyMatrixFour**|*O3EList*|181||ro||
| |- Count|O3EInt8|1||||
| |- TopologyElement|*O3EComplexType*|36||||
| |- - NodeID|O3EByteVal|1||||
| |- - [BusType](## "{0: OwnBus, 1: PlusBus, 2: CanInternal, 3: CanExternal, 4: InternalUart, 5: Zigbee, 6: CanRaw, 7: Unkown, 8: ModBus, 9: EEBUS, 10: PlusBusTwo, 11: ISquaredCBus, 12: HEMS_Bus, 13: TL_SolarLogBus, 14: ServiceBus}")|O3EEnum|1||||
| |- - DeviceProperty|O3EByteVal|1||||
| |- - DeviceFunction|O3EByteVal|1||||
| |- - SW-Version|O3ESoftVers|8||||
| |- - HW-Version|O3ESoftVers|8||||
| |- - VIN|O3EUtf8|16||||
|**1289**|**BusTopologyMatrixFive**|*O3EList*|181||ro||
| |- Count|O3EInt8|1||||
| |- TopologyElement|*O3EComplexType*|36||||
| |- - NodeID|O3EByteVal|1||||
| |- - [BusType](## "{0: OwnBus, 1: PlusBus, 2: CanInternal, 3: CanExternal, 4: InternalUart, 5: Zigbee, 6: CanRaw, 7: Unkown, 8: ModBus, 9: EEBUS, 10: PlusBusTwo, 11: ISquaredCBus, 12: HEMS_Bus, 13: TL_SolarLogBus, 14: ServiceBus}")|O3EEnum|1||||
| |- - DeviceProperty|O3EByteVal|1||||
| |- - DeviceFunction|O3EByteVal|1||||
| |- - SW-Version|O3ESoftVers|8||||
| |- - HW-Version|O3ESoftVers|8||||
| |- - VIN|O3EUtf8|16||||
|**1290**|**DomesticHotWaterShiftLoadPump**|RawCodec|4||ro||
|**1294**|[**EnergyConsumptionCentralHeatingMonthMatrix**](## "Energy Consumption Central Heating Per Month")|*O3EComplexType*|124||ro||
| |- [CurrentMonth](## "Energy Consumption Central Heating Current Month")|*O3EList*|62||||
| |- - 01|O3EInt16|2|kWh|||
| |- - 02|O3EInt16|2|kWh|||
| |- - 03|O3EInt16|2|kWh|||
| |- - 04|O3EInt16|2|kWh|||
| |- - 05|O3EInt16|2|kWh|||
| |- - 06|O3EInt16|2|kWh|||
| |- - 07|O3EInt16|2|kWh|||
| |- - 08|O3EInt16|2|kWh|||
| |- - 09|O3EInt16|2|kWh|||
| |- - 10|O3EInt16|2|kWh|||
| |- - 11|O3EInt16|2|kWh|||
| |- - 12|O3EInt16|2|kWh|||
| |- - 13|O3EInt16|2|kWh|||
| |- - 14|O3EInt16|2|kWh|||
| |- - 15|O3EInt16|2|kWh|||
| |- - 16|O3EInt16|2|kWh|||
| |- - 17|O3EInt16|2|kWh|||
| |- - 18|O3EInt16|2|kWh|||
| |- - 19|O3EInt16|2|kWh|||
| |- - 20|O3EInt16|2|kWh|||
| |- - 21|O3EInt16|2|kWh|||
| |- - 22|O3EInt16|2|kWh|||
| |- - 23|O3EInt16|2|kWh|||
| |- - 24|O3EInt16|2|kWh|||
| |- - 25|O3EInt16|2|kWh|||
| |- - 26|O3EInt16|2|kWh|||
| |- - 27|O3EInt16|2|kWh|||
| |- - 28|O3EInt16|2|kWh|||
| |- - 29|O3EInt16|2|kWh|||
| |- - 30|O3EInt16|2|kWh|||
| |- - 31|O3EInt16|2|kWh|||
| |- [LastMonth](## "Energy Consumption Central Heating Previous Month")|*O3EList*|62||||
| |- - 01|O3EInt16|2|kWh|||
| |- - 02|O3EInt16|2|kWh|||
| |- - 03|O3EInt16|2|kWh|||
| |- - 04|O3EInt16|2|kWh|||
| |- - 05|O3EInt16|2|kWh|||
| |- - 06|O3EInt16|2|kWh|||
| |- - 07|O3EInt16|2|kWh|||
| |- - 08|O3EInt16|2|kWh|||
| |- - 09|O3EInt16|2|kWh|||
| |- - 10|O3EInt16|2|kWh|||
| |- - 11|O3EInt16|2|kWh|||
| |- - 12|O3EInt16|2|kWh|||
| |- - 13|O3EInt16|2|kWh|||
| |- - 14|O3EInt16|2|kWh|||
| |- - 15|O3EInt16|2|kWh|||
| |- - 16|O3EInt16|2|kWh|||
| |- - 17|O3EInt16|2|kWh|||
| |- - 18|O3EInt16|2|kWh|||
| |- - 19|O3EInt16|2|kWh|||
| |- - 20|O3EInt16|2|kWh|||
| |- - 21|O3EInt16|2|kWh|||
| |- - 22|O3EInt16|2|kWh|||
| |- - 23|O3EInt16|2|kWh|||
| |- - 24|O3EInt16|2|kWh|||
| |- - 25|O3EInt16|2|kWh|||
| |- - 26|O3EInt16|2|kWh|||
| |- - 27|O3EInt16|2|kWh|||
| |- - 28|O3EInt16|2|kWh|||
| |- - 29|O3EInt16|2|kWh|||
| |- - 30|O3EInt16|2|kWh|||
| |- - 31|O3EInt16|2|kWh|||
|**1311**|[**EnergyConsumptionDomesticHotWaterMonthMatrix**](## "Energy Consumption Domestic Hot Water Per Month")|*O3EComplexType*|124||ro||
| |- [CurrentMonth](## "Energy Consumption Domestic Hot Water Current Month")|*O3EList*|62||||
| |- - 01|O3EInt16|2|kWh|||
| |- - 02|O3EInt16|2|kWh|||
| |- - 03|O3EInt16|2|kWh|||
| |- - 04|O3EInt16|2|kWh|||
| |- - 05|O3EInt16|2|kWh|||
| |- - 06|O3EInt16|2|kWh|||
| |- - 07|O3EInt16|2|kWh|||
| |- - 08|O3EInt16|2|kWh|||
| |- - 09|O3EInt16|2|kWh|||
| |- - 10|O3EInt16|2|kWh|||
| |- - 11|O3EInt16|2|kWh|||
| |- - 12|O3EInt16|2|kWh|||
| |- - 13|O3EInt16|2|kWh|||
| |- - 14|O3EInt16|2|kWh|||
| |- - 15|O3EInt16|2|kWh|||
| |- - 16|O3EInt16|2|kWh|||
| |- - 17|O3EInt16|2|kWh|||
| |- - 18|O3EInt16|2|kWh|||
| |- - 19|O3EInt16|2|kWh|||
| |- - 20|O3EInt16|2|kWh|||
| |- - 21|O3EInt16|2|kWh|||
| |- - 22|O3EInt16|2|kWh|||
| |- - 23|O3EInt16|2|kWh|||
| |- - 24|O3EInt16|2|kWh|||
| |- - 25|O3EInt16|2|kWh|||
| |- - 26|O3EInt16|2|kWh|||
| |- - 27|O3EInt16|2|kWh|||
| |- - 28|O3EInt16|2|kWh|||
| |- - 29|O3EInt16|2|kWh|||
| |- - 30|O3EInt16|2|kWh|||
| |- - 31|O3EInt16|2|kWh|||
| |- [LastMonth](## "Energy Consumption Domestic Hot Water Previous Month")|*O3EList*|62||||
| |- - 01|O3EInt16|2|kWh|||
| |- - 02|O3EInt16|2|kWh|||
| |- - 03|O3EInt16|2|kWh|||
| |- - 04|O3EInt16|2|kWh|||
| |- - 05|O3EInt16|2|kWh|||
| |- - 06|O3EInt16|2|kWh|||
| |- - 07|O3EInt16|2|kWh|||
| |- - 08|O3EInt16|2|kWh|||
| |- - 09|O3EInt16|2|kWh|||
| |- - 10|O3EInt16|2|kWh|||
| |- - 11|O3EInt16|2|kWh|||
| |- - 12|O3EInt16|2|kWh|||
| |- - 13|O3EInt16|2|kWh|||
| |- - 14|O3EInt16|2|kWh|||
| |- - 15|O3EInt16|2|kWh|||
| |- - 16|O3EInt16|2|kWh|||
| |- - 17|O3EInt16|2|kWh|||
| |- - 18|O3EInt16|2|kWh|||
| |- - 19|O3EInt16|2|kWh|||
| |- - 20|O3EInt16|2|kWh|||
| |- - 21|O3EInt16|2|kWh|||
| |- - 22|O3EInt16|2|kWh|||
| |- - 23|O3EInt16|2|kWh|||
| |- - 24|O3EInt16|2|kWh|||
| |- - 25|O3EInt16|2|kWh|||
| |- - 26|O3EInt16|2|kWh|||
| |- - 27|O3EInt16|2|kWh|||
| |- - 28|O3EInt16|2|kWh|||
| |- - 29|O3EInt16|2|kWh|||
| |- - 30|O3EInt16|2|kWh|||
| |- - 31|O3EInt16|2|kWh|||
|**1312**|[**EnergyConsumptionCoolingMonthMatrix**](## "Energy Consumption Cooling Per Month")|*O3EComplexType*|124||ro||
| |- [CurrentMonth](## "Energy Consumption Cooling Current Month")|*O3EList*|62||||
| |- - 01|O3EInt16|2|kWh|||
| |- - 02|O3EInt16|2|kWh|||
| |- - 03|O3EInt16|2|kWh|||
| |- - 04|O3EInt16|2|kWh|||
| |- - 05|O3EInt16|2|kWh|||
| |- - 06|O3EInt16|2|kWh|||
| |- - 07|O3EInt16|2|kWh|||
| |- - 08|O3EInt16|2|kWh|||
| |- - 09|O3EInt16|2|kWh|||
| |- - 10|O3EInt16|2|kWh|||
| |- - 11|O3EInt16|2|kWh|||
| |- - 12|O3EInt16|2|kWh|||
| |- - 13|O3EInt16|2|kWh|||
| |- - 14|O3EInt16|2|kWh|||
| |- - 15|O3EInt16|2|kWh|||
| |- - 16|O3EInt16|2|kWh|||
| |- - 17|O3EInt16|2|kWh|||
| |- - 18|O3EInt16|2|kWh|||
| |- - 19|O3EInt16|2|kWh|||
| |- - 20|O3EInt16|2|kWh|||
| |- - 21|O3EInt16|2|kWh|||
| |- - 22|O3EInt16|2|kWh|||
| |- - 23|O3EInt16|2|kWh|||
| |- - 24|O3EInt16|2|kWh|||
| |- - 25|O3EInt16|2|kWh|||
| |- - 26|O3EInt16|2|kWh|||
| |- - 27|O3EInt16|2|kWh|||
| |- - 28|O3EInt16|2|kWh|||
| |- - 29|O3EInt16|2|kWh|||
| |- - 30|O3EInt16|2|kWh|||
| |- - 31|O3EInt16|2|kWh|||
| |- [LastMonth](## "Energy Consumption Cooling Previous Matrix")|*O3EList*|62||||
| |- - 01|O3EInt16|2|kWh|||
| |- - 02|O3EInt16|2|kWh|||
| |- - 03|O3EInt16|2|kWh|||
| |- - 04|O3EInt16|2|kWh|||
| |- - 05|O3EInt16|2|kWh|||
| |- - 06|O3EInt16|2|kWh|||
| |- - 07|O3EInt16|2|kWh|||
| |- - 08|O3EInt16|2|kWh|||
| |- - 09|O3EInt16|2|kWh|||
| |- - 10|O3EInt16|2|kWh|||
| |- - 11|O3EInt16|2|kWh|||
| |- - 12|O3EInt16|2|kWh|||
| |- - 13|O3EInt16|2|kWh|||
| |- - 14|O3EInt16|2|kWh|||
| |- - 15|O3EInt16|2|kWh|||
| |- - 16|O3EInt16|2|kWh|||
| |- - 17|O3EInt16|2|kWh|||
| |- - 18|O3EInt16|2|kWh|||
| |- - 19|O3EInt16|2|kWh|||
| |- - 20|O3EInt16|2|kWh|||
| |- - 21|O3EInt16|2|kWh|||
| |- - 22|O3EInt16|2|kWh|||
| |- - 23|O3EInt16|2|kWh|||
| |- - 24|O3EInt16|2|kWh|||
| |- - 25|O3EInt16|2|kWh|||
| |- - 26|O3EInt16|2|kWh|||
| |- - 27|O3EInt16|2|kWh|||
| |- - 28|O3EInt16|2|kWh|||
| |- - 29|O3EInt16|2|kWh|||
| |- - 30|O3EInt16|2|kWh|||
| |- - 31|O3EInt16|2|kWh|||
|**1313**|[**GeneratedElectricityMonthMatrix**](## "Generated Electricity Per Month")|*O3EComplexType*|124||ro||
| |- [CurrentMonth](## "Generated Electricity Current Month")|*O3EList*|62||||
| |- - 01|O3EInt16|2|kWh|||
| |- - 02|O3EInt16|2|kWh|||
| |- - 03|O3EInt16|2|kWh|||
| |- - 04|O3EInt16|2|kWh|||
| |- - 05|O3EInt16|2|kWh|||
| |- - 06|O3EInt16|2|kWh|||
| |- - 07|O3EInt16|2|kWh|||
| |- - 08|O3EInt16|2|kWh|||
| |- - 09|O3EInt16|2|kWh|||
| |- - 10|O3EInt16|2|kWh|||
| |- - 11|O3EInt16|2|kWh|||
| |- - 12|O3EInt16|2|kWh|||
| |- - 13|O3EInt16|2|kWh|||
| |- - 14|O3EInt16|2|kWh|||
| |- - 15|O3EInt16|2|kWh|||
| |- - 16|O3EInt16|2|kWh|||
| |- - 17|O3EInt16|2|kWh|||
| |- - 18|O3EInt16|2|kWh|||
| |- - 19|O3EInt16|2|kWh|||
| |- - 20|O3EInt16|2|kWh|||
| |- - 21|O3EInt16|2|kWh|||
| |- - 22|O3EInt16|2|kWh|||
| |- - 23|O3EInt16|2|kWh|||
| |- - 24|O3EInt16|2|kWh|||
| |- - 25|O3EInt16|2|kWh|||
| |- - 26|O3EInt16|2|kWh|||
| |- - 27|O3EInt16|2|kWh|||
| |- - 28|O3EInt16|2|kWh|||
| |- - 29|O3EInt16|2|kWh|||
| |- - 30|O3EInt16|2|kWh|||
| |- - 31|O3EInt16|2|kWh|||
| |- [LastMonth](## "Generated Electricity Previous Month")|*O3EList*|62||||
| |- - 01|O3EInt16|2|kWh|||
| |- - 02|O3EInt16|2|kWh|||
| |- - 03|O3EInt16|2|kWh|||
| |- - 04|O3EInt16|2|kWh|||
| |- - 05|O3EInt16|2|kWh|||
| |- - 06|O3EInt16|2|kWh|||
| |- - 07|O3EInt16|2|kWh|||
| |- - 08|O3EInt16|2|kWh|||
| |- - 09|O3EInt16|2|kWh|||
| |- - 10|O3EInt16|2|kWh|||
| |- - 11|O3EInt16|2|kWh|||
| |- - 12|O3EInt16|2|kWh|||
| |- - 13|O3EInt16|2|kWh|||
| |- - 14|O3EInt16|2|kWh|||
| |- - 15|O3EInt16|2|kWh|||
| |- - 16|O3EInt16|2|kWh|||
| |- - 17|O3EInt16|2|kWh|||
| |- - 18|O3EInt16|2|kWh|||
| |- - 19|O3EInt16|2|kWh|||
| |- - 20|O3EInt16|2|kWh|||
| |- - 21|O3EInt16|2|kWh|||
| |- - 22|O3EInt16|2|kWh|||
| |- - 23|O3EInt16|2|kWh|||
| |- - 24|O3EInt16|2|kWh|||
| |- - 25|O3EInt16|2|kWh|||
| |- - 26|O3EInt16|2|kWh|||
| |- - 27|O3EInt16|2|kWh|||
| |- - 28|O3EInt16|2|kWh|||
| |- - 29|O3EInt16|2|kWh|||
| |- - 30|O3EInt16|2|kWh|||
| |- - 31|O3EInt16|2|kWh|||
|**1314**|[**SolarEnergyYieldMonthMatrix**](## "Solar Energy Yield Per Month")|*O3EComplexType*|124||ro||
| |- [CurrentMonth](## "Solar Energy Yield Current Month")|*O3EList*|62||||
| |- - 01|O3EInt16|2|kWh|||
| |- - 02|O3EInt16|2|kWh|||
| |- - 03|O3EInt16|2|kWh|||
| |- - 04|O3EInt16|2|kWh|||
| |- - 05|O3EInt16|2|kWh|||
| |- - 06|O3EInt16|2|kWh|||
| |- - 07|O3EInt16|2|kWh|||
| |- - 08|O3EInt16|2|kWh|||
| |- - 09|O3EInt16|2|kWh|||
| |- - 10|O3EInt16|2|kWh|||
| |- - 11|O3EInt16|2|kWh|||
| |- - 12|O3EInt16|2|kWh|||
| |- - 13|O3EInt16|2|kWh|||
| |- - 14|O3EInt16|2|kWh|||
| |- - 15|O3EInt16|2|kWh|||
| |- - 16|O3EInt16|2|kWh|||
| |- - 17|O3EInt16|2|kWh|||
| |- - 18|O3EInt16|2|kWh|||
| |- - 19|O3EInt16|2|kWh|||
| |- - 20|O3EInt16|2|kWh|||
| |- - 21|O3EInt16|2|kWh|||
| |- - 22|O3EInt16|2|kWh|||
| |- - 23|O3EInt16|2|kWh|||
| |- - 24|O3EInt16|2|kWh|||
| |- - 25|O3EInt16|2|kWh|||
| |- - 26|O3EInt16|2|kWh|||
| |- - 27|O3EInt16|2|kWh|||
| |- - 28|O3EInt16|2|kWh|||
| |- - 29|O3EInt16|2|kWh|||
| |- - 30|O3EInt16|2|kWh|||
| |- - 31|O3EInt16|2|kWh|||
| |- [LastMonth](## "Solar Energy Yield Previous Month")|*O3EList*|62||||
| |- - 01|O3EInt16|2|kWh|||
| |- - 02|O3EInt16|2|kWh|||
| |- - 03|O3EInt16|2|kWh|||
| |- - 04|O3EInt16|2|kWh|||
| |- - 05|O3EInt16|2|kWh|||
| |- - 06|O3EInt16|2|kWh|||
| |- - 07|O3EInt16|2|kWh|||
| |- - 08|O3EInt16|2|kWh|||
| |- - 09|O3EInt16|2|kWh|||
| |- - 10|O3EInt16|2|kWh|||
| |- - 11|O3EInt16|2|kWh|||
| |- - 12|O3EInt16|2|kWh|||
| |- - 13|O3EInt16|2|kWh|||
| |- - 14|O3EInt16|2|kWh|||
| |- - 15|O3EInt16|2|kWh|||
| |- - 16|O3EInt16|2|kWh|||
| |- - 17|O3EInt16|2|kWh|||
| |- - 18|O3EInt16|2|kWh|||
| |- - 19|O3EInt16|2|kWh|||
| |- - 20|O3EInt16|2|kWh|||
| |- - 21|O3EInt16|2|kWh|||
| |- - 22|O3EInt16|2|kWh|||
| |- - 23|O3EInt16|2|kWh|||
| |- - 24|O3EInt16|2|kWh|||
| |- - 25|O3EInt16|2|kWh|||
| |- - 26|O3EInt16|2|kWh|||
| |- - 27|O3EInt16|2|kWh|||
| |- - 28|O3EInt16|2|kWh|||
| |- - 29|O3EInt16|2|kWh|||
| |- - 30|O3EInt16|2|kWh|||
| |- - 31|O3EInt16|2|kWh|||
|**1315**|[**GeneratedCentralHeatingOutputMonthMatrix**](## "Generated Central Heating Output Per Month")|*O3EComplexType*|124||ro||
| |- [CurrentMonth](## "Generated Central Heating Output Current Month")|*O3EList*|62||||
| |- - 01|O3EInt16|2|kWh|||
| |- - 02|O3EInt16|2|kWh|||
| |- - 03|O3EInt16|2|kWh|||
| |- - 04|O3EInt16|2|kWh|||
| |- - 05|O3EInt16|2|kWh|||
| |- - 06|O3EInt16|2|kWh|||
| |- - 07|O3EInt16|2|kWh|||
| |- - 08|O3EInt16|2|kWh|||
| |- - 09|O3EInt16|2|kWh|||
| |- - 10|O3EInt16|2|kWh|||
| |- - 11|O3EInt16|2|kWh|||
| |- - 12|O3EInt16|2|kWh|||
| |- - 13|O3EInt16|2|kWh|||
| |- - 14|O3EInt16|2|kWh|||
| |- - 15|O3EInt16|2|kWh|||
| |- - 16|O3EInt16|2|kWh|||
| |- - 17|O3EInt16|2|kWh|||
| |- - 18|O3EInt16|2|kWh|||
| |- - 19|O3EInt16|2|kWh|||
| |- - 20|O3EInt16|2|kWh|||
| |- - 21|O3EInt16|2|kWh|||
| |- - 22|O3EInt16|2|kWh|||
| |- - 23|O3EInt16|2|kWh|||
| |- - 24|O3EInt16|2|kWh|||
| |- - 25|O3EInt16|2|kWh|||
| |- - 26|O3EInt16|2|kWh|||
| |- - 27|O3EInt16|2|kWh|||
| |- - 28|O3EInt16|2|kWh|||
| |- - 29|O3EInt16|2|kWh|||
| |- - 30|O3EInt16|2|kWh|||
| |- - 31|O3EInt16|2|kWh|||
| |- [LastMonth](## "Generated Central Heating Output Previous Month")|*O3EList*|62||||
| |- - 01|O3EInt16|2|kWh|||
| |- - 02|O3EInt16|2|kWh|||
| |- - 03|O3EInt16|2|kWh|||
| |- - 04|O3EInt16|2|kWh|||
| |- - 05|O3EInt16|2|kWh|||
| |- - 06|O3EInt16|2|kWh|||
| |- - 07|O3EInt16|2|kWh|||
| |- - 08|O3EInt16|2|kWh|||
| |- - 09|O3EInt16|2|kWh|||
| |- - 10|O3EInt16|2|kWh|||
| |- - 11|O3EInt16|2|kWh|||
| |- - 12|O3EInt16|2|kWh|||
| |- - 13|O3EInt16|2|kWh|||
| |- - 14|O3EInt16|2|kWh|||
| |- - 15|O3EInt16|2|kWh|||
| |- - 16|O3EInt16|2|kWh|||
| |- - 17|O3EInt16|2|kWh|||
| |- - 18|O3EInt16|2|kWh|||
| |- - 19|O3EInt16|2|kWh|||
| |- - 20|O3EInt16|2|kWh|||
| |- - 21|O3EInt16|2|kWh|||
| |- - 22|O3EInt16|2|kWh|||
| |- - 23|O3EInt16|2|kWh|||
| |- - 24|O3EInt16|2|kWh|||
| |- - 25|O3EInt16|2|kWh|||
| |- - 26|O3EInt16|2|kWh|||
| |- - 27|O3EInt16|2|kWh|||
| |- - 28|O3EInt16|2|kWh|||
| |- - 29|O3EInt16|2|kWh|||
| |- - 30|O3EInt16|2|kWh|||
| |- - 31|O3EInt16|2|kWh|||
|**1316**|[**EnergyConsumptionCentralHeatingYearMatrix**](## "Energy Consumption Central Heating Per Year")|*O3EComplexType*|96||ro||
| |- [CurrentYear](## "Energy Consumption Central Heating Current Year")|*O3EList*|48||||
| |- - 01_January|O3EInt32|4|kWh|||
| |- - 02_February|O3EInt32|4|kWh|||
| |- - 03_March|O3EInt32|4|kWh|||
| |- - 04_April|O3EInt32|4|kWh|||
| |- - 05_May|O3EInt32|4|kWh|||
| |- - 06_June|O3EInt32|4|kWh|||
| |- - 07_July|O3EInt32|4|kWh|||
| |- - 08_August|O3EInt32|4|kWh|||
| |- - 09_September|O3EInt32|4|kWh|||
| |- - 10_October|O3EInt32|4|kWh|||
| |- - 11_November|O3EInt32|4|kWh|||
| |- - 12_December|O3EInt32|4|kWh|||
| |- [LastYear](## "Energy Consumption Central Heating Last Year")|*O3EList*|48||||
| |- - 01_January|O3EInt32|4|kWh|||
| |- - 02_February|O3EInt32|4|kWh|||
| |- - 03_March|O3EInt32|4|kWh|||
| |- - 04_April|O3EInt32|4|kWh|||
| |- - 05_May|O3EInt32|4|kWh|||
| |- - 06_June|O3EInt32|4|kWh|||
| |- - 07_July|O3EInt32|4|kWh|||
| |- - 08_August|O3EInt32|4|kWh|||
| |- - 09_September|O3EInt32|4|kWh|||
| |- - 10_October|O3EInt32|4|kWh|||
| |- - 11_November|O3EInt32|4|kWh|||
| |- - 12_December|O3EInt32|4|kWh|||
|**1333**|[**EnergyConsumptionDomesticHotWaterYearMatrix**](## "Energy Consumption Domestic Hot Water Per Year")|*O3EComplexType*|96||ro||
| |- [CurrentYear](## "Energy Consumption Domestic Hot Water Current Year")|*O3EList*|48||||
| |- - 01_January|O3EInt32|4||||
| |- - 02_February|O3EInt32|4||||
| |- - 03_March|O3EInt32|4||||
| |- - 04_April|O3EInt32|4||||
| |- - 05_May|O3EInt32|4||||
| |- - 06_June|O3EInt32|4||||
| |- - 07_July|O3EInt32|4||||
| |- - 08_August|O3EInt32|4||||
| |- - 09_September|O3EInt32|4||||
| |- - 10_October|O3EInt32|4||||
| |- - 11_November|O3EInt32|4||||
| |- - 12_December|O3EInt32|4||||
| |- [LastYear](## "Energy Consumption Domestic Hot Water Last Year")|*O3EList*|48||||
| |- - 01_January|O3EInt32|4||||
| |- - 02_February|O3EInt32|4||||
| |- - 03_March|O3EInt32|4||||
| |- - 04_April|O3EInt32|4||||
| |- - 05_May|O3EInt32|4||||
| |- - 06_June|O3EInt32|4||||
| |- - 07_July|O3EInt32|4||||
| |- - 08_August|O3EInt32|4||||
| |- - 09_September|O3EInt32|4||||
| |- - 10_October|O3EInt32|4||||
| |- - 11_November|O3EInt32|4||||
| |- - 12_December|O3EInt32|4||||
|**1334**|[**EnergyConsumptionCoolingYearMatrix**](## "Energy Consumption Cooling Per Year")|*O3EComplexType*|96||ro||
| |- [CurrentYear](## "Energy Consumption Cooling Current Year")|*O3EList*|48||||
| |- - 01_January|O3EInt32|4||||
| |- - 02_February|O3EInt32|4||||
| |- - 03_March|O3EInt32|4||||
| |- - 04_April|O3EInt32|4||||
| |- - 05_May|O3EInt32|4||||
| |- - 06_June|O3EInt32|4||||
| |- - 07_July|O3EInt32|4||||
| |- - 08_August|O3EInt32|4||||
| |- - 09_September|O3EInt32|4||||
| |- - 10_October|O3EInt32|4||||
| |- - 11_November|O3EInt32|4||||
| |- - 12_December|O3EInt32|4||||
| |- [LastYear](## "Energy Consumption Cooling Last Year")|*O3EList*|48||||
| |- - 01_January|O3EInt32|4||||
| |- - 02_February|O3EInt32|4||||
| |- - 03_March|O3EInt32|4||||
| |- - 04_April|O3EInt32|4||||
| |- - 05_May|O3EInt32|4||||
| |- - 06_June|O3EInt32|4||||
| |- - 07_July|O3EInt32|4||||
| |- - 08_August|O3EInt32|4||||
| |- - 09_September|O3EInt32|4||||
| |- - 10_October|O3EInt32|4||||
| |- - 11_November|O3EInt32|4||||
| |- - 12_December|O3EInt32|4||||
|**1335**|[**GeneratedElectricityYearMatrix**](## "Generated Electricity Per Year")|*O3EComplexType*|96||ro||
| |- CurrentYear|*O3EList*|48||||
| |- - 01_January|O3EInt32|4||||
| |- - 02_February|O3EInt32|4||||
| |- - 03_March|O3EInt32|4||||
| |- - 04_April|O3EInt32|4||||
| |- - 05_May|O3EInt32|4||||
| |- - 06_June|O3EInt32|4||||
| |- - 07_July|O3EInt32|4||||
| |- - 08_August|O3EInt32|4||||
| |- - 09_September|O3EInt32|4||||
| |- - 10_October|O3EInt32|4||||
| |- - 11_November|O3EInt32|4||||
| |- - [12_December](## "Generated Electricity Current Year")|O3EInt32|4||||
| |- LastYear|*O3EList*|48||||
| |- - 01_January|O3EInt32|4||||
| |- - 02_February|O3EInt32|4||||
| |- - 03_March|O3EInt32|4||||
| |- - 04_April|O3EInt32|4||||
| |- - 05_May|O3EInt32|4||||
| |- - 06_June|O3EInt32|4||||
| |- - 07_July|O3EInt32|4||||
| |- - 08_August|O3EInt32|4||||
| |- - 09_September|O3EInt32|4||||
| |- - 10_October|O3EInt32|4||||
| |- - 11_November|O3EInt32|4||||
| |- - [12_December](## "Generated Electricity Last Year")|O3EInt32|4||||
|**1336**|[**SolarEnergyYieldYearMatrix**](## "Solar Energy Yield Per Month")|*O3EComplexType*|96||ro||
| |- [CurrentYear](## "Solar Energy Yield Current Year")|*O3EList*|48||||
| |- - 01_January|O3EInt32|4||||
| |- - 02_February|O3EInt32|4||||
| |- - 03_March|O3EInt32|4||||
| |- - 04_April|O3EInt32|4||||
| |- - 05_May|O3EInt32|4||||
| |- - 06_June|O3EInt32|4||||
| |- - 07_July|O3EInt32|4||||
| |- - 08_August|O3EInt32|4||||
| |- - 09_September|O3EInt32|4||||
| |- - 10_October|O3EInt32|4||||
| |- - 11_November|O3EInt32|4||||
| |- - 12_December|O3EInt32|4||||
| |- [LastYear](## "Solar Energy Yield Last Year")|*O3EList*|48||||
| |- - 01_January|O3EInt32|4||||
| |- - 02_February|O3EInt32|4||||
| |- - 03_March|O3EInt32|4||||
| |- - 04_April|O3EInt32|4||||
| |- - 05_May|O3EInt32|4||||
| |- - 06_June|O3EInt32|4||||
| |- - 07_July|O3EInt32|4||||
| |- - 08_August|O3EInt32|4||||
| |- - 09_September|O3EInt32|4||||
| |- - 10_October|O3EInt32|4||||
| |- - 11_November|O3EInt32|4||||
| |- - 12_December|O3EInt32|4||||
|**1337**|[**GeneratedCentralHeatingOutputYearMatrix**](## "Generated Central Heating Output Per Year")|*O3EComplexType*|96||ro||
| |- [CurrentYear](## "Generated Central Heating Output Current Year")|*O3EList*|48||||
| |- - 01_January|O3EInt32|4||||
| |- - 02_February|O3EInt32|4||||
| |- - 03_March|O3EInt32|4||||
| |- - 04_April|O3EInt32|4||||
| |- - 05_May|O3EInt32|4||||
| |- - 06_June|O3EInt32|4||||
| |- - 07_July|O3EInt32|4||||
| |- - 08_August|O3EInt32|4||||
| |- - 09_September|O3EInt32|4||||
| |- - 10_October|O3EInt32|4||||
| |- - 11_November|O3EInt32|4||||
| |- - 12_December|O3EInt32|4||||
| |- [LastYear](## "Generated Central Heating Output Last Year")|*O3EList*|48||||
| |- - 01_January|O3EInt32|4||||
| |- - 02_February|O3EInt32|4||||
| |- - 03_March|O3EInt32|4||||
| |- - 04_April|O3EInt32|4||||
| |- - 05_May|O3EInt32|4||||
| |- - 06_June|O3EInt32|4||||
| |- - 07_July|O3EInt32|4||||
| |- - 08_August|O3EInt32|4||||
| |- - 09_September|O3EInt32|4||||
| |- - 10_October|O3EInt32|4||||
| |- - 11_November|O3EInt32|4||||
| |- - 12_December|O3EInt32|4||||
|**1338**|**ScreedDryingProfileDefinition**|RawCodec|31||ro||
|**1339**|**MalfunctionHeatingUnitBlocked**|O3EByteVal|1||ro||
|**1340**|**FuelCellGeneratedHeatOutputMonthMatrix**|*O3EComplexType*|124||ro||
| |- CurrentMonth|*O3EList*|62||||
| |- - 01|O3EInt16|2||||
| |- - 02|O3EInt16|2||||
| |- - 03|O3EInt16|2||||
| |- - 04|O3EInt16|2||||
| |- - 05|O3EInt16|2||||
| |- - 06|O3EInt16|2||||
| |- - 07|O3EInt16|2||||
| |- - 08|O3EInt16|2||||
| |- - 09|O3EInt16|2||||
| |- - 10|O3EInt16|2||||
| |- - 11|O3EInt16|2||||
| |- - 12|O3EInt16|2||||
| |- - 13|O3EInt16|2||||
| |- - 14|O3EInt16|2||||
| |- - 15|O3EInt16|2||||
| |- - 16|O3EInt16|2||||
| |- - 17|O3EInt16|2||||
| |- - 18|O3EInt16|2||||
| |- - 19|O3EInt16|2||||
| |- - 20|O3EInt16|2||||
| |- - 21|O3EInt16|2||||
| |- - 22|O3EInt16|2||||
| |- - 23|O3EInt16|2||||
| |- - 24|O3EInt16|2||||
| |- - 25|O3EInt16|2||||
| |- - 26|O3EInt16|2||||
| |- - 27|O3EInt16|2||||
| |- - 28|O3EInt16|2||||
| |- - 29|O3EInt16|2||||
| |- - 30|O3EInt16|2||||
| |- - 31|O3EInt16|2||||
| |- LastMonth|*O3EList*|62||||
| |- - 01|O3EInt16|2||||
| |- - 02|O3EInt16|2||||
| |- - 03|O3EInt16|2||||
| |- - 04|O3EInt16|2||||
| |- - 05|O3EInt16|2||||
| |- - 06|O3EInt16|2||||
| |- - 07|O3EInt16|2||||
| |- - 08|O3EInt16|2||||
| |- - 09|O3EInt16|2||||
| |- - 10|O3EInt16|2||||
| |- - 11|O3EInt16|2||||
| |- - 12|O3EInt16|2||||
| |- - 13|O3EInt16|2||||
| |- - 14|O3EInt16|2||||
| |- - 15|O3EInt16|2||||
| |- - 16|O3EInt16|2||||
| |- - 17|O3EInt16|2||||
| |- - 18|O3EInt16|2||||
| |- - 19|O3EInt16|2||||
| |- - 20|O3EInt16|2||||
| |- - 21|O3EInt16|2||||
| |- - 22|O3EInt16|2||||
| |- - 23|O3EInt16|2||||
| |- - 24|O3EInt16|2||||
| |- - 25|O3EInt16|2||||
| |- - 26|O3EInt16|2||||
| |- - 27|O3EInt16|2||||
| |- - 28|O3EInt16|2||||
| |- - 29|O3EInt16|2||||
| |- - 30|O3EInt16|2||||
| |- - 31|O3EInt16|2||||
|**1341**|**FuelCellGeneratedHeatOutputYearMatrix**|*O3EComplexType*|96||ro||
| |- CurrentYear|*O3EList*|48||||
| |- - 01_January|O3EInt32|4||||
| |- - 02_February|O3EInt32|4||||
| |- - 03_March|O3EInt32|4||||
| |- - 04_April|O3EInt32|4||||
| |- - 05_May|O3EInt32|4||||
| |- - 06_June|O3EInt32|4||||
| |- - 07_July|O3EInt32|4||||
| |- - 08_August|O3EInt32|4||||
| |- - 09_September|O3EInt32|4||||
| |- - 10_October|O3EInt32|4||||
| |- - 11_November|O3EInt32|4||||
| |- - 12_December|O3EInt32|4||||
| |- LastYear|*O3EList*|48||||
| |- - 01_January|O3EInt32|4||||
| |- - 02_February|O3EInt32|4||||
| |- - 03_March|O3EInt32|4||||
| |- - 04_April|O3EInt32|4||||
| |- - 05_May|O3EInt32|4||||
| |- - 06_June|O3EInt32|4||||
| |- - 07_July|O3EInt32|4||||
| |- - 08_August|O3EInt32|4||||
| |- - 09_September|O3EInt32|4||||
| |- - 10_October|O3EInt32|4||||
| |- - 11_November|O3EInt32|4||||
| |- - 12_December|O3EInt32|4||||
|**1342**|**GasConsumptionCentralHeatingMonthMatrix**|*O3EComplexType*|124||ro||
| |- CurrentMonth|*O3EList*|62||||
| |- - 01|O3EInt16|2||||
| |- - 02|O3EInt16|2||||
| |- - 03|O3EInt16|2||||
| |- - 04|O3EInt16|2||||
| |- - 05|O3EInt16|2||||
| |- - 06|O3EInt16|2||||
| |- - 07|O3EInt16|2||||
| |- - 08|O3EInt16|2||||
| |- - 09|O3EInt16|2||||
| |- - 10|O3EInt16|2||||
| |- - 11|O3EInt16|2||||
| |- - 12|O3EInt16|2||||
| |- - 13|O3EInt16|2||||
| |- - 14|O3EInt16|2||||
| |- - 15|O3EInt16|2||||
| |- - 16|O3EInt16|2||||
| |- - 17|O3EInt16|2||||
| |- - 18|O3EInt16|2||||
| |- - 19|O3EInt16|2||||
| |- - 20|O3EInt16|2||||
| |- - 21|O3EInt16|2||||
| |- - 22|O3EInt16|2||||
| |- - 23|O3EInt16|2||||
| |- - 24|O3EInt16|2||||
| |- - 25|O3EInt16|2||||
| |- - 26|O3EInt16|2||||
| |- - 27|O3EInt16|2||||
| |- - 28|O3EInt16|2||||
| |- - 29|O3EInt16|2||||
| |- - 30|O3EInt16|2||||
| |- - 31|O3EInt16|2||||
| |- LastMonth|*O3EList*|62||||
| |- - 01|O3EInt16|2||||
| |- - 02|O3EInt16|2||||
| |- - 03|O3EInt16|2||||
| |- - 04|O3EInt16|2||||
| |- - 05|O3EInt16|2||||
| |- - 06|O3EInt16|2||||
| |- - 07|O3EInt16|2||||
| |- - 08|O3EInt16|2||||
| |- - 09|O3EInt16|2||||
| |- - 10|O3EInt16|2||||
| |- - 11|O3EInt16|2||||
| |- - 12|O3EInt16|2||||
| |- - 13|O3EInt16|2||||
| |- - 14|O3EInt16|2||||
| |- - 15|O3EInt16|2||||
| |- - 16|O3EInt16|2||||
| |- - 17|O3EInt16|2||||
| |- - 18|O3EInt16|2||||
| |- - 19|O3EInt16|2||||
| |- - 20|O3EInt16|2||||
| |- - 21|O3EInt16|2||||
| |- - 22|O3EInt16|2||||
| |- - 23|O3EInt16|2||||
| |- - 24|O3EInt16|2||||
| |- - 25|O3EInt16|2||||
| |- - 26|O3EInt16|2||||
| |- - 27|O3EInt16|2||||
| |- - 28|O3EInt16|2||||
| |- - 29|O3EInt16|2||||
| |- - 30|O3EInt16|2||||
| |- - 31|O3EInt16|2||||
|**1343**|**GasConsumptionCentralHeatingYearMatrix**|*O3EComplexType*|48||ro||
| |- CurrentYear|*O3EList*|24||||
| |- - 01_January|O3EInt16|2||||
| |- - 02_February|O3EInt16|2||||
| |- - 03_March|O3EInt16|2||||
| |- - 04_April|O3EInt16|2||||
| |- - 05_May|O3EInt16|2||||
| |- - 06_June|O3EInt16|2||||
| |- - 07_July|O3EInt16|2||||
| |- - 08_August|O3EInt16|2||||
| |- - 09_September|O3EInt16|2||||
| |- - 10_October|O3EInt16|2||||
| |- - 11_November|O3EInt16|2||||
| |- - 12_December|O3EInt16|2||||
| |- LastYear|*O3EList*|24||||
| |- - 01_January|O3EInt16|2||||
| |- - 02_February|O3EInt16|2||||
| |- - 03_March|O3EInt16|2||||
| |- - 04_April|O3EInt16|2||||
| |- - 05_May|O3EInt16|2||||
| |- - 06_June|O3EInt16|2||||
| |- - 07_July|O3EInt16|2||||
| |- - 08_August|O3EInt16|2||||
| |- - 09_September|O3EInt16|2||||
| |- - 10_October|O3EInt16|2||||
| |- - 11_November|O3EInt16|2||||
| |- - 12_December|O3EInt16|2||||
|**1344**|**GasConsumptionDomesticHotWaterMonthMatrix**|*O3EComplexType*|124||ro||
| |- CurrentMonth|*O3EList*|62||||
| |- - 01|O3EInt16|2||||
| |- - 02|O3EInt16|2||||
| |- - 03|O3EInt16|2||||
| |- - 04|O3EInt16|2||||
| |- - 05|O3EInt16|2||||
| |- - 06|O3EInt16|2||||
| |- - 07|O3EInt16|2||||
| |- - 08|O3EInt16|2||||
| |- - 09|O3EInt16|2||||
| |- - 10|O3EInt16|2||||
| |- - 11|O3EInt16|2||||
| |- - 12|O3EInt16|2||||
| |- - 13|O3EInt16|2||||
| |- - 14|O3EInt16|2||||
| |- - 15|O3EInt16|2||||
| |- - 16|O3EInt16|2||||
| |- - 17|O3EInt16|2||||
| |- - 18|O3EInt16|2||||
| |- - 19|O3EInt16|2||||
| |- - 20|O3EInt16|2||||
| |- - 21|O3EInt16|2||||
| |- - 22|O3EInt16|2||||
| |- - 23|O3EInt16|2||||
| |- - 24|O3EInt16|2||||
| |- - 25|O3EInt16|2||||
| |- - 26|O3EInt16|2||||
| |- - 27|O3EInt16|2||||
| |- - 28|O3EInt16|2||||
| |- - 29|O3EInt16|2||||
| |- - 30|O3EInt16|2||||
| |- - 31|O3EInt16|2||||
| |- LastMonth|*O3EList*|62||||
| |- - 01|O3EInt16|2||||
| |- - 02|O3EInt16|2||||
| |- - 03|O3EInt16|2||||
| |- - 04|O3EInt16|2||||
| |- - 05|O3EInt16|2||||
| |- - 06|O3EInt16|2||||
| |- - 07|O3EInt16|2||||
| |- - 08|O3EInt16|2||||
| |- - 09|O3EInt16|2||||
| |- - 10|O3EInt16|2||||
| |- - 11|O3EInt16|2||||
| |- - 12|O3EInt16|2||||
| |- - 13|O3EInt16|2||||
| |- - 14|O3EInt16|2||||
| |- - 15|O3EInt16|2||||
| |- - 16|O3EInt16|2||||
| |- - 17|O3EInt16|2||||
| |- - 18|O3EInt16|2||||
| |- - 19|O3EInt16|2||||
| |- - 20|O3EInt16|2||||
| |- - 21|O3EInt16|2||||
| |- - 22|O3EInt16|2||||
| |- - 23|O3EInt16|2||||
| |- - 24|O3EInt16|2||||
| |- - 25|O3EInt16|2||||
| |- - 26|O3EInt16|2||||
| |- - 27|O3EInt16|2||||
| |- - 28|O3EInt16|2||||
| |- - 29|O3EInt16|2||||
| |- - 30|O3EInt16|2||||
| |- - 31|O3EInt16|2||||
|**1345**|**GasConsumptionDomesticHotWaterYearMatrix**|*O3EComplexType*|48||ro||
| |- CurrentYear|*O3EList*|24||||
| |- - 01_January|O3EInt16|2||||
| |- - 02_February|O3EInt16|2||||
| |- - 03_March|O3EInt16|2||||
| |- - 04_April|O3EInt16|2||||
| |- - 05_May|O3EInt16|2||||
| |- - 06_June|O3EInt16|2||||
| |- - 07_July|O3EInt16|2||||
| |- - 08_August|O3EInt16|2||||
| |- - 09_September|O3EInt16|2||||
| |- - 10_October|O3EInt16|2||||
| |- - 11_November|O3EInt16|2||||
| |- - 12_December|O3EInt16|2||||
| |- LastYear|*O3EList*|24||||
| |- - 01_January|O3EInt16|2||||
| |- - 02_February|O3EInt16|2||||
| |- - 03_March|O3EInt16|2||||
| |- - 04_April|O3EInt16|2||||
| |- - 05_May|O3EInt16|2||||
| |- - 06_June|O3EInt16|2||||
| |- - 07_July|O3EInt16|2||||
| |- - 08_August|O3EInt16|2||||
| |- - 09_September|O3EInt16|2||||
| |- - 10_October|O3EInt16|2||||
| |- - 11_November|O3EInt16|2||||
| |- - 12_December|O3EInt16|2||||
|**1346**|**HeatEngineStatistical**|*O3EComplexType*|12||ro||
| |- OperatingHours|O3EInt32|4||||
| |- BurnerHours|O3EInt32|4||||
| |- BurnerStarts|O3EInt32|4||||
|**1347**|**ObjectElectricalEnergyStatus**|RawCodec|10||ro||
|**1348**|**FuelCellGasConsumption**|*O3EComplexType*|12||ro||
| |- Today|O3EInt16|2||||
| |- Week|O3EInt16|2||||
| |- CurrentMonth|O3EInt16|2||||
| |- PastMonth|O3EInt16|2||||
| |- CurrentYear|O3EInt16|2||||
| |- PastYear|O3EInt16|2||||
|**1349**|**FuelCellGasConsumptionMonthMatrix**|RawCodec|124||ro||
|**1350**|**FuelCellGasConsumptionYearMatrix**|RawCodec|48||ro||
|**1351**|**FeedInEnergy**|RawCodec|24||ro||
|**1352**|**FeedInEnergyMonthMatrix**|RawCodec|124||ro||
|**1353**|**FeedInEnergyYearMatrix**|RawCodec|96||ro||
|**1354**|**ProductionCoverageRate**|RawCodec|6||ro||
|**1355**|**ProductionCoverageRateMonthMatrix**|RawCodec|62||ro||
|**1356**|**ProductionCoverageRateYearMatrix**|RawCodec|24||ro||
|**1357**|**FuelCellOperationTime**|RawCodec|11||ro||
|**1358**|**FuelCellOperationTimeMonthMatrix**|RawCodec|124||ro||
|**1359**|**FuelCellOperationTimeYearMatrix**|RawCodec|48||ro||
|**1360**|**FuelCellRunTime**|RawCodec|11||ro||
|**1361**|**FuelCellRunTimeMonthMatrix**|RawCodec|124||ro||
|**1362**|**FuelCellRunTimeYearMatrix**|RawCodec|48||ro||
|**1363**|**FuelCellTargetOperationMode**|RawCodec|1||**rw**||
|**1364**|**GenericSdioAccessoryOneModulFunction**|O3EByteVal|1||ro||
|**1367**|**FuelCellThermalPower**|O3EInt16|2||ro||
|**1371**|**DemandCoverageRate**|RawCodec|6||ro||
|**1372**|**DemandCoverageRateMonthMatrix**|RawCodec|62||ro||
|**1373**|**DemandCoverageRateYearMatrix**|RawCodec|24||ro||
|**1383**|**FuelCellBreakdownRate**|RawCodec|11||ro||
|**1384**|**FuelCellBreakdownRateMonthMatrix**|RawCodec|124||ro||
|**1385**|**FuelCellBreakdownRateYearMatrix**|RawCodec|48||ro||
|**1389**|**CoTwoSavingsMonthMatrix**|RawCodec|124||ro||
|**1390**|**CoTwoSavingsYearMatrix**|RawCodec|96||ro||
|**1391**|[**GeneratedDomesticHotWaterOutput**](## "Generated Domestic Hot Water Output per specific period")|*O3EComplexType*|24||ro||
| |- Today|O3EInt32|4|kWh|||
| |- Past7Days|O3EInt32|4|kWh|||
| |- CurrentMonth|O3EInt32|4|kWh|||
| |- PastMonth|O3EInt32|4|kWh|||
| |- CurrentYear|O3EInt32|4|kWh|||
| |- PastYear|O3EInt32|4|kWh|||
|**1392**|[**GeneratedDomesticHotWaterOutputMonthMatrix**](## "Generated Domestic Hot Water Output Per Month")|*O3EComplexType*|124||ro||
| |- [CurrentMonth](## "Generated Domestic Hot Water Output Current Month")|*O3EList*|62||||
| |- - 01|O3EInt16|2|kWh|||
| |- - 02|O3EInt16|2|kWh|||
| |- - 03|O3EInt16|2|kWh|||
| |- - 04|O3EInt16|2|kWh|||
| |- - 05|O3EInt16|2|kWh|||
| |- - 06|O3EInt16|2|kWh|||
| |- - 07|O3EInt16|2|kWh|||
| |- - 08|O3EInt16|2|kWh|||
| |- - 09|O3EInt16|2|kWh|||
| |- - 10|O3EInt16|2|kWh|||
| |- - 11|O3EInt16|2|kWh|||
| |- - 12|O3EInt16|2|kWh|||
| |- - 13|O3EInt16|2|kWh|||
| |- - 14|O3EInt16|2|kWh|||
| |- - 15|O3EInt16|2|kWh|||
| |- - 16|O3EInt16|2|kWh|||
| |- - 17|O3EInt16|2|kWh|||
| |- - 18|O3EInt16|2|kWh|||
| |- - 19|O3EInt16|2|kWh|||
| |- - 20|O3EInt16|2|kWh|||
| |- - 21|O3EInt16|2|kWh|||
| |- - 22|O3EInt16|2|kWh|||
| |- - 23|O3EInt16|2|kWh|||
| |- - 24|O3EInt16|2|kWh|||
| |- - 25|O3EInt16|2|kWh|||
| |- - 26|O3EInt16|2|kWh|||
| |- - 27|O3EInt16|2|kWh|||
| |- - 28|O3EInt16|2|kWh|||
| |- - 29|O3EInt16|2|kWh|||
| |- - 30|O3EInt16|2|kWh|||
| |- - 31|O3EInt16|2|kWh|||
| |- [LastMonth](## "Generated Domestic Hot Water Output Previous Month")|*O3EList*|62||||
| |- - 01|O3EInt16|2|kWh|||
| |- - 02|O3EInt16|2|kWh|||
| |- - 03|O3EInt16|2|kWh|||
| |- - 04|O3EInt16|2|kWh|||
| |- - 05|O3EInt16|2|kWh|||
| |- - 06|O3EInt16|2|kWh|||
| |- - 07|O3EInt16|2|kWh|||
| |- - 08|O3EInt16|2|kWh|||
| |- - 09|O3EInt16|2|kWh|||
| |- - 10|O3EInt16|2|kWh|||
| |- - 11|O3EInt16|2|kWh|||
| |- - 12|O3EInt16|2|kWh|||
| |- - 13|O3EInt16|2|kWh|||
| |- - 14|O3EInt16|2|kWh|||
| |- - 15|O3EInt16|2|kWh|||
| |- - 16|O3EInt16|2|kWh|||
| |- - 17|O3EInt16|2|kWh|||
| |- - 18|O3EInt16|2|kWh|||
| |- - 19|O3EInt16|2|kWh|||
| |- - 20|O3EInt16|2|kWh|||
| |- - 21|O3EInt16|2|kWh|||
| |- - 22|O3EInt16|2|kWh|||
| |- - 23|O3EInt16|2|kWh|||
| |- - 24|O3EInt16|2|kWh|||
| |- - 25|O3EInt16|2|kWh|||
| |- - 26|O3EInt16|2|kWh|||
| |- - 27|O3EInt16|2|kWh|||
| |- - 28|O3EInt16|2|kWh|||
| |- - 29|O3EInt16|2|kWh|||
| |- - 30|O3EInt16|2|kWh|||
| |- - 31|O3EInt16|2|kWh|||
|**1393**|[**GeneratedDomesticHotWaterOutputYearMatrix**](## "Generated Domestic Hot Water Output Per Year")|*O3EComplexType*|96||ro||
| |- [CurrentYear](## "Generated Domestic Hot Water Output Current Year")|*O3EList*|48||||
| |- - 01_January|O3EInt32|4|kWh|||
| |- - 02_February|O3EInt32|4|kWh|||
| |- - 03_March|O3EInt32|4|kWh|||
| |- - 04_April|O3EInt32|4|kWh|||
| |- - 05_May|O3EInt32|4|kWh|||
| |- - 06_June|O3EInt32|4|kWh|||
| |- - 07_July|O3EInt32|4|kWh|||
| |- - 08_August|O3EInt32|4|kWh|||
| |- - 09_September|O3EInt32|4|kWh|||
| |- - 10_October|O3EInt32|4|kWh|||
| |- - 11_November|O3EInt32|4|kWh|||
| |- - 12_December|O3EInt32|4|kWh|||
| |- [LastYear](## "Generated Domestic Hot Water Output Last Year")|*O3EList*|48||||
| |- - 01_January|O3EInt32|4|kWh|||
| |- - 02_February|O3EInt32|4|kWh|||
| |- - 03_March|O3EInt32|4|kWh|||
| |- - 04_April|O3EInt32|4|kWh|||
| |- - 05_May|O3EInt32|4|kWh|||
| |- - 06_June|O3EInt32|4|kWh|||
| |- - 07_July|O3EInt32|4|kWh|||
| |- - 08_August|O3EInt32|4|kWh|||
| |- - 09_September|O3EInt32|4|kWh|||
| |- - 10_October|O3EInt32|4|kWh|||
| |- - 11_November|O3EInt32|4|kWh|||
| |- - 12_December|O3EInt32|4|kWh|||
|**1394**|**SolarChargingDomesticHotWaterSetpoint**|O3EInt16|2||**rw**||
|**1395**|**MixerOneCircuitSummerSavingTemperatureThreshold**|*O3EComplexType*|3||ro||
| |- State|O3EByteVal|1||||
| |- Temperature|O3EInt16|2||||
|**1396**|**MixerTwoCircuitSummerSavingTemperatureThreshold**|*O3EComplexType*|3||ro||
| |- State|O3EByteVal|1||||
| |- Temperature|O3EInt16|2||||
|**1397**|**MixerThreeCircuitSummerSavingTemperatureThreshold**|*O3EComplexType*|3||ro||
| |- State|O3EByteVal|1||||
| |- Temperature|O3EInt16|2||||
|**1398**|**MixerFourCircuitSummerSavingTemperatureThreshold**|*O3EComplexType*|3||ro||
| |- State|O3EByteVal|1||||
| |- Temperature|O3EInt16|2||||
|**1411**|**ResetServiceInterval**|O3EByteVal|1||ro||
|**1415**|[**MixerOneCircuitOperationState**](## "Heating curcuit 1: Operating Mode")|*O3EComplexType*|2||**rw**||
| |- [Mode](## "Requested Operating Mode {0: Off, 1: Heating, 2: Parallel Operation: Heating HotWater, 3: Parallel Operation: Heating Cooling, 4: TestMode, 5: Cooling, 255: Automatic}")|O3EEnum|1||||
| |- [State](## "Actual Operating Mode {0: ShutDown, 1: Reduced, 2: Normal, 3: Comfort, 5: Fixed Value, 6: Antifreeze protection, 7: Energy Save: reduced, 8: Energy Save: normal, 9: Energy Save: comfort, 10: Cooling: normal, 11: Cooling: comfort, 12: No request}")|O3EEnum|1||||
|**1416**|[**MixerTwoCircuitOperationState**](## "Heating curcuit 2: Operating Mode")|*O3EComplexType*|2||**rw**||
| |- [Mode](## "Requested Operating Mode {0: Off, 1: Heating, 2: Parallel Operation: Heating HotWater, 3: Parallel Operation: Heating Cooling, 4: TestMode, 5: Cooling, 255: Automatic}")|O3EEnum|1||||
| |- [State](## "Actual Operating Mode {0: ShutDown, 1: Reduced, 2: Normal, 3: Comfort, 5: Fixed Value, 6: Antifreeze protection, 7: Energy Save: reduced, 8: Energy Save: normal, 9: Energy Save: comfort, 10: Cooling: normal, 11: Cooling: comfort, 12: No request}")|O3EEnum|1||||
|**1417**|[**MixerThreeCircuitOperationState**](## "Heating curcuit 3: Operating Mode")|*O3EComplexType*|2||**rw**||
| |- [Mode](## "Requested Operating Mode {0: Off, 1: Heating, 2: Parallel Operation: Heating HotWater, 3: Parallel Operation: Heating Cooling, 4: TestMode, 5: Cooling, 255: Automatic}")|O3EEnum|1||||
| |- [State](## "Actual Operating Mode {0: ShutDown, 1: Reduced, 2: Normal, 3: Comfort, 5: Fixed Value, 6: Antifreeze protection, 7: Energy Save: reduced, 8: Energy Save: normal, 9: Energy Save: comfort, 10: Cooling: normal, 11: Cooling: comfort, 12: No request}")|O3EEnum|1||||
|**1418**|[**MixerFourCircuitOperationState**](## "Heating curcuit 4: Operating Mode")|*O3EComplexType*|2||**rw**||
| |- [Mode](## "Requested Operating Mode {0: Off, 1: Heating, 2: Parallel Operation: Heating HotWater, 3: Parallel Operation: Heating Cooling, 4: TestMode, 5: Cooling, 255: Automatic}")|O3EEnum|1||||
| |- [State](## "Actual Operating Mode {0: ShutDown, 1: Reduced, 2: Normal, 3: Comfort, 5: Fixed Value, 6: Antifreeze protection, 7: Energy Save: reduced, 8: Energy Save: normal, 9: Energy Save: comfort, 10: Cooling: normal, 11: Cooling: comfort, 12: No request}")|O3EEnum|1||||
|**1419**|[**MixerFiveCircuitOperationState**](## "Heating curcuit 5: Operating Mode")|*O3EComplexType*|2||**rw**||
| |- [Mode](## "Requested Operating Mode {0: Off, 1: Heating, 2: Parallel Operation: Heating HotWater, 3: Parallel Operation: Heating Cooling, 4: TestMode, 5: Cooling, 255: Automatic}")|O3EEnum|1||||
| |- [State](## "Actual Operating Mode {0: ShutDown, 1: Reduced, 2: Normal, 3: Comfort, 5: Fixed Value, 6: Antifreeze protection, 7: Energy Save: reduced, 8: Energy Save: normal, 9: Energy Save: comfort, 10: Cooling: normal, 11: Cooling: comfort, 12: No request}")|O3EEnum|1||||
|**1420**|[**MixerSixCircuitOperationState**](## "Heating curcuit 6: Operating Mode")|*O3EComplexType*|2||**rw**||
| |- [Mode](## "Requested Operating Mode {0: Off, 1: Heating, 2: Parallel Operation: Heating HotWater, 3: Parallel Operation: Heating Cooling, 4: TestMode, 5: Cooling, 255: Automatic}")|O3EEnum|1||||
| |- [State](## "Actual Operating Mode {0: ShutDown, 1: Reduced, 2: Normal, 3: Comfort, 5: Fixed Value, 6: Antifreeze protection, 7: Energy Save: reduced, 8: Energy Save: normal, 9: Energy Save: comfort, 10: Cooling: normal, 11: Cooling: comfort, 12: No request}")|O3EEnum|1||||
|**1421**|[**MixerSevenCircuitOperationState**](## "Heating curcuit 7: Operating Mode")|*O3EComplexType*|2||**rw**||
| |- [Mode](## "Requested Operating Mode {0: Off, 1: Heating, 2: Parallel Operation: Heating HotWater, 3: Parallel Operation: Heating Cooling, 4: TestMode, 5: Cooling, 255: Automatic}")|O3EEnum|1||||
| |- [State](## "Actual Operating Mode {0: ShutDown, 1: Reduced, 2: Normal, 3: Comfort, 5: Fixed Value, 6: Antifreeze protection, 7: Energy Save: reduced, 8: Energy Save: normal, 9: Energy Save: comfort, 10: Cooling: normal, 11: Cooling: comfort, 12: No request}")|O3EEnum|1||||
|**1422**|[**MixerEightCircuitOperationState**](## "Heating curcuit 8: Operating Mode")|*O3EComplexType*|2||**rw**||
| |- [Mode](## "Requested Operating Mode {0: Off, 1: Heating, 2: Parallel Operation: Heating HotWater, 3: Parallel Operation: Heating Cooling, 4: TestMode, 5: Cooling, 255: Automatic}")|O3EEnum|1||||
| |- [State](## "Actual Operating Mode {0: ShutDown, 1: Reduced, 2: Normal, 3: Comfort, 5: Fixed Value, 6: Antifreeze protection, 7: Energy Save: reduced, 8: Energy Save: normal, 9: Energy Save: comfort, 10: Cooling: normal, 11: Cooling: comfort, 12: No request}")|O3EEnum|1||||
|**1431**|**CarbonEmissionSettings**|RawCodec|8||ro||
|**1432**|**CentralHeatingPumpPerformance**|*O3EComplexType*|4||ro||
| |- Unknown|RawCodec|2||||
| |- ResidualHead|O3EByteVal|1||||
| |- DifferentialPressure|O3EByteVal|1||||
|**1434**|**ResetFuelCellStatistics**|RawCodec|1||ro||
|**1435**|**FluelCellFlowTemperatueSensor**|*O3EComplexType*|9||ro||
| |- Actual|O3EInt16|2||||
| |- Minimum|O3EInt16|2||||
| |- Maximum|O3EInt16|2||||
| |- Average|O3EInt16|2||||
| |- Error|O3EByteVal|1||||
|**1436**|**FuelCellReturnTemperatureSensor**|*O3EComplexType*|9||ro||
| |- Actual|O3EInt16|2||||
| |- Minimum|O3EInt16|2||||
| |- Maximum|O3EInt16|2||||
| |- Average|O3EInt16|2||||
| |- Error|O3EByteVal|1||||
|**1439**|**NoiseReductionTimeScheduleMonday**|RawCodec|41||**rw**||
|**1440**|**NoiseReductionTimeScheduleTuesday**|RawCodec|41||**rw**||
|**1441**|**NoiseReductionTimeScheduleWednesday**|RawCodec|41||**rw**||
|**1442**|**NoiseReductionTimeScheduleThursday**|RawCodec|41||**rw**||
|**1443**|**NoiseReductionTimeScheduleFriday**|RawCodec|41||**rw**||
|**1444**|**NoiseReductionTimeScheduleSaturday**|RawCodec|41||**rw**||
|**1445**|**NoiseReductionTimeScheduleSunday**|RawCodec|41||**rw**||
|**1451**|**ApplicationChecksum**|RawCodec|4||ro||
|**1467**|**SafetyRelevantRemoteUnlock**|RawCodec|2||ro||
|**1468**|**FuelCellGasPressure**|RawCodec|9||ro||
|**1469**|**SensorActuatorTestGroupHeatEngine**|RawCodec|31||ro||
|**1470**|**SensorActuatorTestGroupDomesticHotWater**|RawCodec|31||ro||
|**1471**|**SensorActuatorTestGroupFuelCell**|RawCodec|31||ro||
|**1472**|**SensorActuatorTestGroupHeatingCircuit**|RawCodec|31||ro||
|**1473**|**SensorActuatorTestGroupSolar**|RawCodec|31||ro||
|**1492**|**SolarCircuitPumpHysteresis**|RawCodec|4||ro||
|**1493**|**HeatEnginePerformanceStatistics**|*O3EComplexType*|16||ro||
| |- HoursLoadClassOne|O3EInt32|4||||
| |- HoursLoadClassTwo|O3EInt32|4||||
| |- HoursLoadClassThree|O3EInt32|4||||
| |- HoursLoadClassFour|O3EInt32|4||||
|**1494**|**OemProductVersion**|O3ESoftVers|8||ro||
|**1503**|**MinimumLoadPercent**|RawCodec|1||ro||
|**1504**|[**TimeSettingSource**](## "{0: Local, 1: SuperordinateSystem, 2: NetworkTimeProtocol, 3: TCU}")|O3EEnum|1||ro||
|**1505**|**SolarStagnationTemperatureOffset**|RawCodec|2||**rw**||
|**1529**|**SolarRechargeSuppressionImpact**|O3EByteVal|1||ro||
|**1533**|**InstallationWizardInProgress**|RawCodec|2||ro||
|**1535**|**FlueGasSensorTestMode**|RawCodec|3||ro||
|**1536**|**PrimaryCircuitWaterFlowTestMode**|RawCodec|3||ro||
|**1537**|**ChimneySweeperTestMode**|RawCodec|3||ro||
|**1538**|**ZigbeeEnable**|O3EByteVal|1||ro||
|**1539**|**ZigbeeStatus**|O3EByteVal|1||ro||
|**1540**|**ZigbeeIdentification**|RawCodec|26||ro||
|**1541**|**LegionellaProtectionPump**|RawCodec|5||ro||
|**1549**|**HydraulicMatrixConfiguration**|RawCodec|97||ro||
|**1550**|**FunctionMatrix**|RawCodec|22||ro||
|**1551**|**FuelCellExternalControl**|RawCodec|1||ro||
|**1552**|**ElectricalEnergyStorageOperationState**|RawCodec|7||**rw**||
|**1553**|**ElectronicControlUnitOdxVersion**|RawCodec|6||ro||
|**1554**|**HeatingSupport**|RawCodec|2||ro||
|**1555**|**MixerOneCircuitFixedValueFlowTemperatureSetpoint**|RawCodec|6||**rw**||
|**1556**|**MixerTwoCircuitFixedValueFlowTemperatureSetpoint**|RawCodec|6||**rw**||
|**1557**|**MixerThreeCircuitFixedValueFlowTemperatureSetpoint**|RawCodec|6||**rw**||
|**1558**|**MixerFourCircuitFixedValueFlowTemperatureSetpoint**|RawCodec|6||**rw**||
|**1559**|**MixerFiveCircuitFixedValueFlowTemperatureSetpoint**|RawCodec|6||**rw**||
|**1560**|**MixerSixCircuitFixedValueFlowTemperatureSetpoint**|RawCodec|6||**rw**||
|**1561**|**MixerSevenCircuitFixedValueFlowTemperatureSetpoint**|RawCodec|6||**rw**||
|**1562**|**MixerEightCircuitFixedValueFlowTemperatureSetpoint**|RawCodec|6||**rw**||
|**1573**|**SystemReturnTemperatureSensor**|*O3EComplexType*|9||ro||
| |- Actual|O3EInt16|2||||
| |- Minimum|O3EInt16|2||||
| |- Maximum|O3EInt16|2||||
| |- Average|O3EInt16|2||||
| |- Error|O3EByteVal|1||||
|**1577**|**ElectricalEnergyStorageModuleOneOperatingData**|RawCodec|139||ro||
|**1578**|**ElectricalEnergyStorageModuleTwoOperatingData**|RawCodec|139||ro||
|**1579**|**ElectricalEnergyStorageModuleThreeOperatingData**|RawCodec|139||ro||
|**1580**|**ElectricalEnergyStorageModuleFourOperatingData**|RawCodec|139||ro||
|**1581**|**ElectricalEnergyStorageModuleFiveOperatingData**|RawCodec|139||ro||
|**1582**|**ElectricalEnergyStorageModuleSixOperatingData**|RawCodec|139||ro||
|**1585**|**IncreasedReturnTemperatureSetpoint**|RawCodec|2||**rw**||
|**1587**|**ExternalAlternatingCurrentPowerSetpointMetaData**|RawCodec|4||**rw**||
|**1588**|**AlternatingCurrentPowerSetpoint**|RawCodec|4||**rw**||
|**1589**|**AlternatingCurrentPowerSetpointMetaData**|RawCodec|4||**rw**||
|**1590**|**ElectricalEnergySystemOperationState**|RawCodec|6||**rw**||
|**1591**|**ElectricalEnergyInverterOperationState**|RawCodec|6||**rw**||
|**1592**|**ElectricalEnergyInverterPath**|RawCodec|1||ro||
|**1593**|**BufferHysteresis**|RawCodec|4||ro||
|**1594**|**LastApplicationUpdate**|O3ESdate|3||ro||
|**1595**|**ParameterIdentificationVersionFactory**|RawCodec|8||ro||
|**1596**|**IncreasedReturnTemperatureSensor**|*O3EComplexType*|9||ro||
| |- Actual|O3EInt16|2||||
| |- Minimum|O3EInt16|2||||
| |- Maximum|O3EInt16|2||||
| |- Average|O3EInt16|2||||
| |- Error|O3EByteVal|1||||
|**1598**|**SolarStaticTemperatureControlHysteresis**|RawCodec|4||ro||
|**1599**|**SolarSecondaryDeltaTemperatureHysteresis**|RawCodec|4||ro||
|**1600**|**BufferDischargeFunctionThreeWayValvePositionPercent**|RawCodec|2||ro||
|**1601**|**FuelCellCondition**|RawCodec|1||ro||
|**1603**|[**PointOfCommonCouplingPower**](## "Actual Power at Point of Common Coupling")|*O3EComplexType*|4||ro|[Link](https://github.com/open3e/open3e/wiki/036-DoI-%E2%80%90-Data-points-of-Interest/#data-points-of-vx3)|
| |- [ActivePower](## "Active Power")|O3EInt16|2|W|||
| |- [ReactivePower](## "Reactive Power")|O3EInt16|2|VA|||
|**1603**|[**PointOfCommonCouplingPower**](## "Actual Power at Point of Common Coupling")|*O3EComplexType*|12||ro||
| |- [ActivePower](## "Active Power")|O3EInt16|2|W|||
| |- [ReactivePower](## "Reactive Power")|O3EInt16|2|VA|||
| |- [ActivePowerDup](## "Active Power Duplicate")|O3EInt16|2|W|||
| |- PadZeros|O3EInt16|2||||
| |- [ReactivePowerDup](## "Reactive Power Duplicate")|O3EInt16|2|VA|||
| |- PadOnes|O3EInt16|2||||
|**1604**|**GatewayExternalTargetFlowTemperatureSetpoint**|RawCodec|2||**rw**||
|**1605**|**GatewayExternalHeatEngineTargetOperationMode**|*O3EComplexType*|2||**rw**||
| |- Mode|O3EByteVal|1||||
| |- State|O3EByteVal|1||||
|**1606**|**IntervalStrategyProperties**|*O3EComplexType*|8||ro||
| |- State|O3EByteVal|1||||
| |- unknown|RawCodec|1||||
| |- BurnerOffMinTime|O3EInt16|2||||
| |- BurnerOffMaxTime|O3EInt16|2||||
| |- IntegralValue|O3EInt16|2||||
|**1607**|**MalfunctionUnitBlocked**|O3EByteVal|1||ro||
|**1608**|**DifferentialTemperatureControllerHeatSourceTemperatureSensor**|*O3EComplexType*|9||ro||
| |- Actual|O3EInt16|2||||
| |- Minimum|O3EInt16|2||||
| |- Maximum|O3EInt16|2||||
| |- Average|O3EInt16|2||||
| |- [SensorStatus](## "{0: no_error, 1: interruption, 2: short_circuit, 3: electrical_fault, 4: not_available, 5: invalidates}")|O3EEnum|1||||
|**1609**|**DifferentialTemperatureControllerHeatSinkTemperatureSensor**|*O3EComplexType*|9||ro||
| |- Actual|O3EInt16|2||||
| |- Minimum|O3EInt16|2||||
| |- Maximum|O3EInt16|2||||
| |- Average|O3EInt16|2||||
| |- [SensorStatus](## "{0: no_error, 1: interruption, 2: short_circuit, 3: electrical_fault, 4: not_available, 5: invalidates}")|O3EEnum|1||||
|**1610**|**HeatingSupportBufferTemperatureSensor**|*O3EComplexType*|9||ro||
| |- Actual|O3EInt16|2||||
| |- Minimum|O3EInt16|2||||
| |- Maximum|O3EInt16|2||||
| |- Average|O3EInt16|2||||
| |- [SensorStatus](## "{0: no_error, 1: interruption, 2: short_circuit, 3: electrical_fault, 4: not_available, 5: invalidates}")|O3EEnum|1||||
|**1611**|**PreheatingReferenceTemperatureSensor**|*O3EComplexType*|9||ro||
| |- Actual|O3EInt16|2||||
| |- Minimum|O3EInt16|2||||
| |- Maximum|O3EInt16|2||||
| |- Average|O3EInt16|2||||
| |- [SensorStatus](## "{0: no_error, 1: interruption, 2: short_circuit, 3: electrical_fault, 4: not_available, 5: invalidates}")|O3EEnum|1||||
|**1612**|**ExternalMixerTwoCircuitTargetOperationMode**|*O3EComplexType*|2||**rw**||
| |- Mode|O3EByteVal|1||||
| |- State|O3EByteVal|1||||
|**1613**|**ExternalMixerThreeCircuitTargetOperationMode**|*O3EComplexType*|2||**rw**||
| |- Mode|O3EByteVal|1||||
| |- State|O3EByteVal|1||||
|**1614**|**ExternalMixerFourCircuitTargetOperationMode**|*O3EComplexType*|2||**rw**||
| |- Mode|O3EByteVal|1||||
| |- State|O3EByteVal|1||||
|**1627**|**ExternalMixerOneCircuitFixedValueTargetTemperatureSetpoint**|O3EInt16|2||**rw**||
|**1628**|**ExternalMixerTwoCircuitFixedValueTargetTemperatureSetpoint**|O3EInt16|2||**rw**||
|**1629**|**ExternalMixerThreeCircuitFixedValueTargetTemperatureSetpoint**|O3EInt16|2||**rw**||
|**1630**|**ExternalMixerFourCircuitFixedValueTargetTemperatureSetpoint**|O3EInt16|2||**rw**||
|**1643**|[**MixerOneCircuitCurrentTemperatureSetpoint**](## "Heating Circuit 1: Flow or Room Temperature Setpoint")|O3EInt16|2|[°C](## "°C or °F (system configuration)")|**rw**||
|**1644**|[**MixerTwoCircuitCurrentTemperatureSetpoint**](## "Heating Circuit 2: Flow or Room Temperature Setpoint")|O3EInt16|2|[°C](## "°C or °F (system configuration)")|**rw**||
|**1645**|[**MixerThreeCircuitCurrentTemperatureSetpoint**](## "Heating Circuit 3: Flow or Room Temperature Setpoint")|O3EInt16|2|[°C](## "°C or °F (system configuration)")|**rw**||
|**1646**|[**MixerFourCircuitCurrentTemperatureSetpoint**](## "Heating Circuit 4: Flow or Room Temperature Setpoint")|O3EInt16|2|[°C](## "°C or °F (system configuration)")|**rw**||
|**1659**|[**EndResultDomesticHotWaterTemperatureSetpoint**](## "Resulting Setpoint for and Actual State of Domestic Hot Water Preparation (probably READ ONLY)")|*O3EComplexType*|3||ro|[Link](https://github.com/open3e/open3e/discussions/214)|
| |- Setpoint|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- [State](## "Actual Operating State {0: Off, 1: Hot water, 2: Parallel operation, 3: Chimney sweep, 4: Test mode, 5: External temperature setpoint, 6: External modulation setpoint, 7: Hygiene function, 8: Automatic}")|O3EEnum|1||||
|**1660**|**SupportedFeatures**|RawCodec|16||ro||
|**1661**|**SolarSecondaryTransferPump**|RawCodec|5||ro||
|**1662**|**HeatingSupportBufferThreeWayValvePositionPercent**|RawCodec|2||ro||
|**1663**|**TestStatus**|RawCodec|41||ro||
|**1664**|[**ElectricalEnergyStorageStateOfCharge**](## "SoC of Battery")|O3EInt8|1|%|ro|[Link](https://github.com/open3e/open3e/wiki/036-DoI-%E2%80%90-Data-points-of-Interest/#data-points-of-vx3)|
|**1667**|**MixerOneCircuitPumpOscillationTime**|RawCodec|2||ro||
|**1668**|**MixerTwoCircuitPumpOscillationTime**|RawCodec|2||ro||
|**1669**|**MixerThreeCircuitPumpOscillationTime**|RawCodec|2||ro||
|**1670**|**MixerFourCircuitPumpOscillationTime**|RawCodec|2||ro||
|**1684**|[**AmbientTemperatureSensor**](## "Actual Ambient Temperature")|*O3EComplexType*|9||ro||
| |- Actual|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- Minimum|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- Maximum|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- Average|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- [SensorStatus](## "{0: no_error, 1: interruption, 2: short_circuit, 3: electrical_fault, 4: not_available, 5: invalidates}")|O3EEnum|1||||
|**1685**|**ElectricalEnergyInverterDCConfiguration**|RawCodec|3||ro||
|**1686**|**ElectricalEnergySystemPhotovoltaicLimitation**|RawCodec|3||ro||
|**1687**|**ElectricalEnergySystemPhotovoltaicConfiguration**|O3EInt16|2||ro||
|**1690**|[**ElectricalEnergySystemPhotovoltaicStatus**](## "Actual Power of Photovoltaic")|*O3EComplexType*|17||ro|[Link](https://github.com/open3e/open3e/wiki/036-DoI-%E2%80%90-Data-points-of-Interest/#data-points-of-vx3)|
| |- ActivePower cumulated|O3EInt16|2|W|||
| |- RectivePower cumulated|O3EInt16|2|VA|||
| |- ActivePower String C|O3EInt16|2|W|||
| |- RectivePower String C|O3EInt16|2|VA|||
| |- ActivePower String B|O3EInt16|2|W|||
| |- RectivePower String B|O3EInt16|2|VA|||
| |- ActivePower String A|O3EInt16|2|W|||
| |- RectivePower String A|O3EInt16|2|VA|||
| |- OpMode|O3EInt8|1||||
|**1691**|**BusTopologyScanStatus**|O3EByteVal|1||ro||
|**1692**|**PowerGridCodeConfiguration**|RawCodec|1||ro||
|**1693**|**GridOperatorConfigurationLock**|O3EByteVal|1||ro||
|**1694**|**GatewayEthernetEnable**|O3EByteVal|1||ro||
|**1695**|**GatewayEthernetConfig**|RawCodec|21||ro||
|**1696**|**GatewayEthernetIp**|RawCodec|20||ro||
|**1697**|**GatewayEthernetNetworkStatus**|O3EByteVal|1||ro||
|**1698**|**SupportedFeaturesTelemetryControlUnit**|RawCodec|16||ro||
|**1699**|**ActivatedFeaturesTelemetryControlUnit**|RawCodec|16||ro||
|**1700**|**EebusDeviceList**|RawCodec|104||ro||
|**1701**|**EebusOwnInfo**|RawCodec|104||ro||
|**1702**|**EebusPartnerInfo**|RawCodec|104||ro||
|**1703**|**EebusConnectionStatus**|RawCodec|1||ro||
|**1706**|**GenericMZIOAccessoryTwoModuleFunction**|RawCodec|1||ro||
|**1710**|**FunctionalSoftwareVersion**|O3ESoftVers|8||ro||
|**1718**|**ElectricalEnergySystemConfiguration**|*O3EComplexType*|2||ro||
| |- Netzbetriebsart|O3EByteVal|1||||
| |- Elektrische Anlagenkomponenten|O3EByteVal|1||||
|**1719**|**SolarIntervalFunction**|RawCodec|3||ro||
|**1721**|**WaterPressureConfiguration**|RawCodec|8||ro||
|**1728**|**ThermostatTerminalOneCircuitPump**|RawCodec|2||ro||
|**1729**|**ThermostatTerminalTwoCircuitPump**|RawCodec|2||ro||
|**1730**|**ThermostatTerminalThreeCircuitPump**|RawCodec|2||ro||
|**1731**|**ExternalLockActive**|O3EByteVal|1||ro||
|**1732**|**FixedRoomTemperatureSetpoint**|RawCodec|6||**rw**||
|**1749**|**TimeSeriesRecordedModulationCurrentValueStepsAndDurationOne**|RawCodec|176||ro||
|**1750**|**TimeSeriesRecordedModulationCurrentValueStepsAndDurationTwo**|RawCodec|176||ro||
|**1751**|**TimeSeriesRecordedModulationCurrentValueStepsAndDurationThree**|RawCodec|132||ro||
|**1752**|**TimeSeriesRecordedFlowTemperatureSensorStepsAndDurationOne**|RawCodec|176||ro||
|**1753**|**TimeSeriesRecordedFlowTemperatureSensorStepsAndDurationTwo**|RawCodec|176||ro||
|**1754**|**TimeSeriesRecordedFlowTemperatureSensorStepsAndDurationThree**|RawCodec|132||ro||
|**1759**|**TimeSeriesRecordedDomesticHotWaterOutletTemperature**|RawCodec|40||ro||
|**1760**|**TimeSeriesRecordedCombustionAirInletTemperature**|RawCodec|40||ro||
|**1761**|**TimeSeriesRecordedCentralHeatingPumpSpeed**|RawCodec|40||ro||
|**1762**|**LowWaterCutOffSignalInput**|RawCodec|1||ro||
|**1763**|**LowGasPressureSignalInput**|RawCodec|1||ro||
|**1764**|**HighGasPressureSignalInput**|RawCodec|1||ro||
|**1765**|**CombustionAirInterlock**|RawCodec|2||ro||
|**1766**|**ElectricalEnergyStorageModuleOperatingData**|RawCodec|141||ro||
|**1768**|**ReceiverTemperatureSensor**|*O3EComplexType*|9||ro||
| |- Actual|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- Minimum|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- Maximum|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- Average|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- [SensorStatus](## "{0: no_error, 1: interruption, 2: short_circuit, 3: electrical_fault, 4: not_available, 5: invalidates}")|O3EEnum|1||||
|**1769**|[**PrimaryInletTemperatureSensor**](## "Temperature at Primary Inlet of Heat Pump")|*O3EComplexType*|9||ro|[Link](https://github.com/open3e/open3e/wiki/036-DoI-%E2%80%90-Data-points-of-Interest)|
| |- Actual|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- Minimum|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- Maximum|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- Average|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- [SensorStatus](## "{0: no_error, 1: interruption, 2: short_circuit, 3: electrical_fault, 4: not_available, 5: invalidates}")|O3EEnum|1||||
|**1770**|**SecondaryOutletTemperatureSensor**|*O3EComplexType*|9||ro||
| |- Actual|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- Minimum|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- Maximum|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- Average|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- [SensorStatus](## "{0: no_error, 1: interruption, 2: short_circuit, 3: electrical_fault, 4: not_available, 5: invalidates}")|O3EEnum|1||||
|**1771**|[**EngineRoomTemperatureSensor**](## "Actual Temperature at Engine Room")|*O3EComplexType*|9||ro||
| |- Actual|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- Minimum|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- Maximum|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- Average|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- [SensorStatus](## "{0: no_error, 1: interruption, 2: short_circuit, 3: electrical_fault, 4: not_available, 5: invalidates}")|O3EEnum|1||||
|**1772**|[**CompressorOilTemperatureSensor**](## "Actual Compressor Oil Temperature")|*O3EComplexType*|9||ro|[Link](https://github.com/open3e/open3e/wiki/036-DoI-%E2%80%90-Data-points-of-Interest)|
| |- Actual|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- Minimum|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- Maximum|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- Average|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- [SensorStatus](## "{0: no_error, 1: interruption, 2: short_circuit, 3: electrical_fault, 4: not_available, 5: invalidates}")|O3EEnum|1||||
|**1773**|**RefrigerantCircuitFourWayValve**|O3EByteVal|1||ro||
|**1774**|**CompressorCrankCaseHeater**|O3EByteVal|1||ro||
|**1775**|[**PrimaryCircuitFanOne**](## "Speed of Fan 1")|O3EByteVal|1|%|ro|[Link](https://github.com/open3e/open3e/wiki/036-DoI-%E2%80%90-Data-points-of-Interest)|
|**1776**|[**PrimaryCircuitFanTwo**](## "Speed of Fan 2")|O3EByteVal|1|%|ro|[Link](https://github.com/open3e/open3e/wiki/036-DoI-%E2%80%90-Data-points-of-Interest)|
|**1777**|**TimeSeriesRecordedFlueGasTemperatureSensorStepsAndDurationOne**|RawCodec|176||ro||
|**1778**|**TimeSeriesRecordedFlueGasTemperatureSensorStepsAndDurationTwo**|RawCodec|176||ro||
|**1779**|**TimeSeriesRecordedFlueGasTemperatureSensorStepsAndDurationThree**|RawCodec|132||ro||
|**1780**|**TimeSeriesRecordedIgnitionTimeSteps**|RawCodec|80||ro||
|**1781**|**TimeSeriesRecordedCalibrationCount**|RawCodec|16||ro||
|**1782**|**TimeSeriesRecordedMonitoringIonizationMaximum**|RawCodec|56||ro||
|**1783**|**TimeSeriesRecordedHeatingBurnerStopEvents**|RawCodec|120||ro||
|**1784**|**TimeSeriesRecordedDomesticHotWaterBurnerStopEvents**|RawCodec|120||ro||
|**1785**|**TimeSeriesRecordedFlameLossModulation**|RawCodec|40||ro||
|**1786**|**TimeSeriesRecordedWaterPressureStagnation**|RawCodec|52||ro||
|**1787**|**TimeSeriesRecordedWaterPressurePeaks**|RawCodec|32||ro||
|**1788**|**CanInterfaceVersion**|RawCodec|8||ro||
|**1791**|**DiverterValveDefaultPositionConfiguration**|O3EByteVal|1||ro||
|**1792**|**ResetElectricalEnergyHistory**|RawCodec|1||ro||
|**1793**|**BurnerPreconditions**|RawCodec|1||ro||
|**1794**|**HeatingCircuitHeatDeficit**|RawCodec|4||ro||
|**1795**|**FuelCellRuntimePrediction**|O3EInt8|1||ro||
|**1796**|**DomesticElectricalEnergyConsumption**|RawCodec|2||ro||
|**1797**|**PredictionDomesticElectricalEnergyConsumptionNextHour**|RawCodec|2||ro||
|**1798**|**FuelCellHoursTillNextStart**|O3EInt8|1||ro||
|**1799**|[**PrimaryCircuitCurrentTemperatureSetpoint**](## "Heating Circuit 1: Temperature Setpoint")|O3EInt16|2|[°C](## "°C or °F (system configuration)")|**rw**||
|**1800**|**ResetTimeSeriesRecordingGroups**|RawCodec|4||ro||
|**1801**|[**ElectricalEnergyStorageEnergyTransferStatistic**](## "Statistics of Transfered Electrical Energy")|*O3EComplexType*|40||ro|[Link](https://github.com/open3e/open3e/wiki/036-DoI-%E2%80%90-Data-points-of-Interest/#data-points-of-vx3)|
| |- BatteryChargeToday|O3EInt32|4|Wh|||
| |- BatteryChargeWeek|O3EInt32|4|Wh|||
| |- BatteryChargeMonth|O3EInt32|4|Wh|||
| |- BatteryChargeYear|O3EInt32|4|Wh|||
| |- BatteryChargeTotal|O3EInt32|4|Wh|||
| |- BatteryDischargeToday|O3EInt32|4|Wh|||
| |- BatteryDischargeWeek|O3EInt32|4|Wh|||
| |- BatteryDischargeMonth|O3EInt32|4|Wh|||
| |- BatteryDischargeYear|O3EInt32|4|Wh|||
| |- BatteryDischargeTotal|O3EInt32|4|Wh|||
|**1802**|[**EnergyProductionPhotovoltaic**](## "Statistics of Photovoltaic Production")|*O3EComplexType*|80||ro|[Link](https://github.com/open3e/open3e/wiki/036-DoI-%E2%80%90-Data-points-of-Interest/#data-points-of-vx3)|
| |- PhotovoltaicProductionToday|O3EInt32|4|Wh|||
| |- PhotovoltaicProductionWeek|O3EInt32|4|Wh|||
| |- PhotovoltaicProductionMonth|O3EInt32|4|Wh|||
| |- PhotovoltaicProductionYear|O3EInt32|4|Wh|||
| |- PhotovoltaicProductionTotal|O3EInt32|4|Wh|||
| |- PhotovoltaicProductionToday1|O3EInt32|4|Wh|||
| |- PhotovoltaicProductionWeek1|O3EInt32|4|Wh|||
| |- PhotovoltaicProductionMonth1|O3EInt32|4|Wh|||
| |- PhotovoltaicProductionYear1|O3EInt32|4|Wh|||
| |- PhotovoltaicProductionTotal1|O3EInt32|4|Wh|||
| |- PhotovoltaicProductionToday2|O3EInt32|4|Wh|||
| |- PhotovoltaicProductionWeek2|O3EInt32|4|Wh|||
| |- PhotovoltaicProductionMonth2|O3EInt32|4|Wh|||
| |- PhotovoltaicProductionYear2|O3EInt32|4|Wh|||
| |- PhotovoltaicProductionTotal2|O3EInt32|4|Wh|||
| |- PhotovoltaicProductionToday3|O3EInt32|4|Wh|||
| |- PhotovoltaicProductionWeek3|O3EInt32|4|Wh|||
| |- PhotovoltaicProductionMonth3|O3EInt32|4|Wh|||
| |- PhotovoltaicProductionYear3|O3EInt32|4|Wh|||
| |- PhotovoltaicProductionTotal3|O3EInt32|4|Wh|||
|**1807**|**ElectricalEnergyInverterDcInputOne**|RawCodec|10||ro||
|**1808**|**ElectricalEnergyInverterDcInputTwo**|RawCodec|10||ro||
|**1809**|**ElectricalEnergyInverterDcInputThree**|RawCodec|10||ro||
|**1810**|**ElectricalEnergyInverterPowerAc**|*O3EComplexType*|4||ro||
| |- ActivePower|O3EInt16|2||||
| |- ReactivePower|O3EInt16|2||||
|**1811**|**ElectricalEnergyStorageModuleSetUpCheck**|RawCodec|1||ro||
|**1812**|**PointOfCommonCouplingConfiguredEnergyMeter**|RawCodec|2||ro||
|**1813**|**EnhancedVapourInjectionValve**|O3EInt8|1||ro||
|**1814**|**ReceiverLiquidLevelSensor**|RawCodec|5||ro||
|**1815**|**ElectricalHeaterPhaseOne**|O3EInt8|1||ro||
|**1816**|**ElectricalHeaterPhaseTwo**|O3EInt8|1||ro||
|**1817**|**ElectricalHeaterPhaseThree**|O3EInt8|1||ro||
|**1819**|**SolarPumpConfigurationSelection**|O3EByteVal|1||ro||
|**1822**|**ThreePhaseInverterCurrent**|RawCodec|51||ro||
|**1823**|**ThreePhaseInverterVoltage**|RawCodec|27||ro||
|**1824**|**ThreePhaseInverterCurrentPower**|*O3EComplexType*|16||ro||
| |- cumulated|O3EInt32|4||||
| |- L1|O3EInt32|4||||
| |- L2|O3EInt32|4||||
| |- L3|O3EInt32|4||||
|**1825**|**ThreePhaseInverterCurrentApparentPower**|*O3EComplexType*|16||ro||
| |- cumulated|O3EInt32|4||||
| |- L1|O3EInt32|4||||
| |- L2|O3EInt32|4||||
| |- L3|O3EInt32|4||||
|**1826**|**ThreePhaseInverterMaximunNominalPower**|*O3EComplexType*|4||ro||
| |- Power|O3EInt16|2||||
| |- Unknown|RawCodec|2||||
|**1827**|[**InverterElectricalEnergyStorageMaximumNominalChargePower**](## "Nominal Electrical Power of Inverter for Charging")|*O3EComplexType*|4||ro||
| |- Power|O3EInt16|2|W|||
| |- Unknown|RawCodec|2||||
|**1828**|[**InverterElectricalEnergyStorageCurrentMaximumlChargePower**](## "Maximum Electrical Power of Inverter for Charging")|*O3EComplexType*|4||ro||
| |- Power|O3EInt16|2|W|||
| |- Unknown|RawCodec|2||||
|**1829**|[**InverterElectricalEnergyStorageMaximumNominalDischargePower**](## "Nominal Electrical Power of Inverter for Discharging")|*O3EComplexType*|4||ro||
| |- Power|O3EInt16|2|W|||
| |- Unknown|RawCodec|2||||
|**1830**|[**InverterElectricalEnergyStorageCurrentMaximumlDishargePower**](## "Maximum Electrical Power of Inverter for Discharging")|*O3EComplexType*|4||ro||
| |- Power|O3EInt16|2|W|||
| |- Unknown|RawCodec|2||||
|**1831**|[**PhotovoltaicCurrentStringPower**](## "Current Photovoltaic Power per String")|*O3EComplexType*|12||ro||
| |- String1|O3EInt32|4|W|||
| |- String2|O3EInt32|4|W|||
| |- String3|O3EInt32|4|W|||
|**1832**|[**PhotovoltaicStringCurrent**](## "Current Photovoltaic Current per String (resolution is 1 Ampere)")|*O3EComplexType*|12||ro||
| |- String1|O3EInt32|4|A|||
| |- String2|O3EInt32|4|A|||
| |- String3|O3EInt32|4|V|||
|**1833**|[**PhotovoltaicStringVoltage**](## "Current Photovoltaic Voltage per String")|*O3EComplexType*|12||ro|[Link](https://github.com/open3e/open3e/wiki/036-DoI-%E2%80%90-Data-points-of-Interest/#data-points-of-vx3)|
| |- String1|O3EInt32|4|V|||
| |- String2|O3EInt32|4|V|||
| |- String3|O3EInt32|4|V|||
|**1834**|[**ElectricalEnergyStorageStateOfEnergy**](## "SoC of Battery")|*O3EComplexType*|4||ro||
| |- StateOfEnergy|O3EInt16|2|Wh|||
| |- Unknown|O3EInt16|2||||
|**1835**|**ManufacturerProperties**|RawCodec|20||ro||
|**1836**|[**ElectricalEnergyStorageCurrentPower**](## "Current Power for Battery Discharging (positive values) and Charging (negative values)")|O3EInt32|4|W|ro||
|**1837**|**ElectricalEnergyStorageCurrent**|*O3EComplexType*|4||ro||
| |- Current|O3EInt16|2||||
| |- Unknown|RawCodec|2||||
|**1838**|**ElectricalEnergyStorageVoltage**|O3EInt16|2||ro||
|**1839**|**ElectricalEnergyStorageUsableEnergy**|RawCodec|4||ro||
|**1840**|**ElectricalEnergyStorageUsableNominalEnergy**|RawCodec|4||ro||
|**1841**|**PointOfCommonCouplingOverview**|RawCodec|32||ro||
|**1842**|[**SecondaryCircuitFourThreeWayValve**](## "Circuit 2: Position of Four Three Way Valve")|*O3EComplexType*|2||ro||
| |- Setpoint|O3EInt8|1|%|||
| |- CurrentPosition|O3EInt8|1|%|||
|**1843**|**MixerOneCircuitHumidityProtection**|RawCodec|2||ro||
|**1844**|**MixerTwoCircuitHumidityProtection**|RawCodec|2||ro||
|**1845**|**HeatPumpCompressorEnvelope**|RawCodec|36||ro||
|**1846**|**HeatPumpCompressorCurrentOperatingPoint**|RawCodec|4||ro||
|**1847**|**CustomerDetailsExtensions**|RawCodec|81||ro||
|**1848**|**ApartmentOneProperty**|RawCodec|27||ro||
|**1849**|**ApartmentOneSetpoints**|RawCodec|50||**rw**||
|**1850**|**ApartmentOneTimeScheduleMonday**|RawCodec|57||**rw**||
|**1851**|**ApartmentOneTimeScheduleTuesday**|RawCodec|57||**rw**||
|**1852**|**ApartmentOneTimeScheduleWednesday**|RawCodec|57||**rw**||
|**1853**|**ApartmentOneTimeScheduleThursday**|RawCodec|57||**rw**||
|**1854**|**ApartmentOneTimeScheduleFriday**|RawCodec|57||**rw**||
|**1855**|**ApartmentOneTimeScheduleSaturday**|RawCodec|57||**rw**||
|**1856**|**ApartmentOneTimeScheduleSunday**|RawCodec|57||**rw**||
|**1884**|**RoomOneProperty**|RawCodec|84||ro||
|**1884**|**RoomOneProperty**|*O3EComplexType*|85||ro||
| |- Roomname|O3EUtf8|39||||
| |- Unknown1|RawCodec|4||||
| |- [Roomtype](## "{2: Bathroom, 3: Bedroom, 4: Hallway, 5: Living Room, 6: Childrens Room, 7: Kitchen, 8: Office, 9: Guest Toilet, 11: Others}")|O3EEnum|1||||
| |- Unknown2|RawCodec|1||||
| |- [TemperatureControl](## "{1: MaximumEco, 2: MoreEco, 3: Eco, 4: Komfort (Default), 5: More Comfort, 6: Maximum Comfort}")|O3EEnum|1||||
| |- Unknown3|RawCodec|29||||
| |- [WindowDetection](## "{0: Not Active, 1: Active}")|O3EEnum|1||||
| |- Unknown4|RawCodec|9||||
|**1885**|**RoomOneSetpoints**|RawCodec|30||**rw**||
|**1886**|**RoomOneCurrentValues**|RawCodec|46||ro||
|**1887**|**RoomTwoProperty**|RawCodec|84||ro||
|**1887**|**RoomTwoProperty**|*O3EComplexType*|85||ro||
| |- Roomname|O3EUtf8|39||||
| |- Unknown1|RawCodec|4||||
| |- [Roomtype](## "{2: Bathroom, 3: Bedroom, 4: Hallway, 5: Living Room, 6: Childrens Room, 7: Kitchen, 8: Office, 9: Guest Toilet, 11: Others}")|O3EEnum|1||||
| |- Unknown2|RawCodec|1||||
| |- [TemperatureControl](## "{1: MaximumEco, 2: MoreEco, 3: Eco, 4: Komfort (Default), 5: More Comfort, 6: Maximum Comfort}")|O3EEnum|1||||
| |- Unknown3|RawCodec|29||||
| |- [WindowDetection](## "{0: Not Active, 1: Active}")|O3EEnum|1||||
| |- Unknown4|RawCodec|9||||
|**1888**|**RoomTwoSetpoints**|RawCodec|30||**rw**||
|**1889**|**RoomTwoCurrentValues**|RawCodec|46||ro||
|**1890**|**RoomThreeProperty**|RawCodec|84||ro||
|**1890**|**RoomThreeProperty**|*O3EComplexType*|85||ro||
| |- Roomname|O3EUtf8|39||||
| |- Unknown1|RawCodec|4||||
| |- [Roomtype](## "{2: Bathroom, 3: Bedroom, 4: Hallway, 5: Living Room, 6: Childrens Room, 7: Kitchen, 8: Office, 9: Guest Toilet, 11: Others}")|O3EEnum|1||||
| |- Unknown2|RawCodec|1||||
| |- [TemperatureControl](## "{1: MaximumEco, 2: MoreEco, 3: Eco, 4: Komfort (Default), 5: More Comfort, 6: Maximum Comfort}")|O3EEnum|1||||
| |- Unknown3|RawCodec|29||||
| |- [WindowDetection](## "{0: Not Active, 1: Active}")|O3EEnum|1||||
| |- Unknown4|RawCodec|9||||
|**1891**|**RoomThreeSetpoints**|RawCodec|30||**rw**||
|**1892**|**RoomThreeCurrentValues**|RawCodec|46||ro||
|**1893**|**RoomFourProperty**|RawCodec|84||ro||
|**1893**|**RoomFourProperty**|*O3EComplexType*|85||ro||
| |- Roomname|O3EUtf8|39||||
| |- Unknown1|RawCodec|4||||
| |- [Roomtype](## "{2: Bathroom, 3: Bedroom, 4: Hallway, 5: Living Room, 6: Childrens Room, 7: Kitchen, 8: Office, 9: Guest Toilet, 11: Others}")|O3EEnum|1||||
| |- Unknown2|RawCodec|1||||
| |- [TemperatureControl](## "{1: MaximumEco, 2: MoreEco, 3: Eco, 4: Komfort (Default), 5: More Comfort, 6: Maximum Comfort}")|O3EEnum|1||||
| |- Unknown3|RawCodec|29||||
| |- [WindowDetection](## "{0: Not Active, 1: Active}")|O3EEnum|1||||
| |- Unknown4|RawCodec|9||||
|**1894**|**RoomFourSetpoints**|RawCodec|30||**rw**||
|**1895**|**RoomFourCurrentValues**|RawCodec|46||ro||
|**1896**|**RoomFiveProperty**|RawCodec|84||ro||
|**1896**|**RoomFiveProperty**|*O3EComplexType*|85||ro||
| |- Roomname|O3EUtf8|39||||
| |- Unknown1|RawCodec|4||||
| |- [Roomtype](## "{2: Bathroom, 3: Bedroom, 4: Hallway, 5: Living Room, 6: Childrens Room, 7: Kitchen, 8: Office, 9: Guest Toilet, 11: Others}")|O3EEnum|1||||
| |- Unknown2|RawCodec|1||||
| |- [TemperatureControl](## "{1: MaximumEco, 2: MoreEco, 3: Eco, 4: Komfort (Default), 5: More Comfort, 6: Maximum Comfort}")|O3EEnum|1||||
| |- Unknown3|RawCodec|29||||
| |- [WindowDetection](## "{0: Not Active, 1: Active}")|O3EEnum|1||||
| |- Unknown4|RawCodec|9||||
|**1897**|**RoomFiveSetpoints**|RawCodec|30||**rw**||
|**1898**|**RoomFiveCurrentValues**|RawCodec|46||ro||
|**1899**|**RoomSixProperty**|RawCodec|84||ro||
|**1899**|**RoomSixProperty**|*O3EComplexType*|85||ro||
| |- Roomname|O3EUtf8|39||||
| |- Unknown1|RawCodec|4||||
| |- [Roomtype](## "{2: Bathroom, 3: Bedroom, 4: Hallway, 5: Living Room, 6: Childrens Room, 7: Kitchen, 8: Office, 9: Guest Toilet, 11: Others}")|O3EEnum|1||||
| |- Unknown2|RawCodec|1||||
| |- [TemperatureControl](## "{1: MaximumEco, 2: MoreEco, 3: Eco, 4: Komfort (Default), 5: More Comfort, 6: Maximum Comfort}")|O3EEnum|1||||
| |- Unknown3|RawCodec|29||||
| |- [WindowDetection](## "{0: Not Active, 1: Active}")|O3EEnum|1||||
| |- Unknown4|RawCodec|9||||
|**1900**|**RoomSixSetpoints**|RawCodec|30||**rw**||
|**1901**|**RoomSixCurrentValues**|RawCodec|46||ro||
|**1902**|**RoomSevenProperty**|RawCodec|84||ro||
|**1902**|**RoomSevenProperty**|*O3EComplexType*|85||ro||
| |- Roomname|O3EUtf8|39||||
| |- Unknown1|RawCodec|4||||
| |- [Roomtype](## "{2: Bathroom, 3: Bedroom, 4: Hallway, 5: Living Room, 6: Childrens Room, 7: Kitchen, 8: Office, 9: Guest Toilet, 11: Others}")|O3EEnum|1||||
| |- Unknown2|RawCodec|1||||
| |- [TemperatureControl](## "{1: MaximumEco, 2: MoreEco, 3: Eco, 4: Komfort (Default), 5: More Comfort, 6: Maximum Comfort}")|O3EEnum|1||||
| |- Unknown3|RawCodec|29||||
| |- [WindowDetection](## "{0: Not Active, 1: Active}")|O3EEnum|1||||
| |- Unknown4|RawCodec|9||||
|**1903**|**RoomSevenSetpoints**|RawCodec|30||**rw**||
|**1904**|**RoomSevenCurrentValues**|RawCodec|46||ro||
|**1905**|**RoomEightProperty**|RawCodec|84||ro||
|**1905**|**RoomEightProperty**|*O3EComplexType*|85||ro||
| |- Roomname|O3EUtf8|39||||
| |- Unknown1|RawCodec|4||||
| |- [Roomtype](## "{2: Bathroom, 3: Bedroom, 4: Hallway, 5: Living Room, 6: Childrens Room, 7: Kitchen, 8: Office, 9: Guest Toilet, 11: Others}")|O3EEnum|1||||
| |- Unknown2|RawCodec|1||||
| |- [TemperatureControl](## "{1: MaximumEco, 2: MoreEco, 3: Eco, 4: Komfort (Default), 5: More Comfort, 6: Maximum Comfort}")|O3EEnum|1||||
| |- Unknown3|RawCodec|29||||
| |- [WindowDetection](## "{0: Not Active, 1: Active}")|O3EEnum|1||||
| |- Unknown4|RawCodec|9||||
|**1906**|**RoomEightSetpoints**|RawCodec|30||**rw**||
|**1907**|**RoomEightCurrentValues**|RawCodec|46||ro||
|**1908**|**RoomNineProperty**|RawCodec|84||ro||
|**1908**|**RoomNineProperty**|*O3EComplexType*|85||ro||
| |- Roomname|O3EUtf8|39||||
| |- Unknown1|RawCodec|4||||
| |- [Roomtype](## "{2: Bathroom, 3: Bedroom, 4: Hallway, 5: Living Room, 6: Childrens Room, 7: Kitchen, 8: Office, 9: Guest Toilet, 11: Others}")|O3EEnum|1||||
| |- Unknown2|RawCodec|1||||
| |- [TemperatureControl](## "{1: MaximumEco, 2: MoreEco, 3: Eco, 4: Komfort (Default), 5: More Comfort, 6: Maximum Comfort}")|O3EEnum|1||||
| |- Unknown3|RawCodec|29||||
| |- [WindowDetection](## "{0: Not Active, 1: Active}")|O3EEnum|1||||
| |- Unknown4|RawCodec|9||||
|**1909**|**RoomNineSetpoints**|RawCodec|30||**rw**||
|**1910**|**RoomNineCurrentValues**|RawCodec|46||ro||
|**1911**|**RoomTenProperty**|RawCodec|84||ro||
|**1911**|**RoomTenProperty**|*O3EComplexType*|85||ro||
| |- Roomname|O3EUtf8|39||||
| |- Unknown1|RawCodec|4||||
| |- [Roomtype](## "{2: Bathroom, 3: Bedroom, 4: Hallway, 5: Living Room, 6: Childrens Room, 7: Kitchen, 8: Office, 9: Guest Toilet, 11: Others}")|O3EEnum|1||||
| |- Unknown2|RawCodec|1||||
| |- [TemperatureControl](## "{1: MaximumEco, 2: MoreEco, 3: Eco, 4: Komfort (Default), 5: More Comfort, 6: Maximum Comfort}")|O3EEnum|1||||
| |- Unknown3|RawCodec|29||||
| |- [WindowDetection](## "{0: Not Active, 1: Active}")|O3EEnum|1||||
| |- Unknown4|RawCodec|9||||
|**1912**|**RoomTenSetpoints**|RawCodec|30||**rw**||
|**1913**|**RoomTenCurrentValues**|RawCodec|46||ro||
|**1914**|**RoomElevenProperty**|RawCodec|84||ro||
|**1915**|**RoomElevenSetpoints**|RawCodec|30||**rw**||
|**1916**|**RoomElevenCurrentValues**|RawCodec|46||ro||
|**1917**|**RoomTwelveProperty**|RawCodec|84||ro||
|**1918**|**RoomTwelveSetpoints**|RawCodec|30||**rw**||
|**1919**|**RoomTwelveCurrentValues**|RawCodec|46||ro||
|**1920**|**RoomThirteenProperty**|RawCodec|84||ro||
|**1920**|**RoomThirteenProperty**|*O3EComplexType*|85||ro||
| |- Roomname|O3EUtf8|39||||
| |- Unknown1|RawCodec|4||||
| |- [Roomtype](## "{2: Bathroom, 3: Bedroom, 4: Hallway, 5: Living Room, 6: Childrens Room, 7: Kitchen, 8: Office, 9: Guest Toilet, 11: Others}")|O3EEnum|1||||
| |- Unknown2|RawCodec|1||||
| |- [TemperatureControl](## "{1: MaximumEco, 2: MoreEco, 3: Eco, 4: Komfort (Default), 5: More Comfort, 6: Maximum Comfort}")|O3EEnum|1||||
| |- Unknown3|RawCodec|29||||
| |- [WindowDetection](## "{0: Not Active, 1: Active}")|O3EEnum|1||||
| |- Unknown4|RawCodec|9||||
|**1921**|**RoomThirteenSetpoints**|RawCodec|30||**rw**||
|**1922**|**RoomThirteenCurrentValues**|RawCodec|46||ro||
|**1923**|**RoomFourteenProperty**|RawCodec|84||ro||
|**1923**|**RoomFourteenProperty**|*O3EComplexType*|85||ro||
| |- Roomname|O3EUtf8|39||||
| |- Unknown1|RawCodec|4||||
| |- [Roomtype](## "{2: Bathroom, 3: Bedroom, 4: Hallway, 5: Living Room, 6: Childrens Room, 7: Kitchen, 8: Office, 9: Guest Toilet, 11: Others}")|O3EEnum|1||||
| |- Unknown2|RawCodec|1||||
| |- [TemperatureControl](## "{1: MaximumEco, 2: MoreEco, 3: Eco, 4: Komfort (Default), 5: More Comfort, 6: Maximum Comfort}")|O3EEnum|1||||
| |- Unknown3|RawCodec|29||||
| |- [WindowDetection](## "{0: Not Active, 1: Active}")|O3EEnum|1||||
| |- Unknown4|RawCodec|9||||
|**1924**|**RoomFourteenSetpoints**|RawCodec|30||**rw**||
|**1925**|**RoomFourteenCurrentValues**|RawCodec|46||ro||
|**1926**|**RoomFifteenProperty**|RawCodec|84||ro||
|**1926**|**RoomFifteenProperty**|*O3EComplexType*|85||ro||
| |- Roomname|O3EUtf8|39||||
| |- Unknown1|RawCodec|4||||
| |- [Roomtype](## "{2: Bathroom, 3: Bedroom, 4: Hallway, 5: Living Room, 6: Childrens Room, 7: Kitchen, 8: Office, 9: Guest Toilet, 11: Others}")|O3EEnum|1||||
| |- Unknown2|RawCodec|1||||
| |- [TemperatureControl](## "{1: MaximumEco, 2: MoreEco, 3: Eco, 4: Komfort (Default), 5: More Comfort, 6: Maximum Comfort}")|O3EEnum|1||||
| |- Unknown3|RawCodec|29||||
| |- [WindowDetection](## "{0: Not Active, 1: Active}")|O3EEnum|1||||
| |- Unknown4|RawCodec|9||||
|**1927**|**RoomFifteenSetpoints**|RawCodec|30||**rw**||
|**1928**|**RoomFifteenCurrentValues**|RawCodec|46||ro||
|**1929**|**RoomSixteenProperty**|RawCodec|84||ro||
|**1929**|**RoomSixteenProperty**|*O3EComplexType*|85||ro||
| |- Roomname|O3EUtf8|39||||
| |- Unknown1|RawCodec|4||||
| |- [Roomtype](## "{2: Bathroom, 3: Bedroom, 4: Hallway, 5: Living Room, 6: Childrens Room, 7: Kitchen, 8: Office, 9: Guest Toilet, 11: Others}")|O3EEnum|1||||
| |- Unknown2|RawCodec|1||||
| |- [TemperatureControl](## "{1: MaximumEco, 2: MoreEco, 3: Eco, 4: Komfort (Default), 5: More Comfort, 6: Maximum Comfort}")|O3EEnum|1||||
| |- Unknown3|RawCodec|29||||
| |- [WindowDetection](## "{0: Not Active, 1: Active}")|O3EEnum|1||||
| |- Unknown4|RawCodec|9||||
|**1930**|**RoomSixteenSetpoints**|RawCodec|30||**rw**||
|**1931**|**RoomSixteenCurrentValues**|RawCodec|46||ro||
|**1932**|**RoomSeventeenProperty**|RawCodec|84||ro||
|**1932**|**RoomSeventeenProperty**|*O3EComplexType*|85||ro||
| |- Roomname|O3EUtf8|39||||
| |- Unknown1|RawCodec|4||||
| |- [Roomtype](## "{2: Bathroom, 3: Bedroom, 4: Hallway, 5: Living Room, 6: Childrens Room, 7: Kitchen, 8: Office, 9: Guest Toilet, 11: Others}")|O3EEnum|1||||
| |- Unknown2|RawCodec|1||||
| |- [TemperatureControl](## "{1: MaximumEco, 2: MoreEco, 3: Eco, 4: Komfort (Default), 5: More Comfort, 6: Maximum Comfort}")|O3EEnum|1||||
| |- Unknown3|RawCodec|29||||
| |- [WindowDetection](## "{0: Not Active, 1: Active}")|O3EEnum|1||||
| |- Unknown4|RawCodec|9||||
|**1933**|**RoomSeventeenSetpoints**|RawCodec|30||**rw**||
|**1934**|**RoomSeventeenCurrentValues**|RawCodec|46||ro||
|**1935**|**RoomEighteenProperty**|RawCodec|84||ro||
|**1935**|**RoomEightteenProperty**|*O3EComplexType*|85||ro||
| |- Roomname|O3EUtf8|39||||
| |- Unknown1|RawCodec|4||||
| |- [Roomtype](## "{2: Bathroom, 3: Bedroom, 4: Hallway, 5: Living Room, 6: Childrens Room, 7: Kitchen, 8: Office, 9: Guest Toilet, 11: Others}")|O3EEnum|1||||
| |- Unknown2|RawCodec|1||||
| |- [TemperatureControl](## "{1: MaximumEco, 2: MoreEco, 3: Eco, 4: Komfort (Default), 5: More Comfort, 6: Maximum Comfort}")|O3EEnum|1||||
| |- Unknown3|RawCodec|29||||
| |- [WindowDetection](## "{0: Not Active, 1: Active}")|O3EEnum|1||||
| |- Unknown4|RawCodec|9||||
|**1936**|**RoomEighteenSetpoints**|RawCodec|30||**rw**||
|**1937**|**RoomEighteenCurrentValues**|RawCodec|46||ro||
|**1938**|**RoomNineteenProperty**|RawCodec|84||ro||
|**1938**|**RoomNineteenProperty**|*O3EComplexType*|85||ro||
| |- Roomname|O3EUtf8|39||||
| |- Unknown1|RawCodec|4||||
| |- [Roomtype](## "{2: Bathroom, 3: Bedroom, 4: Hallway, 5: Living Room, 6: Childrens Room, 7: Kitchen, 8: Office, 9: Guest Toilet, 11: Others}")|O3EEnum|1||||
| |- Unknown2|RawCodec|1||||
| |- [TemperatureControl](## "{1: MaximumEco, 2: MoreEco, 3: Eco, 4: Komfort (Default), 5: More Comfort, 6: Maximum Comfort}")|O3EEnum|1||||
| |- Unknown3|RawCodec|29||||
| |- [WindowDetection](## "{0: Not Active, 1: Active}")|O3EEnum|1||||
| |- Unknown4|RawCodec|9||||
|**1939**|**RoomNineteenSetpoints**|RawCodec|30||**rw**||
|**1940**|**RoomNineteenCurrentValues**|RawCodec|46||ro||
|**1941**|**RoomTwentyProperty**|RawCodec|84||ro||
|**1941**|**RoomTwentyProperty**|*O3EComplexType*|85||ro||
| |- Roomname|O3EUtf8|39||||
| |- Unknown1|RawCodec|4||||
| |- [Roomtype](## "{2: Bathroom, 3: Bedroom, 4: Hallway, 5: Living Room, 6: Childrens Room, 7: Kitchen, 8: Office, 9: Guest Toilet, 11: Others}")|O3EEnum|1||||
| |- Unknown2|RawCodec|1||||
| |- [TemperatureControl](## "{1: MaximumEco, 2: MoreEco, 3: Eco, 4: Komfort (Default), 5: More Comfort, 6: Maximum Comfort}")|O3EEnum|1||||
| |- Unknown3|RawCodec|29||||
| |- [WindowDetection](## "{0: Not Active, 1: Active}")|O3EEnum|1||||
| |- Unknown4|RawCodec|9||||
|**1942**|**RoomTwentySetpoints**|RawCodec|30||**rw**||
|**1943**|**RoomTwentyCurrentValues**|RawCodec|46||ro||
|**1944**|**RoomOneTimeScheduleMonday**|RawCodec|57||**rw**||
|**1945**|**RoomOneTimeScheduleTuesday**|RawCodec|57||**rw**||
|**1946**|**RoomOneTimeScheduleWednesday**|RawCodec|57||**rw**||
|**1947**|**RoomOneTimeScheduleThursday**|RawCodec|57||**rw**||
|**1948**|**RoomOneTimeScheduleFriday**|RawCodec|57||**rw**||
|**1949**|**RoomOneTimeScheduleSaturday**|RawCodec|57||**rw**||
|**1950**|**RoomOneTimeScheduleSunday**|RawCodec|57||**rw**||
|**1951**|**RoomTwoTimeScheduleMonday**|RawCodec|57||**rw**||
|**1952**|**RoomTwoTimeScheduleTuesday**|RawCodec|57||**rw**||
|**1953**|**RoomTwoTimeScheduleWednesday**|RawCodec|57||**rw**||
|**1954**|**RoomTwoTimeScheduleThursday**|RawCodec|57||**rw**||
|**1955**|**RoomTwoTimeScheduleFriday**|RawCodec|57||**rw**||
|**1956**|**RoomTwoTimeScheduleSaturday**|RawCodec|57||**rw**||
|**1957**|**RoomTwoTimeScheduleSunday**|RawCodec|57||**rw**||
|**1958**|**RoomThreeTimeScheduleMonday**|RawCodec|57||**rw**||
|**1959**|**RoomThreeTimeScheduleTuesday**|RawCodec|57||**rw**||
|**1960**|**RoomThreeTimeScheduleWednesday**|RawCodec|57||**rw**||
|**1961**|**RoomThreeTimeScheduleThursday**|RawCodec|57||**rw**||
|**1962**|**RoomThreeTimeScheduleFriday**|RawCodec|57||**rw**||
|**1963**|**RoomThreeTimeScheduleSaturday**|RawCodec|57||**rw**||
|**1964**|**RoomThreeTimeScheduleSunday**|RawCodec|57||**rw**||
|**1965**|**RoomFourTimeScheduleMonday**|RawCodec|57||**rw**||
|**1966**|**RoomFourTimeScheduleTuesday**|RawCodec|57||**rw**||
|**1967**|**RoomFourTimeScheduleWednesday**|RawCodec|57||**rw**||
|**1968**|**RoomFourTimeScheduleThursday**|RawCodec|57||**rw**||
|**1969**|**RoomFourTimeScheduleFriday**|RawCodec|57||**rw**||
|**1970**|**RoomFourTimeScheduleSaturday**|RawCodec|57||**rw**||
|**1971**|**RoomFourTimeScheduleSunday**|RawCodec|57||**rw**||
|**1972**|**RoomFiveTimeScheduleMonday**|RawCodec|57||**rw**||
|**1973**|**RoomFiveTimeScheduleTuesday**|RawCodec|57||**rw**||
|**1974**|**RoomFiveTimeScheduleWednesday**|RawCodec|57||**rw**||
|**1975**|**RoomFiveTimeScheduleThursday**|RawCodec|57||**rw**||
|**1976**|**RoomFiveTimeScheduleFriday**|RawCodec|57||**rw**||
|**1977**|**RoomFiveTimeScheduleSaturday**|RawCodec|57||**rw**||
|**1978**|**RoomFiveTimeScheduleSunday**|RawCodec|57||**rw**||
|**1979**|**RoomSixTimeScheduleMonday**|RawCodec|57||**rw**||
|**1980**|**RoomSixTimeScheduleTuesday**|RawCodec|57||**rw**||
|**1981**|**RoomSixTimeScheduleWednesday**|RawCodec|57||**rw**||
|**1982**|**RoomSixTimeScheduleThursday**|RawCodec|57||**rw**||
|**1983**|**RoomSixTimeScheduleFriday**|RawCodec|57||**rw**||
|**1984**|**RoomSixTimeScheduleSaturday**|RawCodec|57||**rw**||
|**1985**|**RoomSixTimeScheduleSunday**|RawCodec|57||**rw**||
|**1986**|**RoomSevenTimeScheduleMonday**|RawCodec|57||**rw**||
|**1987**|**RoomSevenTimeScheduleTuesday**|RawCodec|57||**rw**||
|**1988**|**RoomSevenTimeScheduleWednesday**|RawCodec|57||**rw**||
|**1989**|**RoomSevenTimeScheduleThursday**|RawCodec|57||**rw**||
|**1990**|**RoomSevenTimeScheduleFriday**|RawCodec|57||**rw**||
|**1991**|**RoomSevenTimeScheduleSaturday**|RawCodec|57||**rw**||
|**1992**|**RoomSevenTimeScheduleSunday**|RawCodec|57||**rw**||
|**1993**|**RoomEightTimeScheduleMonday**|RawCodec|57||**rw**||
|**1994**|**RoomEightTimeScheduleTuesday**|RawCodec|57||**rw**||
|**1995**|**RoomEightTimeScheduleWednesday**|RawCodec|57||**rw**||
|**1996**|**RoomEightTimeScheduleThursday**|RawCodec|57||**rw**||
|**1997**|**RoomEightTimeScheduleFriday**|RawCodec|57||**rw**||
|**1998**|**RoomEightTimeScheduleSaturday**|RawCodec|57||**rw**||
|**1999**|**RoomEightTimeScheduleSunday**|RawCodec|57||**rw**||
|**2000**|**RoomNineTimeScheduleMonday**|RawCodec|57||**rw**||
|**2001**|**RoomNineTimeScheduleTuesday**|RawCodec|57||**rw**||
|**2002**|**RoomNineTimeScheduleWednesday**|RawCodec|57||**rw**||
|**2003**|**RoomNineTimeScheduleThursday**|RawCodec|57||**rw**||
|**2004**|**RoomNineTimeScheduleFriday**|RawCodec|57||**rw**||
|**2005**|**RoomNineTimeScheduleSaturday**|RawCodec|57||**rw**||
|**2006**|**RoomNineTimeScheduleSunday**|RawCodec|57||**rw**||
|**2007**|**RoomTenTimeScheduleMonday**|RawCodec|57||**rw**||
|**2008**|**RoomTenTimeScheduleTuesday**|RawCodec|57||**rw**||
|**2009**|**RoomTenTimeScheduleWednesday**|RawCodec|57||**rw**||
|**2010**|**RoomTenTimeScheduleThursday**|RawCodec|57||**rw**||
|**2011**|**RoomTenTimeScheduleFriday**|RawCodec|57||**rw**||
|**2012**|**RoomTenTimeScheduleSaturday**|RawCodec|57||**rw**||
|**2013**|**RoomTenTimeScheduleSunday**|RawCodec|57||**rw**||
|**2014**|**RoomElevenTimeScheduleMonday**|RawCodec|57||**rw**||
|**2015**|**RoomElevenTimeScheduleTuesday**|RawCodec|57||**rw**||
|**2016**|**RoomElevenTimeScheduleWednesday**|RawCodec|57||**rw**||
|**2017**|**RoomElevenTimeScheduleThursday**|RawCodec|57||**rw**||
|**2018**|**RoomElevenTimeScheduleFriday**|RawCodec|57||**rw**||
|**2019**|**RoomElevenTimeScheduleSaturday**|RawCodec|57||**rw**||
|**2020**|**RoomElevenTimeScheduleSunday**|RawCodec|57||**rw**||
|**2021**|**RoomTwelveTimeScheduleMonday**|RawCodec|57||**rw**||
|**2022**|**RoomTwelveTimeScheduleTuesday**|RawCodec|57||**rw**||
|**2023**|**RoomTwelveTimeScheduleWednesday**|RawCodec|57||**rw**||
|**2024**|**RoomTwelveTimeScheduleThursday**|RawCodec|57||**rw**||
|**2025**|**RoomTwelveTimeScheduleFriday**|RawCodec|57||**rw**||
|**2026**|**RoomTwelveTimeScheduleSaturday**|RawCodec|57||**rw**||
|**2027**|**RoomTwelveTimeScheduleSunday**|RawCodec|57||**rw**||
|**2028**|**RoomThirteenTimeScheduleMonday**|RawCodec|57||**rw**||
|**2029**|**RoomThirteenTimeScheduleTuesday**|RawCodec|57||**rw**||
|**2030**|**RoomThirteenTimeScheduleWednesday**|RawCodec|57||**rw**||
|**2031**|**RoomThirteenTimeScheduleThursday**|RawCodec|57||**rw**||
|**2032**|**RoomThirteenTimeScheduleFriday**|RawCodec|57||**rw**||
|**2033**|**RoomThirteenTimeScheduleSaturday**|RawCodec|57||**rw**||
|**2034**|**RoomThirteenTimeScheduleSunday**|RawCodec|57||**rw**||
|**2035**|**RoomFourteenTimeScheduleMonday**|RawCodec|57||**rw**||
|**2036**|**RoomFourteenTimeScheduleTuesday**|RawCodec|57||**rw**||
|**2037**|**RoomFourteenTimeScheduleWednesday**|RawCodec|57||**rw**||
|**2038**|**RoomFourteenTimeScheduleThursday**|RawCodec|57||**rw**||
|**2039**|**RoomFourteenTimeScheduleFriday**|RawCodec|57||**rw**||
|**2040**|**RoomFourteenTimeScheduleSaturday**|RawCodec|57||**rw**||
|**2041**|**RoomFourteenTimeScheduleSunday**|RawCodec|57||**rw**||
|**2042**|**RoomFifteenTimeScheduleMonday**|RawCodec|57||**rw**||
|**2043**|**RoomFifteenTimeScheduleTuesday**|RawCodec|57||**rw**||
|**2044**|**RoomFifteenTimeScheduleWednesday**|RawCodec|57||**rw**||
|**2045**|**RoomFifteenTimeScheduleThursday**|RawCodec|57||**rw**||
|**2046**|**RoomFifteenTimeScheduleFriday**|RawCodec|57||**rw**||
|**2047**|**RoomFifteenTimeScheduleSaturday**|RawCodec|57||**rw**||
|**2048**|**RoomFifteenTimeScheduleSunday**|RawCodec|57||**rw**||
|**2049**|**RoomSixteenTimeScheduleMonday**|RawCodec|57||**rw**||
|**2050**|**RoomSixteenTimeScheduleTuesday**|RawCodec|57||**rw**||
|**2051**|**RoomSixteenTimeScheduleWednesday**|RawCodec|57||**rw**||
|**2052**|**RoomSixteenTimeScheduleThursday**|RawCodec|57||**rw**||
|**2053**|**RoomSixteenTimeScheduleFriday**|RawCodec|57||**rw**||
|**2054**|**RoomSixteenTimeScheduleSaturday**|RawCodec|57||**rw**||
|**2055**|**RoomSixteenTimeScheduleSunday**|RawCodec|57||**rw**||
|**2056**|**RoomSeventeenTimeScheduleMonday**|RawCodec|57||**rw**||
|**2057**|**RoomSeventeenTimeScheduleTuesday**|RawCodec|57||**rw**||
|**2058**|**RoomSeventeenTimeScheduleWednesday**|RawCodec|57||**rw**||
|**2059**|**RoomSeventeenTimeScheduleThursday**|RawCodec|57||**rw**||
|**2060**|**RoomSeventeenTimeScheduleFriday**|RawCodec|57||**rw**||
|**2061**|**RoomSeventeenTimeScheduleSaturday**|RawCodec|57||**rw**||
|**2062**|**RoomSeventeenTimeScheduleSunday**|RawCodec|57||**rw**||
|**2063**|**RoomEighteenTimeScheduleMonday**|RawCodec|57||**rw**||
|**2064**|**RoomEighteenTimeScheduleTuesday**|RawCodec|57||**rw**||
|**2065**|**RoomEighteenTimeScheduleWednesday**|RawCodec|57||**rw**||
|**2066**|**RoomEighteenTimeScheduleThursday**|RawCodec|57||**rw**||
|**2067**|**RoomEighteenTimeScheduleFriday**|RawCodec|57||**rw**||
|**2068**|**RoomEighteenTimeScheduleSaturday**|RawCodec|57||**rw**||
|**2069**|**RoomEighteenTimeScheduleSunday**|RawCodec|57||**rw**||
|**2070**|**RoomNineteenTimeScheduleMonday**|RawCodec|57||**rw**||
|**2071**|**RoomNineteenTimeScheduleTuesday**|RawCodec|57||**rw**||
|**2072**|**RoomNineteenTimeScheduleWednesday**|RawCodec|57||**rw**||
|**2073**|**RoomNineteenTimeScheduleThursday**|RawCodec|57||**rw**||
|**2074**|**RoomNineteenTimeScheduleFriday**|RawCodec|57||**rw**||
|**2075**|**RoomNineteenTimeScheduleSaturday**|RawCodec|57||**rw**||
|**2076**|**RoomNineteenTimeScheduleSunday**|RawCodec|57||**rw**||
|**2077**|**RoomTwentyTimeScheduleMonday**|RawCodec|57||**rw**||
|**2078**|**RoomTwentyTimeScheduleTuesday**|RawCodec|57||**rw**||
|**2079**|**RoomTwentyTimeScheduleWednesday**|RawCodec|57||**rw**||
|**2080**|**RoomTwentyTimeScheduleThursday**|RawCodec|57||**rw**||
|**2081**|**RoomTwentyTimeScheduleFriday**|RawCodec|57||**rw**||
|**2082**|**RoomTwentyTimeScheduleSaturday**|RawCodec|57||**rw**||
|**2083**|**RoomTwentyTimeScheduleSunday**|RawCodec|57||**rw**||
|**2084**|**ZigBeeOneDeviceProperty**|*O3EComplexType*|84||ro||
| |- Serialnumber|RawCodec|8||||
| |- SerialnumberPostfix|RawCodec|1||||
| |- Devicename|O3EUtf8|39||||
| |- Unknown1|RawCodec|1||||
| |- ViCareDevice|O3EEnum|1||||
| |- Firmware-Version|O3ESoftVers|8||||
| |- Unknown2|RawCodec|26||||
|**2085**|**ZigBeeOneDeviceSetpoint**|*O3EComplexType*|13||**rw**||
| |- Prefix|RawCodec|2||||
| |- MaximumFlowTemperature|O3EInt16|2||||
| |- Unused|RawCodec|9||||
|**2086**|**ZigBeeOneDeviceCurrentValues**|RawCodec|57||ro||
|**2086**|**ZigBeeOneDeviceCurrentValues**|*O3EComplexType*|68||ro||
| |- Unknown1|RawCodec|2||||
| |- BatteryLevel|O3EInt8|1||||
| |- Unknown2|RawCodec|38||||
| |- ValveType|O3EInt8|1||||
| |- ActualTemperature|O3EInt8|1||||
| |- OperatingStatus|O3EInt8|1||||
| |- Unknown3|RawCodec|4||||
| |- [DeviceDisplayTurned](## "{0: Standard, 1: Turned}")|O3EEnum|1||||
| |- Unknown4|RawCodec|5||||
| |- [DeviceChildLockActive](## "{0: Not Active, 1: Active}")|O3EEnum|1||||
| |- DeviceTemperatureSetpoint|O3EInt8|1||||
| |- Unknown5|RawCodec|12||||
|**2087**|**ZigBeeTwoDeviceProperty**|*O3EComplexType*|84||ro||
| |- Serialnumber|RawCodec|8||||
| |- SerialnumberPostfix|RawCodec|1||||
| |- Devicename|O3EUtf8|39||||
| |- Unknown1|RawCodec|1||||
| |- ViCareDevice|O3EEnum|1||||
| |- Firmware-Version|O3ESoftVers|8||||
| |- Unknown2|RawCodec|26||||
|**2088**|**ZigBeeTwoDeviceSetpoint**|*O3EComplexType*|13||**rw**||
| |- Prefix|RawCodec|2||||
| |- MaximumFlowTemperature|O3EInt16|2||||
| |- Unused|RawCodec|9||||
|**2089**|**ZigBeeTwoDeviceCurrentValues**|RawCodec|57||ro||
|**2089**|**ZigBeeTwoDeviceCurrentValues**|*O3EComplexType*|68||ro||
| |- Unknown1|RawCodec|2||||
| |- BatteryLevel|O3EInt8|1||||
| |- Unknown2|RawCodec|38||||
| |- Valve Type|O3EInt8|1||||
| |- ActualTemperature|O3EInt8|1||||
| |- OperatingStatus|O3EInt8|1||||
| |- Unknown3|RawCodec|4||||
| |- [DeviceDisplayTurned](## "{0: Standard, 1: Turned}")|O3EEnum|1||||
| |- Unknown4|RawCodec|5||||
| |- [DeviceChildLockActive](## "{0: Not Active, 1: Active}")|O3EEnum|1||||
| |- DeviceTemperatureSetpoint|O3EInt8|1||||
| |- Unknown5|RawCodec|12||||
|**2090**|**ZigBeeThreeDeviceProperty**|*O3EComplexType*|84||ro||
| |- Serialnumber|RawCodec|8||||
| |- SerialnumberPostfix|RawCodec|1||||
| |- Devicename|O3EUtf8|39||||
| |- Unknown1|RawCodec|1||||
| |- ViCareDevice|O3EEnum|1||||
| |- Firmware-Version|O3ESoftVers|8||||
| |- Unknown2|RawCodec|26||||
|**2091**|**ZigBeeThreeDeviceSetpoint**|*O3EComplexType*|13||**rw**||
| |- Prefix|RawCodec|2||||
| |- MaximumFlowTemperature|O3EInt16|2||||
| |- Unused|RawCodec|9||||
|**2092**|**ZigBeeThreeDeviceCurrentValues**|RawCodec|57||ro||
|**2092**|**ZigBeeThreeDeviceCurrentValues**|*O3EComplexType*|68||ro||
| |- Unknown1|RawCodec|2||||
| |- BatteryLevel|O3EInt8|1||||
| |- Unknown2|RawCodec|38||||
| |- Valve Type|O3EInt8|1||||
| |- ActualTemperature|O3EInt8|1||||
| |- OperatingStatus|O3EInt8|1||||
| |- Unknown3|RawCodec|4||||
| |- [DeviceDisplayTurned](## "{0: Standard, 1: Turned}")|O3EEnum|1||||
| |- Unknown4|RawCodec|5||||
| |- [DeviceChildLockActive](## "{0: Not Active, 1: Active}")|O3EEnum|1||||
| |- DeviceTemperatureSetpoint|O3EInt8|1||||
| |- Unknown5|RawCodec|12||||
|**2093**|**ZigBeeFourDeviceProperty**|*O3EComplexType*|84||ro||
| |- Serialnumber|RawCodec|8||||
| |- SerialnumberPostfix|RawCodec|1||||
| |- Devicename|O3EUtf8|39||||
| |- Unknown1|RawCodec|1||||
| |- ViCareDevice|O3EEnum|1||||
| |- Firmware-Version|O3ESoftVers|8||||
| |- Unknown2|RawCodec|26||||
|**2094**|**ZigBeeFourDeviceSetpoint**|*O3EComplexType*|13||**rw**||
| |- Prefix|RawCodec|2||||
| |- MaximumFlowTemperature|O3EInt16|2||||
| |- Unused|RawCodec|9||||
|**2095**|**ZigBeeFourDeviceCurrentValues**|RawCodec|57||ro||
|**2095**|**ZigBeeFourDeviceCurrentValues**|*O3EComplexType*|68||ro||
| |- Unknown1|RawCodec|2||||
| |- BatteryLevel|O3EInt8|1||||
| |- Unknown2|RawCodec|38||||
| |- Valve Type|O3EInt8|1||||
| |- ActualTemperature|O3EInt8|1||||
| |- OperatingStatus|O3EInt8|1||||
| |- Unknown3|RawCodec|4||||
| |- [DeviceDisplayTurned](## "{0: Standard, 1: Turned}")|O3EEnum|1||||
| |- Unknown4|RawCodec|5||||
| |- [DeviceChildLockActive](## "{0: Not Active, 1: Active}")|O3EEnum|1||||
| |- DeviceTemperatureSetpoint|O3EInt8|1||||
| |- Unknown5|RawCodec|12||||
|**2096**|**ZigBeeFiveDeviceProperty**|*O3EComplexType*|84||ro||
| |- Serialnumber|RawCodec|8||||
| |- SerialnumberPostfix|RawCodec|1||||
| |- Devicename|O3EUtf8|39||||
| |- Unknown1|RawCodec|1||||
| |- ViCareDevice|O3EEnum|1||||
| |- Firmware-Version|O3ESoftVers|8||||
| |- Unknown2|RawCodec|26||||
|**2097**|**ZigBeeFiveDeviceSetpoint**|*O3EComplexType*|13||**rw**||
| |- Prefix|RawCodec|2||||
| |- MaximumFlowTemperature|O3EInt16|2||||
| |- Unused|RawCodec|9||||
|**2098**|**ZigBeeFiveDeviceCurrentValues**|RawCodec|57||ro||
|**2098**|**ZigBeeFiveDeviceCurrentValues**|*O3EComplexType*|68||ro||
| |- Unknown1|RawCodec|2||||
| |- BatteryLevel|O3EInt8|1||||
| |- Unknown2|RawCodec|38||||
| |- Valve Type|O3EInt8|1||||
| |- ActualTemperature|O3EInt8|1||||
| |- OperatingStatus|O3EInt8|1||||
| |- Unknown3|RawCodec|4||||
| |- [DeviceDisplayTurned](## "{0: Standard, 1: Turned}")|O3EEnum|1||||
| |- Unknown4|RawCodec|5||||
| |- [DeviceChildLockActive](## "{0: Not Active, 1: Active}")|O3EEnum|1||||
| |- DeviceTemperatureSetpoint|O3EInt8|1||||
| |- Unknown5|RawCodec|12||||
|**2099**|**ZigBeeSixDeviceProperty**|*O3EComplexType*|84||ro||
| |- Serialnumber|RawCodec|8||||
| |- SerialnumberPostfix|RawCodec|1||||
| |- Devicename|O3EUtf8|39||||
| |- Unknown1|RawCodec|1||||
| |- ViCareDevice|O3EEnum|1||||
| |- Firmware-Version|O3ESoftVers|8||||
| |- Unknown2|RawCodec|26||||
|**2100**|**ZigBeeSixDeviceSetpoint**|*O3EComplexType*|13||**rw**||
| |- Prefix|RawCodec|2||||
| |- MaximumFlowTemperature|O3EInt16|2||||
| |- Unused|RawCodec|9||||
|**2101**|**ZigBeeSixDeviceCurrentValues**|RawCodec|57||ro||
|**2101**|**ZigBeeSixDeviceCurrentValues**|*O3EComplexType*|68||ro||
| |- Unknown1|RawCodec|2||||
| |- BatteryLevel|O3EInt8|1||||
| |- Unknown2|RawCodec|38||||
| |- Valve Type|O3EInt8|1||||
| |- ActualTemperature|O3EInt8|1||||
| |- OperatingStatus|O3EInt8|1||||
| |- Unknown3|RawCodec|4||||
| |- [DeviceDisplayTurned](## "{0: Standard, 1: Turned}")|O3EEnum|1||||
| |- Unknown4|RawCodec|5||||
| |- [DeviceChildLockActive](## "{0: Not Active, 1: Active}")|O3EEnum|1||||
| |- DeviceTemperatureSetpoint|O3EInt8|1||||
| |- Unknown5|RawCodec|12||||
|**2102**|**ZigBeeSevenDeviceProperty**|*O3EComplexType*|84||ro||
| |- Serialnumber|RawCodec|8||||
| |- SerialnumberPostfix|RawCodec|1||||
| |- Devicename|O3EUtf8|39||||
| |- Unknown1|RawCodec|1||||
| |- ViCareDevice|O3EEnum|1||||
| |- Firmware-Version|O3ESoftVers|8||||
| |- Unknown2|RawCodec|26||||
|**2103**|**ZigBeeSevenDeviceSetpoint**|*O3EComplexType*|13||**rw**||
| |- Prefix|RawCodec|2||||
| |- MaximumFlowTemperature|O3EInt16|2||||
| |- Unused|RawCodec|9||||
|**2104**|**ZigBeeSevenDeviceCurrentValues**|RawCodec|57||ro||
|**2104**|**ZigBeeSevenDeviceCurrentValues**|*O3EComplexType*|68||ro||
| |- Unknown1|RawCodec|2||||
| |- BatteryLevel|O3EInt8|1||||
| |- Unknown2|RawCodec|38||||
| |- Valve Type|O3EInt8|1||||
| |- ActualTemperature|O3EInt8|1||||
| |- OperatingStatus|O3EInt8|1||||
| |- Unknown3|RawCodec|4||||
| |- [DeviceDisplayTurned](## "{0: Standard, 1: Turned}")|O3EEnum|1||||
| |- Unknown4|RawCodec|5||||
| |- [DeviceChildLockActive](## "{0: Not Active, 1: Active}")|O3EEnum|1||||
| |- DeviceTemperatureSetpoint|O3EInt8|1||||
| |- Unknown5|RawCodec|12||||
|**2105**|**ZigBeeEightDeviceProperty**|*O3EComplexType*|84||ro||
| |- Serialnumber|RawCodec|8||||
| |- SerialnumberPostfix|RawCodec|1||||
| |- Devicename|O3EUtf8|39||||
| |- Unknown1|RawCodec|1||||
| |- ViCareDevice|O3EEnum|1||||
| |- Firmware-Version|O3ESoftVers|8||||
| |- Unknown2|RawCodec|26||||
|**2106**|**ZigBeeEightDeviceSetpoint**|*O3EComplexType*|13||**rw**||
| |- Prefix|RawCodec|2||||
| |- MaximumFlowTemperature|O3EInt16|2||||
| |- Unused|RawCodec|9||||
|**2107**|**ZigBeeEightDeviceCurrentValues**|RawCodec|57||ro||
|**2107**|**ZigBeeEightDeviceCurrentValues**|*O3EComplexType*|68||ro||
| |- Unknown1|RawCodec|2||||
| |- BatteryLevel|O3EInt8|1||||
| |- Unknown2|RawCodec|38||||
| |- Valve Type|O3EInt8|1||||
| |- ActualTemperature|O3EInt8|1||||
| |- OperatingStatus|O3EInt8|1||||
| |- Unknown3|RawCodec|4||||
| |- [DeviceDisplayTurned](## "{0: Standard, 1: Turned}")|O3EEnum|1||||
| |- Unknown4|RawCodec|5||||
| |- [DeviceChildLockActive](## "{0: Not Active, 1: Active}")|O3EEnum|1||||
| |- DeviceTemperatureSetpoint|O3EInt8|1||||
| |- Unknown5|RawCodec|12||||
|**2108**|**ZigBeeNineDeviceProperty**|*O3EComplexType*|84||ro||
| |- Serialnumber|RawCodec|8||||
| |- SerialnumberPostfix|RawCodec|1||||
| |- Devicename|O3EUtf8|39||||
| |- Unknown1|RawCodec|1||||
| |- ViCareDevice|O3EEnum|1||||
| |- Firmware-Version|O3ESoftVers|8||||
| |- Unknown2|RawCodec|26||||
|**2109**|**ZigBeeNineDeviceSetpoint**|*O3EComplexType*|13||**rw**||
| |- Prefix|RawCodec|2||||
| |- MaximumFlowTemperature|O3EInt16|2||||
| |- Unused|RawCodec|9||||
|**2110**|**ZigBeeNineDeviceCurrentValues**|RawCodec|57||ro||
|**2110**|**ZigBeeNineDeviceCurrentValues**|*O3EComplexType*|68||ro||
| |- Unknown1|RawCodec|2||||
| |- BatteryLevel|O3EInt8|1||||
| |- Unknown2|RawCodec|38||||
| |- Valve Type|O3EInt8|1||||
| |- ActualTemperature|O3EInt8|1||||
| |- OperatingStatus|O3EInt8|1||||
| |- Unknown3|RawCodec|4||||
| |- [DeviceDisplayTurned](## "{0: Standard, 1: Turned}")|O3EEnum|1||||
| |- Unknown4|RawCodec|5||||
| |- [DeviceChildLockActive](## "{0: Not Active, 1: Active}")|O3EEnum|1||||
| |- DeviceTemperatureSetpoint|O3EInt8|1||||
| |- Unknown5|RawCodec|12||||
|**2111**|**ZigBeeTenDeviceProperty**|*O3EComplexType*|84||ro||
| |- Serialnumber|RawCodec|8||||
| |- SerialnumberPostfix|RawCodec|1||||
| |- Devicename|O3EUtf8|39||||
| |- Unknown1|RawCodec|1||||
| |- ViCareDevice|O3EEnum|1||||
| |- Firmware-Version|O3ESoftVers|8||||
| |- Unknown2|RawCodec|26||||
|**2112**|**ZigBeeTenDeviceSetpoint**|*O3EComplexType*|13||**rw**||
| |- Prefix|RawCodec|2||||
| |- MaximumFlowTemperature|O3EInt16|2||||
| |- Unused|RawCodec|9||||
|**2113**|**ZigBeeTenDeviceCurrentValues**|RawCodec|57||ro||
|**2113**|**ZigBeeTenDeviceCurrentValues**|*O3EComplexType*|68||ro||
| |- Unknown1|RawCodec|2||||
| |- BatteryLevel|O3EInt8|1||||
| |- Unknown2|RawCodec|38||||
| |- Valve Type|O3EInt8|1||||
| |- ActualTemperature|O3EInt8|1||||
| |- OperatingStatus|O3EInt8|1||||
| |- Unknown3|RawCodec|4||||
| |- [DeviceDisplayTurned](## "{0: Standard, 1: Turned}")|O3EEnum|1||||
| |- Unknown4|RawCodec|5||||
| |- [DeviceChildLockActive](## "{0: Not Active, 1: Active}")|O3EEnum|1||||
| |- DeviceTemperatureSetpoint|O3EInt8|1||||
| |- Unknown5|RawCodec|12||||
|**2114**|**ZigBeeElevenDeviceProperty**|*O3EComplexType*|84||ro||
| |- Serialnumber|RawCodec|8||||
| |- SerialnumberPostfix|RawCodec|1||||
| |- Devicename|O3EUtf8|39||||
| |- Unknown1|RawCodec|1||||
| |- ViCareDevice|O3EEnum|1||||
| |- Firmware-Version|O3ESoftVers|8||||
| |- Unknown2|RawCodec|26||||
|**2115**|**ZigBeeElevenDeviceSetpoint**|*O3EComplexType*|13||**rw**||
| |- Prefix|RawCodec|2||||
| |- MaximumFlowTemperature|O3EInt16|2||||
| |- Unused|RawCodec|9||||
|**2116**|**ZigBeeElevenDeviceCurrentValues**|RawCodec|57||ro||
|**2116**|**ZigBeeElevenDeviceCurrentValues**|*O3EComplexType*|68||ro||
| |- Unknown1|RawCodec|2||||
| |- BatteryLevel|O3EInt8|1||||
| |- Unknown2|RawCodec|38||||
| |- Valve Type|O3EInt8|1||||
| |- ActualTemperature|O3EInt8|1||||
| |- OperatingStatus|O3EInt8|1||||
| |- Unknown3|RawCodec|4||||
| |- [DeviceDisplayTurned](## "{0: Standard, 1: Turned}")|O3EEnum|1||||
| |- Unknown4|RawCodec|5||||
| |- [DeviceChildLockActive](## "{0: Not Active, 1: Active}")|O3EEnum|1||||
| |- DeviceTemperatureSetpoint|O3EInt8|1||||
| |- Unknown5|RawCodec|12||||
|**2117**|**ZigBeeTwelveDeviceProperty**|*O3EComplexType*|84||ro||
| |- Serialnumber|RawCodec|8||||
| |- SerialnumberPostfix|RawCodec|1||||
| |- Devicename|O3EUtf8|39||||
| |- Unknown1|RawCodec|1||||
| |- ViCareDevice|O3EEnum|1||||
| |- Firmware-Version|O3ESoftVers|8||||
| |- Unknown2|RawCodec|26||||
|**2118**|**ZigBeeTwelveDeviceSetpoint**|*O3EComplexType*|13||**rw**||
| |- Prefix|RawCodec|2||||
| |- MaximumFlowTemperature|O3EInt16|2||||
| |- Unused|RawCodec|9||||
|**2119**|**ZigBeeTwelveDeviceCurrentValues**|RawCodec|57||ro||
|**2119**|**ZigBeeTwelveDeviceCurrentValues**|*O3EComplexType*|68||ro||
| |- Unknown1|RawCodec|2||||
| |- BatteryLevel|O3EInt8|1||||
| |- Unknown2|RawCodec|38||||
| |- Valve Type|O3EInt8|1||||
| |- ActualTemperature|O3EInt8|1||||
| |- OperatingStatus|O3EInt8|1||||
| |- Unknown3|RawCodec|4||||
| |- [DeviceDisplayTurned](## "{0: Standard, 1: Turned}")|O3EEnum|1||||
| |- Unknown4|RawCodec|5||||
| |- [DeviceChildLockActive](## "{0: Not Active, 1: Active}")|O3EEnum|1||||
| |- DeviceTemperatureSetpoint|O3EInt8|1||||
| |- Unknown5|RawCodec|12||||
|**2120**|**ZigBeeThirteenDeviceProperty**|*O3EComplexType*|84||ro||
| |- Serialnumber|RawCodec|8||||
| |- SerialnumberPostfix|RawCodec|1||||
| |- Devicename|O3EUtf8|39||||
| |- Unknown1|RawCodec|1||||
| |- ViCareDevice|O3EEnum|1||||
| |- Firmware-Version|O3ESoftVers|8||||
| |- Unknown2|RawCodec|26||||
|**2121**|**ZigBeeThirteenDeviceSetpoint**|*O3EComplexType*|13||**rw**||
| |- Prefix|RawCodec|2||||
| |- MaximumFlowTemperature|O3EInt16|2||||
| |- Unused|RawCodec|9||||
|**2122**|**ZigBeeThirteenDeviceCurrentValues**|RawCodec|57||ro||
|**2122**|**ZigBeeThirteenDeviceCurrentValues**|*O3EComplexType*|68||ro||
| |- Unknown1|RawCodec|2||||
| |- BatteryLevel|O3EInt8|1||||
| |- Unknown2|RawCodec|38||||
| |- Valve Type|O3EInt8|1||||
| |- ActualTemperature|O3EInt8|1||||
| |- OperatingStatus|O3EInt8|1||||
| |- Unknown3|RawCodec|4||||
| |- [DeviceDisplayTurned](## "{0: Standard, 1: Turned}")|O3EEnum|1||||
| |- Unknown4|RawCodec|5||||
| |- [DeviceChildLockActive](## "{0: Not Active, 1: Active}")|O3EEnum|1||||
| |- DeviceTemperatureSetpoint|O3EInt8|1||||
| |- Unknown5|RawCodec|12||||
|**2123**|**ZigBeeFourteenDeviceProperty**|*O3EComplexType*|84||ro||
| |- Serialnumber|RawCodec|8||||
| |- SerialnumberPostfix|RawCodec|1||||
| |- Devicename|O3EUtf8|39||||
| |- Unknown1|RawCodec|1||||
| |- ViCareDevice|O3EEnum|1||||
| |- Firmware-Version|O3ESoftVers|8||||
| |- Unknown2|RawCodec|26||||
|**2124**|**ZigBeeFourteenDeviceSetpoint**|*O3EComplexType*|13||**rw**||
| |- Prefix|RawCodec|2||||
| |- MaximumFlowTemperature|O3EInt16|2||||
| |- Unused|RawCodec|9||||
|**2125**|**ZigBeeFourteenDeviceCurrentValues**|RawCodec|57||ro||
|**2125**|**ZigBeeFourteenDeviceCurrentValues**|*O3EComplexType*|68||ro||
| |- Unknown1|RawCodec|2||||
| |- BatteryLevel|O3EInt8|1||||
| |- Unknown2|RawCodec|38||||
| |- Valve Type|O3EInt8|1||||
| |- ActualTemperature|O3EInt8|1||||
| |- OperatingStatus|O3EInt8|1||||
| |- Unknown3|RawCodec|4||||
| |- [DeviceDisplayTurned](## "{0: Standard, 1: Turned}")|O3EEnum|1||||
| |- Unknown4|RawCodec|5||||
| |- [DeviceChildLockActive](## "{0: Not Active, 1: Active}")|O3EEnum|1||||
| |- DeviceTemperatureSetpoint|O3EInt8|1||||
| |- Unknown5|RawCodec|12||||
|**2126**|**ZigBeeFifteenDeviceProperty**|*O3EComplexType*|84||ro||
| |- Serialnumber|RawCodec|8||||
| |- SerialnumberPostfix|RawCodec|1||||
| |- Devicename|O3EUtf8|39||||
| |- Unknown1|RawCodec|1||||
| |- ViCareDevice|O3EEnum|1||||
| |- Firmware-Version|O3ESoftVers|8||||
| |- Unknown2|RawCodec|26||||
|**2127**|**ZigBeeFifteenDeviceSetpoint**|*O3EComplexType*|13||**rw**||
| |- Prefix|RawCodec|2||||
| |- MaximumFlowTemperature|O3EInt16|2||||
| |- Unused|RawCodec|9||||
|**2128**|**ZigBeeFifteenDeviceCurrentValues**|RawCodec|57||ro||
|**2128**|**ZigBeeFifteenDeviceCurrentValues**|*O3EComplexType*|68||ro||
| |- Unknown1|RawCodec|2||||
| |- BatteryLevel|O3EInt8|1||||
| |- Unknown2|RawCodec|38||||
| |- Valve Type|O3EInt8|1||||
| |- ActualTemperature|O3EInt8|1||||
| |- OperatingStatus|O3EInt8|1||||
| |- Unknown3|RawCodec|4||||
| |- [DeviceDisplayTurned](## "{0: Standard, 1: Turned}")|O3EEnum|1||||
| |- Unknown4|RawCodec|5||||
| |- [DeviceChildLockActive](## "{0: Not Active, 1: Active}")|O3EEnum|1||||
| |- DeviceTemperatureSetpoint|O3EInt8|1||||
| |- Unknown5|RawCodec|12||||
|**2129**|**ZigBeeSixteenDeviceProperty**|*O3EComplexType*|84||ro||
| |- Serialnumber|RawCodec|8||||
| |- SerialnumberPostfix|RawCodec|1||||
| |- Devicename|O3EUtf8|39||||
| |- Unknown1|RawCodec|1||||
| |- ViCareDevice|O3EEnum|1||||
| |- Firmware-Version|O3ESoftVers|8||||
| |- Unknown2|RawCodec|26||||
|**2130**|**ZigBeeSixteenDeviceSetpoint**|*O3EComplexType*|13||**rw**||
| |- Prefix|RawCodec|2||||
| |- MaximumFlowTemperature|O3EInt16|2||||
| |- Unused|RawCodec|9||||
|**2131**|**ZigBeeSixteenDeviceCurrentValues**|RawCodec|57||ro||
|**2131**|**ZigBeeSixteenDeviceCurrentValues**|*O3EComplexType*|68||ro||
| |- Unknown1|RawCodec|2||||
| |- BatteryLevel|O3EInt8|1||||
| |- Unknown2|RawCodec|38||||
| |- Valve Type|O3EInt8|1||||
| |- ActualTemperature|O3EInt8|1||||
| |- OperatingStatus|O3EInt8|1||||
| |- Unknown3|RawCodec|4||||
| |- [DeviceDisplayTurned](## "{0: Standard, 1: Turned}")|O3EEnum|1||||
| |- Unknown4|RawCodec|5||||
| |- [DeviceChildLockActive](## "{0: Not Active, 1: Active}")|O3EEnum|1||||
| |- DeviceTemperatureSetpoint|O3EInt8|1||||
| |- Unknown5|RawCodec|12||||
|**2132**|**ZigBeeSeventeenDeviceProperty**|*O3EComplexType*|84||ro||
| |- Serialnumber|RawCodec|8||||
| |- SerialnumberPostfix|RawCodec|1||||
| |- Devicename|O3EUtf8|39||||
| |- Unknown1|RawCodec|1||||
| |- ViCareDevice|O3EEnum|1||||
| |- Firmware-Version|O3ESoftVers|8||||
| |- Unknown2|RawCodec|26||||
|**2133**|**ZigBeeSeventeenDeviceSetpoint**|*O3EComplexType*|13||**rw**||
| |- Prefix|RawCodec|2||||
| |- MaximumFlowTemperature|O3EInt16|2||||
| |- Unused|RawCodec|9||||
|**2134**|**ZigBeeSeventeenDeviceCurrentValues**|RawCodec|57||ro||
|**2134**|**ZigBeeSeventeenDeviceCurrentValues**|*O3EComplexType*|68||ro||
| |- Unknown1|RawCodec|2||||
| |- BatteryLevel|O3EInt8|1||||
| |- Unknown2|RawCodec|38||||
| |- Valve Type|O3EInt8|1||||
| |- ActualTemperature|O3EInt8|1||||
| |- OperatingStatus|O3EInt8|1||||
| |- Unknown3|RawCodec|4||||
| |- [DeviceDisplayTurned](## "{0: Standard, 1: Turned}")|O3EEnum|1||||
| |- Unknown4|RawCodec|5||||
| |- [DeviceChildLockActive](## "{0: Not Active, 1: Active}")|O3EEnum|1||||
| |- DeviceTemperatureSetpoint|O3EInt8|1||||
| |- Unknown5|RawCodec|12||||
|**2135**|**ZigBeeEighteenDeviceProperty**|*O3EComplexType*|84||ro||
| |- Serialnumber|RawCodec|8||||
| |- SerialnumberPostfix|RawCodec|1||||
| |- Devicename|O3EUtf8|39||||
| |- Unknown1|RawCodec|1||||
| |- ViCareDevice|O3EEnum|1||||
| |- Firmware-Version|O3ESoftVers|8||||
| |- Unknown2|RawCodec|26||||
|**2136**|**ZigBeeEighteenDeviceSetpoint**|*O3EComplexType*|13||**rw**||
| |- Prefix|RawCodec|2||||
| |- MaximumFlowTemperature|O3EInt16|2||||
| |- Unused|RawCodec|9||||
|**2137**|**ZigBeeEighteenDeviceCurrentValues**|RawCodec|57||ro||
|**2137**|**ZigBeeEighteenDeviceCurrentValues**|*O3EComplexType*|68||ro||
| |- Unknown1|RawCodec|2||||
| |- BatteryLevel|O3EInt8|1||||
| |- Unknown2|RawCodec|38||||
| |- Valve Type|O3EInt8|1||||
| |- ActualTemperature|O3EInt8|1||||
| |- OperatingStatus|O3EInt8|1||||
| |- Unknown3|RawCodec|4||||
| |- [DeviceDisplayTurned](## "{0: Standard, 1: Turned}")|O3EEnum|1||||
| |- Unknown4|RawCodec|5||||
| |- [DeviceChildLockActive](## "{0: Not Active, 1: Active}")|O3EEnum|1||||
| |- DeviceTemperatureSetpoint|O3EInt8|1||||
| |- Unknown5|RawCodec|12||||
|**2138**|**ZigBeeNineteenDeviceProperty**|*O3EComplexType*|84||ro||
| |- Serialnumber|RawCodec|8||||
| |- SerialnumberPostfix|RawCodec|1||||
| |- Devicename|O3EUtf8|39||||
| |- Unknown1|RawCodec|1||||
| |- ViCareDevice|O3EEnum|1||||
| |- Firmware-Version|O3ESoftVers|8||||
| |- Unknown2|RawCodec|26||||
|**2139**|**ZigBeeNineteenDeviceSetpoint**|*O3EComplexType*|13||**rw**||
| |- Prefix|RawCodec|2||||
| |- MaximumFlowTemperature|O3EInt16|2||||
| |- Unused|RawCodec|9||||
|**2140**|**ZigBeeNineteenDeviceCurrentValues**|RawCodec|57||ro||
|**2140**|**ZigBeeNineteenDeviceCurrentValues**|*O3EComplexType*|68||ro||
| |- Unknown1|RawCodec|2||||
| |- BatteryLevel|O3EInt8|1||||
| |- Unknown2|RawCodec|38||||
| |- Valve Type|O3EInt8|1||||
| |- ActualTemperature|O3EInt8|1||||
| |- OperatingStatus|O3EInt8|1||||
| |- Unknown3|RawCodec|4||||
| |- [DeviceDisplayTurned](## "{0: Standard, 1: Turned}")|O3EEnum|1||||
| |- Unknown4|RawCodec|5||||
| |- [DeviceChildLockActive](## "{0: Not Active, 1: Active}")|O3EEnum|1||||
| |- DeviceTemperatureSetpoint|O3EInt8|1||||
| |- Unknown5|RawCodec|12||||
|**2141**|**ZigBeeTwentyDeviceProperty**|*O3EComplexType*|84||ro||
| |- Serialnumber|RawCodec|8||||
| |- SerialnumberPostfix|RawCodec|1||||
| |- Devicename|O3EUtf8|39||||
| |- Unknown1|RawCodec|1||||
| |- ViCareDevice|O3EEnum|1||||
| |- Firmware-Version|O3ESoftVers|8||||
| |- Unknown2|RawCodec|26||||
|**2142**|**ZigBeeTwentyDeviceSetpoint**|*O3EComplexType*|13||**rw**||
| |- Prefix|RawCodec|2||||
| |- MaximumFlowTemperature|O3EInt16|2||||
| |- Unused|RawCodec|9||||
|**2143**|**ZigBeeTwentyDeviceCurrentValues**|RawCodec|57||ro||
|**2143**|**ZigBeeTwentyDeviceCurrentValues**|*O3EComplexType*|68||ro||
| |- Unknown1|RawCodec|2||||
| |- BatteryLevel|O3EInt8|1||||
| |- Unknown2|RawCodec|38||||
| |- Valve Type|O3EInt8|1||||
| |- ActualTemperature|O3EInt8|1||||
| |- OperatingStatus|O3EInt8|1||||
| |- Unknown3|RawCodec|4||||
| |- [DeviceDisplayTurned](## "{0: Standard, 1: Turned}")|O3EEnum|1||||
| |- Unknown4|RawCodec|5||||
| |- [DeviceChildLockActive](## "{0: Not Active, 1: Active}")|O3EEnum|1||||
| |- DeviceTemperatureSetpoint|O3EInt8|1||||
| |- Unknown5|RawCodec|12||||
|**2144**|**PointOfCommonCouplingAcActiveCurrent**|RawCodec|16||ro||
|**2145**|**ObjectTopology**|RawCodec|38||ro||
|**2146**|**ZigBeeApartmentOneProperty**|RawCodec|8||ro||
|**2147**|**ZigBeeApartmentOneTopology**|RawCodec|106||ro||
|**2158**|**ActivatedFeatures**|RawCodec|16||ro||
|**2159**|**ApartmentOneCurrentValues**|RawCodec|84||ro||
|**2164**|**DeviceDigitalInputSixValue**|O3EByteVal|1||ro||
|**2165**|**DevicePwmOutputThreeValue**|O3EInt8|1||ro||
|**2166**|**MixerOneCircuitExternalHookupDemandInput**|RawCodec|1||ro||
|**2167**|**MixerTwoCircuitExternalHookupDemandInput**|RawCodec|1||ro||
|**2168**|**MixerThreeCircuitExternalHookupDemandInput**|RawCodec|1||ro||
|**2169**|**MixerFourCircuitExternalHookupDemandInput**|RawCodec|1||ro||
|**2182**|**SupportedApartmentFeatures**|RawCodec|15||ro||
|**2183**|**ActivatedApartmentFeatures**|RawCodec|15||ro||
|**2184**|**BackupBoxTest**|RawCodec|2||ro||
|**2185**|**BatteryStateOfChargeHistogram**|RawCodec|40||ro||
|**2188**|**PointOfCommonCouplingSetActivePowerTotal**|RawCodec|6||ro||
|**2189**|**EebusDeviceListTwo**|RawCodec|104||ro||
|**2190**|**EebusDeviceListThree**|RawCodec|104||ro||
|**2191**|**EebusDeviceListFour**|RawCodec|104||ro||
|**2192**|**EebusDeviceListFive**|RawCodec|104||ro||
|**2193**|**ApartmentOneSupplyChannelTwoTimeScheduleMonday**|RawCodec|57||**rw**||
|**2194**|**ApartmentOneSupplyChannelTwoTimeScheduleTuesday**|RawCodec|57||**rw**||
|**2195**|**ApartmentOneSupplyChannelTwoTimeScheduleWednesday**|RawCodec|57||**rw**||
|**2196**|**ApartmentOneSupplyChannelTwoTimeScheduleThursday**|RawCodec|57||**rw**||
|**2197**|**ApartmentOneSupplyChannelTwoTimeScheduleFriday**|RawCodec|57||**rw**||
|**2198**|**ApartmentOneSupplyChannelTwoTimeScheduleSaturday**|RawCodec|57||**rw**||
|**2199**|**ApartmentOneSupplyChannelTwoTimeScheduleSunday**|RawCodec|57||**rw**||
|**2200**|**ApartmentOneSupplyChannelThreeTimeScheduleMonday**|RawCodec|57||**rw**||
|**2201**|**ApartmentOneSupplyChannelThreeTimeScheduleTuesday**|RawCodec|57||**rw**||
|**2202**|**ApartmentOneSupplyChannelThreeTimeScheduleWednesday**|RawCodec|57||**rw**||
|**2203**|**ApartmentOneSupplyChannelThreeTimeScheduleThursday**|RawCodec|57||**rw**||
|**2204**|**ApartmentOneSupplyChannelThreeTimeScheduleFriday**|RawCodec|57||**rw**||
|**2205**|**ApartmentOneSupplyChannelThreeTimeScheduleSaturday**|RawCodec|57||**rw**||
|**2206**|**ApartmentOneSupplyChannelThreeTimeScheduleSunday**|RawCodec|57||**rw**||
|**2207**|**ApartmentOneSupplyChannelFourTimeScheduleMonday**|RawCodec|57||**rw**||
|**2208**|**ApartmentOneSupplyChannelFourTimeScheduleTuesday**|RawCodec|57||**rw**||
|**2209**|**ApartmentOneSupplyChannelFourTimeScheduleWednesday**|RawCodec|57||**rw**||
|**2210**|**ApartmentOneSupplyChannelFourTimeScheduleThursday**|RawCodec|57||**rw**||
|**2211**|**ApartmentOneSupplyChannelFourTimeScheduleFriday**|RawCodec|57||**rw**||
|**2212**|**ApartmentOneSupplyChannelFourTimeScheduleSaturday**|RawCodec|57||**rw**||
|**2213**|**ApartmentOneSupplyChannelFourTimeScheduleSunday**|RawCodec|57||**rw**||
|**2214**|[**BackupBoxConfiguration**](## "Configuration for Backup Box")|*O3EComplexType*|2||**rw**||
| |- [DischargeLimit](## "Discharge limit of battery")|O3EInt8|1|%|||
| |- Unknown|O3EInt8|1||||
|**2217**|**InputDemandSideManagementlReceiver**|RawCodec|1||ro||
|**2218**|**RemoteLimitValueDemandSideManagement**|RawCodec|4||ro||
|**2219**|**BatteryCalibration**|RawCodec|1||ro||
|**2220**|**BatteryReactivePowerMode**|RawCodec|1||ro||
|**2221**|**BatteryReactivePowerFixCosinusPhi**|RawCodec|3||ro||
|**2222**|**BatteryReactivePower**|RawCodec|18||ro||
|**2223**|**BatteryReactivePowerCosinusPhi**|RawCodec|15||ro||
|**2224**|**PhotovoltaicsActivePowerLimitation**|RawCodec|16||ro||
|**2225**|**ElectricEnergyStorageSetpoint**|RawCodec|12||**rw**||
|**2226**|**ElectricEnergyStorageMaximum**|RawCodec|12||ro||
|**2229**|**ThermostatTerminalOneFunction**|RawCodec|1||ro||
|**2230**|**ThermostatTerminalTwoFunction**|RawCodec|1||ro||
|**2231**|**ThermostatTerminalThreeFunction**|RawCodec|1||ro||
|**2233**|**PersistentStorageStatus**|O3EByteVal|1||ro||
|**2234**|**PowerGridCodeSettingsNormOne**|RawCodec|27||ro||
|**2235**|**CascadeSystemConfiguration**|RawCodec|65||ro||
|**2236**|**CascadeDeviceSetpoint**|RawCodec|10||**rw**||
|**2237**|**CascadeDeviceStatus**|RawCodec|18||ro||
|**2239**|**ElectricEnergyStorageControlMode**|RawCodec|1||ro||
|**2240**|**BatteryTemperatureSensor**|*O3EComplexType*|9||ro||
| |- Actual|O3EInt16|2||||
| |- Minimum|O3EInt16|2||||
| |- Maximum|O3EInt16|2||||
| |- Average|O3EInt16|2||||
| |- [SensorStatus](## "{0: no_error, 1: interruption, 2: short_circuit, 3: electrical_fault, 4: not_available, 5: invalidates}")|O3EEnum|1||||
|**2241**|**OutsideTemperatureSensorSource**|RawCodec|1||ro||
|**2242**|**PowerGridCodeSettingsNormTwo**|RawCodec|27||ro||
|**2244**|**PowerGridCodeSettingsNormFour**|RawCodec|27||ro||
|**2246**|**FixReactivePowerIn**|RawCodec|26||ro||
|**2247**|**FilterRuntime**|*O3EComplexType*|12||ro||
| |- Actual|O3EInt32|4||||
| |- Remaining|O3EInt32|4||||
| |- Overdue|O3EInt32|4||||
|**2248**|**CurrentVentilationHeatRecovery**|O3EByteVal|1||ro||
|**2249**|**DigitalSwitchSettingOne**|RawCodec|8||ro||
|**2250**|**DigitalSwitchSettingTwo**|RawCodec|8||ro||
|**2251**|**LedStatusOne**|RawCodec|8||ro||
|**2252**|**LedStatusTwo**|RawCodec|8||ro||
|**2253**|**DeviceDigitalInputSevenValue**|O3EByteVal|1||ro||
|**2254**|**PowerGridCodeSettingConfiguration**|RawCodec|1||ro||
|**2255**|**MinimumSecondaryReturnTemperatureRefrigerantCircuit**|O3EInt16|2||ro||
|**2256**|[**DesiredThermalEnergyDefrost**](## "Target value of thermal energy to perform next defrosting")|O3EInt16|2|Wh|ro||
|**2257**|**DomesticHotWaterTemperatureSetpointOffset**|O3EInt16|2||**rw**||
|**2259**|**RefrigerationCircuitStatus**|O3EByteVal|1||ro||
|**2260**|**ZigBeeTwentyOneDeviceProperty**|*O3EComplexType*|84||ro||
| |- Serialnumber|RawCodec|8||||
| |- SerialnumberPostfix|RawCodec|1||||
| |- Devicename|O3EUtf8|39||||
| |- Unknown1|RawCodec|1||||
| |- ViCareDevice|O3EEnum|1||||
| |- Firmware-Version|O3ESoftVers|8||||
| |- Unknown2|RawCodec|26||||
|**2261**|**ZigBeeTwentyOneDeviceSetpoint**|*O3EComplexType*|13||**rw**||
| |- Prefix|RawCodec|2||||
| |- MaximumFlowTemperature|O3EInt16|2||||
| |- Unused|RawCodec|9||||
|**2262**|**ZigBeeTwentyOneDeviceCurrentValues**|RawCodec|57||ro||
|**2262**|**ZigBeeTwentyOneDeviceCurrentValues**|*O3EComplexType*|68||ro||
| |- Unknown1|RawCodec|2||||
| |- BatteryLevel|O3EInt8|1||||
| |- Unknown2|RawCodec|38||||
| |- Valve Type|O3EInt8|1||||
| |- ActualTemperature|O3EInt8|1||||
| |- OperatingStatus|O3EInt8|1||||
| |- Unknown3|RawCodec|4||||
| |- [DeviceDisplayTurned](## "{0: Standard, 1: Turned}")|O3EEnum|1||||
| |- Unknown4|RawCodec|5||||
| |- [DeviceChildLockActive](## "{0: Not Active, 1: Active}")|O3EEnum|1||||
| |- DeviceTemperatureSetpoint|O3EInt8|1||||
| |- Unknown5|RawCodec|12||||
|**2263**|**ZigBeeTwentyTwoDeviceProperty**|*O3EComplexType*|84||ro||
| |- Serialnumber|RawCodec|8||||
| |- SerialnumberPostfix|RawCodec|1||||
| |- Devicename|O3EUtf8|39||||
| |- Unknown1|RawCodec|1||||
| |- ViCareDevice|O3EEnum|1||||
| |- Firmware-Version|O3ESoftVers|8||||
| |- Unknown2|RawCodec|26||||
|**2264**|**ZigBeeTwentyTwoDeviceSetpoint**|*O3EComplexType*|13||**rw**||
| |- Prefix|RawCodec|2||||
| |- MaximumFlowTemperature|O3EInt16|2||||
| |- Unused|RawCodec|9||||
|**2265**|**ZigBeeTwentyTwoDeviceCurrentValues**|RawCodec|57||ro||
|**2265**|**ZigBeeTwentyTwoDeviceCurrentValues**|*O3EComplexType*|68||ro||
| |- Unknown1|RawCodec|2||||
| |- BatteryLevel|O3EInt8|1||||
| |- Unknown2|RawCodec|38||||
| |- Valve Type|O3EInt8|1||||
| |- ActualTemperature|O3EInt8|1||||
| |- OperatingStatus|O3EInt8|1||||
| |- Unknown3|RawCodec|4||||
| |- [DeviceDisplayTurned](## "{0: Standard, 1: Turned}")|O3EEnum|1||||
| |- Unknown4|RawCodec|5||||
| |- [DeviceChildLockActive](## "{0: Not Active, 1: Active}")|O3EEnum|1||||
| |- DeviceTemperatureSetpoint|O3EInt8|1||||
| |- Unknown5|RawCodec|12||||
|**2266**|**ZigBeeTwentyThreeDeviceProperty**|*O3EComplexType*|84||ro||
| |- Serialnumber|RawCodec|8||||
| |- SerialnumberPostfix|RawCodec|1||||
| |- Devicename|O3EUtf8|39||||
| |- Unknown1|RawCodec|1||||
| |- ViCareDevice|O3EEnum|1||||
| |- Firmware-Version|O3ESoftVers|8||||
| |- Unknown2|RawCodec|26||||
|**2267**|**ZigBeeTwentyThreeDeviceSetpoint**|*O3EComplexType*|13||**rw**||
| |- Prefix|RawCodec|2||||
| |- MaximumFlowTemperature|O3EInt16|2||||
| |- Unused|RawCodec|9||||
|**2268**|**ZigBeeTwentyThreeDeviceCurrentValues**|RawCodec|57||ro||
|**2268**|**ZigBeeTwentyThreeDeviceCurrentValues**|*O3EComplexType*|68||ro||
| |- Unknown1|RawCodec|2||||
| |- BatteryLevel|O3EInt8|1||||
| |- Unknown2|RawCodec|38||||
| |- Valve Type|O3EInt8|1||||
| |- ActualTemperature|O3EInt8|1||||
| |- OperatingStatus|O3EInt8|1||||
| |- Unknown3|RawCodec|4||||
| |- [DeviceDisplayTurned](## "{0: Standard, 1: Turned}")|O3EEnum|1||||
| |- Unknown4|RawCodec|5||||
| |- [DeviceChildLockActive](## "{0: Not Active, 1: Active}")|O3EEnum|1||||
| |- DeviceTemperatureSetpoint|O3EInt8|1||||
| |- Unknown5|RawCodec|12||||
|**2269**|**ZigBeeTwentyFourDeviceProperty**|*O3EComplexType*|84||ro||
| |- Serialnumber|RawCodec|8||||
| |- SerialnumberPostfix|RawCodec|1||||
| |- Devicename|O3EUtf8|39||||
| |- Unknown1|RawCodec|1||||
| |- ViCareDevice|O3EEnum|1||||
| |- Firmware-Version|O3ESoftVers|8||||
| |- Unknown2|RawCodec|26||||
|**2270**|**ZigBeeTwentyFourDeviceSetpoint**|*O3EComplexType*|13||**rw**||
| |- Prefix|RawCodec|2||||
| |- MaximumFlowTemperature|O3EInt16|2||||
| |- Unused|RawCodec|9||||
|**2271**|**ZigBeeTwentyFourDeviceCurrentValues**|RawCodec|57||ro||
|**2271**|**ZigBeeTwentyFourDeviceCurrentValues**|*O3EComplexType*|68||ro||
| |- Unknown1|RawCodec|2||||
| |- BatteryLevel|O3EInt8|1||||
| |- Unknown2|RawCodec|38||||
| |- Valve Type|O3EInt8|1||||
| |- ActualTemperature|O3EInt8|1||||
| |- OperatingStatus|O3EInt8|1||||
| |- Unknown3|RawCodec|4||||
| |- [DeviceDisplayTurned](## "{0: Standard, 1: Turned}")|O3EEnum|1||||
| |- Unknown4|RawCodec|5||||
| |- [DeviceChildLockActive](## "{0: Not Active, 1: Active}")|O3EEnum|1||||
| |- DeviceTemperatureSetpoint|O3EInt8|1||||
| |- Unknown5|RawCodec|12||||
|**2272**|**ZigBeeTwentyFiveDeviceProperty**|*O3EComplexType*|84||ro||
| |- Serialnumber|RawCodec|8||||
| |- SerialnumberPostfix|RawCodec|1||||
| |- Devicename|O3EUtf8|39||||
| |- Unknown1|RawCodec|1||||
| |- ViCareDevice|O3EEnum|1||||
| |- Firmware-Version|O3ESoftVers|8||||
| |- Unknown2|RawCodec|26||||
|**2273**|**ZigBeeTwentyFiveDeviceSetpoint**|*O3EComplexType*|13||**rw**||
| |- Prefix|RawCodec|2||||
| |- MaximumFlowTemperature|O3EInt16|2||||
| |- Unused|RawCodec|9||||
|**2274**|**ZigBeeTwentyFiveDeviceCurrentValues**|RawCodec|57||ro||
|**2274**|**ZigBeeTwentyFiveDeviceCurrentValues**|*O3EComplexType*|68||ro||
| |- Unknown1|RawCodec|2||||
| |- BatteryLevel|O3EInt8|1||||
| |- Unknown2|RawCodec|38||||
| |- Valve Type|O3EInt8|1||||
| |- ActualTemperature|O3EInt8|1||||
| |- OperatingStatus|O3EInt8|1||||
| |- Unknown3|RawCodec|4||||
| |- [DeviceDisplayTurned](## "{0: Standard, 1: Turned}")|O3EEnum|1||||
| |- Unknown4|RawCodec|5||||
| |- [DeviceChildLockActive](## "{0: Not Active, 1: Active}")|O3EEnum|1||||
| |- DeviceTemperatureSetpoint|O3EInt8|1||||
| |- Unknown5|RawCodec|12||||
|**2275**|**ZigBeeTwentySixDeviceProperty**|*O3EComplexType*|84||ro||
| |- Serialnumber|RawCodec|8||||
| |- SerialnumberPostfix|RawCodec|1||||
| |- Devicename|O3EUtf8|39||||
| |- Unknown1|RawCodec|1||||
| |- ViCareDevice|O3EEnum|1||||
| |- Firmware-Version|O3ESoftVers|8||||
| |- Unknown2|RawCodec|26||||
|**2276**|**ZigBeeTwentySixDeviceSetpoint**|*O3EComplexType*|13||**rw**||
| |- Prefix|RawCodec|2||||
| |- MaximumFlowTemperature|O3EInt16|2||||
| |- Unused|RawCodec|9||||
|**2277**|**ZigBeeTwentySixDeviceCurrentValues**|RawCodec|57||ro||
|**2277**|**ZigBeeTwentySixDeviceCurrentValues**|*O3EComplexType*|68||ro||
| |- Unknown1|RawCodec|2||||
| |- BatteryLevel|O3EInt8|1||||
| |- Unknown2|RawCodec|38||||
| |- Valve Type|O3EInt8|1||||
| |- ActualTemperature|O3EInt8|1||||
| |- OperatingStatus|O3EInt8|1||||
| |- Unknown3|RawCodec|4||||
| |- [DeviceDisplayTurned](## "{0: Standard, 1: Turned}")|O3EEnum|1||||
| |- Unknown4|RawCodec|5||||
| |- [DeviceChildLockActive](## "{0: Not Active, 1: Active}")|O3EEnum|1||||
| |- DeviceTemperatureSetpoint|O3EInt8|1||||
| |- Unknown5|RawCodec|12||||
|**2278**|**ZigBeeTwentySevenDeviceProperty**|*O3EComplexType*|84||ro||
| |- Serialnumber|RawCodec|8||||
| |- SerialnumberPostfix|RawCodec|1||||
| |- Devicename|O3EUtf8|39||||
| |- Unknown1|RawCodec|1||||
| |- ViCareDevice|O3EEnum|1||||
| |- Firmware-Version|O3ESoftVers|8||||
| |- Unknown2|RawCodec|26||||
|**2279**|**ZigBeeTwentySevenDeviceSetpoint**|*O3EComplexType*|13||**rw**||
| |- Prefix|RawCodec|2||||
| |- MaximumFlowTemperature|O3EInt16|2||||
| |- Unused|RawCodec|9||||
|**2280**|**ZigBeeTwentySevenDeviceCurrentValues**|RawCodec|57||ro||
|**2280**|**ZigBeeTwentySevenDeviceCurrentValues**|*O3EComplexType*|68||ro||
| |- Unknown1|RawCodec|2||||
| |- BatteryLevel|O3EInt8|1||||
| |- Unknown2|RawCodec|38||||
| |- Valve Type|O3EInt8|1||||
| |- ActualTemperature|O3EInt8|1||||
| |- OperatingStatus|O3EInt8|1||||
| |- Unknown3|RawCodec|4||||
| |- [DeviceDisplayTurned](## "{0: Standard, 1: Turned}")|O3EEnum|1||||
| |- Unknown4|RawCodec|5||||
| |- [DeviceChildLockActive](## "{0: Not Active, 1: Active}")|O3EEnum|1||||
| |- DeviceTemperatureSetpoint|O3EInt8|1||||
| |- Unknown5|RawCodec|12||||
|**2281**|**ZigBeeTwentyEightDeviceProperty**|*O3EComplexType*|84||ro||
| |- Serialnumber|RawCodec|8||||
| |- SerialnumberPostfix|RawCodec|1||||
| |- Devicename|O3EUtf8|39||||
| |- Unknown1|RawCodec|1||||
| |- ViCareDevice|O3EEnum|1||||
| |- Firmware-Version|O3ESoftVers|8||||
| |- Unknown2|RawCodec|26||||
|**2282**|**ZigBeeTwentyEightDeviceSetpoint**|*O3EComplexType*|13||**rw**||
| |- Prefix|RawCodec|2||||
| |- MaximumFlowTemperature|O3EInt16|2||||
| |- Unused|RawCodec|9||||
|**2283**|**ZigBeeTwentyEightDeviceCurrentValues**|RawCodec|57||ro||
|**2283**|**ZigBeeTwentyEightDeviceCurrentValues**|*O3EComplexType*|68||ro||
| |- Unknown1|RawCodec|2||||
| |- BatteryLevel|O3EInt8|1||||
| |- Unknown2|RawCodec|38||||
| |- Valve Type|O3EInt8|1||||
| |- ActualTemperature|O3EInt8|1||||
| |- OperatingStatus|O3EInt8|1||||
| |- Unknown3|RawCodec|4||||
| |- [DeviceDisplayTurned](## "{0: Standard, 1: Turned}")|O3EEnum|1||||
| |- Unknown4|RawCodec|5||||
| |- [DeviceChildLockActive](## "{0: Not Active, 1: Active}")|O3EEnum|1||||
| |- DeviceTemperatureSetpoint|O3EInt8|1||||
| |- Unknown5|RawCodec|12||||
|**2284**|**ZigBeeTwentyNineDeviceProperty**|*O3EComplexType*|84||ro||
| |- Serialnumber|RawCodec|8||||
| |- SerialnumberPostfix|RawCodec|1||||
| |- Devicename|O3EUtf8|39||||
| |- Unknown1|RawCodec|1||||
| |- ViCareDevice|O3EEnum|1||||
| |- Firmware-Version|O3ESoftVers|8||||
| |- Unknown2|RawCodec|26||||
|**2285**|**ZigBeeTwentyNineDeviceSetpoint**|*O3EComplexType*|13||**rw**||
| |- Prefix|RawCodec|2||||
| |- MaximumFlowTemperature|O3EInt16|2||||
| |- Unused|RawCodec|9||||
|**2286**|**ZigBeeTwentyNineDeviceCurrentValues**|RawCodec|57||ro||
|**2286**|**ZigBeeTwentyNineDeviceCurrentValues**|*O3EComplexType*|68||ro||
| |- Unknown1|RawCodec|2||||
| |- BatteryLevel|O3EInt8|1||||
| |- Unknown2|RawCodec|38||||
| |- Valve Type|O3EInt8|1||||
| |- ActualTemperature|O3EInt8|1||||
| |- OperatingStatus|O3EInt8|1||||
| |- Unknown3|RawCodec|4||||
| |- [DeviceDisplayTurned](## "{0: Standard, 1: Turned}")|O3EEnum|1||||
| |- Unknown4|RawCodec|5||||
| |- [DeviceChildLockActive](## "{0: Not Active, 1: Active}")|O3EEnum|1||||
| |- DeviceTemperatureSetpoint|O3EInt8|1||||
| |- Unknown5|RawCodec|12||||
|**2287**|**ZigBeeThirtyDeviceProperty**|*O3EComplexType*|84||ro||
| |- Serialnumber|RawCodec|8||||
| |- SerialnumberPostfix|RawCodec|1||||
| |- Devicename|O3EUtf8|39||||
| |- Unknown1|RawCodec|1||||
| |- ViCareDevice|O3EEnum|1||||
| |- Firmware-Version|O3ESoftVers|8||||
| |- Unknown2|RawCodec|26||||
|**2288**|**ZigBeeThirtyDeviceSetpoint**|*O3EComplexType*|13||**rw**||
| |- Prefix|RawCodec|2||||
| |- MaximumFlowTemperature|O3EInt16|2||||
| |- Unused|RawCodec|9||||
|**2289**|**ZigBeeThirtyDeviceCurrentValues**|RawCodec|57||ro||
|**2289**|**ZigBeeThirtyDeviceCurrentValues**|*O3EComplexType*|68||ro||
| |- Unknown1|RawCodec|2||||
| |- BatteryLevel|O3EInt8|1||||
| |- Unknown2|RawCodec|38||||
| |- Valve Type|O3EInt8|1||||
| |- ActualTemperature|O3EInt8|1||||
| |- OperatingStatus|O3EInt8|1||||
| |- Unknown3|RawCodec|4||||
| |- [DeviceDisplayTurned](## "{0: Standard, 1: Turned}")|O3EEnum|1||||
| |- Unknown4|RawCodec|5||||
| |- [DeviceChildLockActive](## "{0: Not Active, 1: Active}")|O3EEnum|1||||
| |- DeviceTemperatureSetpoint|O3EInt8|1||||
| |- Unknown5|RawCodec|12||||
|**2290**|**ZigBeeThirtyOneDeviceProperty**|*O3EComplexType*|84||ro||
| |- Serialnumber|RawCodec|8||||
| |- SerialnumberPostfix|RawCodec|1||||
| |- Devicename|O3EUtf8|39||||
| |- Unknown1|RawCodec|1||||
| |- ViCareDevice|O3EEnum|1||||
| |- Firmware-Version|O3ESoftVers|8||||
| |- Unknown2|RawCodec|26||||
|**2291**|**ZigBeeThirtyOneDeviceSetpoint**|*O3EComplexType*|13||**rw**||
| |- Prefix|RawCodec|2||||
| |- MaximumFlowTemperature|O3EInt16|2||||
| |- Unused|RawCodec|9||||
|**2292**|**ZigBeeThirtyOneDeviceCurrentValues**|RawCodec|57||ro||
|**2292**|**ZigBeeThirtyOneDeviceCurrentValues**|*O3EComplexType*|68||ro||
| |- Unknown1|RawCodec|2||||
| |- BatteryLevel|O3EInt8|1||||
| |- Unknown2|RawCodec|38||||
| |- Valve Type|O3EInt8|1||||
| |- ActualTemperature|O3EInt8|1||||
| |- OperatingStatus|O3EInt8|1||||
| |- Unknown3|RawCodec|4||||
| |- [DeviceDisplayTurned](## "{0: Standard, 1: Turned}")|O3EEnum|1||||
| |- Unknown4|RawCodec|5||||
| |- [DeviceChildLockActive](## "{0: Not Active, 1: Active}")|O3EEnum|1||||
| |- DeviceTemperatureSetpoint|O3EInt8|1||||
| |- Unknown5|RawCodec|12||||
|**2293**|**ZigBeeThirtyTwoDeviceProperty**|*O3EComplexType*|84||ro||
| |- Serialnumber|RawCodec|8||||
| |- SerialnumberPostfix|RawCodec|1||||
| |- Devicename|O3EUtf8|39||||
| |- Unknown1|RawCodec|1||||
| |- ViCareDevice|O3EEnum|1||||
| |- Firmware-Version|O3ESoftVers|8||||
| |- Unknown2|RawCodec|26||||
|**2294**|**ZigBeeThirtyTwoDeviceSetpoint**|*O3EComplexType*|13||**rw**||
| |- Prefix|RawCodec|2||||
| |- MaximumFlowTemperature|O3EInt16|2||||
| |- Unused|RawCodec|9||||
|**2295**|**ZigBeeThirtyTwoDeviceCurrentValues**|RawCodec|57||ro||
|**2295**|**ZigBeeThirtyTwoDeviceCurrentValues**|*O3EComplexType*|68||ro||
| |- Unknown1|RawCodec|2||||
| |- BatteryLevel|O3EInt8|1||||
| |- Unknown2|RawCodec|38||||
| |- Valve Type|O3EInt8|1||||
| |- ActualTemperature|O3EInt8|1||||
| |- OperatingStatus|O3EInt8|1||||
| |- Unknown3|RawCodec|4||||
| |- [DeviceDisplayTurned](## "{0: Standard, 1: Turned}")|O3EEnum|1||||
| |- Unknown4|RawCodec|5||||
| |- [DeviceChildLockActive](## "{0: Not Active, 1: Active}")|O3EEnum|1||||
| |- DeviceTemperatureSetpoint|O3EInt8|1||||
| |- Unknown5|RawCodec|12||||
|**2296**|**ZigBeeThirtyThreeDeviceProperty**|*O3EComplexType*|84||ro||
| |- Serialnumber|RawCodec|8||||
| |- SerialnumberPostfix|RawCodec|1||||
| |- Devicename|O3EUtf8|39||||
| |- Unknown1|RawCodec|1||||
| |- ViCareDevice|O3EEnum|1||||
| |- Firmware-Version|O3ESoftVers|8||||
| |- Unknown2|RawCodec|26||||
|**2297**|**ZigBeeThirtyThreeDeviceSetpoint**|*O3EComplexType*|13||**rw**||
| |- Prefix|RawCodec|2||||
| |- MaximumFlowTemperature|O3EInt16|2||||
| |- Unused|RawCodec|9||||
|**2298**|**ZigBeeThirtyThreeDeviceCurrentValues**|RawCodec|57||ro||
|**2298**|**ZigBeeThirtyThreeDeviceCurrentValues**|*O3EComplexType*|68||ro||
| |- Unknown1|RawCodec|2||||
| |- BatteryLevel|O3EInt8|1||||
| |- Unknown2|RawCodec|38||||
| |- Valve Type|O3EInt8|1||||
| |- ActualTemperature|O3EInt8|1||||
| |- OperatingStatus|O3EInt8|1||||
| |- Unknown3|RawCodec|4||||
| |- [DeviceDisplayTurned](## "{0: Standard, 1: Turned}")|O3EEnum|1||||
| |- Unknown4|RawCodec|5||||
| |- [DeviceChildLockActive](## "{0: Not Active, 1: Active}")|O3EEnum|1||||
| |- DeviceTemperatureSetpoint|O3EInt8|1||||
| |- Unknown5|RawCodec|12||||
|**2299**|**ZigBeeThirtyFourDeviceProperty**|*O3EComplexType*|84||ro||
| |- Serialnumber|RawCodec|8||||
| |- SerialnumberPostfix|RawCodec|1||||
| |- Devicename|O3EUtf8|39||||
| |- Unknown1|RawCodec|1||||
| |- ViCareDevice|O3EEnum|1||||
| |- Firmware-Version|O3ESoftVers|8||||
| |- Unknown2|RawCodec|26||||
|**2300**|**ZigBeeThirtyFourDeviceSetpoint**|*O3EComplexType*|13||**rw**||
| |- Prefix|RawCodec|2||||
| |- MaximumFlowTemperature|O3EInt16|2||||
| |- Unused|RawCodec|9||||
|**2301**|**ZigBeeThirtyFourDeviceCurrentValues**|RawCodec|57||ro||
|**2301**|**ZigBeeThirtyFourDeviceCurrentValues**|*O3EComplexType*|68||ro||
| |- Unknown1|RawCodec|2||||
| |- BatteryLevel|O3EInt8|1||||
| |- Unknown2|RawCodec|38||||
| |- Valve Type|O3EInt8|1||||
| |- ActualTemperature|O3EInt8|1||||
| |- OperatingStatus|O3EInt8|1||||
| |- Unknown3|RawCodec|4||||
| |- [DeviceDisplayTurned](## "{0: Standard, 1: Turned}")|O3EEnum|1||||
| |- Unknown4|RawCodec|5||||
| |- [DeviceChildLockActive](## "{0: Not Active, 1: Active}")|O3EEnum|1||||
| |- DeviceTemperatureSetpoint|O3EInt8|1||||
| |- Unknown5|RawCodec|12||||
|**2302**|**ZigBeeThirtyFiveDeviceProperty**|*O3EComplexType*|84||ro||
| |- Serialnumber|RawCodec|8||||
| |- SerialnumberPostfix|RawCodec|1||||
| |- Devicename|O3EUtf8|39||||
| |- Unknown1|RawCodec|1||||
| |- ViCareDevice|O3EEnum|1||||
| |- Firmware-Version|O3ESoftVers|8||||
| |- Unknown2|RawCodec|26||||
|**2303**|**ZigBeeThirtyFiveDeviceSetpoint**|*O3EComplexType*|13||**rw**||
| |- Prefix|RawCodec|2||||
| |- MaximumFlowTemperature|O3EInt16|2||||
| |- Unused|RawCodec|9||||
|**2304**|**ZigBeeThirtyFiveDeviceCurrentValues**|RawCodec|57||ro||
|**2304**|**ZigBeeThirtyFiveDeviceCurrentValues**|*O3EComplexType*|68||ro||
| |- Unknown1|RawCodec|2||||
| |- BatteryLevel|O3EInt8|1||||
| |- Unknown2|RawCodec|38||||
| |- Valve Type|O3EInt8|1||||
| |- ActualTemperature|O3EInt8|1||||
| |- OperatingStatus|O3EInt8|1||||
| |- Unknown3|RawCodec|4||||
| |- [DeviceDisplayTurned](## "{0: Standard, 1: Turned}")|O3EEnum|1||||
| |- Unknown4|RawCodec|5||||
| |- [DeviceChildLockActive](## "{0: Not Active, 1: Active}")|O3EEnum|1||||
| |- DeviceTemperatureSetpoint|O3EInt8|1||||
| |- Unknown5|RawCodec|12||||
|**2305**|**ZigBeeThirtySixDeviceProperty**|*O3EComplexType*|84||ro||
| |- Serialnumber|RawCodec|8||||
| |- SerialnumberPostfix|RawCodec|1||||
| |- Devicename|O3EUtf8|39||||
| |- Unknown1|RawCodec|1||||
| |- ViCareDevice|O3EEnum|1||||
| |- Firmware-Version|O3ESoftVers|8||||
| |- Unknown2|RawCodec|26||||
|**2306**|**ZigBeeThirtySixDeviceSetpoint**|*O3EComplexType*|13||**rw**||
| |- Prefix|RawCodec|2||||
| |- MaximumFlowTemperature|O3EInt16|2||||
| |- Unused|RawCodec|9||||
|**2307**|**ZigBeeThirtySixDeviceCurrentValues**|RawCodec|57||ro||
|**2307**|**ZigBeeThirtySixDeviceCurrentValues**|*O3EComplexType*|68||ro||
| |- Unknown1|RawCodec|2||||
| |- BatteryLevel|O3EInt8|1||||
| |- Unknown2|RawCodec|38||||
| |- Valve Type|O3EInt8|1||||
| |- ActualTemperature|O3EInt8|1||||
| |- OperatingStatus|O3EInt8|1||||
| |- Unknown3|RawCodec|4||||
| |- [DeviceDisplayTurned](## "{0: Standard, 1: Turned}")|O3EEnum|1||||
| |- Unknown4|RawCodec|5||||
| |- [DeviceChildLockActive](## "{0: Not Active, 1: Active}")|O3EEnum|1||||
| |- DeviceTemperatureSetpoint|O3EInt8|1||||
| |- Unknown5|RawCodec|12||||
|**2308**|**ZigBeeThirtySevenDeviceProperty**|*O3EComplexType*|84||ro||
| |- Serialnumber|RawCodec|8||||
| |- SerialnumberPostfix|RawCodec|1||||
| |- Devicename|O3EUtf8|39||||
| |- Unknown1|RawCodec|1||||
| |- ViCareDevice|O3EEnum|1||||
| |- Firmware-Version|O3ESoftVers|8||||
| |- Unknown2|RawCodec|26||||
|**2309**|**ZigBeeThirtySevenDeviceSetpoint**|*O3EComplexType*|13||**rw**||
| |- Prefix|RawCodec|2||||
| |- MaximumFlowTemperature|O3EInt16|2||||
| |- Unused|RawCodec|9||||
|**2310**|**ZigBeeThirtySevenDeviceCurrentValues**|RawCodec|57||ro||
|**2310**|**ZigBeeThirtySevenDeviceCurrentValues**|*O3EComplexType*|68||ro||
| |- Unknown1|RawCodec|2||||
| |- BatteryLevel|O3EInt8|1||||
| |- Unknown2|RawCodec|38||||
| |- Valve Type|O3EInt8|1||||
| |- ActualTemperature|O3EInt8|1||||
| |- OperatingStatus|O3EInt8|1||||
| |- Unknown3|RawCodec|4||||
| |- [DeviceDisplayTurned](## "{0: Standard, 1: Turned}")|O3EEnum|1||||
| |- Unknown4|RawCodec|5||||
| |- [DeviceChildLockActive](## "{0: Not Active, 1: Active}")|O3EEnum|1||||
| |- DeviceTemperatureSetpoint|O3EInt8|1||||
| |- Unknown5|RawCodec|12||||
|**2311**|**ZigBeeThirtyEightDeviceProperty**|*O3EComplexType*|84||ro||
| |- Serialnumber|RawCodec|8||||
| |- SerialnumberPostfix|RawCodec|1||||
| |- Devicename|O3EUtf8|39||||
| |- Unknown1|RawCodec|1||||
| |- ViCareDevice|O3EEnum|1||||
| |- Firmware-Version|O3ESoftVers|8||||
| |- Unknown2|RawCodec|26||||
|**2312**|**ZigBeeThirtyEightDeviceSetpoint**|*O3EComplexType*|13||**rw**||
| |- Prefix|RawCodec|2||||
| |- MaximumFlowTemperature|O3EInt16|2||||
| |- Unused|RawCodec|9||||
|**2313**|**ZigBeeThirtyEightDeviceCurrentValues**|RawCodec|57||ro||
|**2313**|**ZigBeeThirtyEightDeviceCurrentValues**|*O3EComplexType*|68||ro||
| |- Unknown1|RawCodec|2||||
| |- BatteryLevel|O3EInt8|1||||
| |- Unknown2|RawCodec|38||||
| |- Valve Type|O3EInt8|1||||
| |- ActualTemperature|O3EInt8|1||||
| |- OperatingStatus|O3EInt8|1||||
| |- Unknown3|RawCodec|4||||
| |- [DeviceDisplayTurned](## "{0: Standard, 1: Turned}")|O3EEnum|1||||
| |- Unknown4|RawCodec|5||||
| |- [DeviceChildLockActive](## "{0: Not Active, 1: Active}")|O3EEnum|1||||
| |- DeviceTemperatureSetpoint|O3EInt8|1||||
| |- Unknown5|RawCodec|12||||
|**2314**|**ZigBeeThirtyNineDeviceProperty**|*O3EComplexType*|84||ro||
| |- Serialnumber|RawCodec|8||||
| |- SerialnumberPostfix|RawCodec|1||||
| |- Devicename|O3EUtf8|39||||
| |- Unknown1|RawCodec|1||||
| |- ViCareDevice|O3EEnum|1||||
| |- Firmware-Version|O3ESoftVers|8||||
| |- Unknown2|RawCodec|26||||
|**2315**|**ZigBeeThirtyNineDeviceSetpoint**|*O3EComplexType*|13||**rw**||
| |- Prefix|RawCodec|2||||
| |- MaximumFlowTemperature|O3EInt16|2||||
| |- Unused|RawCodec|9||||
|**2316**|**ZigBeeThirtyNineDeviceCurrentValues**|RawCodec|57||ro||
|**2316**|**ZigBeeThirtyNineDeviceCurrentValues**|*O3EComplexType*|68||ro||
| |- Unknown1|RawCodec|2||||
| |- BatteryLevel|O3EInt8|1||||
| |- Unknown2|RawCodec|38||||
| |- Valve Type|O3EInt8|1||||
| |- ActualTemperature|O3EInt8|1||||
| |- OperatingStatus|O3EInt8|1||||
| |- Unknown3|RawCodec|4||||
| |- [DeviceDisplayTurned](## "{0: Standard, 1: Turned}")|O3EEnum|1||||
| |- Unknown4|RawCodec|5||||
| |- [DeviceChildLockActive](## "{0: Not Active, 1: Active}")|O3EEnum|1||||
| |- DeviceTemperatureSetpoint|O3EInt8|1||||
| |- Unknown5|RawCodec|12||||
|**2317**|**ZigBeeFourtyDeviceProperty**|*O3EComplexType*|84||ro||
| |- Serialnumber|RawCodec|8||||
| |- SerialnumberPostfix|RawCodec|1||||
| |- Devicename|O3EUtf8|39||||
| |- Unknown1|RawCodec|1||||
| |- ViCareDevice|O3EEnum|1||||
| |- Firmware-Version|O3ESoftVers|8||||
| |- Unknown2|RawCodec|26||||
|**2318**|**ZigBeeFourtyDeviceSetpoint**|*O3EComplexType*|13||**rw**||
| |- Prefix|RawCodec|2||||
| |- MaximumFlowTemperature|O3EInt16|2||||
| |- Unused|RawCodec|9||||
|**2319**|**ZigBeeFourtyDeviceCurrentValues**|RawCodec|57||ro||
|**2319**|**ZigBeeFourtyDeviceCurrentValues**|*O3EComplexType*|68||ro||
| |- Unknown1|RawCodec|2||||
| |- BatteryLevel|O3EInt8|1||||
| |- Unknown2|RawCodec|38||||
| |- Valve Type|O3EInt8|1||||
| |- ActualTemperature|O3EInt8|1||||
| |- OperatingStatus|O3EInt8|1||||
| |- Unknown3|RawCodec|4||||
| |- [DeviceDisplayTurned](## "{0: Standard, 1: Turned}")|O3EEnum|1||||
| |- Unknown4|RawCodec|5||||
| |- [DeviceChildLockActive](## "{0: Not Active, 1: Active}")|O3EEnum|1||||
| |- DeviceTemperatureSetpoint|O3EInt8|1||||
| |- Unknown5|RawCodec|12||||
|**2320**|[**DomesticHotWaterStatus**](## "Status of domestic hot water preparation {0: Idle, 1: Active, 2: Postrun}")|O3EEnum|1||ro||
|**2321**|**ZigBeeApartmentOneDecoupleList**|RawCodec|91||ro||
|**2327**|**VentilationTargetVolumeFlow**|*O3EComplexType*|4||**rw**||
| |- ActualFlow|O3EInt16|2||||
| |- Unknown|O3EInt16|2||||
|**2328**|**VentilationCurrentVolumeFlow**|*O3EComplexType*|4||ro||
| |- TargetFlow|O3EInt16|2||||
| |- Unknown|O3EInt16|2||||
|**2329**|**BatteryEnergyUsedAverage**|RawCodec|14||ro||
|**2330**|[**GenericDigitalInputConfigurationOnBoardTwo**](## "{0: Nothing, 1: FaultSignal, 2: DhwCirculation, 3: FaultSignalAndLocked, 4: ExternalHeatDemand, 5: ExternalLocked, 6: ExternalThermostat, 7: RoomTemperatureLimiter, 8: CallForHeat, 9: SmartGridReadyInputOne, 10: SmartGridReadyInputTwo, 11: PowerSupplierLock, 12: ExternalCoolingDemand, 13: PrioritizedDemandDeactivationOtherCircuits, 14: LockCircuitOne, 15: LockCircuitTwo, 16: ExternalDemandAutomatic, 17: FanControl, 18: FanRpmControl, 19: DefrostHeaterControlOne, 20: DefrostHeaterControlTwo, 21: DayNigthOperation, 22: DayNigthOperationPlusDirectControlDigitalOutputOne, 23: PermanentHeating, 24: DirectControlDryContactOne, 25: DirectControlDryContactTwo, 26: DirectControlDryContactThree, 27: DirectControlDigitalOutputTwentyFourVolt}")|O3EEnum|1||ro||
|**2331**|[**GenericDigitalInputConfigurationOnBoardThree**](## "{0: Nothing, 1: FaultSignal, 2: DhwCirculation, 3: FaultSignalAndLocked, 4: ExternalHeatDemand, 5: ExternalLocked, 6: ExternalThermostat, 7: RoomTemperatureLimiter, 8: CallForHeat, 9: SmartGridReadyInputOne, 10: SmartGridReadyInputTwo, 11: PowerSupplierLock, 12: ExternalCoolingDemand, 13: PrioritizedDemandDeactivationOtherCircuits, 14: LockCircuitOne, 15: LockCircuitTwo, 16: ExternalDemandAutomatic, 17: FanControl, 18: FanRpmControl, 19: DefrostHeaterControlOne, 20: DefrostHeaterControlTwo, 21: DayNigthOperation, 22: DayNigthOperationPlusDirectControlDigitalOutputOne, 23: PermanentHeating, 24: DirectControlDryContactOne, 25: DirectControlDryContactTwo, 26: DirectControlDryContactThree, 27: DirectControlDigitalOutputTwentyFourVolt}")|O3EEnum|1||ro||
|**2332**|[**GenericDigitalInputConfigurationOnBoardFour**](## "{0: Nothing, 1: FaultSignal, 2: DhwCirculation, 3: FaultSignalAndLocked, 4: ExternalHeatDemand, 5: ExternalLocked, 6: ExternalThermostat, 7: RoomTemperatureLimiter, 8: CallForHeat, 9: SmartGridReadyInputOne, 10: SmartGridReadyInputTwo, 11: PowerSupplierLock, 12: ExternalCoolingDemand, 13: PrioritizedDemandDeactivationOtherCircuits, 14: LockCircuitOne, 15: LockCircuitTwo, 16: ExternalDemandAutomatic, 17: FanControl, 18: FanRpmControl, 19: DefrostHeaterControlOne, 20: DefrostHeaterControlTwo, 21: DayNigthOperation, 22: DayNigthOperationPlusDirectControlDigitalOutputOne, 23: PermanentHeating, 24: DirectControlDryContactOne, 25: DirectControlDryContactTwo, 26: DirectControlDryContactThree, 27: DirectControlDigitalOutputTwentyFourVolt}")|O3EEnum|1||ro||
|**2333**|[**EconomizerLiquidTemperatureSensor**](## "Actual temperature economizer inlet")|*O3EComplexType*|9||ro|[Link](https://github.com/open3e/open3e/wiki/036-DoI-%E2%80%90-Data-points-of-Interest/#data-points-of-vitocal-250)|
| |- Actual|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- Minimum|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- Maximum|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- Average|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- [SensorStatus](## "{0: no_error, 1: interruption, 2: short_circuit, 3: electrical_fault, 4: not_available, 5: invalidates}")|O3EEnum|1||||
|**2334**|[**EvaporatorVaporTemperatureSensor**](## "Actual temperature avaporator inlet")|*O3EComplexType*|9||ro|[Link](https://github.com/open3e/open3e/wiki/036-DoI-%E2%80%90-Data-points-of-Interest/#data-points-of-vitocal-250)|
| |- Actual|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- Minimum|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- Maximum|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- Average|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- [SensorStatus](## "{0: no_error, 1: interruption, 2: short_circuit, 3: electrical_fault, 4: not_available, 5: invalidates}")|O3EEnum|1||||
|**2335**|**BatteryModuleCoulombCounters**|RawCodec|8||ro||
|**2336**|**ControllerBoardTemperatureSensor**|*O3EComplexType*|9||ro||
| |- Sensor1|O3EInt16|2||||
| |- Sensor2|O3EInt16|2||||
| |- Unknown|RawCodec|5||||
|**2337**|**UltraLowNitroOxideStatusActive**|RawCodec|1||ro||
|**2338**|**HighLimitTestMode**|RawCodec|3||ro||
|**2339**|**SafetyLimiterThresholdTemperature**|RawCodec|2||ro||
|**2340**|**ElectricalHeaterConfiguration**|RawCodec|2||ro||
|**2341**|**CoefficientOfPerformanceConfiguration**|RawCodec|4||ro||
|**2342**|**NominalThermalCapacityHeating**|O3EInt32|4||ro||
|**2343**|**NominalThermalCapacityCooling**|O3EInt32|4||ro||
|**2344**|**CombustionAirInterlockSettings**|RawCodec|1||ro||
|**2345**|[**CompressorSetpointPercent**](## "Setpoint of speed of heat pump compressor")|O3EInt8|1|%|**rw**||
|**2346**|[**CompressorSpeedPercent**](## "Actual speed of heat pump compressor")|O3EInt8|1|%|ro|[Link](https://github.com/open3e/open3e/wiki/036-DoI-%E2%80%90-Data-points-of-Interest/#data-points-of-vitocal-250)|
|**2348**|**PhotovoltaicsActivePowerLimitationEnergyManagementSystem**|RawCodec|8||ro||
|**2349**|**PhotovoltaicsActivePowerLimitationFallbackEnergyManagementSystem**|RawCodec|8||ro||
|**2350**|**EnergyManagmentSystemResultingControlState**|O3EByteVal|1||ro||
|**2351**|[**HeatPumpCompressor**](## "Actual state of the heat pump compressor")|*O3EComplexType*|2||ro||
| |- [PowerState](## "{0: Off, 1: On, 2: Out of range}")|O3EEnum|1||||
| |- ErrorState|O3EByteVal|1||||
|**2352**|[**AdditionalElectricHeater**](## "Actual state of the electric auxiliary heating")|*O3EComplexType*|2||ro||
| |- [PowerState](## "{0: Off, 1: On, 2: Out of range}")|O3EEnum|1||||
| |- ErrorState|O3EByteVal|1||||
|**2353**|**TargetDemandHeatProducer**|*O3EComplexType*|4||**rw**||
| |- StateHeating|O3EByteVal|1||||
| |- FlowTemperature|O3EInt16|2||||
| |- Modulation|O3EByteVal|1||||
|**2355**|**MinimumVentilationSupplyAirTemperature**|*O3EComplexType*|4||ro||
| |- Sensor1|O3EInt16|2||||
| |- Sensor2|O3EInt16|2||||
|**2356**|**CurrentSystemHeatingCoolingLevel**|O3EInt8|1||ro||
|**2369**|[**HeatPumpCompressorStatistical**](## "Statistics for heat pump compressor starts")|*O3EComplexType*|14||ro||
| |- Unknown1|RawCodec|6||||
| |- [starts](## "Number of starts")|O3EInt16|2||||
| |- Unknown2|RawCodec|2||||
| |- [hours](## "Operating hours")|O3EInt16|2|h|||
| |- Unknown3|RawCodec|2||||
|**2370**|**AdditionalElectricHeaterStatistical**|*O3EComplexType*|11||ro||
| |- Unknown1|RawCodec|3||||
| |- [starts](## "Number of starts")|O3EInt16|2||||
| |- Unknown2|RawCodec|2||||
| |- [hours](## "Operating hours")|O3EInt16|2|h|||
| |- Unknown3|RawCodec|2||||
|**2371**|**VentilationControlMode**|*O3EComplexType*|2||ro||
| |- Mode|O3EByteVal|1||||
| |- Unknown|RawCodec|1||||
|**2372**|**VentilationControllerOperationState**|*O3EComplexType*|2||**rw**||
| |- Unknown1|RawCodec|1||||
| |- Unknown2|RawCodec|1||||
|**2373**|**VentilationAirVolumeFlowBalancingOffset**|RawCodec|2||**rw**||
|**2374**|**VentilationExternalLockFunctionSetting**|O3EByteVal|1||ro||
|**2375**|**NarrowBandInternetOfThingsConfiguration**|RawCodec|7||ro||
|**2376**|**NarrowBandInternetOfThingsRadio**|RawCodec|132||ro||
|**2377**|**EvolvedUniversalTerrestrialRadioAccessDataLinkInfo**|RawCodec|45||ro||
|**2378**|**EvolvedUniversalTerrestrialRadioAccessNeighborCells**|RawCodec|48||ro||
|**2379**|**EvolvedUniversalTerrestrialRadioAccessServingCellInfo**|RawCodec|22||ro||
|**2380**|**EvolvedUniversalTerrestrialRadioAccessServingCellMeasurements**|RawCodec|17||ro||
|**2382**|**PaddleSwitch**|RawCodec|2||ro||
|**2403**|**BypassOperationLevel**|O3EInt8|1||ro||
|**2404**|**BivalenceControlMode**|*O3EComplexType*|6||ro||
| |- OperationMode|O3EByteVal|1||||
| |- BivalenceControlTemperature|O3EInt16|2||||
| |- BivalenceControlAlternativeTemperature|O3EInt16|2||||
| |- ControlMode|O3EByteVal|1||||
|**2405**|**MixerOneCircuitConstantFlowSetTemperatureCooling**|*O3EComplexType*|6||ro||
| |- EffectiveSetTemperature|O3EInt16|2||||
| |- FactorySelectedUnderfloorHeating|O3EInt16|2||||
| |- FactorySelectedFanConvector|O3EInt16|2||||
|**2406**|**MixerTwoCircuitConstantFlowSetTemperatureCooling**|*O3EComplexType*|6||ro||
| |- EffectiveSetTemperature|O3EInt16|2||||
| |- FactorySelectedUnderfloorHeating|O3EInt16|2||||
| |- FactorySelectedFanConvector|O3EInt16|2||||
|**2407**|**MixerThreeCircuitConstantFlowSetTemperatureCooling**|*O3EComplexType*|6||ro||
| |- EffectiveSetTemperature|O3EInt16|2||||
| |- FactorySelectedUnderfloorHeating|O3EInt16|2||||
| |- FactorySelectedFanConvector|O3EInt16|2||||
|**2408**|**MixerFourCircuitConstantFlowSetTemperatureCooling**|*O3EComplexType*|6||ro||
| |- EffectiveSetTemperature|O3EInt16|2||||
| |- FactorySelectedUnderfloorHeating|O3EInt16|2||||
| |- FactorySelectedFanConvector|O3EInt16|2||||
|**2409**|**MixerOneCircuitMinimumMaximumFlowSetTemperatureCooling**|RawCodec|12||ro||
|**2410**|**MixerTwoCircuitMinimumMaximumFlowSetTemperatureCooling**|RawCodec|12||ro||
|**2411**|**MixerThreeCircuitMinimumMaximumFlowSetTemperatureCooling**|RawCodec|12||ro||
|**2412**|**MixerFourCircuitMinimumMaximumFlowSetTemperatureCooling**|RawCodec|12||ro||
|**2413**|**MixerOneCircuitThresholdCooling**|*O3EComplexType*|4||ro||
| |- HysteresisOn|O3EInt16|2||||
| |- HysteresisOff|O3EInt16|2||||
|**2414**|**MixerTwoCircuitThresholdCooling**|*O3EComplexType*|4||ro||
| |- HysteresisOn|O3EInt16|2||||
| |- HysteresisOff|O3EInt16|2||||
|**2415**|**MixerThreeCircuitThresholdCooling**|*O3EComplexType*|4||ro||
| |- HysteresisOn|O3EInt16|2||||
| |- HysteresisOff|O3EInt16|2||||
|**2416**|**MixerFourCircuitThresholdCooling**|*O3EComplexType*|4||ro||
| |- HysteresisOn|O3EInt16|2||||
| |- HysteresisOff|O3EInt16|2||||
|**2417**|**MixerOneCircuitTargetValueRelativeHumidityCooling**|RawCodec|6||**rw**||
|**2418**|**MixerTwoCircuitTargetValueRelativeHumidityCooling**|RawCodec|6||**rw**||
|**2419**|**MixerThreeCircuitTargetValueRelativeHumidityCooling**|RawCodec|6||**rw**||
|**2420**|**MixerFourCircuitTargetValueRelativeHumidityCooling**|RawCodec|6||**rw**||
|**2421**|**MixerOneCircuitTemperatureOffsetCooling**|RawCodec|2||**rw**||
|**2422**|**MixerTwoCircuitTemperatureOffsetCooling**|RawCodec|2||**rw**||
|**2423**|**MixerThreeCircuitTemperatureOffsetCooling**|RawCodec|2||**rw**||
|**2424**|**MixerFourCircuitTemperatureOffsetCooling**|RawCodec|2||**rw**||
|**2425**|**BatteryModuleTypeId**|RawCodec|2||ro||
|**2426**|**MixerOneCircuitRoomEcoFunctionSettings**|*O3EComplexType*|6||ro||
| |- State|O3EBool|1||||
| |- OutsideTemperatureLimit|O3EInt16|2||||
| |- Unknown|O3EByteVal|1||||
| |- RoomTemperatureLimit|O3EInt16|2||||
|**2427**|**MixerTwoCircuitRoomEcoFunctionSettings**|*O3EComplexType*|6||ro||
| |- State|O3EBool|1||||
| |- OutsideTemperatureLimit|O3EInt16|2||||
| |- Unknown|O3EByteVal|1||||
| |- RoomTemperatureLimit|O3EInt16|2||||
|**2428**|**MixerThreeCircuitRoomEcoFunctionSettings**|*O3EComplexType*|6||ro||
| |- State|O3EBool|1||||
| |- OutsideTemperatureLimit|O3EInt16|2||||
| |- Unknown|O3EByteVal|1||||
| |- RoomTemperatureLimit|O3EInt16|2||||
|**2429**|**MixerFourCircuitRoomEcoFunctionSettings**|*O3EComplexType*|6||ro||
| |- State|O3EBool|1||||
| |- OutsideTemperatureLimit|O3EInt16|2||||
| |- Unknown|O3EByteVal|1||||
| |- RoomTemperatureLimit|O3EInt16|2||||
|**2442**|**HeatPumpFrostProtection**|O3EInt8|1||ro||
|**2444**|**LogLevelEmbbededApplication**|O3EInt8|1||ro||
|**2445**|**SupplementalHeatEngineConfiguration**|RawCodec|2||ro||
|**2446**|**HmiWakeupTrigger**|RawCodec|4||ro||
|**2447**|**SupplyAirVolumeFlowDeviceLimit**|*O3EComplexType*|4||ro||
| |- Minimum|O3EInt16|2||||
| |- Maximum|O3EInt16|2||||
|**2448**|**ExhaustAirVolumeFlowDeviceLimit**|*O3EComplexType*|4||ro||
| |- Minimum|O3EInt16|2||||
| |- Maximum|O3EInt16|2||||
|**2449**|**CustomerSpecificDeviceName**|RawCodec|2||ro||
|**2450**|**CascadeSequenceCurrentBoiler**|RawCodec|16||ro||
|**2451**|**CascadeEmergencyOperationMode**|RawCodec|3||ro||
|**2452**|**MixerOneCircuitRoomTemperatureThresholdCooling**|*O3EComplexType*|4||ro||
| |- RoomHysteresisOn|O3EInt16|2||||
| |- RoomHysteresisOff|O3EInt16|2||||
|**2453**|**MixerTwoCircuitRoomTemperatureThresholdCooling**|*O3EComplexType*|4||ro||
| |- RoomHysteresisOn|O3EInt16|2||||
| |- RoomHysteresisOff|O3EInt16|2||||
|**2454**|**MixerThreeCircuitRoomTemperatureThresholdCooling**|*O3EComplexType*|4||ro||
| |- RoomHysteresisOn|O3EInt16|2||||
| |- RoomHysteresisOff|O3EInt16|2||||
|**2455**|**MixerFourCircuitRoomTemperatureThresholdCooling**|*O3EComplexType*|4||ro||
| |- RoomHysteresisOn|O3EInt16|2||||
| |- RoomHysteresisOff|O3EInt16|2||||
|**2457**|**CalculatedOutsideTemperature**|*O3EComplexType*|9||ro||
| |- DampedActual|O3EInt16|2||||
| |- DampedMin|O3EInt16|2||||
| |- DampedMax|O3EInt16|2||||
| |- DampedAverage|O3EInt16|2||||
| |- Unknown|RawCodec|1||||
|**2458**|**CascadeDeviceStatusLead**|RawCodec|18||ro||
|**2459**|**CascadeDeviceStatusLagOne**|RawCodec|18||ro||
|**2460**|**CascadeDeviceStatusLagTwo**|RawCodec|18||ro||
|**2461**|**CascadeDeviceStatusLagThree**|RawCodec|18||ro||
|**2462**|**CascadeDeviceStatusLagFour**|RawCodec|18||ro||
|**2463**|**CascadeDeviceStatusLagFive**|RawCodec|18||ro||
|**2464**|**CascadeDeviceStatusLagSix**|RawCodec|18||ro||
|**2465**|**CascadeDeviceStatusLagSeven**|RawCodec|18||ro||
|**2466**|**CascadeDeviceStatusLagEight**|RawCodec|18||ro||
|**2467**|**CascadeDeviceStatusLagNine**|RawCodec|18||ro||
|**2468**|**CascadeDeviceStatusLagTen**|RawCodec|18||ro||
|**2469**|**CascadeDeviceStatusLagEleven**|RawCodec|18||ro||
|**2470**|**CascadeDeviceStatusLagTwelve**|RawCodec|18||ro||
|**2471**|**CascadeDeviceStatusLagThirteen**|RawCodec|18||ro||
|**2472**|**CascadeDeviceStatusLagFourteen**|RawCodec|18||ro||
|**2473**|**CascadeDeviceStatusLagFifteen**|RawCodec|18||ro||
|**2474**|**CascadeCommonFlowTemperatureSensor**|RawCodec|9||ro||
|**2475**|**CascadeCommonFlowCurrentTemperatureSetpoint**|O3EInt16|2||**rw**||
|**2476**|**EnvironmentAirQualityTargetValues**|RawCodec|21||**rw**||
|**2477**|**EnvironmentAirQualitySensor**|O3EByteVal|1||ro||
|**2479**|**MixerOneCircuitRoomAirHumiditySensor**|RawCodec|5||ro||
|**2480**|**MixerTwoCircuitRoomAirHumiditySensor**|RawCodec|5||ro||
|**2481**|**MixerThreeCircuitRoomAirHumiditySensor**|RawCodec|5||ro||
|**2482**|**MixerFourCircuitRoomAirHumiditySensor**|RawCodec|5||ro||
|**2484**|**ElectricalPowerRangeMetaData**|RawCodec|8||ro||
|**2486**|[**CurrentElectricalPowerConsumptionRefrigerantCircuit**](## "Actual electrical power consumption of the refrigeration circuit")|O3EInt32|4|W|ro||
|**2487**|[**CurrentElectricalPowerConsumptionElectricHeater**](## "Actual electrical power consumption of the auxiliary heater")|O3EInt32|4|W|ro||
|**2488**|[**CurrentElectricalPowerConsumptionSystem**](## "Actual total electrical power consumption of the system")|O3EInt32|4|W|ro||
|**2489**|**FrostProtectionStatus**|RawCodec|3||ro||
|**2490**|**StartUpWizardState**|RawCodec|1||ro||
|**2491**|**DomesticHotWaterDemandInput**|RawCodec|1||ro||
|**2493**|**VentilationBypassPosition**|RawCodec|2||ro||
|**2494**|[**CurrentThermalCapacityRefrigerantCircuit**](## "Actual thermal power output of the refrigeration circuit")|O3EInt32|4|W|ro||
|**2495**|[**CurrentThermalCapacityElectricHeater**](## "Actual thermal power output of the auxiliary heater")|O3EInt32|4|W|ro||
|**2496**|[**CurrentThermalCapacitySystem**](## "Actual thermal power output of the system")|O3EInt32|4|W|ro||
|**2497**|**ResetStatisticalValuesDate**|RawCodec|3||ro||
|**2498**|**CentralHeatingPumpType**|O3EByteVal|1||ro||
|**2499**|**MixerOneCircuitPumpType**|O3EByteVal|1||ro||
|**2500**|**MixerTwoCircuitPumpType**|O3EByteVal|1||ro||
|**2501**|**MixerThreeCircuitPumpType**|O3EByteVal|1||ro||
|**2502**|**MixerFourCircuitPumpType**|O3EByteVal|1||ro||
|**2515**|**EnergyConsumptionDomesticHotWaterMonthMatrixElectricHeater**|*O3EComplexType*|124||ro||
| |- CurrentMonth|*O3EList*|62||||
| |- - 01|O3EInt16|2||||
| |- - 02|O3EInt16|2||||
| |- - 03|O3EInt16|2||||
| |- - 04|O3EInt16|2||||
| |- - 05|O3EInt16|2||||
| |- - 06|O3EInt16|2||||
| |- - 07|O3EInt16|2||||
| |- - 08|O3EInt16|2||||
| |- - 09|O3EInt16|2||||
| |- - 10|O3EInt16|2||||
| |- - 11|O3EInt16|2||||
| |- - 12|O3EInt16|2||||
| |- - 13|O3EInt16|2||||
| |- - 14|O3EInt16|2||||
| |- - 15|O3EInt16|2||||
| |- - 16|O3EInt16|2||||
| |- - 17|O3EInt16|2||||
| |- - 18|O3EInt16|2||||
| |- - 19|O3EInt16|2||||
| |- - 20|O3EInt16|2||||
| |- - 21|O3EInt16|2||||
| |- - 22|O3EInt16|2||||
| |- - 23|O3EInt16|2||||
| |- - 24|O3EInt16|2||||
| |- - 25|O3EInt16|2||||
| |- - 26|O3EInt16|2||||
| |- - 27|O3EInt16|2||||
| |- - 28|O3EInt16|2||||
| |- - 29|O3EInt16|2||||
| |- - 30|O3EInt16|2||||
| |- - 31|O3EInt16|2||||
| |- LastMonth|*O3EList*|62||||
| |- - 01|O3EInt16|2||||
| |- - 02|O3EInt16|2||||
| |- - 03|O3EInt16|2||||
| |- - 04|O3EInt16|2||||
| |- - 05|O3EInt16|2||||
| |- - 06|O3EInt16|2||||
| |- - 07|O3EInt16|2||||
| |- - 08|O3EInt16|2||||
| |- - 09|O3EInt16|2||||
| |- - 10|O3EInt16|2||||
| |- - 11|O3EInt16|2||||
| |- - 12|O3EInt16|2||||
| |- - 13|O3EInt16|2||||
| |- - 14|O3EInt16|2||||
| |- - 15|O3EInt16|2||||
| |- - 16|O3EInt16|2||||
| |- - 17|O3EInt16|2||||
| |- - 18|O3EInt16|2||||
| |- - 19|O3EInt16|2||||
| |- - 20|O3EInt16|2||||
| |- - 21|O3EInt16|2||||
| |- - 22|O3EInt16|2||||
| |- - 23|O3EInt16|2||||
| |- - 24|O3EInt16|2||||
| |- - 25|O3EInt16|2||||
| |- - 26|O3EInt16|2||||
| |- - 27|O3EInt16|2||||
| |- - 28|O3EInt16|2||||
| |- - 29|O3EInt16|2||||
| |- - 30|O3EInt16|2||||
| |- - 31|O3EInt16|2||||
|**2516**|**EnergyConsumptionDomesticHotWaterYearMatrixElectricHeater**|*O3EComplexType*|96||ro||
| |- CurrentYear|*O3EList*|48||||
| |- - 01_January|O3EInt32|4||||
| |- - 02_February|O3EInt32|4||||
| |- - 03_March|O3EInt32|4||||
| |- - 04_April|O3EInt32|4||||
| |- - 05_May|O3EInt32|4||||
| |- - 06_June|O3EInt32|4||||
| |- - 07_July|O3EInt32|4||||
| |- - 08_August|O3EInt32|4||||
| |- - 09_September|O3EInt32|4||||
| |- - 10_October|O3EInt32|4||||
| |- - 11_November|O3EInt32|4||||
| |- - 12_December|O3EInt32|4||||
| |- LastYear|*O3EList*|48||||
| |- - 01_January|O3EInt32|4||||
| |- - 02_February|O3EInt32|4||||
| |- - 03_March|O3EInt32|4||||
| |- - 04_April|O3EInt32|4||||
| |- - 05_May|O3EInt32|4||||
| |- - 06_June|O3EInt32|4||||
| |- - 07_July|O3EInt32|4||||
| |- - 08_August|O3EInt32|4||||
| |- - 09_September|O3EInt32|4||||
| |- - 10_October|O3EInt32|4||||
| |- - 11_November|O3EInt32|4||||
| |- - 12_December|O3EInt32|4||||
|**2517**|**EnergyConsumptionDomesticHotWaterElectricHeater**|*O3EComplexType*|24||ro||
| |- Today|O3EInt32|4||||
| |- Past7Days|O3EInt32|4||||
| |- CurrentMonth|O3EInt32|4||||
| |- PastMonth|O3EInt32|4||||
| |- CurrentYear|O3EInt32|4||||
| |- PastYear|O3EInt32|4||||
|**2524**|**EnergyConsumptionCentralHeatingMonthMatrixElectricHeater**|*O3EComplexType*|124||ro||
| |- CurrentMonth|*O3EList*|62||||
| |- - 01|O3EInt16|2||||
| |- - 02|O3EInt16|2||||
| |- - 03|O3EInt16|2||||
| |- - 04|O3EInt16|2||||
| |- - 05|O3EInt16|2||||
| |- - 06|O3EInt16|2||||
| |- - 07|O3EInt16|2||||
| |- - 08|O3EInt16|2||||
| |- - 09|O3EInt16|2||||
| |- - 10|O3EInt16|2||||
| |- - 11|O3EInt16|2||||
| |- - 12|O3EInt16|2||||
| |- - 13|O3EInt16|2||||
| |- - 14|O3EInt16|2||||
| |- - 15|O3EInt16|2||||
| |- - 16|O3EInt16|2||||
| |- - 17|O3EInt16|2||||
| |- - 18|O3EInt16|2||||
| |- - 19|O3EInt16|2||||
| |- - 20|O3EInt16|2||||
| |- - 21|O3EInt16|2||||
| |- - 22|O3EInt16|2||||
| |- - 23|O3EInt16|2||||
| |- - 24|O3EInt16|2||||
| |- - 25|O3EInt16|2||||
| |- - 26|O3EInt16|2||||
| |- - 27|O3EInt16|2||||
| |- - 28|O3EInt16|2||||
| |- - 29|O3EInt16|2||||
| |- - 30|O3EInt16|2||||
| |- - 31|O3EInt16|2||||
| |- LastMonth|*O3EList*|62||||
| |- - 01|O3EInt16|2||||
| |- - 02|O3EInt16|2||||
| |- - 03|O3EInt16|2||||
| |- - 04|O3EInt16|2||||
| |- - 05|O3EInt16|2||||
| |- - 06|O3EInt16|2||||
| |- - 07|O3EInt16|2||||
| |- - 08|O3EInt16|2||||
| |- - 09|O3EInt16|2||||
| |- - 10|O3EInt16|2||||
| |- - 11|O3EInt16|2||||
| |- - 12|O3EInt16|2||||
| |- - 13|O3EInt16|2||||
| |- - 14|O3EInt16|2||||
| |- - 15|O3EInt16|2||||
| |- - 16|O3EInt16|2||||
| |- - 17|O3EInt16|2||||
| |- - 18|O3EInt16|2||||
| |- - 19|O3EInt16|2||||
| |- - 20|O3EInt16|2||||
| |- - 21|O3EInt16|2||||
| |- - 22|O3EInt16|2||||
| |- - 23|O3EInt16|2||||
| |- - 24|O3EInt16|2||||
| |- - 25|O3EInt16|2||||
| |- - 26|O3EInt16|2||||
| |- - 27|O3EInt16|2||||
| |- - 28|O3EInt16|2||||
| |- - 29|O3EInt16|2||||
| |- - 30|O3EInt16|2||||
| |- - 31|O3EInt16|2||||
|**2525**|**EnergyConsumptionCentralHeatingYearMatrixElectricHeater**|*O3EComplexType*|96||ro||
| |- CurrentYear|*O3EList*|48||||
| |- - 01_January|O3EInt32|4||||
| |- - 02_February|O3EInt32|4||||
| |- - 03_March|O3EInt32|4||||
| |- - 04_April|O3EInt32|4||||
| |- - 05_May|O3EInt32|4||||
| |- - 06_June|O3EInt32|4||||
| |- - 07_July|O3EInt32|4||||
| |- - 08_August|O3EInt32|4||||
| |- - 09_September|O3EInt32|4||||
| |- - 10_October|O3EInt32|4||||
| |- - 11_November|O3EInt32|4||||
| |- - 12_December|O3EInt32|4||||
| |- LastYear|*O3EList*|48||||
| |- - 01_January|O3EInt32|4||||
| |- - 02_February|O3EInt32|4||||
| |- - 03_March|O3EInt32|4||||
| |- - 04_April|O3EInt32|4||||
| |- - 05_May|O3EInt32|4||||
| |- - 06_June|O3EInt32|4||||
| |- - 07_July|O3EInt32|4||||
| |- - 08_August|O3EInt32|4||||
| |- - 09_September|O3EInt32|4||||
| |- - 10_October|O3EInt32|4||||
| |- - 11_November|O3EInt32|4||||
| |- - 12_December|O3EInt32|4||||
|**2526**|**EnergyConsumptionCentralHeatingElectricHeater**|*O3EComplexType*|24||ro||
| |- Today|O3EInt32|4||||
| |- Past7Days|O3EInt32|4||||
| |- CurrentMonth|O3EInt32|4||||
| |- PastMonth|O3EInt32|4||||
| |- CurrentYear|O3EInt32|4||||
| |- PastYear|O3EInt32|4||||
|**2527**|**GeneratedCoolingOutputMonthMatrix**|*O3EComplexType*|124||ro||
| |- CurrentMonth|*O3EList*|62||||
| |- - 01|O3EInt16|2||||
| |- - 02|O3EInt16|2||||
| |- - 03|O3EInt16|2||||
| |- - 04|O3EInt16|2||||
| |- - 05|O3EInt16|2||||
| |- - 06|O3EInt16|2||||
| |- - 07|O3EInt16|2||||
| |- - 08|O3EInt16|2||||
| |- - 09|O3EInt16|2||||
| |- - 10|O3EInt16|2||||
| |- - 11|O3EInt16|2||||
| |- - 12|O3EInt16|2||||
| |- - 13|O3EInt16|2||||
| |- - 14|O3EInt16|2||||
| |- - 15|O3EInt16|2||||
| |- - 16|O3EInt16|2||||
| |- - 17|O3EInt16|2||||
| |- - 18|O3EInt16|2||||
| |- - 19|O3EInt16|2||||
| |- - 20|O3EInt16|2||||
| |- - 21|O3EInt16|2||||
| |- - 22|O3EInt16|2||||
| |- - 23|O3EInt16|2||||
| |- - 24|O3EInt16|2||||
| |- - 25|O3EInt16|2||||
| |- - 26|O3EInt16|2||||
| |- - 27|O3EInt16|2||||
| |- - 28|O3EInt16|2||||
| |- - 29|O3EInt16|2||||
| |- - 30|O3EInt16|2||||
| |- - 31|O3EInt16|2||||
| |- LastMonth|*O3EList*|62||||
| |- - 01|O3EInt16|2||||
| |- - 02|O3EInt16|2||||
| |- - 03|O3EInt16|2||||
| |- - 04|O3EInt16|2||||
| |- - 05|O3EInt16|2||||
| |- - 06|O3EInt16|2||||
| |- - 07|O3EInt16|2||||
| |- - 08|O3EInt16|2||||
| |- - 09|O3EInt16|2||||
| |- - 10|O3EInt16|2||||
| |- - 11|O3EInt16|2||||
| |- - 12|O3EInt16|2||||
| |- - 13|O3EInt16|2||||
| |- - 14|O3EInt16|2||||
| |- - 15|O3EInt16|2||||
| |- - 16|O3EInt16|2||||
| |- - 17|O3EInt16|2||||
| |- - 18|O3EInt16|2||||
| |- - 19|O3EInt16|2||||
| |- - 20|O3EInt16|2||||
| |- - 21|O3EInt16|2||||
| |- - 22|O3EInt16|2||||
| |- - 23|O3EInt16|2||||
| |- - 24|O3EInt16|2||||
| |- - 25|O3EInt16|2||||
| |- - 26|O3EInt16|2||||
| |- - 27|O3EInt16|2||||
| |- - 28|O3EInt16|2||||
| |- - 29|O3EInt16|2||||
| |- - 30|O3EInt16|2||||
| |- - 31|O3EInt16|2||||
|**2528**|**GeneratedCoolingOutputYearMatrix**|*O3EComplexType*|96||ro||
| |- CurrentYear|*O3EList*|48||||
| |- - 01_January|O3EInt32|4||||
| |- - 02_February|O3EInt32|4||||
| |- - 03_March|O3EInt32|4||||
| |- - 04_April|O3EInt32|4||||
| |- - 05_May|O3EInt32|4||||
| |- - 06_June|O3EInt32|4||||
| |- - 07_July|O3EInt32|4||||
| |- - 08_August|O3EInt32|4||||
| |- - 09_September|O3EInt32|4||||
| |- - 10_October|O3EInt32|4||||
| |- - 11_November|O3EInt32|4||||
| |- - 12_December|O3EInt32|4||||
| |- LastYear|*O3EList*|48||||
| |- - 01_January|O3EInt32|4||||
| |- - 02_February|O3EInt32|4||||
| |- - 03_March|O3EInt32|4||||
| |- - 04_April|O3EInt32|4||||
| |- - 05_May|O3EInt32|4||||
| |- - 06_June|O3EInt32|4||||
| |- - 07_July|O3EInt32|4||||
| |- - 08_August|O3EInt32|4||||
| |- - 09_September|O3EInt32|4||||
| |- - 10_October|O3EInt32|4||||
| |- - 11_November|O3EInt32|4||||
| |- - 12_December|O3EInt32|4||||
|**2529**|**GeneratedCoolingOutput**|*O3EComplexType*|24||ro||
| |- Today|O3EInt32|4||||
| |- Past7Days|O3EInt32|4||||
| |- CurrentMonth|O3EInt32|4||||
| |- PastMonth|O3EInt32|4||||
| |- CurrentYear|O3EInt32|4||||
| |- PastYear|O3EInt32|4||||
|**2533**|**PowerGridCodeSettingsNormSix**|RawCodec|27||ro||
|**2534**|**BusTopologyMatrixSix**|RawCodec|181||ro||
|**2535**|**BusTopologyMatrixSeven**|RawCodec|181||ro||
|**2536**|**BusTopologyMatrixEight**|RawCodec|181||ro||
|**2537**|**BusTopologyMatrixNine**|RawCodec|181||ro||
|**2538**|**BusTopologyMatrixTen**|RawCodec|181||ro||
|**2539**|**AlternatingCurrentEnergyStatistic**|RawCodec|40||ro||
|**2540**|**NoiseReductionSettings**|RawCodec|6||ro||
|**2541**|**SupplyAirVolumeFlowConfigurationLimit**|*O3EComplexType*|4||ro||
| |- Minimum|O3EInt16|2||||
| |- Maximum|O3EInt16|2||||
|**2542**|**ExhaustAirVolumeFlowConfigurationLimit**|*O3EComplexType*|4||ro||
| |- Minimum|O3EInt16|2||||
| |- Maximum|O3EInt16|2||||
|**2543**|**SmartGridTemperatureOffsets**|*O3EComplexType*|10||**rw**||
| |- SetpointIncreaseRoomTemperatureHeating|O3EInt16|2||||
| |- SetpointDecreaseRoomTemperatureCooling|O3EInt16|2||||
| |- SetpointIncreaseDHWTemperature|O3EInt16|2||||
| |- SetpointIncreaseBufferTemperatureHeating|O3EInt16|2||||
| |- SetpointDecreaseBufferTemperatureCooling|O3EInt16|2||||
|**2544**|**EnableElectricalHeaterSmartGridLock**|O3EByteVal|1||ro||
|**2545**|**EnableElectricalHeaterSmartGridIncreaseMaxDemand**|O3EByteVal|1||ro||
|**2546**|**MixerOneCircuitRoomTemperatureSetpointCooling**|*O3EComplexType*|9||**rw**||
| |- Comfort|O3EInt16|2||||
| |- Normal|O3EInt16|2||||
| |- Reduced|O3EInt16|2||||
| |- Unknown|O3EInt16|2||||
| |- [State](## "{0: ShutDown, 1: Reduced, 2: Normal, 3: Comfort, 5: Fixed Value, 6: Antifreeze protection, 7: Energy Save: reduced, 8: Energy Save: normal, 9: Energy Save: comfort, 10: Cooling: normal, 11: Cooling: comfort, 12: No request}")|O3EEnum|1||||
|**2547**|**MixerTwoCircuitRoomTemperatureSetpointCooling**|*O3EComplexType*|9||**rw**||
| |- Comfort|O3EInt16|2||||
| |- Normal|O3EInt16|2||||
| |- Reduced|O3EInt16|2||||
| |- Unknown|O3EInt16|2||||
| |- [State](## "{0: ShutDown, 1: Reduced, 2: Normal, 3: Comfort, 5: Fixed Value, 6: Antifreeze protection, 7: Energy Save: reduced, 8: Energy Save: normal, 9: Energy Save: comfort, 10: Cooling: normal, 11: Cooling: comfort, 12: No request}")|O3EEnum|1||||
|**2548**|**MixerThreeCircuitRoomTemperatureSetpointCooling**|*O3EComplexType*|9||**rw**||
| |- Comfort|O3EInt16|2||||
| |- Normal|O3EInt16|2||||
| |- Reduced|O3EInt16|2||||
| |- Unknown|O3EInt16|2||||
| |- [State](## "{0: ShutDown, 1: Reduced, 2: Normal, 3: Comfort, 5: Fixed Value, 6: Antifreeze protection, 7: Energy Save: reduced, 8: Energy Save: normal, 9: Energy Save: comfort, 10: Cooling: normal, 11: Cooling: comfort, 12: No request}")|O3EEnum|1||||
|**2549**|**MixerFourCircuitRoomTemperatureSetpointCooling**|*O3EComplexType*|9||**rw**||
| |- Comfort|O3EInt16|2||||
| |- Normal|O3EInt16|2||||
| |- Reduced|O3EInt16|2||||
| |- Unknown|O3EInt16|2||||
| |- [State](## "{0: ShutDown, 1: Reduced, 2: Normal, 3: Comfort, 5: Fixed Value, 6: Antifreeze protection, 7: Energy Save: reduced, 8: Energy Save: normal, 9: Energy Save: comfort, 10: Cooling: normal, 11: Cooling: comfort, 12: No request}")|O3EEnum|1||||
|**2551**|**FlameBurnerTwo**|RawCodec|6||ro||
|**2552**|**ModulationCurrentValueBurnerTwo**|RawCodec|2||ro||
|**2553**|**HeatEngineStatisticalBurnerTwo**|RawCodec|12||ro||
|**2554**|**CellularModemIdentification**|RawCodec|62||ro||
|**2555**|**ElectricalPowerSetPoint**|RawCodec|4||**rw**||
|**2556**|**ElectricalEnergyRemainingCapacity**|RawCodec|4||ro||
|**2557**|**HeatPumpState**|O3EByteVal|1||ro||
|**2558**|**HeatPumpSupportedStates**|RawCodec|3||ro||
|**2559**|**VentilationFanModbusId**|RawCodec|2||ro||
|**2560**|**SmartGridFeatureSelection**|O3EByteVal|1||ro||
|**2563**|**ZigBeeDeviceDecoupleList**|RawCodec|91||ro||
|**2564**|**HydraulicFlapState**|RawCodec|1||ro||
|**2566**|**VentilationSupplyFanRuntime**|O3EInt32|4||ro||
|**2567**|**VentilationExhaustFanRuntime**|O3EInt32|4||ro||
|**2568**|**RefrigerantType**|O3EInt8|1||ro||
|**2569**|[**CompressorSpeedRps**](## "Actual speed of the heat pump compressor")|O3EInt16|2|rps|ro||
|**2570**|**CompressorModulType**|O3EInt16|2||ro||
|**2571**|**CompressorSuctionSuperheat**|O3EInt16|2||ro||
|**2572**|**ActualCompressorInletMassflow**|RawCodec|4||ro||
|**2573**|**CompressorOnTimer**|RawCodec|2||ro||
|**2574**|**NominalPowerElectricalHeater**|*O3EComplexType*|8||ro||
| |- Power|O3EInt16|2||||
| |- Unknown|RawCodec|6||||
|**2575**|**RefrigerationCycleApplicationState**|O3EInt16|2||ro||
|**2576**|**FuelCellTestModeOne**|RawCodec|2||ro||
|**2577**|**FuelCellTestModeTwo**|RawCodec|6||ro||
|**2578**|**RefrigerationCircuitDesiredOperatingMode**|O3EInt8|1||ro||
|**2579**|**CompressorMinMaxAllowedPrimaryTemperatureHeating**|RawCodec|4||ro||
|**2580**|**CompressorSetpointRps**|O3EInt16|2||**rw**||
|**2581**|**CompressorCalculatedSetpointRps**|O3EInt16|2||**rw**||
|**2582**|**CompressorOffTimer**|RawCodec|2||ro||
|**2583**|**OxygenProbeProcessValuesBurnerOne**|RawCodec|15||ro||
|**2584**|**OxygenProbeProcessValuesBurnerTwo**|RawCodec|15||ro||
|**2586**|**DigitalOutputCooling**|RawCodec|2||ro||
|**2587**|**BatteryModuleWarrantyDataListLastEntry**|RawCodec|5||ro||
|**2588**|**BatteryModuleWarrantyDataListOne**|RawCodec|197||ro||
|**2589**|**BatteryModuleWarrantyDataListTwo**|RawCodec|197||ro||
|**2590**|**HeatPumpCommonSettingsHeating**|RawCodec|8||ro||
|**2591**|**HeatPumpCommonSettingsCooling**|RawCodec|8||ro||
|**2592**|**ExpansionValveTheoreticalSetpoint**|RawCodec|4||**rw**||
|**2593**|**ProductMatrix**|*O3EList*|181||ro||
| |- Count|O3EInt8|1||||
| |- - Unknown|RawCodec|2||||
| |- - VIN|O3EUtf8|16||||
|**2594**|**ElectricalPreHeaterMonthMatrix**|RawCodec|124||ro||
|**2595**|**ElectricalPreHeaterYearMatrix**|RawCodec|96||ro||
|**2598**|**VentilationFanAssignmentAvailable**|O3EByteVal|1||ro||
|**2599**|**VentilationFanAssignmentSwitch**|O3EByteVal|1||ro||
|**2600**|**ElectricalHeaterActivation**|RawCodec|2||ro||
|**2601**|**ElectricalHeaterVentilationConfiguration**|RawCodec|2||ro||
|**2602**|**PrimaryHeatExchangerStatus**|RawCodec|10||ro||
|**2603**|**PrimaryHeatExchangerCommonSettings**|RawCodec|4||ro||
|**2604**|**LevelSwitchActivation**|O3EByteVal|1||ro||
|**2605**|**QuickModeRuntime**|*O3EComplexType*|4||ro||
| |- NoiseReduced|O3EInt16|2||||
| |- Intensive|O3EInt16|2||||
|**2606**|**ExternalTriggerActivation**|O3EByteVal|1||ro||
|**2607**|**ExternalTriggerSettings**|O3EByteVal|1||ro||
|**2608**|**FilterSettings**|RawCodec|28||ro||
|**2609**|**CommissioningStatus**|RawCodec|6||ro||
|**2610**|**SetDeliveryStateExpert**|RawCodec|1||ro||
|**2611**|**NominalThermalCapacityIndoorUnit**|O3EInt32|4||ro||
|**2612**|**PrimarySourceCommonSettingsHeating**|*O3EComplexType*|7||ro||
| |- Mode|O3EByteVal|1||||
| |- MaxFanSpeed|O3EInt16|2||||
| |- DefaultFanSpeed|O3EInt16|2||||
| |- MinFanSpeed|O3EInt16|2||||
|**2613**|**PrimarySourceCommonSettingsCooling**|*O3EComplexType*|7||ro||
| |- Mode|O3EByteVal|1||||
| |- MaxFanSpeed|O3EInt16|2||||
| |- DefaultFanSpeed|O3EInt16|2||||
| |- MinFanSpeed|O3EInt16|2||||
|**2621**|**MaximumOperatingPressureActualTemperatureSetpoint**|O3EInt16|2||**rw**||
|**2622**|**SeasonalCoefficientOfPerformanceHeating**|*O3EComplexType*|9||ro||
| |- CurrentYear|O3EInt8|1||||
| |- EnergyThermal|O3EInt32|4||||
| |- EnergyElectric|O3EInt32|4||||
|**2623**|**SeasonalEnergyEfficiencyRatioCooling**|*O3EComplexType*|9||ro||
| |- CurrentYear|O3EInt8|1||||
| |- EnergyThermal|O3EInt32|4||||
| |- EnergyElectric|O3EInt32|4||||
|**2624**|**SeasonalCoefficientOfPerformanceDomesticHotWater**|*O3EComplexType*|9||ro||
| |- CurrentYear|O3EInt8|1||||
| |- EnergyThermal|O3EInt32|4||||
| |- EnergyElectric|O3EInt32|4||||
|**2625**|**SeasonalCoefficientOfPerformanceHeatingAndDomesticHotWater**|*O3EComplexType*|9||ro||
| |- CurrentYear|O3EInt8|1||||
| |- EnergyThermal|O3EInt32|4||||
| |- EnergyElectric|O3EInt32|4||||
|**2626**|**MaximumPowerElectricalHeater**|O3EInt32|4||ro||
|**2627**|**CompressorStartUpTimer**|O3EInt16|2||ro||
|**2629**|**DesiredThermalCapacity**|O3EInt32|4||ro||
|**2630**|**CompressorMinMaxSpeedHeating**|*O3EComplexType*|4||ro||
| |- Min|O3EInt16|2||||
| |- Max|O3EInt16|2||||
|**2631**|**CompressorMinMaxSpeedCooling**|*O3EComplexType*|4||ro||
| |- Min|O3EInt16|2||||
| |- Max|O3EInt16|2||||
|**2632**|**CompressorMinMaxSpeedDefrost**|*O3EComplexType*|4||ro||
| |- Min|O3EInt16|2||||
| |- Max|O3EInt16|2||||
|**2633**|**MaxSpeedNoiseReductionMode**|RawCodec|12||ro||
|**2634**|**NoiseReductionMode**|O3EByteVal|1||ro||
|**2635**|**BurnerProcessDataFlags**|RawCodec|8||ro||
|**2636**|**BurnerTwoProcessDataFlags**|RawCodec|8||ro||
|**2637**|**BurnerThreeProcessDataFlags**|RawCodec|8||ro||
|**2638**|**SupportedCountryCodes**|RawCodec|4||ro||
|**2643**|**MaximumRechargePower**|O3EInt16|2||ro||
|**2733**|**InstallationConfirmation**|RawCodec|3||ro||
|**2735**|[**FourThreeWayValveValveCurrentPosition**](## "Current position of the four/three-way valve {0: Heating/Cooling, 1: Internal Buffer, 2: Domestic Hot Water, 3: Heating/Cooling and Internal Buffer, 4: Domestic Hot Water and Internal Buffer}")|O3EEnum|1||ro||
|**2741**|**ComfortEnsuringMode**|RawCodec|3||ro||
|**2742**|**DiagnosticHydraulicFilterInterval**|O3EInt8|1||ro||
|**2743**|**DiagnosticElectricalHeaterSafetyTemperatureLimiter**|O3EInt8|1||ro||
|**2744**|**DiagnosticSecondaryFourThreeWayValve**|O3EInt8|1||ro||
|**2745**|**DiagnosticHydraulicFilterContamination**|O3EInt8|1||ro||
|**2746**|**DiagnosticHydraulicSafetyValve**|O3EInt8|1||ro||
|**2748**|**DiagnosticControlledLowPressureShutDown**|O3EInt8|1||ro||
|**2749**|**DiagnosticControlledHighPressureShutDown**|O3EInt8|1||ro||
|**2750**|**DiagnosticHydraulicTemperatureSensors**|O3EInt8|1||ro||
|**2751**|**DiagnosticElectronicExpansionValve**|O3EInt8|1||ro||
|**2752**|**DiagnosticFanOperation**|O3EInt8|1||ro||
|**2753**|**DiagnosticHeatExchangerConstraints**|O3EInt8|1||ro||
|**2758**|**GasPressureSwitchErrorReaction**|RawCodec|1||ro||
|**2759**|**EnergyRecoveredCrossHeatExchanger**|RawCodec|24||ro||
|**2760**|[**EnergyOwnConsumption**](## "Own Energy Consumption")|*O3EComplexType*|24||ro||
| |- Today|O3EInt32|4|kWh|||
| |- Past7Days|O3EInt32|4|kWh|||
| |- CurrentMonth|O3EInt32|4|kWh|||
| |- PastMonth|O3EInt32|4|kWh|||
| |- CurrentYear|O3EInt32|4|kWh|||
| |- PastYear|O3EInt32|4|kWh|||
|**2767**|**DiagnosticMonitoringPressureDrop**|O3EInt8|1||ro||
|**2768**|**DiagnosticMonitoringPressurePeaks**|O3EInt8|1||ro||
|**2772**|**EnergyRecoveredCrossHeatExchangerMonthMatrix**|RawCodec|124||ro||
|**2773**|**EnergyRecoveredCrossHeatExchangerYearMatrix**|RawCodec|96||ro||
|**2774**|**EnergyOwnConsumptionMonthMatrix**|RawCodec|124||ro||
|**2775**|**EnergyOwnConsumptionYearMatrix**|RawCodec|96||ro||
|**2776**|**ProductMatrixTwo**|RawCodec|181||ro||
|**2777**|**PrimaryBootLoaderVersion**|RawCodec|8||ro||
|**2778**|**ErrorMessageInputSelection**|RawCodec|2||ro||
|**2779**|**DeltaTemperaturePumpControlSetpoint**|RawCodec|2||**rw**||
|**2780**|**DomesticHotWaterFlowRangeDwellDuration**|RawCodec|1||ro||
|**2781**|**AirVolumeFlowSetpoint**|RawCodec|7||**rw**||
|**2782**|**AirVolumeFlowStatus**|RawCodec|24||ro||
|**2783**|**VentilationSelfCheckDuration**|RawCodec|4||ro||
|**2784**|**SecondaryHeatExchangerVaporPressureSensor**|*O3EComplexType*|9||ro||
| |- Pressure|O3EInt16|2||||
| |- Unknown|RawCodec|7||||
|**2785**|**ElectricalHeaterStarts**|RawCodec|16||ro||
|**2786**|**ElectricalPreheaterCurrentPowerConsumption**|RawCodec|2||ro||
|**2791**|**CentralHeatingPumpStatus**|*O3EComplexType*|5||ro||
| |- Actual|O3EInt8|1||||
| |- Unknown|RawCodec|4||||
|**2792**|**MixerOneCircuitPumpStatus**|*O3EComplexType*|5||ro||
| |- Actual|O3EInt8|1||||
| |- Unknown|RawCodec|4||||
|**2793**|**MixerTwoCircuitPumpStatus**|*O3EComplexType*|5||ro||
| |- Actual|O3EInt8|1||||
| |- Unknown|RawCodec|4||||
|**2794**|**MixerThreeCircuitPumpStatus**|*O3EComplexType*|5||ro||
| |- Actual|O3EInt8|1||||
| |- Unknown|RawCodec|4||||
|**2795**|**MixerFourCircuitPumpStatus**|*O3EComplexType*|5||ro||
| |- Actual|O3EInt8|1||||
| |- Unknown|RawCodec|4||||
|**2796**|**ExternalHeaterConfiguration**|*O3EComplexType*|2||ro||
| |- StateRoomHeating|O3EBool|1||||
| |- StateDHWHeating|O3EBool|1||||
|**2797**|**VentilationBypassFlapAvailableCount**|O3EByteVal|1||ro||
|**2798**|**RelativeHumiditySensorSelection**|O3EByteVal|1||ro||
|**2799**|**ElectricalHeatersShutdownDelay**|O3EByteVal|1||ro||
|**2800**|**VentilationHeatExchangerType**|O3EByteVal|1||ro||
|**2801**|**VentilationFanAssignmentSwitchManufacturing**|O3EByteVal|1||ro||
|**2802**|**InverterSelfTestStatus**|RawCodec|6||ro||
|**2804**|**InverterSelfTestResultTwo**|RawCodec|151||ro||
|**2805**|**InverterSelfTestResultThree**|RawCodec|151||ro||
|**2806**|[**RefrigerationCircuitOperationMode**](## "Actual operating mode of the refrigeration circuit")|*O3EComplexType*|2||ro||
| |- Mode|O3EByteVal|1||||
| |- [State](## "{0: Off, 1: ShutDown, 2: Heating, 3: Cooling, 4: Manual, 5: De-icing, 6: Grid-lock}")|O3EEnum|1||||
|**2807**|**InverterHousingTemperature**|RawCodec|9||ro||
|**2808**|**InverterInternalPowerModuleTemperature**|RawCodec|9||ro||
|**2809**|**PumpMinSpeedConfiguration**|RawCodec|1||ro||
|**2810**|**CentralHeatingPumpFeedbackSignalHandlingMode**|RawCodec|1||ro||
|**2826**|**FuelCellNetworkSystemProtectionErrorHistory**|RawCodec|40||ro||
|**2827**|**FuelCellNetworkSystemProtectionParameters**|RawCodec|48||ro||
|**2828**|**FuelCellSdCardRecording**|RawCodec|2||ro||
|**2829**|**ProductIdentification**|RawCodec|20||ro||
|**2830**|**EmergencyMode**|RawCodec|1||ro||
|**2831**|**BivalenceControlAlternativeTemperature**|O3EInt16|2||ro||
|**2832**|**BaseHeaterTimer**|RawCodec|4||ro||
|**2833**|**BaseHeaterTimerMode**|O3EInt8|1||ro||
|**2834**|**BaseHeaterTimerDuration**|O3EInt16|2||ro||
|**2835**|**BaseHeaterTemperatureThreshold**|O3EInt16|2||ro||
|**2836**|**SecondaryHeatExchangerMinimumVolumeFlowThreshold**|O3EInt16|2||ro||
|**2837**|**SecondaryHeatExchangerOptimumTemperatureSpreadExponent**|O3EInt16|2||ro||
|**2838**|**SecondaryHeatExchangerOptimumTemperatureSpreadHeating**|RawCodec|4||ro||
|**2839**|**SecondaryHeatExchangerOptimumTemperatureSpreadCooling**|RawCodec|4||ro||
|**2840**|**SecondaryHeatExchangerOptimumVolumeFlowDefrost**|O3EInt16|2||ro||
|**2842**|**SecondaryHeatExchangerHxSubcooling**|O3EInt16|2||ro||
|**2843**|**SecondaryHeatExchangerMinimumVolumeFlow**|O3EInt16|2||ro||
|**2844**|**SecondaryHeatExchangerMinimumOutletTemperature**|O3EInt16|2||ro||
|**2845**|**SecondaryHeatExchangerMaximumOutletTemperature**|O3EInt16|2||ro||
|**2847**|**CrankCaseHeaterStatistics**|RawCodec|8||ro||
|**2848**|**CrankCaseHeaterTemperatureStatistics**|O3EInt16|2||ro||
|**2849**|**CrankCaseHeaterOnTimer**|RawCodec|27||ro||
|**2850**|**InstalledHeater**|*O3EComplexType*|3||ro||
| |- [FanDuctHeater](## "{0: Not Available, 1: Not Installed, 2: Installed, 3: Factory Installed}")|O3EEnum|1||||
| |- [CrankCaseHeater](## "{0: Not Available, 1: Not Installed, 2: Installed, 3: Factory Installed}")|O3EEnum|1||||
| |- [BaseHeater](## "{0: Not Available, 1: Not Installed, 2: Installed, 3: Factory Installed}")|O3EEnum|1||||
|**2851**|**PreStartDuration**|O3EInt16|2||ro||
|**2852**|**FanDuctHeater**|O3EByteVal|1||ro||
|**2853**|**ExternalHeaterTimeIntegralThershold**|O3EInt16|2||ro||
|**2855**|**MixerOneCircuitFrostProtectionConfiguration**|*O3EComplexType*|3||ro||
| |- State|O3EByteVal|1||||
| |- Temperature|O3EInt16|2||||
|**2856**|**MixerTwoCircuitFrostProtectionConfiguration**|*O3EComplexType*|3||ro||
| |- State|O3EByteVal|1||||
| |- Temperature|O3EInt16|2||||
|**2857**|**MixerThreeCircuitFrostProtectionConfiguration**|*O3EComplexType*|3||ro||
| |- State|O3EByteVal|1||||
| |- Temperature|O3EInt16|2||||
|**2858**|**MixerFourCircuitFrostProtectionConfiguration**|*O3EComplexType*|3||ro||
| |- State|O3EByteVal|1||||
| |- Temperature|O3EInt16|2||||
|**2874**|**PrimarySourceRpsOne**|O3EInt16|2||ro||
|**2875**|**PrimarySourceRpsTwo**|O3EInt16|2||ro||
|**2876**|**PrimaryPumpCommonSetpoint**|O3EInt16|2||**rw**||
|**2877**|**SuctionSuperheatSetpoint**|O3EInt16|2||**rw**||
|**2878**|**SubcoolingSetpoint**|O3EInt16|2||**rw**||
|**2879**|**MixerOneCircuitHeatingBlocked**|RawCodec|2||ro||
|**2880**|**MixerTwoCircuitHeatingBlocked**|RawCodec|2||ro||
|**2881**|**ExpansionValveOneTimer**|RawCodec|4||ro||
|**2882**|**ExpansionValveTwoTimer**|RawCodec|4||ro||
|**2883**|**ExpansionValveMaximumOperatingPressureTemperatureSetpoint**|O3EInt16|2||**rw**||
|**2884**|**ExpansionValveOneStatus**|O3EInt16|2||ro||
|**2885**|**ExpansionValveTwoStatus**|O3EInt16|2||ro||
|**2886**|**RefrigerantCyclePostStopDuration**|O3EInt16|2||ro||
|**2887**|**RefrigerantCycleAlarmPauseDuration**|O3EInt16|2||ro||
|**2888**|**RefrigerantCyclePumpdownStoppingDelay**|O3EInt16|2||ro||
|**2889**|**RefrigerantCycleTimers**|RawCodec|6||ro||
|**2890**|**RefrigerantCyclePumpdownHoldTimer**|O3EInt16|2||ro||
|**2891**|**RefrigerantCycleDefrostTimers**|RawCodec|6||ro||
|**2892**|**RefrigerantCycleTransitionToHeatingTimer**|O3EInt16|2||ro||
|**2893**|**RefrigerantCycleTransitionToCoolingTimer**|O3EInt16|2||ro||
|**2894**|**RefrigerantCycleAvailability**|O3EByteVal|1||ro||
|**2895**|**PrimaryPumpSettings**|RawCodec|5||ro||
|**2896**|**PrimaryPumpOneStatus**|O3EInt8|1||ro||
|**2897**|**PrimaryPumpTwoStatus**|O3EInt8|1||ro||
|**2908**|**InverterModuleType**|O3EInt8|1||ro||
|**2909**|**CompressorMinMaxRequestedSecondaryReturnTemperatureCooling**|RawCodec|4||ro||
|**2910**|**CompressorMinMaxRequestedSecondaryReturnTemperaturePreStartDefrost**|RawCodec|4||ro||
|**2911**|**CompressorMaximumRequestedSecondaryReturnTempDefrost**|O3EInt16|2||ro||
|**2912**|**CompressorMaximumDischargeTemperature**|O3EInt16|2||ro||
|**2913**|**CompressorMinimumAllowedSecondaryOutletTemperatureHeating**|O3EInt16|2||ro||
|**2914**|**CompressorMinMaxAllowedPrimaryTemperatureCooling**|RawCodec|4||ro||
|**2915**|**CompressorMaximumCondensingPressure**|O3EInt16|2||ro||
|**2916**|**CompressorMaximumEvaporatingPressure**|O3EInt16|2||ro||
|**2917**|**CompressorMinimumEvaporatingPressureHeating**|O3EInt16|2||ro||
|**2918**|**CompressorMinimumEvaporatingPressureCooling**|O3EInt16|2||ro||
|**2920**|**ExternalHeaterSpecification**|RawCodec|2||ro||
|**2921**|**DiagnosticHydraulicFilterIntervalSettings**|RawCodec|2||ro||
|**2922**|**DiagnosticHydraulicFilterIntervalTemporalSettings**|RawCodec|2||ro||
|**2923**|**DiagnosticSecondaryFourThreeWayValveSettings**|RawCodec|6||ro||
|**2924**|**DiagnosticHydraulicFilterContaminationSettings**|RawCodec|4||ro||
|**2925**|**DiagnosticMonitoringPressurePeaksSettings**|RawCodec|2||ro||
|**2926**|**DiagnosticMonitoringPressureDropSettings**|RawCodec|6||ro||
|**2927**|**DiagnosticElectronicExpansionValveSettings**|O3EInt8|1||ro||
|**2928**|**DiagnosticHeatExchangerConstraintsSettings**|O3EInt16|2||ro||
|**2929**|**DiagnosticRefrigerantCircuitPressureSensors**|O3EInt8|1||ro||
|**2930**|**DiagnosticRefrigerantCircuitFourTwoWayValve**|O3EInt8|1||ro||
|**2931**|**DiagnosticRefrigerantCircuitTemperatureSensors**|O3EInt8|1||ro||
|**2932**|**TimeCounterSinceLastReset**|RawCodec|4||ro||
|**2934**|**CurrentElectricalSystemPowerSetpoint**|O3EInt32|4||**rw**||
|**2936**|**ElectricalEnergyStorageSystemState**|RawCodec|3||ro||
|**2937**|**SystemPumpConfiguration**|RawCodec|2||ro||
|**2938**|**CascadeSystemPump**|RawCodec|4||ro||
|**2939**|**PrimaryHeatExchangerLowEvaporatingTemperatureAlarmDelay**|O3EInt16|2||ro||
|**2940**|**ExternalHeaterDelayTimer**|*O3EComplexType*|3||ro||
| |- SwitchOnDelay|O3EInt8|1||||
| |- MinRunTime|O3EInt8|1||||
| |- SwitchOffDelay|O3EInt8|1||||
|**2942**|**ListOfLayerSettingServiceDevices**|RawCodec|137||ro||
|**2944**|**NodeIdOnExternalCan**|O3EByteVal|1||ro||
|**2945**|**PointOfCommonCouplingEnergyMeterConnectedPhases**|RawCodec|1||ro||
|**2946**|**EnergyConsumptionElectricalPreHeater**|RawCodec|24||ro||
|**2947**|**SleepModePrevention**|RawCodec|5||ro||
|**2952**|**ListOfLayerSettingServiceDevicesTwo**|RawCodec|137||ro||
|**2953**|**CascadeSystemConfigurationArray**|RawCodec|10||ro||
|**2956**|**DeviceDigitalInputEightValue**|O3EInt8|1||ro||
|**2957**|**DeviceDigitalInputNineValue**|O3EInt8|1||ro||
|**2969**|**ElectronicControlUnitSafeStateStatus**|O3EByteVal|1||ro||
|**2985**|**ExternalHeaterTemperatureSetpoint**|O3EInt16|2||**rw**||
|**2986**|**ExternalHeaterOperationState**|O3EByteVal|1||**rw**||
|**2987**|**RefrigerantCycleUnlock**|O3EInt8|1||ro||
|**2996**|**BatteryAmbientTemperatureHistogramTwoPointFour**|RawCodec|40||ro||
|**2997**|**BatteryTemperatureHistogramTwoPointFour**|RawCodec|56||ro||
|**2998**|**HardwareSignalCheckCsc**|RawCodec|8||ro||
|**2999**|**ElectricalHeatersOperationHours**|RawCodec|16||ro||
|**3000**|**EcuResetInformationList**|RawCodec|115||ro||
|**3001**|**LowEvaporatingLowCondensingDriveDuration**|RawCodec|196||ro||
|**3002**|**MidEvaporatingLowCondensingDriveDuration**|RawCodec|196||ro||
|**3003**|**HighEvaporatingLowCondensingDriveDuration**|RawCodec|196||ro||
|**3004**|**LowEvaporatingHighCondensingDriveDuration**|RawCodec|196||ro||
|**3005**|**MidEvaporatingHighCondensingDriveDuration**|RawCodec|196||ro||
|**3006**|**HighEvaporatingHighCondensingDriveDuration**|RawCodec|196||ro||
|**3008**|**FanDuctHeaterOnDuration**|O3EInt16|2||ro||
|**3009**|**FanDuctHeaterOnTimer**|RawCodec|4||ro||
|**3013**|**MixerHybridThreeWayValvePositionPercent**|RawCodec|2||ro||
|**3014**|**OutdoorMiddleCoilTemperatureSensor**|*O3EComplexType*|9||ro||
| |- Actual|O3EInt16|2||||
| |- Minimum|O3EInt16|2||||
| |- Maximum|O3EInt16|2||||
| |- Average|O3EInt16|2||||
| |- [SensorStatus](## "{0: no_error, 1: interruption, 2: short_circuit, 3: electrical_fault, 4: not_available, 5: invalidates}")|O3EEnum|1||||
|**3015**|**HeatSinkTemperatureSensor**|*O3EComplexType*|9||ro||
| |- Actual|O3EInt16|2||||
| |- Minimum|O3EInt16|2||||
| |- Maximum|O3EInt16|2||||
| |- Average|O3EInt16|2||||
| |- [SensorStatus](## "{0: no_error, 1: interruption, 2: short_circuit, 3: electrical_fault, 4: not_available, 5: invalidates}")|O3EEnum|1||||
|**3016**|[**HeatingBufferTemperatureSensor**](## "Actual temperature of the heating buffer")|*O3EComplexType*|9||ro||
| |- Actual|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- Minimum|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- Maximum|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- Average|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- [SensorStatus](## "{0: no_error, 1: interruption, 2: short_circuit, 3: electrical_fault, 4: not_available, 5: invalidates}")|O3EEnum|1||||
|**3017**|**CoolingBufferTemperatureSensor**|*O3EComplexType*|9||ro||
| |- Actual|O3EInt16|2||||
| |- Minimum|O3EInt16|2||||
| |- Maximum|O3EInt16|2||||
| |- Average|O3EInt16|2||||
| |- [SensorStatus](## "{0: no_error, 1: interruption, 2: short_circuit, 3: electrical_fault, 4: not_available, 5: invalidates}")|O3EEnum|1||||
|**3018**|**HeatingCoolingBufferTemperatureSensor**|*O3EComplexType*|9||ro||
| |- Actual|O3EInt16|2||||
| |- Minimum|O3EInt16|2||||
| |- Maximum|O3EInt16|2||||
| |- Average|O3EInt16|2||||
| |- [SensorStatus](## "{0: no_error, 1: interruption, 2: short_circuit, 3: electrical_fault, 4: not_available, 5: invalidates}")|O3EEnum|1||||
|**3019**|**CompressorOutletTargetTemperature**|*O3EComplexType*|9||**rw**||
| |- Actual|O3EInt16|2||||
| |- Minimum|O3EInt16|2||||
| |- Maximum|O3EInt16|2||||
| |- Average|O3EInt16|2||||
| |- [SensorStatus](## "{0: no_error, 1: interruption, 2: short_circuit, 3: electrical_fault, 4: not_available, 5: invalidates}")|O3EEnum|1||||
|**3029**|**DomesticHotWaterEfficiencyMode**|O3EByteVal|1||ro||
|**3030**|**DomesticHotWaterEfficiencyModeAvailability**|RawCodec|2||ro||
|**3031**|**ExternalHeater**|RawCodec|2||ro||
|**3032**|**PrimaryEnergyFactorElectricity**|O3EInt16|2||ro||
|**3034**|**DomesticHotWaterReturnTemperaturTankLoadSystem**|*O3EComplexType*|9||ro||
| |- Actual|O3EInt16|2||||
| |- Minimum|O3EInt16|2||||
| |- Maximum|O3EInt16|2||||
| |- Average|O3EInt16|2||||
| |- [SensorStatus](## "{0: no_error, 1: interruption, 2: short_circuit, 3: electrical_fault, 4: not_available, 5: invalidates}")|O3EEnum|1||||
|**3035**|**DomesticHotWaterFlowTemperaturTankLoadSystem**|*O3EComplexType*|9||ro||
| |- Actual|O3EInt16|2||||
| |- Minimum|O3EInt16|2||||
| |- Maximum|O3EInt16|2||||
| |- Average|O3EInt16|2||||
| |- [SensorStatus](## "{0: no_error, 1: interruption, 2: short_circuit, 3: electrical_fault, 4: not_available, 5: invalidates}")|O3EEnum|1||||
|**3036**|**PrimaryEnergyFactorExternalHeater**|O3EInt16|2||ro||
|**3037**|**ElectricityPriceTimeScheduleMonday**|RawCodec|57||**rw**||
|**3038**|**ElectricityPriceTimeScheduleTuesday**|RawCodec|57||**rw**||
|**3039**|**ElectricityPriceTimeScheduleWednesday**|RawCodec|57||**rw**||
|**3040**|**ElectricityPriceTimeScheduleThursday**|RawCodec|57||**rw**||
|**3041**|**ElectricityPriceTimeScheduleFriday**|RawCodec|57||**rw**||
|**3042**|**ElectricityPriceTimeScheduleSaturday**|RawCodec|57||**rw**||
|**3043**|**ElectricityPriceTimeScheduleSunday**|RawCodec|57||**rw**||
|**3056**|**NarrowBandInternetOfThingsNetworkStatus**|O3EInt8|1||ro||
|**3057**|**NarrowBandInternetOfThingsCloudStatus**|O3EInt8|1||ro||
|**3066**|**DomesticHotWaterHighDemandDetection**|RawCodec|4||ro||
|**3067**|**AirVolumeFlowValue**|RawCodec|9||ro||
|**3068**|[**DomesticHotWaterTemperatureSetpointComfort**](## "Temperature setpoint domestic hot water comfort")|O3EInt16|2|[°C](## "°C or °F (system configuration)")|**rw**||
|**3069**|**DomesticHotWaterSensorForDemand**|O3EByteVal|1||ro||
|**3070**|**BufferTargetOperationMode**|O3EByteVal|1||**rw**||
|**3085**|**ElectricalEnergyStorageModuleOneInformation**|RawCodec|18||ro||
|**3086**|**ElectricalEnergyStorageModuleTwoInformation**|RawCodec|18||ro||
|**3087**|**ElectricalEnergyStorageModuleThreeInformation**|RawCodec|18||ro||
|**3088**|**ElectricalEnergyStorageModuleFourInformation**|RawCodec|18||ro||
|**3089**|**ElectricalEnergyStorageModuleFiveInformation**|RawCodec|18||ro||
|**3090**|**ElectricalEnergyStorageModuleSixInformation**|RawCodec|18||ro||
|**3091**|**GatewayEthernetTwoEnable**|O3EByteVal|1||ro||
|**3092**|**GatewayEthernetTwoConfig**|RawCodec|21||ro||
|**3093**|**GatewayEthernetTwoIp**|RawCodec|20||ro||
|**3094**|**GatewayEthernetTwoNetworkStatus**|O3EByteVal|1||ro||
|**3095**|**MacAddressLanTwo**|RawCodec|6||ro||
|**3096**|**GatewayWifiStationEnable**|O3EByteVal|1||ro||
|**3097**|**GatewayInternetAccess**|O3EByteVal|1||ro||
|**3098**|**ExternalHeaterTemperatureOffset**|*O3EComplexType*|2||**rw**||
| |- Offset|O3EInt8|1||||
| |- Unknown|RawCodec|1||||
|**3103**|**IsCountryModeLoadInformation**|RawCodec|6||ro||
|**3106**|**BufferMinimumMaximumSetTemperature**|*O3EComplexType*|4||**rw**||
| |- BufferMin|O3EInt16|2||||
| |- BufferMax|O3EInt16|2||||
|**3107**|**BatteryModuleExchangeAssistent**|RawCodec|7||ro||
|**3108**|**PhotovoltaicsActivePowerLimitationRampRate**|RawCodec|9||ro||
|**3109**|**PrimaryHeatExchangerBaseHeaterStatistical**|RawCodec|8||ro||
|**3113**|**DeviceDigitalOutputOneValueStatistical**|RawCodec|8||ro||
|**3114**|**DeviceDigitalOutputTwoValueStatistical**|RawCodec|8||ro||
|**3115**|**DeviceDigitalOutputThreeValueStatistical**|RawCodec|8||ro||
|**3116**|**DeviceDigitalOutputFourValueStatistical**|RawCodec|8||ro||
|**3117**|**DeviceDigitalOutputFiveValueStatistical**|RawCodec|8||ro||
|**3119**|**RefrigerantCircuitFourWayValveStatistical**|RawCodec|8||ro||
|**3120**|**CompressorCrankCaseHeaterStatistical**|RawCodec|8||ro||
|**3129**|**FanDuctHeaterStatistical**|RawCodec|8||ro||
|**3134**|**DomesticHotWaterCirculationPumpStatistical**|RawCodec|8||**rw**||
|**3146**|**ElectricalHeaterPhaseOneStatistical**|RawCodec|8||ro||
|**3147**|**ElectricalHeaterPhaseTwoStatistical**|RawCodec|8||ro||
|**3148**|**ElectricalHeaterPhaseThreeStatistical**|RawCodec|8||ro||
|**3155**|**DomesticHotWaterShiftLoadPumpStatus**|RawCodec|5||ro||
|**3156**|**DomesticHotWaterShiftLoadPumpType**|O3EByteVal|1||ro||
|**3190**|**RefrigerantCircuitFourWayValvePosition**|O3EByteVal|1||ro||
|**3191**|**ExtendedEventLoggingHistory**|RawCodec|199||ro||
|**3212**|**BivalentMixerDomesticHotWaterTemperatureOffset**|*O3EComplexType*|2||**rw**||
| |- Offset|O3EInt8|1||||
| |- Unknown|RawCodec|1||||
|**3213**|**ExternalHeaterTemperatureSensor**|*O3EComplexType*|9||ro||
| |- Actual|O3EInt16|2||||
| |- Minimum|O3EInt16|2||||
| |- Maximum|O3EInt16|2||||
| |- Average|O3EInt16|2||||
| |- [SensorStatus](## "{0: no_error, 1: interruption, 2: short_circuit, 3: electrical_fault, 4: not_available, 5: invalidates}")|O3EEnum|1||||
|**3215**|**ExternalHeaterSeparatorTemperatureSensor**|*O3EComplexType*|9||ro||
| |- Actual|O3EInt16|2||||
| |- Minimum|O3EInt16|2||||
| |- Maximum|O3EInt16|2||||
| |- Average|O3EInt16|2||||
| |- [SensorStatus](## "{0: no_error, 1: interruption, 2: short_circuit, 3: electrical_fault, 4: not_available, 5: invalidates}")|O3EEnum|1||||
|**3228**|**EnergyMeterOne**|*O3EComplexType*|73||ro||
| |- PowerL1|O3EInt32|4||||
| |- ReactivePowerL1|O3EInt32|4||||
| |- PowerL2|O3EInt32|4||||
| |- ReactivePowerL2|O3EInt32|4||||
| |- PowerL3|O3EInt32|4||||
| |- ReactivePowerL3|O3EInt32|4||||
| |- EnergyImport|O3EInt64|8||||
| |- EnergyExport|O3EInt64|8||||
| |- Unknown1|O3EInt64|8||||
| |- Unknown2|RawCodec|8||||
| |- VoltageL1|O3EInt16|2||||
| |- VoltageL2|O3EInt16|2||||
| |- VoltageL3|O3EInt16|2||||
| |- CurrentL1|O3EInt16|2||||
| |- CurrentL2|O3EInt16|2||||
| |- CurrentL3|O3EInt16|2||||
| |- PowerFactor|O3EInt16|2||||
| |- Unknown3|RawCodec|3||||
|**3229**|**EnergyMeterTwo**|*O3EComplexType*|73||ro||
| |- PowerL1|O3EInt32|4||||
| |- ReactivePowerL1|O3EInt32|4||||
| |- PowerL2|O3EInt32|4||||
| |- ReactivePowerL2|O3EInt32|4||||
| |- PowerL3|O3EInt32|4||||
| |- ReactivePowerL3|O3EInt32|4||||
| |- EnergyImport|O3EInt64|8||||
| |- EnergyExport|O3EInt64|8||||
| |- Unknown1|O3EInt64|8||||
| |- Unknown2|RawCodec|8||||
| |- VoltageL1|O3EInt16|2||||
| |- VoltageL2|O3EInt16|2||||
| |- VoltageL3|O3EInt16|2||||
| |- CurrentL1|O3EInt16|2||||
| |- CurrentL2|O3EInt16|2||||
| |- CurrentL3|O3EInt16|2||||
| |- PowerFactor|O3EInt16|2||||
| |- Unknown3|RawCodec|3||||
|**3230**|**EnergyMeterThree**|*O3EComplexType*|73||ro||
| |- PowerL1|O3EInt32|4||||
| |- ReactivePowerL1|O3EInt32|4||||
| |- PowerL2|O3EInt32|4||||
| |- ReactivePowerL2|O3EInt32|4||||
| |- PowerL3|O3EInt32|4||||
| |- ReactivePowerL3|O3EInt32|4||||
| |- EnergyImport|O3EInt64|8||||
| |- EnergyExport|O3EInt64|8||||
| |- Unknown1|O3EInt64|8||||
| |- Unknown2|RawCodec|8||||
| |- VoltageL1|O3EInt16|2||||
| |- VoltageL2|O3EInt16|2||||
| |- VoltageL3|O3EInt16|2||||
| |- CurrentL1|O3EInt16|2||||
| |- CurrentL2|O3EInt16|2||||
| |- CurrentL3|O3EInt16|2||||
| |- PowerFactor|O3EInt16|2||||
| |- Unknown3|RawCodec|3||||
|**3231**|**EnergyMeterFour**|*O3EComplexType*|73||ro||
| |- PowerL1|O3EInt32|4||||
| |- ReactivePowerL1|O3EInt32|4||||
| |- PowerL2|O3EInt32|4||||
| |- ReactivePowerL2|O3EInt32|4||||
| |- PowerL3|O3EInt32|4||||
| |- ReactivePowerL3|O3EInt32|4||||
| |- EnergyImport|O3EInt64|8||||
| |- EnergyExport|O3EInt64|8||||
| |- Unknown1|O3EInt64|8||||
| |- Unknown2|RawCodec|8||||
| |- VoltageL1|O3EInt16|2||||
| |- VoltageL2|O3EInt16|2||||
| |- VoltageL3|O3EInt16|2||||
| |- CurrentL1|O3EInt16|2||||
| |- CurrentL2|O3EInt16|2||||
| |- CurrentL3|O3EInt16|2||||
| |- PowerFactor|O3EInt16|2||||
| |- Unknown3|RawCodec|3||||
|**3232**|**DomesticHotWaterBufferBottomTemperatureSensor**|*O3EComplexType*|9||ro||
| |- Actual|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- Minimum|O3EInt16|2||||
| |- Maximum|O3EInt16|2||||
| |- Average|O3EInt16|2||||
| |- [SensorStatus](## "{0: no_error, 1: interruption, 2: short_circuit, 3: electrical_fault, 4: not_available, 5: invalidates}")|O3EEnum|1||||
|**3233**|**DomesticHotWaterBufferMidTemperatureSensor**|*O3EComplexType*|9||ro||
| |- Actual|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- Minimum|O3EInt16|2||||
| |- Maximum|O3EInt16|2||||
| |- Average|O3EInt16|2||||
| |- [SensorStatus](## "{0: no_error, 1: interruption, 2: short_circuit, 3: electrical_fault, 4: not_available, 5: invalidates}")|O3EEnum|1||||
|**3234**|**DomesticHotWaterBufferTopTemperatureSensor**|*O3EComplexType*|9||ro||
| |- Actual|O3EInt16|2|[°C](## "°C or °F (system configuration)")|||
| |- Minimum|O3EInt16|2||||
| |- Maximum|O3EInt16|2||||
| |- Average|O3EInt16|2||||
| |- [SensorStatus](## "{0: no_error, 1: interruption, 2: short_circuit, 3: electrical_fault, 4: not_available, 5: invalidates}")|O3EEnum|1||||
|**3235**|**BufferLoadingTimeLimit**|O3EInt16|2||**rw**||
|**3282**|**DomesticHotWaterMinimumComfortTemperatureSetpoint**|O3EInt16|2|[°C](## "°C or °F (system configuration)")|**rw**||
|**3335**|**HeatingCoolingHysteresisHeatingCircuitOne**|*O3EComplexType*|8||ro||
| |- TurnOnHysteresis_Heating|O3EInt16|2||||
| |- TurnOffHysteresis_Heating|O3EInt16|2||||
| |- TurnOnHysteresis_Cooling|O3EInt16|2||||
| |- TurnOffHysteresis_Cooling|O3EInt16|2||||
|**3336**|**HeatingCoolingHysteresisHeatingCircuitTwo**|*O3EComplexType*|8||ro||
| |- TurnOnHysteresis_Heating|O3EInt16|2||||
| |- TurnOffHysteresis_Heating|O3EInt16|2||||
| |- TurnOnHysteresis_Cooling|O3EInt16|2||||
| |- TurnOffHysteresis_Cooling|O3EInt16|2||||
|**3337**|**HeatingCoolingHysteresisHeatingCircuitThree**|*O3EComplexType*|8||ro||
| |- TurnOnHysteresis_Heating|O3EInt16|2||||
| |- TurnOffHysteresis_Heating|O3EInt16|2||||
| |- TurnOnHysteresis_Cooling|O3EInt16|2||||
| |- TurnOffHysteresis_Cooling|O3EInt16|2||||
|**3338**|**HeatingCoolingHysteresisHeatingCircuitFour**|*O3EComplexType*|8||ro||
| |- TurnOnHysteresis_Heating|O3EInt16|2||||
| |- TurnOffHysteresis_Heating|O3EInt16|2||||
| |- TurnOnHysteresis_Cooling|O3EInt16|2||||
| |- TurnOffHysteresis_Cooling|O3EInt16|2||||
|**3366**|**ElectricalActivePowerStatusReport**|*O3EComplexType*|16||ro||
| |- 15MinPower|O3EInt32|4||||
| |- 15MinEnergy|O3EInt32|4||||
| |- Unknown1|O3EInt32|4||||
| |- Unknown2|O3EInt32|4||||
|**3384**|**ElectricalActivePowerConsumptionLimitationDefaultValue**|*O3EComplexType*|4||ro||
| |- Default|O3EInt16|2||||
| |- CurrentValue|O3EInt16|2||||
## All presently known data points in compact format

[Back to table of contents](#table-of-contents)

|  Did | ID   | Codec | Length | Unit  |   Access | Further info |
| ---: | :--- | :---  | ---:   | :---: |  :---:  | :---         |
|**256**|[**BusIdentification**](## "Device infos")|*O3EComplexType*|36||ro||
|**257**|[**StatusDtcList**](## "List of active status messages")|*O3EList*|122||ro||
|**258**|[**StatusDtcHistory**](## "History of status messages")|*O3EList*|122||ro||
|**259**|[**InfoDtcList**](## "List of active info messages")|*O3EList*|122||ro||
|**260**|[**InfoDtcHistory**](## "History of info messages")|*O3EList*|122||ro||
|**261**|[**ServiceDtcList**](## "List of active service messages")|*O3EList*|122||ro||
|**262**|[**ServiceDtcHistory**](## "History of service messages")|*O3EList*|122||ro||
|**263**|[**WarningDtcList**](## "List of active warning messages")|*O3EList*|122||ro||
|**264**|[**WarningDtcHistory**](## "History of warning messages")|*O3EList*|124||ro||
|**265**|[**ErrorDtcList**](## "List of active error messages")|*O3EList*|122||ro||
|**266**|[**ErrorDtcHistory**](## "History of error messages")|*O3EList*|124||ro||
|**268**|[**FlowTemperatureSensor**](## "Flow temperature in the primary circuit downstream from the heat generator")|*O3EComplexType*|9||ro|[Link](https://github.com/open3e/open3e/wiki/036-DoI-%E2%80%90-Data-points-of-Interest/#data-points-of-vitocal-250)|
|**269**|[**ReturnTemperatureSensor**](## "Flow temperature in the primary circuit upstream from the heat generator")|*O3EComplexType*|9||ro|[Link](https://github.com/open3e/open3e/wiki/036-DoI-%E2%80%90-Data-points-of-Interest/#data-points-of-vitocal-250)|
|**271**|[**DomesticHotWaterSensor**](## "Actual temperature domestic hot water buffer")|*O3EComplexType*|9||ro|[Link](https://github.com/open3e/open3e/wiki/036-DoI-%E2%80%90-Data-points-of-Interest/#data-points-of-vitocal-250)|
|**272**|**DomesticHotWaterFlowSensor**|RawCodec|10||ro||
|**273**|[**SolarRoofTemperatureSensor**](## "Actual collector temperature value")|*O3EComplexType*|9||ro||
|**274**|[**OutsideTemperatureSensor**](## "Outside temperature value")|*O3EComplexType*|9||ro||
|**275**|[**SolarBottomTemperatureSensor**](## "Actual collector return temperature value")|*O3EComplexType*|9||ro||
|**277**|[**BufferBottomTemperatureSensor**](## "Actual buffer bottom temperature value")|*O3EComplexType*|9||ro||
|**278**|[**BufferMidBottomTemperatureSensor**](## "Actual buffer mid bottom temperature value")|*O3EComplexType*|9||ro||
|**279**|[**BufferMidTemperatureSensor**](## "Actual buffer mid temperature value")|*O3EComplexType*|9||ro||
|**281**|[**BufferTopTemperatureSensor**](## "Actual buffer top temperature value")|*O3EComplexType*|9||ro||
|**282**|[**HydraulicSeparatorTemperatureSensor**](## "Actual flow temperature of the hydraulic switch")|*O3EComplexType*|9||ro||
|**283**|[**HydraulicSeparatorReturnTemperatureSensor**](## "Actual return temperature of the hydraulic switch")|*O3EComplexType*|9||ro||
|**284**|[**MixerOneCircuitFlowTemperatureSensor**](## "Heating circuit 1: Actual flow temperature value")|*O3EComplexType*|9||ro||
|**285**|[**MixerOneCircuitReturnTemperatureSensor**](## "Heating circuit 1: Actual return temperature value")|*O3EComplexType*|9||ro||
|**286**|[**MixerTwoCircuitFlowTemperatureSensor**](## "Heating circuit 2: Actual flow temperature value")|*O3EComplexType*|9||ro||
|**287**|[**MixerTwoCircuitReturnTemperatureSensor**](## "Heating circuit 2: Actual return temperature value")|*O3EComplexType*|9||ro||
|**288**|[**MixerThreeCircuitFlowTemperatureSensor**](## "Heating circuit 3: Actual flow temperature value")|*O3EComplexType*|9||ro||
|**289**|[**MixerThreeCircuitReturnTemperatureSensor**](## "Heating circuit 3: Actual return temperature value")|*O3EComplexType*|9||ro||
|**290**|[**MixerFourCircuitFlowTemperatureSensor**](## "Heating circuit 4: Actual flow temperature value")|*O3EComplexType*|9||ro||
|**291**|[**MixerFourCircuitReturnTemperatureSensor**](## "Heating circuit 4: Actual return temperature value")|*O3EComplexType*|9||ro||
|**318**|[**WaterPressureSensor**](## "Actual pressure heat generator circulation")|*O3EComplexType*|9||ro||
|**320**|[**PrimaryHeatExchangerLiquidTemperatureSensor**](## "Actual temperature primary heat exchanger inlet")|*O3EComplexType*|9||ro||
|**321**|[**CompressorInletTemperatureSensor**](## "Actual temperature compressor inlet")|*O3EComplexType*|9||ro||
|**322**|[**CompressorInletPressureSensor**](## "Actual pressure compressor inlet")|*O3EComplexType*|9||ro||
|**324**|[**CompressorOutletTemperatureSensor**](## "Actual temperature compressor outlet")|*O3EComplexType*|9||ro||
|**325**|[**CompressorOutletPressureSensor**](## "Actual pressure compressor outlet")|*O3EComplexType*|9||ro||
|**327**|**OutdoorAirTemperatureSensor**|*O3EComplexType*|9||ro||
|**328**|**SupplyAirTemperatureSensor**|*O3EComplexType*|9||ro||
|**329**|**ExtractAirTemperatureSensor**|*O3EComplexType*|9||ro||
|**330**|**ExhaustAirTemperatureSensor**|*O3EComplexType*|9||ro||
|**331**|**FlueGasTemperatureSensor**|*O3EComplexType*|9||ro||
|**323**|**EnhancedVapourInjectionTemperatureSensor**|RawCodec|9||ro||
|**334**|**MixerOneCircuitRoomTemperatureSensor**|*O3EComplexType*|9||ro||
|**335**|**MixerTwoCircuitRoomTemperatureSensor**|*O3EComplexType*|9||ro||
|**336**|**MixerThreeCircuitRoomTemperatureSensor**|*O3EComplexType*|9||ro||
|**337**|**MixerFourCircuitRoomTemperatureSensor**|*O3EComplexType*|9||ro||
|**354**|**PrimaryHeatExchangerBaseHeater**|O3EByteVal|1||ro||
|**355**|[**SecondaryHeatExchangerLiquidTemperatureSensor**](## "Actual temperature secondary heat exchanger outlet")|*O3EComplexType*|9||ro||
|**356**|**MainPowerSupplyValue**|O3EInt16|2||ro||
|**360**|**DomesticHotWaterOutletSensor**|*O3EComplexType*|9||ro||
|**364**|**Flame**|*O3EComplexType*|6||ro||
|**365**|**FlameStatistical**|*O3EComplexType*|42||ro||
|**373**|**FanTargetSpeed**|O3EInt16|2||**rw**||
|**374**|**FanCurrentSpeed**|O3EInt16|2||ro||
|**376**|**MassFlowSensor**|*O3EComplexType*|9||ro||
|**377**|**ViessmannIdentificationNumber**|O3EUtf8|16||ro||
|**378**|**PointOfCommonCouplingPhaseOne**|*O3EComplexType*|4||ro||
|**379**|**PointOfCommonCouplingPhaseTwo**|*O3EComplexType*|4||ro||
|**380**|**PointOfCommonCouplingPhaseThree**|*O3EComplexType*|4||ro||
|**381**|[**CentralHeatingPump**](## "Status of the primary circuit pump")|*O3EComplexType*|4||ro|[Link](https://github.com/open3e/open3e/discussions/212)|
|**382**|**UnitsAndFormats**|*O3EComplexType*|5||ro||
|**386**|**DiverterValveTargetPosition**|O3EByteVal|1||**rw**||
|**388**|[**ElectronicExpansionValveOneTargetPositionPercent**](## "Target position expansion valve one (secondary heat exchanger outlet)")|O3EInt8|1|%|**rw**||
|**389**|[**ElectronicExpansionValveOneCurrentPositionPercent**](## "Actual position expansion valve one (secondary heat exchanger outlet)")|O3EInt8|1|%|ro||
|**390**|[**ElectronicExpansionValveTwoTargetPositionPercent**](## "Target position expansion valve two (evaporator outlet)")|O3EInt8|1|%|**rw**||
|**391**|[**ElectronicExpansionValveTwoCurrentPositionPercent**](## "Actual position expansion valve two (evaporator outlet)")|O3EInt8|1|%|ro||
|**392**|**DomesticHotWaterPump**|RawCodec|4||ro||
|**395**|[**CentralHeatingTemperatureSetpoint**](## "Temperature setpoint central heating")|O3EInt16|2|[°C](## "°C or °F (system configuration)")|**rw**||
|**396**|[**DomesticHotWaterTemperatureSetpoint**](## "Temperature setpoint domestic hot water")|O3EInt16|2|[°C](## "°C or °F (system configuration)")|**rw**||
|**401**|**MixerOneCircuitPump**|*O3EComplexType*|5||ro||
|**402**|**MixerTwoCircuitPump**|*O3EComplexType*|5||ro||
|**403**|**MixerThreeCircuitPump**|*O3EComplexType*|5||ro||
|**404**|**MixerFourCircuitPump**|*O3EComplexType*|5||ro||
|**405**|**MixerFiveCircuitPump**|*O3EComplexType*|5||ro||
|**406**|**MixerSixCircuitPump**|*O3EComplexType*|5||ro||
|**407**|**MixerSevenCircuitPump**|*O3EComplexType*|5||ro||
|**408**|**MixerEightCircuitPump**|*O3EComplexType*|5||ro||
|**417**|**SolarCircuitPump**|*O3EComplexType*|5||ro||
|**419**|**OutdoorAirHumiditySensor**|*O3EComplexType*|5||ro||
|**420**|**SupplyAirHumiditySensor**|*O3EComplexType*|5||ro||
|**421**|**ExtractAirHumiditySensor**|*O3EComplexType*|5||ro||
|**422**|**ExhaustAirHumiditySensor**|*O3EComplexType*|5||ro||
|**424**|**MixerOneCircuitRoomTemperatureSetpoint**|*O3EComplexType*|9||**rw**||
|**426**|**MixerTwoCircuitRoomTemperatureSetpoint**|*O3EComplexType*|9||**rw**||
|**428**|**MixerThreeCircuitRoomTemperatureSetpoint**|*O3EComplexType*|9||**rw**||
|**429**|**ElectricalPreHeater**|RawCodec|4||ro||
|**430**|**MixerFourCircuitRoomTemperatureSetpoint**|*O3EComplexType*|9||**rw**||
|**431**|**SupplyAirVolumeFlowSensor**|*O3EComplexType*|9||ro||
|**432**|**MixerFiveCircuitRoomTemperatureSetpoint**|*O3EComplexType*|9||**rw**||
|**433**|**ExhaustAirVolumeFlowSensor**|*O3EComplexType*|9||ro||
|**434**|**MixerSixCircuitRoomTemperatureSetpoint**|*O3EComplexType*|9||**rw**||
|**435**|**VentilationStageTargetVolumeFlow**|*O3EComplexType*|8||**rw**||
|**436**|**MixerSevenCircuitRoomTemperatureSetpoint**|*O3EComplexType*|9||**rw**||
|**437**|**BypassOperationState**|*O3EComplexType*|2||**rw**||
|**438**|**MixerEightCircuitRoomTemperatureSetpoint**|*O3EComplexType*|9||**rw**||
|**439**|**BypassAvailableModes**|O3EByteVal|1||ro||
|**449**|**ElectricalEnergyMatrix**|RawCodec|141||ro||
|**451**|**ExternalAlternatingCurrentPowerSetpoint**|RawCodec|4||**rw**||
|**475**|**MixerOneCircuitThreeWayValvePositionPercent**|*O3EComplexType*|2||ro||
|**476**|**MixerTwoCircuitThreeWayValvePositionPercent**|*O3EComplexType*|2||ro||
|**477**|**MixerThreeCircuitThreeWayValvePositionPercent**|*O3EComplexType*|2||ro||
|**478**|**MixerFourCircuitThreeWayValvePositionPercent**|*O3EComplexType*|2||ro||
|**491**|[**DomesticHotWaterCirculationPump**](## "Request for domestic hot water circulation pump")|*O3EComplexType*|2||**rw**||
|**497**|[**DomesticHotWaterCirculationPumpMode**](## "Operation Mode of domestic hot water circulation pump")|*O3EComplexType*|5||**rw**|[See page 22f](https://static.viessmann-climatesolutions.com/resources/technical_documents/DE/de/VSA/6179923VSA00001_1.pdf?)|
|**500**|**CentralHeatDemandExternalAc**|RawCodec|2||ro||
|**503**|**ScaldProtection**|RawCodec|2||ro||
|**504**|**DomesticHotWaterSetpointMetaData**|*O3EComplexType*|14||**rw**||
|**505**|**Date**|O3ESdate|3||ro||
|**506**|**Time**|O3EStime|3||ro||
|**507**|**UniversalTimeCoordinated**|O3EUtc|4||ro||
|**508**|**UniversalTimeCoordinatedOffset**|O3EByteVal|1||**rw**||
|**510**|**Language**|O3EByteVal|1||ro||
|**511**|**HolidayPhase**|*O3EComplexType*|8||ro||
|**512**|**HolidayAtHomePhase**|*O3EComplexType*|8||ro||
|**513**|**HolidayPhaseCircuitOne**|*O3EComplexType*|8||ro||
|**514**|**HolidayAtHomePhaseCircuitOne**|*O3EComplexType*|8||ro||
|**515**|**HolidayPhaseCircuitTwo**|*O3EComplexType*|8||ro||
|**516**|**HolidayAtHomePhaseCircuitTwo**|*O3EComplexType*|8||ro||
|**517**|**HolidayPhaseCircuitThree**|*O3EComplexType*|8||ro||
|**518**|**HolidayAtHomePhaseCircuitThree**|*O3EComplexType*|8||ro||
|**519**|**HolidayPhaseCircuitFour**|*O3EComplexType*|8||ro||
|**520**|**HolidayAtHomePhaseCircuitFour**|*O3EComplexType*|8||ro||
|**521**|**OperatingHoursTillService**|O3EInt16|2||ro||
|**522**|**ServiceDateNext**|*O3EComplexType*|4||ro||
|**523**|**ServiceDateLast**|O3ESdate|3||ro||
|**524**|**ModulationTargetSetpoint**|O3EInt16|2||**rw**||
|**525**|**ExternalModulationSetpoint**|O3EInt16|2||**rw**||
|**526**|**ModulationCurrentValue**|O3EInt16|2||ro||
|**527**|**FlowTemperatureTargetSetpoint**|O3EInt16|2||**rw**||
|**528**|**ExternalTargetFlowTemperatureSetpoint**|O3EInt16|2||**rw**||
|**531**|[**DomesticHotWaterOperationState**](## "Operation state of domestic hot water preparation")|*O3EComplexType*|2||**rw**||
|**533**|**VentilationTargetOperationLevel**|*O3EComplexType*|2||**rw**||
|**534**|**DomesticHotWaterPumpPostRunTime**|RawCodec|2||ro||
|**535**|[**ObjectElectricalEnergyStatistical**](## "Cumulative Grid Energy Statistics")|*O3EComplexType*|12||ro|[Link](https://github.com/open3e/open3e/wiki/036-DoI-%E2%80%90-Data-points-of-Interest/#data-points-of-vx3)|
|**537**|**ExternalMixerOneCircuitTargetOperationMode**|*O3EComplexType*|2||**rw**||
|**538**|**ExternalDomesticHotWaterTargetOperationMode**|*O3EComplexType*|2||**rw**||
|**543**|**SmartGridReadyConsolidator**|*O3EComplexType*|4||ro||
|**544**|**GasConsumptionCentralHeating**|*O3EComplexType*|12||ro||
|**545**|**GasConsumptionDomesticHotWater**|*O3EComplexType*|12||ro||
|**548**|**EnergyConsumptionCentralHeating**|*O3EComplexType*|24||ro||
|**565**|**EnergyConsumptionDomesticHotWater**|*O3EComplexType*|24||ro||
|**566**|**EnergyConsumptionCooling**|*O3EComplexType*|24||ro||
|**567**|**GeneratedElectricity**|*O3EComplexType*|24||ro||
|**568**|**CoTwoSavings**|RawCodec|24||ro||
|**569**|**ResetSensorMinMaxAverageStatistics**|O3EByteVal|1||ro||
|**570**|**ResetStatistics**|RawCodec|1||ro||
|**572**|**SetDefaultValuesDate**|RawCodec|3||ro||
|**573**|**RemoteReset**|RawCodec|2||ro||
|**575**|**SetDeliveryStatus**|O3EByteVal|1||ro||
|**576**|**SetDeliveryStatusDate**|O3ESdate|3||ro||
|**580**|**SoftwareVersion**|O3ESoftVers|8||ro||
|**581**|**HardwareVersion**|O3ESoftVers|8||ro||
|**589**|**VentilationOperationHours**|O3EInt32|4||ro||
|**592**|**MacAddressLan**|O3EMacAddr|6||ro||
|**593**|**GatewayMac**|O3EMacAddr|6||ro||
|**596**|**CentralHeatingPartLoadPercent**|O3EByteVal|1||ro||
|**597**|**DomesticHotWaterPartLoadPercent**|O3EByteVal|1||ro||
|**600**|**FuelCellReset**|RawCodec|3||ro||
|**602**|**GatewayRemoteLocalNetworkStatus**|O3EByteVal|1||ro||
|**603**|**GatewayApEnable**|O3EByteVal|1||ro||
|**604**|**GatewayApDataSet**|*O3EComplexType*|76||ro||
|**607**|**GatewayRemoteIp**|*O3EComplexType*|20||ro||
|**609**|**ProxyServer**|RawCodec|40||ro||
|**610**|**ProxyPort**|RawCodec|2||ro||
|**611**|**ProxyUser**|O3EUtf8|40||ro||
|**613**|**ProxyEnabled**|O3EByteVal|1||ro||
|**616**|**GatewayRemoteEnable**|O3EByteVal|1||ro||
|**617**|**GatewayRemoteSsid**|O3EUtf8|72||ro||
|**618**|**GatewayRemoteIpStatic**|O3EByteVal|1||ro||
|**619**|**GatewayRemoteScanNetwork**|RawCodec|2||ro||
|**620**|**DiagnosticServiceConnectionStatus**|O3EByteVal|1||ro||
|**621**|**ObjectContactDetails**|*O3EComplexType*|181||ro||
|**622**|**CustomerDetails**|*O3EComplexType*|181||ro||
|**623**|**ServiceEngineer**|*O3EComplexType*|181||ro||
|**624**|**TechnicalSupport**|*O3EComplexType*|181||ro||
|**625**|**ObjectDetails**|*O3EComplexType*|26||ro||
|**627**|**CentralHeatingOneCircuitName**|O3EUtf8|40||ro||
|**627**|**CentralHeatingOneCircuitName**|O3EUtf8|12||ro||
|**628**|**CentralHeatingTwoCircuitName**|O3EUtf8|40||ro||
|**628**|**CentralHeatingTwoCircuitName**|O3EUtf8|12||ro||
|**629**|**CentralHeatingThreeCircuitName**|O3EUtf8|40||ro||
|**629**|**CentralHeatingThreeCircuitName**|O3EUtf8|12||ro||
|**630**|**CentralHeatingFourCircuitName**|O3EUtf8|40||ro||
|**630**|**CentralHeatingFourCircuitName**|O3EUtf8|12||ro||
|**631**|**CentralHeatingFiveCircuitName**|O3EUtf8|12||ro||
|**632**|**CentralHeatingSixCircuitName**|O3EUtf8|12||ro||
|**633**|**CentralHeatingSevenCircuitName**|O3EUtf8|12||ro||
|**634**|**CentralHeatingEightCircuitName**|O3EUtf8|12||ro||
|**645**|**GenericAnalogDigitalAccessoryOneModulFunction**|O3EByteVal|1||ro||
|**646**|**GenericAnalogDigitalAccessoryTwoModulFunction**|O3EByteVal|1||ro||
|**647**|**GenericAnalogDigitalAccessoryThreeModulFunction**|O3EByteVal|1||ro||
|**648**|**GenericAnalogDigitalAccessoryFourModulFunction**|O3EByteVal|1||ro||
|**649**|**GenericAnalogDigitalAccessoryFiveModulFunction**|O3EByteVal|1||ro||
|**650**|**GenericDigitalAccessoryOneModulFunction**|O3EByteVal|1||ro||
|**651**|**GenericDigitalAccessoryTwoModulFunction**|O3EByteVal|1||ro||
|**652**|**GenericDigitalAccessoryThreeModulFunction**|O3EByteVal|1||ro||
|**653**|**GenericDigitalAccessoryFourModulFunction**|O3EByteVal|1||ro||
|**654**|**GenericDigitalAccessoryFiveModulFunction**|O3EByteVal|1||ro||
|**680**|**EnergyMeter**|RawCodec|123||ro||
|**691**|**DomesticHotWaterTimeScheduleMonday**|*O3EList*|57||**rw**||
|**692**|**DomesticHotWaterTimeScheduleTuesday**|*O3EList*|57||**rw**||
|**693**|**DomesticHotWaterTimeScheduleWednesday**|*O3EList*|57||**rw**||
|**694**|**DomesticHotWaterTimeScheduleThursday**|*O3EList*|57||**rw**||
|**695**|**DomesticHotWaterTimeScheduleFriday**|*O3EList*|57||**rw**||
|**696**|**DomesticHotWaterTimeScheduleSaturday**|*O3EList*|57||**rw**||
|**697**|**DomesticHotWaterTimeScheduleSunday**|*O3EList*|57||**rw**||
|**726**|**DomesticHotWaterCirculationTimeScheduleMonday**|*O3EList*|57||**rw**||
|**727**|**DomesticHotWaterCirculationTimeScheduleTuesday**|*O3EList*|57||**rw**||
|**728**|**DomesticHotWaterCirculationTimeScheduleWednesday**|*O3EList*|57||**rw**||
|**729**|**DomesticHotWaterCirculationTimeScheduleThursday**|*O3EList*|57||**rw**||
|**730**|**DomesticHotWaterCirculationTimeScheduleFriday**|*O3EList*|57||**rw**||
|**731**|**DomesticHotWaterCirculationTimeScheduleSaturday**|*O3EList*|57||**rw**||
|**732**|**DomesticHotWaterCirculationTimeScheduleSunday**|*O3EList*|57||**rw**||
|**761**|**MixerOneCircuitTimeScheduleMonday**|*O3EList*|57||**rw**||
|**762**|**MixerOneCircuitTimeScheduleTuesday**|*O3EList*|57||**rw**||
|**763**|**MixerOneCircuitTimeScheduleWednesday**|*O3EList*|57||**rw**||
|**764**|**MixerOneCircuitTimeScheduleThursday**|*O3EList*|57||**rw**||
|**765**|**MixerOneCircuitTimeScheduleFriday**|*O3EList*|57||**rw**||
|**766**|**MixerOneCircuitTimeScheduleSaturday**|*O3EList*|57||**rw**||
|**767**|**MixerOneCircuitTimeScheduleSunday**|*O3EList*|57||**rw**||
|**768**|**MixerTwoCircuitTimeScheduleMonday**|*O3EList*|57||**rw**||
|**769**|**MixerTwoCircuitTimeScheduleTuesday**|*O3EList*|57||**rw**||
|**770**|**MixerTwoCircuitTimeScheduleWednesday**|*O3EList*|57||**rw**||
|**771**|**MixerTwoCircuitTimeScheduleThursday**|*O3EList*|57||**rw**||
|**772**|**MixerTwoCircuitTimeScheduleFriday**|*O3EList*|57||**rw**||
|**773**|**MixerTwoCircuitTimeScheduleSaturday**|*O3EList*|57||**rw**||
|**774**|**MixerTwoCircuitTimeScheduleSunday**|*O3EList*|57||**rw**||
|**775**|**MixerThreeCircuitTimeScheduleMonday**|*O3EList*|57||**rw**||
|**776**|**MixerThreeCircuitTimeScheduleTuesday**|*O3EList*|57||**rw**||
|**777**|**MixerThreeCircuitTimeScheduleWednesday**|*O3EList*|57||**rw**||
|**778**|**MixerThreeCircuitTimeScheduleThursday**|*O3EList*|57||**rw**||
|**779**|**MixerThreeCircuitTimeScheduleFriday**|*O3EList*|57||**rw**||
|**780**|**MixerThreeCircuitTimeScheduleSaturday**|*O3EList*|57||**rw**||
|**781**|**MixerThreeCircuitTimeScheduleSunday**|*O3EList*|57||**rw**||
|**782**|**MixerFourCircuitTimeScheduleMonday**|*O3EList*|57||**rw**||
|**783**|**MixerFourCircuitTimeScheduleTuesday**|*O3EList*|57||**rw**||
|**784**|**MixerFourCircuitTimeScheduleWednesday**|*O3EList*|57||**rw**||
|**785**|**MixerFourCircuitTimeScheduleThursday**|*O3EList*|57||**rw**||
|**786**|**MixerFourCircuitTimeScheduleFriday**|*O3EList*|57||**rw**||
|**787**|**MixerFourCircuitTimeScheduleSaturday**|*O3EList*|57||**rw**||
|**788**|**MixerFourCircuitTimeScheduleSunday**|*O3EList*|57||**rw**||
|**873**|**LegionellaProtectionActivation**|*O3EComplexType*|2||ro||
|**874**|**LegionellaProtectionTargetTemperatureSetpoint**|*O3EComplexType*|3||**rw**||
|**875**|**LegionellaProtectionStartTime**|O3EStime|2||ro||
|**876**|**LegionellaProtectionWeekday**|O3EByteVal|1||ro||
|**877**|**LegionellaProtectionLastSuccessfulStartTime**|O3EStime|3||ro||
|**878**|**LegionellaProtectionLastSuccessfulWeekday**|O3EByteVal|1||ro||
|**880**|**MixerOneCircuitCentralHeatingCurve**|*O3EComplexType*|4||ro||
|**881**|**MixerTwoCircuitCentralHeatingCurve**|*O3EComplexType*|4||ro||
|**882**|**MixerThreeCircuitCentralHeatingCurve**|*O3EComplexType*|4||ro||
|**883**|**MixerFourCircuitCentralHeatingCurve**|*O3EComplexType*|4||ro||
|**884**|**MixerFiveCircuitCentralHeatingCurve**|*O3EComplexType*|4||ro||
|**885**|**MixerSixCircuitCentralHeatingCurve**|*O3EComplexType*|4||ro||
|**886**|**MixerSevenCircuitCentralHeatingCurve**|*O3EComplexType*|4||ro||
|**887**|**MixerEightCircuitCentralHeatingCurve**|*O3EComplexType*|4||ro||
|**896**|**OutsideTemperatureOffset**|O3EInt16|2||**rw**||
|**897**|**ScreedDryingProfileActivation**|O3EByteVal|1||ro||
|**898**|**RemainingFloorDryingDays**|O3EByteVal|1||ro||
|**900**|**GatewayRemoteSignalStrength**|O3EByteVal|1||ro||
|**901**|**ServiceManagerIsRequired**|O3EByteVal|1||ro||
|**902**|[**MalfunctionIdentification**](## "Indicates whether faults are present")|O3EByteVal|1||ro||
|**903**|**DisplaySettings**|RawCodec|4||ro||
|**905**|**ElectricalPostHeater**|RawCodec|4||ro||
|**906**|**ExhaustFlap**|RawCodec|3||ro||
|**907**|**UserInterfaceDefaultHomeScreen**|O3EByteVal|1||ro||
|**908**|**ExternalFaultSignal**|O3EByteVal|1||ro||
|**909**|**ExternalFaultSignalInput**|O3EByteVal|1||ro||
|**912**|**DaylightSavingTimeActive**|RawCodec|5||ro||
|**915**|**LastBackupDate**|O3ESdate|3||ro||
|**917**|**RemoteWeatherService**|RawCodec|20||ro||
|**918**|**TradeFairMode**|O3EByteVal|1||ro||
|**919**|**OutsideTemperatureDampingFactor**|O3EInt16|2||ro||
|**920**|**ThreeAxisAccelerationSensor**|RawCodec|36||ro||
|**921**|**ExternalAccessInProgress**|*O3EComplexType*|2||ro||
|**922**|**ProductionTraceabilityByte**|O3EInt16|2||ro||
|**923**|**RealTimeClockStatus**|RawCodec|8||ro||
|**924**|**StartUpWizard**|O3EByteVal|1||ro||
|**925**|**FillingVenting**|RawCodec|5||ro||
|**927**|[**BuildingType**](## "Type of building {0: OneFamily, 1: MultiFamilyOnlyHeating, 2: MultiFamilyHeatingDomesticHotWater, 3: TownHouse}")|O3EEnum|1||ro||
|**928**|**ElectronicTraceabilityNumber**|O3EUtf8|16||ro||
|**929**|[**GasType**](## "{1: LLGas, 2: EGas, 3: LiquidGas}")|O3EEnum|1||ro||
|**930**|**ExternalTargetCentralHeatingFlowSetpointMetaData**|RawCodec|10||**rw**||
|**931**|**DomesticHotWaterFlowSetpointMetaData**|RawCodec|10||**rw**||
|**933**|**MixerOneCircuitProperty**|*O3EComplexType*|9||ro||
|**934**|**MixerTwoCircuitProperty**|*O3EComplexType*|9||ro||
|**935**|**MixerThreeCircuitProperty**|*O3EComplexType*|9||ro||
|**936**|**MixerFourCircuitProperty**|*O3EComplexType*|9||ro||
|**937**|**MixerFiveCircuitProperty**|*O3EComplexType*|9||ro||
|**938**|**MixerSixCircuitProperty**|*O3EComplexType*|9||ro||
|**939**|**MixerSevenCircuitProperty**|*O3EComplexType*|9||ro||
|**940**|**MixerEightCircuitProperty**|*O3EComplexType*|9||ro||
|**950**|**SolarCircuitWaterFlowRate**|*O3EComplexType*|4||ro||
|**951**|**SolarCircuitExtendedFunctions**|RawCodec|8||ro||
|**952**|**HydraulicMatrix**|RawCodec|51||ro||
|**953**|**SolarEnergyYield**|RawCodec|24||ro||
|**954**|[**BusTopologyMatrix**](## "Matrix of CAN bus topology")|*O3EList*|181||ro||
|**960**|**ExhaustPipeType**|O3EByteVal|1||ro||
|**961**|**SecurityAlgorithmNumber**|RawCodec|2||ro||
|**962**|**BootLoaderVersion**|O3ESoftVers|8||ro||
|**963**|**SparePartNumber**|O3EUtf8|16||ro||
|**964**|[**ActiveDiagnosticSession**](## "{0: NotSet, 1: Default, 2: ProgrammingSession, 3: ExtendedDiagnosticSession, 4: SafetySystemDiagnosticSession, 64: ManufacturerProgramming, 65: ManufacturerDiagnostic, 96: SystemSupplier(VEG)Programming, 97: SystemSupplier(VEG)Diagnostic}")|O3EEnum|1||ro||
|**987**|[**MixerOneCircuitFlowTemperatureTargetSetpoint**](## "Temperature setpoint heating curcuit 1")|O3EInt16|2|[°C](## "°C or °F (system configuration)")|**rw**||
|**988**|[**MixerTwoCircuitFlowTemperatureTargetSetpoint**](## "Temperature setpoint heating curcuit 2")|O3EInt16|2|[°C](## "°C or °F (system configuration)")|**rw**||
|**989**|[**MixerThreeCircuitFlowTemperatureTargetSetpoint**](## "Temperature setpoint heating curcuit 3")|O3EInt16|2|[°C](## "°C or °F (system configuration)")|**rw**||
|**990**|[**MixerFourCircuitFlowTemperatureTargetSetpoint**](## "Temperature setpoint heating curcuit 4")|O3EInt16|2|[°C](## "°C or °F (system configuration)")|**rw**||
|**1004**|[**CentralHeatingRegulationMode**](## "{0: Nothing, 1: ConstantControlled, 4: WeatherByOutsideSensorControlled, 7: WeatherByOutsideSensorAndRoomCorrectionControlled, 10: ConstantControlledWithExternalThermostat, 13: WeatherByOutsideAndZones, 15: WeatherByOutsideSensorAndAutomaticAdaptationControlled}")|O3EEnum|1||ro||
|**1006**|[**TargetQuickMode**](## "External request for one-time charging of domestic hot water (0: off, 2: one-time request)")|*O3EComplexType*|4||**rw**|[Link](https://github.com/open3e/open3e/discussions/318)|
|**1006**|[**TargetQuickMode**](## "External request for one-time charging of domestic hot water (0: off, 2: one-time request)")|*O3EComplexType*|3||**rw**|[Link](https://github.com/open3e/open3e/discussions/318)|
|**1007**|[**CurrentQuickMode**](## "State of external request for one-time charging of domestic hot water (0: off, 2: on)")|*O3EComplexType*|4||ro|[Link](https://github.com/open3e/open3e/discussions/318)|
|**1007**|[**CurrentQuickMode**](## "State of external request for one-time charging of domestic hot water (0: off, 2: on)")|*O3EComplexType*|3||ro|[Link](https://github.com/open3e/open3e/discussions/318)|
|**1008**|**MixerOneCircuitTargetQuickMode**|RawCodec|4||**rw**||
|**1008**|**MixerOneCircuitTargetQuickMode**|*O3EComplexType*|3||**rw**||
|**1009**|**MixerTwoCircuitTargetQuickMode**|RawCodec|4||**rw**||
|**1009**|**MixerTwoCircuitTargetQuickMode**|*O3EComplexType*|3||**rw**||
|**1010**|**MixerThreeCircuitTargetQuickMode**|RawCodec|4||**rw**||
|**1010**|**MixerThreeCircuitTargetQuickMode**|*O3EComplexType*|3||**rw**||
|**1011**|**MixerFourCircuitTargetQuickMode**|RawCodec|4||**rw**||
|**1011**|**MixerFourCircuitTargetQuickMode**|*O3EComplexType*|3||**rw**||
|**1024**|**MixerOneCircuitCurrentQuickMode**|RawCodec|4||ro||
|**1024**|**MixerOneCircuitCurrentQuickMode**|*O3EComplexType*|3||ro||
|**1025**|**MixerTwoCircuitCurrentQuickMode**|RawCodec|4||ro||
|**1025**|**MixerTwoCircuitCurrentQuickMode**|*O3EComplexType*|3||ro||
|**1026**|**MixerThreeCircuitCurrentQuickMode**|RawCodec|4||ro||
|**1026**|**MixerThreeCircuitCurrentQuickMode**|*O3EComplexType*|3||ro||
|**1027**|**MixerFourCircuitCurrentQuickMode**|RawCodec|4||ro||
|**1027**|**MixerFourCircuitCurrentQuickMode**|*O3EComplexType*|3||ro||
|**1040**|**SupplyAirFan**|*O3EComplexType*|6||ro||
|**1041**|**ExhaustAirFan**|*O3EComplexType*|6||ro||
|**1042**|**PrimaryHeatExchangerTemperatureSensor**|RawCodec|9||ro||
|**1043**|[**AllengraSensor**](## "Flow rate and temperature in the primary circuit of the heat generator")|*O3EComplexType*|5||ro|[Link](https://github.com/open3e/open3e/wiki/036-DoI-%E2%80%90-Data-points-of-Interest/#data-points-of-vitocal-250)|
|**1044**|**SecondaryCentralHeatingPump**|RawCodec|2||ro||
|**1047**|**TimeSeriesRecordedFlowTemperatureSensor**|RawCodec|11||ro||
|**1084**|**FlowTemperatureMinimumMaximumLimit**|RawCodec|4||**rw**||
|**1085**|**DomesticHotWaterHysteresis**|*O3EComplexType*|4||ro||
|**1087**|**MaximumDomesticHotWaterLoadingTime**|*O3EComplexType*|2||ro||
|**1088**|**OutsideAirBypass**|O3EByteVal|1||ro||
|**1089**|**InsideAirBypass**|O3EByteVal|1||ro||
|**1090**|**EnvironmentAirQuality**|RawCodec|9||ro||
|**1093**|**ExhaustPipeLength**|RawCodec|2||ro||
|**1096**|**ResetEnergyManagerDataCollector**|O3EByteVal|1||ro||
|**1097**|**ElectricityPrice**|*O3EComplexType*|20||ro||
|**1098**|**GasProperties**|*O3EComplexType*|20||ro||
|**1100**|**CentralHeatingPumpMinimumMaximumLimit**|*O3EComplexType*|3||**rw**||
|**1101**|**DomesticHotWaterPumpMinimumMaximumLimit**|*O3EComplexType*|3||**rw**||
|**1102**|**MixerOneCircuitPumpMinimumMaximumLimit**|*O3EComplexType*|3||**rw**||
|**1103**|**MixerTwoCircuitPumpMinimumMaximumLimit**|*O3EComplexType*|3||**rw**||
|**1104**|**MixerThreeCircuitPumpMinimumMaximumLimit**|*O3EComplexType*|3||**rw**||
|**1105**|**MixerFourCircuitPumpMinimumMaximumLimit**|*O3EComplexType*|3||**rw**||
|**1118**|**SolarCircuitPumpMinimumMaximumLimit**|*O3EComplexType*|3||**rw**||
|**1125**|**SolarMaximumLoadingTemperature**|O3EInt16|2||ro||
|**1128**|**SolarStagnationHours**|O3EInt16|2||ro||
|**1132**|**ViessmannIdentificationNumberListInternal**|*O3EComplexType*|97||ro||
|**1136**|**SolarProperty**|RawCodec|4||ro||
|**1137**|**ServiceModeActivation**|O3EByteVal|1||ro||
|**1138**|**AccentLedBar**|RawCodec|1||ro||
|**1139**|**CentralHeatingCurveAdaptionParameter**|*O3EComplexType*|7||ro||
|**1165**|**BackendConnectionStatus**|O3EByteVal|1||ro||
|**1166**|**ResetDtcHistory**|RawCodec|5||ro||
|**1167**|**ExternalDomesticHotWaterTemperatureSetpoint**|O3EInt16|2||**rw**||
|**1172**|**SolarCircuitPumpStatistical**|RawCodec|14||ro||
|**1175**|**AcknowledgeInfoAlarmMessage**|O3EByteVal|1||ro||
|**1176**|**AcknowledgeWarningAlarmMessage**|O3EByteVal|1||ro||
|**1177**|**AcknowledgeServiceAlarmMessage**|O3EByteVal|1||ro||
|**1178**|**AcknowledgeErrorAlarmMessage**|O3EByteVal|1||ro||
|**1181**|**DisplayTestMode**|O3EInt8|1||ro||
|**1190**|[**ThermalPower**](## "Actual thermal power output of the system")|*O3EComplexType*|4||ro||
|**1191**|**FuelCellStatus**|RawCodec|1||ro||
|**1192**|**MixerOneCircuitFlowTemperatureMinimumMaximumLimit**|*O3EComplexType*|10||**rw**||
|**1193**|**MixerTwoCircuitFlowTemperatureMinimumMaximumLimit**|*O3EComplexType*|10||**rw**||
|**1194**|**MixerThreeCircuitFlowTemperatureMinimumMaximumLimit**|*O3EComplexType*|10||**rw**||
|**1195**|**MixerFourCircuitFlowTemperatureMinimumMaximumLimit**|*O3EComplexType*|10||**rw**||
|**1196**|**MixerFiveCircuitFlowTemperatureMinimumMaximumLimit**|*O3EComplexType*|10||**rw**||
|**1197**|**MixerSixCircuitFlowTemperatureMinimumMaximumLimit**|*O3EComplexType*|10||**rw**||
|**1198**|**MixerSevenCircuitFlowTemperatureMinimumMaximumLimit**|*O3EComplexType*|10||**rw**||
|**1199**|**MixerEightCircuitFlowTemperatureMinimumMaximumLimit**|*O3EComplexType*|10||**rw**||
|**1210**|**FuelCellStatistical**|RawCodec|13||ro||
|**1211**|**GeneratedCentralHeatingOutput**|*O3EComplexType*|24||ro||
|**1214**|**ElectricalPowerOutput**|O3EInt16|2||ro||
|**1215**|**FuelCellState**|RawCodec|1||ro||
|**1216**|**FuelCellStateTwo**|RawCodec|1||ro||
|**1217**|**FuelCellGenerationMode**|RawCodec|1||ro||
|**1218**|**FuelCellInstruction**|RawCodec|1||ro||
|**1220**|**FuelCellMode**|RawCodec|1||ro||
|**1221**|**FuelCellModeResult**|RawCodec|1||ro||
|**1222**|**FuelCellRunRequest**|RawCodec|1||ro||
|**1223**|**FuelCellRunRequestResult**|RawCodec|1||ro||
|**1224**|**FuelCellStopRequest**|RawCodec|1||ro||
|**1226**|**FuelCellProcessNumber**|RawCodec|1||ro||
|**1227**|**FuelCellRequestAction**|RawCodec|1||ro||
|**1228**|**FuelCellCompletionNotification**|RawCodec|1||ro||
|**1229**|**FuelCellGasTypeSetting**|RawCodec|1||ro||
|**1230**|**FuelCellCountrySetting**|RawCodec|1||ro||
|**1231**|**FuelCellPrimaryPump**|RawCodec|4||ro||
|**1232**|[**GenericDigitalInputConfigurationOnBoardOne**](## "{0: Nothing, 1: FaultSignal, 2: DhwCirculation, 3: FaultSignalAndLocked, 4: ExternalHeatDemand, 5: ExternalLocked, 6: ExternalThermostat, 7: RoomTemperatureLimiter, 8: CallForHeat, 9: SmartGridReadyInputOne, 10: SmartGridReadyInputTwo, 11: PowerSupplierLock, 12: ExternalCoolingDemand, 13: PrioritizedDemandDeactivationOtherCircuits, 14: LockCircuitOne, 15: LockCircuitTwo, 16: ExternalDemandAutomatic, 17: FanControl, 18: FanRpmControl, 19: DefrostHeaterControlOne, 20: DefrostHeaterControlTwo, 21: DayNigthOperation, 22: DayNigthOperationPlusDirectControlDigitalOutputOne, 23: PermanentHeating, 24: DirectControlDryContactOne, 25: DirectControlDryContactTwo, 26: DirectControlDryContactThree, 27: DirectControlDigitalOutputTwentyFourVolt}")|O3EEnum|1||ro||
|**1233**|**GatewayRemoteVisibleOneTwo**|RawCodec|68||ro||
|**1234**|**GatewayRemoteVisibleThreeFour**|RawCodec|68||ro||
|**1235**|**GatewayRemoteVisibleFiveSix**|RawCodec|68||ro||
|**1236**|**GatewayRemoteVisibleSevenEight**|RawCodec|68||ro||
|**1237**|**GatewayRemoteVisibleNineTen**|RawCodec|68||ro||
|**1238**|**AvailableActorSensorComponents**|RawCodec|31||ro||
|**1239**|**ActorSensorTest**|RawCodec|2||ro||
|**1240**|**CentralHeatingPumpMode**|O3EByteVal|1||ro||
|**1241**|**MixerOneCircuitPumpMode**|O3EByteVal|1||ro||
|**1242**|**MixerTwoCircuitPumpMode**|O3EByteVal|1||ro||
|**1243**|**MixerThreeCircuitPumpMode**|O3EByteVal|1||ro||
|**1244**|**MixerFourCircuitPumpMode**|O3EByteVal|1||ro||
|**1263**|**DiverterValveBoilerHydraulicTower**|RawCodec|2||ro||
|**1264**|**DiverterValveFuelCellHydraulicTower**|RawCodec|2||ro||
|**1265**|**FanTargetSpeedMeta**|RawCodec|8||**rw**||
|**1266**|**DiverterValveStatistical**|*O3EComplexType*|8||ro||
|**1286**|**BusTopologyMatrixTwo**|*O3EList*|181||ro||
|**1287**|**BusTopologyMatrixThree**|*O3EList*|181||ro||
|**1288**|**BusTopologyMatrixFour**|*O3EList*|181||ro||
|**1289**|**BusTopologyMatrixFive**|*O3EList*|181||ro||
|**1290**|**DomesticHotWaterShiftLoadPump**|RawCodec|4||ro||
|**1294**|[**EnergyConsumptionCentralHeatingMonthMatrix**](## "Energy Consumption Central Heating Per Month")|*O3EComplexType*|124||ro||
|**1311**|[**EnergyConsumptionDomesticHotWaterMonthMatrix**](## "Energy Consumption Domestic Hot Water Per Month")|*O3EComplexType*|124||ro||
|**1312**|[**EnergyConsumptionCoolingMonthMatrix**](## "Energy Consumption Cooling Per Month")|*O3EComplexType*|124||ro||
|**1313**|[**GeneratedElectricityMonthMatrix**](## "Generated Electricity Per Month")|*O3EComplexType*|124||ro||
|**1314**|[**SolarEnergyYieldMonthMatrix**](## "Solar Energy Yield Per Month")|*O3EComplexType*|124||ro||
|**1315**|[**GeneratedCentralHeatingOutputMonthMatrix**](## "Generated Central Heating Output Per Month")|*O3EComplexType*|124||ro||
|**1316**|[**EnergyConsumptionCentralHeatingYearMatrix**](## "Energy Consumption Central Heating Per Year")|*O3EComplexType*|96||ro||
|**1333**|[**EnergyConsumptionDomesticHotWaterYearMatrix**](## "Energy Consumption Domestic Hot Water Per Year")|*O3EComplexType*|96||ro||
|**1334**|[**EnergyConsumptionCoolingYearMatrix**](## "Energy Consumption Cooling Per Year")|*O3EComplexType*|96||ro||
|**1335**|[**GeneratedElectricityYearMatrix**](## "Generated Electricity Per Year")|*O3EComplexType*|96||ro||
|**1336**|[**SolarEnergyYieldYearMatrix**](## "Solar Energy Yield Per Month")|*O3EComplexType*|96||ro||
|**1337**|[**GeneratedCentralHeatingOutputYearMatrix**](## "Generated Central Heating Output Per Year")|*O3EComplexType*|96||ro||
|**1338**|**ScreedDryingProfileDefinition**|RawCodec|31||ro||
|**1339**|**MalfunctionHeatingUnitBlocked**|O3EByteVal|1||ro||
|**1340**|**FuelCellGeneratedHeatOutputMonthMatrix**|*O3EComplexType*|124||ro||
|**1341**|**FuelCellGeneratedHeatOutputYearMatrix**|*O3EComplexType*|96||ro||
|**1342**|**GasConsumptionCentralHeatingMonthMatrix**|*O3EComplexType*|124||ro||
|**1343**|**GasConsumptionCentralHeatingYearMatrix**|*O3EComplexType*|48||ro||
|**1344**|**GasConsumptionDomesticHotWaterMonthMatrix**|*O3EComplexType*|124||ro||
|**1345**|**GasConsumptionDomesticHotWaterYearMatrix**|*O3EComplexType*|48||ro||
|**1346**|**HeatEngineStatistical**|*O3EComplexType*|12||ro||
|**1347**|**ObjectElectricalEnergyStatus**|RawCodec|10||ro||
|**1348**|**FuelCellGasConsumption**|*O3EComplexType*|12||ro||
|**1349**|**FuelCellGasConsumptionMonthMatrix**|RawCodec|124||ro||
|**1350**|**FuelCellGasConsumptionYearMatrix**|RawCodec|48||ro||
|**1351**|**FeedInEnergy**|RawCodec|24||ro||
|**1352**|**FeedInEnergyMonthMatrix**|RawCodec|124||ro||
|**1353**|**FeedInEnergyYearMatrix**|RawCodec|96||ro||
|**1354**|**ProductionCoverageRate**|RawCodec|6||ro||
|**1355**|**ProductionCoverageRateMonthMatrix**|RawCodec|62||ro||
|**1356**|**ProductionCoverageRateYearMatrix**|RawCodec|24||ro||
|**1357**|**FuelCellOperationTime**|RawCodec|11||ro||
|**1358**|**FuelCellOperationTimeMonthMatrix**|RawCodec|124||ro||
|**1359**|**FuelCellOperationTimeYearMatrix**|RawCodec|48||ro||
|**1360**|**FuelCellRunTime**|RawCodec|11||ro||
|**1361**|**FuelCellRunTimeMonthMatrix**|RawCodec|124||ro||
|**1362**|**FuelCellRunTimeYearMatrix**|RawCodec|48||ro||
|**1363**|**FuelCellTargetOperationMode**|RawCodec|1||**rw**||
|**1364**|**GenericSdioAccessoryOneModulFunction**|O3EByteVal|1||ro||
|**1367**|**FuelCellThermalPower**|O3EInt16|2||ro||
|**1371**|**DemandCoverageRate**|RawCodec|6||ro||
|**1372**|**DemandCoverageRateMonthMatrix**|RawCodec|62||ro||
|**1373**|**DemandCoverageRateYearMatrix**|RawCodec|24||ro||
|**1383**|**FuelCellBreakdownRate**|RawCodec|11||ro||
|**1384**|**FuelCellBreakdownRateMonthMatrix**|RawCodec|124||ro||
|**1385**|**FuelCellBreakdownRateYearMatrix**|RawCodec|48||ro||
|**1389**|**CoTwoSavingsMonthMatrix**|RawCodec|124||ro||
|**1390**|**CoTwoSavingsYearMatrix**|RawCodec|96||ro||
|**1391**|[**GeneratedDomesticHotWaterOutput**](## "Generated Domestic Hot Water Output per specific period")|*O3EComplexType*|24||ro||
|**1392**|[**GeneratedDomesticHotWaterOutputMonthMatrix**](## "Generated Domestic Hot Water Output Per Month")|*O3EComplexType*|124||ro||
|**1393**|[**GeneratedDomesticHotWaterOutputYearMatrix**](## "Generated Domestic Hot Water Output Per Year")|*O3EComplexType*|96||ro||
|**1394**|**SolarChargingDomesticHotWaterSetpoint**|O3EInt16|2||**rw**||
|**1395**|**MixerOneCircuitSummerSavingTemperatureThreshold**|*O3EComplexType*|3||ro||
|**1396**|**MixerTwoCircuitSummerSavingTemperatureThreshold**|*O3EComplexType*|3||ro||
|**1397**|**MixerThreeCircuitSummerSavingTemperatureThreshold**|*O3EComplexType*|3||ro||
|**1398**|**MixerFourCircuitSummerSavingTemperatureThreshold**|*O3EComplexType*|3||ro||
|**1411**|**ResetServiceInterval**|O3EByteVal|1||ro||
|**1415**|[**MixerOneCircuitOperationState**](## "Heating curcuit 1: Operating Mode")|*O3EComplexType*|2||**rw**||
|**1416**|[**MixerTwoCircuitOperationState**](## "Heating curcuit 2: Operating Mode")|*O3EComplexType*|2||**rw**||
|**1417**|[**MixerThreeCircuitOperationState**](## "Heating curcuit 3: Operating Mode")|*O3EComplexType*|2||**rw**||
|**1418**|[**MixerFourCircuitOperationState**](## "Heating curcuit 4: Operating Mode")|*O3EComplexType*|2||**rw**||
|**1419**|[**MixerFiveCircuitOperationState**](## "Heating curcuit 5: Operating Mode")|*O3EComplexType*|2||**rw**||
|**1420**|[**MixerSixCircuitOperationState**](## "Heating curcuit 6: Operating Mode")|*O3EComplexType*|2||**rw**||
|**1421**|[**MixerSevenCircuitOperationState**](## "Heating curcuit 7: Operating Mode")|*O3EComplexType*|2||**rw**||
|**1422**|[**MixerEightCircuitOperationState**](## "Heating curcuit 8: Operating Mode")|*O3EComplexType*|2||**rw**||
|**1431**|**CarbonEmissionSettings**|RawCodec|8||ro||
|**1432**|**CentralHeatingPumpPerformance**|*O3EComplexType*|4||ro||
|**1434**|**ResetFuelCellStatistics**|RawCodec|1||ro||
|**1435**|**FluelCellFlowTemperatueSensor**|*O3EComplexType*|9||ro||
|**1436**|**FuelCellReturnTemperatureSensor**|*O3EComplexType*|9||ro||
|**1439**|**NoiseReductionTimeScheduleMonday**|RawCodec|41||**rw**||
|**1440**|**NoiseReductionTimeScheduleTuesday**|RawCodec|41||**rw**||
|**1441**|**NoiseReductionTimeScheduleWednesday**|RawCodec|41||**rw**||
|**1442**|**NoiseReductionTimeScheduleThursday**|RawCodec|41||**rw**||
|**1443**|**NoiseReductionTimeScheduleFriday**|RawCodec|41||**rw**||
|**1444**|**NoiseReductionTimeScheduleSaturday**|RawCodec|41||**rw**||
|**1445**|**NoiseReductionTimeScheduleSunday**|RawCodec|41||**rw**||
|**1451**|**ApplicationChecksum**|RawCodec|4||ro||
|**1467**|**SafetyRelevantRemoteUnlock**|RawCodec|2||ro||
|**1468**|**FuelCellGasPressure**|RawCodec|9||ro||
|**1469**|**SensorActuatorTestGroupHeatEngine**|RawCodec|31||ro||
|**1470**|**SensorActuatorTestGroupDomesticHotWater**|RawCodec|31||ro||
|**1471**|**SensorActuatorTestGroupFuelCell**|RawCodec|31||ro||
|**1472**|**SensorActuatorTestGroupHeatingCircuit**|RawCodec|31||ro||
|**1473**|**SensorActuatorTestGroupSolar**|RawCodec|31||ro||
|**1492**|**SolarCircuitPumpHysteresis**|RawCodec|4||ro||
|**1493**|**HeatEnginePerformanceStatistics**|*O3EComplexType*|16||ro||
|**1494**|**OemProductVersion**|O3ESoftVers|8||ro||
|**1503**|**MinimumLoadPercent**|RawCodec|1||ro||
|**1504**|[**TimeSettingSource**](## "{0: Local, 1: SuperordinateSystem, 2: NetworkTimeProtocol, 3: TCU}")|O3EEnum|1||ro||
|**1505**|**SolarStagnationTemperatureOffset**|RawCodec|2||**rw**||
|**1529**|**SolarRechargeSuppressionImpact**|O3EByteVal|1||ro||
|**1533**|**InstallationWizardInProgress**|RawCodec|2||ro||
|**1535**|**FlueGasSensorTestMode**|RawCodec|3||ro||
|**1536**|**PrimaryCircuitWaterFlowTestMode**|RawCodec|3||ro||
|**1537**|**ChimneySweeperTestMode**|RawCodec|3||ro||
|**1538**|**ZigbeeEnable**|O3EByteVal|1||ro||
|**1539**|**ZigbeeStatus**|O3EByteVal|1||ro||
|**1540**|**ZigbeeIdentification**|RawCodec|26||ro||
|**1541**|**LegionellaProtectionPump**|RawCodec|5||ro||
|**1549**|**HydraulicMatrixConfiguration**|RawCodec|97||ro||
|**1550**|**FunctionMatrix**|RawCodec|22||ro||
|**1551**|**FuelCellExternalControl**|RawCodec|1||ro||
|**1552**|**ElectricalEnergyStorageOperationState**|RawCodec|7||**rw**||
|**1553**|**ElectronicControlUnitOdxVersion**|RawCodec|6||ro||
|**1554**|**HeatingSupport**|RawCodec|2||ro||
|**1555**|**MixerOneCircuitFixedValueFlowTemperatureSetpoint**|RawCodec|6||**rw**||
|**1556**|**MixerTwoCircuitFixedValueFlowTemperatureSetpoint**|RawCodec|6||**rw**||
|**1557**|**MixerThreeCircuitFixedValueFlowTemperatureSetpoint**|RawCodec|6||**rw**||
|**1558**|**MixerFourCircuitFixedValueFlowTemperatureSetpoint**|RawCodec|6||**rw**||
|**1559**|**MixerFiveCircuitFixedValueFlowTemperatureSetpoint**|RawCodec|6||**rw**||
|**1560**|**MixerSixCircuitFixedValueFlowTemperatureSetpoint**|RawCodec|6||**rw**||
|**1561**|**MixerSevenCircuitFixedValueFlowTemperatureSetpoint**|RawCodec|6||**rw**||
|**1562**|**MixerEightCircuitFixedValueFlowTemperatureSetpoint**|RawCodec|6||**rw**||
|**1573**|**SystemReturnTemperatureSensor**|*O3EComplexType*|9||ro||
|**1577**|**ElectricalEnergyStorageModuleOneOperatingData**|RawCodec|139||ro||
|**1578**|**ElectricalEnergyStorageModuleTwoOperatingData**|RawCodec|139||ro||
|**1579**|**ElectricalEnergyStorageModuleThreeOperatingData**|RawCodec|139||ro||
|**1580**|**ElectricalEnergyStorageModuleFourOperatingData**|RawCodec|139||ro||
|**1581**|**ElectricalEnergyStorageModuleFiveOperatingData**|RawCodec|139||ro||
|**1582**|**ElectricalEnergyStorageModuleSixOperatingData**|RawCodec|139||ro||
|**1585**|**IncreasedReturnTemperatureSetpoint**|RawCodec|2||**rw**||
|**1587**|**ExternalAlternatingCurrentPowerSetpointMetaData**|RawCodec|4||**rw**||
|**1588**|**AlternatingCurrentPowerSetpoint**|RawCodec|4||**rw**||
|**1589**|**AlternatingCurrentPowerSetpointMetaData**|RawCodec|4||**rw**||
|**1590**|**ElectricalEnergySystemOperationState**|RawCodec|6||**rw**||
|**1591**|**ElectricalEnergyInverterOperationState**|RawCodec|6||**rw**||
|**1592**|**ElectricalEnergyInverterPath**|RawCodec|1||ro||
|**1593**|**BufferHysteresis**|RawCodec|4||ro||
|**1594**|**LastApplicationUpdate**|O3ESdate|3||ro||
|**1595**|**ParameterIdentificationVersionFactory**|RawCodec|8||ro||
|**1596**|**IncreasedReturnTemperatureSensor**|*O3EComplexType*|9||ro||
|**1598**|**SolarStaticTemperatureControlHysteresis**|RawCodec|4||ro||
|**1599**|**SolarSecondaryDeltaTemperatureHysteresis**|RawCodec|4||ro||
|**1600**|**BufferDischargeFunctionThreeWayValvePositionPercent**|RawCodec|2||ro||
|**1601**|**FuelCellCondition**|RawCodec|1||ro||
|**1603**|[**PointOfCommonCouplingPower**](## "Actual Power at Point of Common Coupling")|*O3EComplexType*|4||ro|[Link](https://github.com/open3e/open3e/wiki/036-DoI-%E2%80%90-Data-points-of-Interest/#data-points-of-vx3)|
|**1603**|[**PointOfCommonCouplingPower**](## "Actual Power at Point of Common Coupling")|*O3EComplexType*|12||ro||
|**1604**|**GatewayExternalTargetFlowTemperatureSetpoint**|RawCodec|2||**rw**||
|**1605**|**GatewayExternalHeatEngineTargetOperationMode**|*O3EComplexType*|2||**rw**||
|**1606**|**IntervalStrategyProperties**|*O3EComplexType*|8||ro||
|**1607**|**MalfunctionUnitBlocked**|O3EByteVal|1||ro||
|**1608**|**DifferentialTemperatureControllerHeatSourceTemperatureSensor**|*O3EComplexType*|9||ro||
|**1609**|**DifferentialTemperatureControllerHeatSinkTemperatureSensor**|*O3EComplexType*|9||ro||
|**1610**|**HeatingSupportBufferTemperatureSensor**|*O3EComplexType*|9||ro||
|**1611**|**PreheatingReferenceTemperatureSensor**|*O3EComplexType*|9||ro||
|**1612**|**ExternalMixerTwoCircuitTargetOperationMode**|*O3EComplexType*|2||**rw**||
|**1613**|**ExternalMixerThreeCircuitTargetOperationMode**|*O3EComplexType*|2||**rw**||
|**1614**|**ExternalMixerFourCircuitTargetOperationMode**|*O3EComplexType*|2||**rw**||
|**1627**|**ExternalMixerOneCircuitFixedValueTargetTemperatureSetpoint**|O3EInt16|2||**rw**||
|**1628**|**ExternalMixerTwoCircuitFixedValueTargetTemperatureSetpoint**|O3EInt16|2||**rw**||
|**1629**|**ExternalMixerThreeCircuitFixedValueTargetTemperatureSetpoint**|O3EInt16|2||**rw**||
|**1630**|**ExternalMixerFourCircuitFixedValueTargetTemperatureSetpoint**|O3EInt16|2||**rw**||
|**1643**|[**MixerOneCircuitCurrentTemperatureSetpoint**](## "Heating Circuit 1: Flow or Room Temperature Setpoint")|O3EInt16|2|[°C](## "°C or °F (system configuration)")|**rw**||
|**1644**|[**MixerTwoCircuitCurrentTemperatureSetpoint**](## "Heating Circuit 2: Flow or Room Temperature Setpoint")|O3EInt16|2|[°C](## "°C or °F (system configuration)")|**rw**||
|**1645**|[**MixerThreeCircuitCurrentTemperatureSetpoint**](## "Heating Circuit 3: Flow or Room Temperature Setpoint")|O3EInt16|2|[°C](## "°C or °F (system configuration)")|**rw**||
|**1646**|[**MixerFourCircuitCurrentTemperatureSetpoint**](## "Heating Circuit 4: Flow or Room Temperature Setpoint")|O3EInt16|2|[°C](## "°C or °F (system configuration)")|**rw**||
|**1659**|[**EndResultDomesticHotWaterTemperatureSetpoint**](## "Resulting Setpoint for and Actual State of Domestic Hot Water Preparation (probably READ ONLY)")|*O3EComplexType*|3||ro|[Link](https://github.com/open3e/open3e/discussions/214)|
|**1660**|**SupportedFeatures**|RawCodec|16||ro||
|**1661**|**SolarSecondaryTransferPump**|RawCodec|5||ro||
|**1662**|**HeatingSupportBufferThreeWayValvePositionPercent**|RawCodec|2||ro||
|**1663**|**TestStatus**|RawCodec|41||ro||
|**1664**|[**ElectricalEnergyStorageStateOfCharge**](## "SoC of Battery")|O3EInt8|1|%|ro|[Link](https://github.com/open3e/open3e/wiki/036-DoI-%E2%80%90-Data-points-of-Interest/#data-points-of-vx3)|
|**1667**|**MixerOneCircuitPumpOscillationTime**|RawCodec|2||ro||
|**1668**|**MixerTwoCircuitPumpOscillationTime**|RawCodec|2||ro||
|**1669**|**MixerThreeCircuitPumpOscillationTime**|RawCodec|2||ro||
|**1670**|**MixerFourCircuitPumpOscillationTime**|RawCodec|2||ro||
|**1684**|[**AmbientTemperatureSensor**](## "Actual Ambient Temperature")|*O3EComplexType*|9||ro||
|**1685**|**ElectricalEnergyInverterDCConfiguration**|RawCodec|3||ro||
|**1686**|**ElectricalEnergySystemPhotovoltaicLimitation**|RawCodec|3||ro||
|**1687**|**ElectricalEnergySystemPhotovoltaicConfiguration**|O3EInt16|2||ro||
|**1690**|[**ElectricalEnergySystemPhotovoltaicStatus**](## "Actual Power of Photovoltaic")|*O3EComplexType*|17||ro|[Link](https://github.com/open3e/open3e/wiki/036-DoI-%E2%80%90-Data-points-of-Interest/#data-points-of-vx3)|
|**1691**|**BusTopologyScanStatus**|O3EByteVal|1||ro||
|**1692**|**PowerGridCodeConfiguration**|RawCodec|1||ro||
|**1693**|**GridOperatorConfigurationLock**|O3EByteVal|1||ro||
|**1694**|**GatewayEthernetEnable**|O3EByteVal|1||ro||
|**1695**|**GatewayEthernetConfig**|RawCodec|21||ro||
|**1696**|**GatewayEthernetIp**|RawCodec|20||ro||
|**1697**|**GatewayEthernetNetworkStatus**|O3EByteVal|1||ro||
|**1698**|**SupportedFeaturesTelemetryControlUnit**|RawCodec|16||ro||
|**1699**|**ActivatedFeaturesTelemetryControlUnit**|RawCodec|16||ro||
|**1700**|**EebusDeviceList**|RawCodec|104||ro||
|**1701**|**EebusOwnInfo**|RawCodec|104||ro||
|**1702**|**EebusPartnerInfo**|RawCodec|104||ro||
|**1703**|**EebusConnectionStatus**|RawCodec|1||ro||
|**1706**|**GenericMZIOAccessoryTwoModuleFunction**|RawCodec|1||ro||
|**1710**|**FunctionalSoftwareVersion**|O3ESoftVers|8||ro||
|**1718**|**ElectricalEnergySystemConfiguration**|*O3EComplexType*|2||ro||
|**1719**|**SolarIntervalFunction**|RawCodec|3||ro||
|**1721**|**WaterPressureConfiguration**|RawCodec|8||ro||
|**1728**|**ThermostatTerminalOneCircuitPump**|RawCodec|2||ro||
|**1729**|**ThermostatTerminalTwoCircuitPump**|RawCodec|2||ro||
|**1730**|**ThermostatTerminalThreeCircuitPump**|RawCodec|2||ro||
|**1731**|**ExternalLockActive**|O3EByteVal|1||ro||
|**1732**|**FixedRoomTemperatureSetpoint**|RawCodec|6||**rw**||
|**1749**|**TimeSeriesRecordedModulationCurrentValueStepsAndDurationOne**|RawCodec|176||ro||
|**1750**|**TimeSeriesRecordedModulationCurrentValueStepsAndDurationTwo**|RawCodec|176||ro||
|**1751**|**TimeSeriesRecordedModulationCurrentValueStepsAndDurationThree**|RawCodec|132||ro||
|**1752**|**TimeSeriesRecordedFlowTemperatureSensorStepsAndDurationOne**|RawCodec|176||ro||
|**1753**|**TimeSeriesRecordedFlowTemperatureSensorStepsAndDurationTwo**|RawCodec|176||ro||
|**1754**|**TimeSeriesRecordedFlowTemperatureSensorStepsAndDurationThree**|RawCodec|132||ro||
|**1759**|**TimeSeriesRecordedDomesticHotWaterOutletTemperature**|RawCodec|40||ro||
|**1760**|**TimeSeriesRecordedCombustionAirInletTemperature**|RawCodec|40||ro||
|**1761**|**TimeSeriesRecordedCentralHeatingPumpSpeed**|RawCodec|40||ro||
|**1762**|**LowWaterCutOffSignalInput**|RawCodec|1||ro||
|**1763**|**LowGasPressureSignalInput**|RawCodec|1||ro||
|**1764**|**HighGasPressureSignalInput**|RawCodec|1||ro||
|**1765**|**CombustionAirInterlock**|RawCodec|2||ro||
|**1766**|**ElectricalEnergyStorageModuleOperatingData**|RawCodec|141||ro||
|**1768**|**ReceiverTemperatureSensor**|*O3EComplexType*|9||ro||
|**1769**|[**PrimaryInletTemperatureSensor**](## "Temperature at Primary Inlet of Heat Pump")|*O3EComplexType*|9||ro|[Link](https://github.com/open3e/open3e/wiki/036-DoI-%E2%80%90-Data-points-of-Interest)|
|**1770**|**SecondaryOutletTemperatureSensor**|*O3EComplexType*|9||ro||
|**1771**|[**EngineRoomTemperatureSensor**](## "Actual Temperature at Engine Room")|*O3EComplexType*|9||ro||
|**1772**|[**CompressorOilTemperatureSensor**](## "Actual Compressor Oil Temperature")|*O3EComplexType*|9||ro|[Link](https://github.com/open3e/open3e/wiki/036-DoI-%E2%80%90-Data-points-of-Interest)|
|**1773**|**RefrigerantCircuitFourWayValve**|O3EByteVal|1||ro||
|**1774**|**CompressorCrankCaseHeater**|O3EByteVal|1||ro||
|**1775**|[**PrimaryCircuitFanOne**](## "Speed of Fan 1")|O3EByteVal|1|%|ro|[Link](https://github.com/open3e/open3e/wiki/036-DoI-%E2%80%90-Data-points-of-Interest)|
|**1776**|[**PrimaryCircuitFanTwo**](## "Speed of Fan 2")|O3EByteVal|1|%|ro|[Link](https://github.com/open3e/open3e/wiki/036-DoI-%E2%80%90-Data-points-of-Interest)|
|**1777**|**TimeSeriesRecordedFlueGasTemperatureSensorStepsAndDurationOne**|RawCodec|176||ro||
|**1778**|**TimeSeriesRecordedFlueGasTemperatureSensorStepsAndDurationTwo**|RawCodec|176||ro||
|**1779**|**TimeSeriesRecordedFlueGasTemperatureSensorStepsAndDurationThree**|RawCodec|132||ro||
|**1780**|**TimeSeriesRecordedIgnitionTimeSteps**|RawCodec|80||ro||
|**1781**|**TimeSeriesRecordedCalibrationCount**|RawCodec|16||ro||
|**1782**|**TimeSeriesRecordedMonitoringIonizationMaximum**|RawCodec|56||ro||
|**1783**|**TimeSeriesRecordedHeatingBurnerStopEvents**|RawCodec|120||ro||
|**1784**|**TimeSeriesRecordedDomesticHotWaterBurnerStopEvents**|RawCodec|120||ro||
|**1785**|**TimeSeriesRecordedFlameLossModulation**|RawCodec|40||ro||
|**1786**|**TimeSeriesRecordedWaterPressureStagnation**|RawCodec|52||ro||
|**1787**|**TimeSeriesRecordedWaterPressurePeaks**|RawCodec|32||ro||
|**1788**|**CanInterfaceVersion**|RawCodec|8||ro||
|**1791**|**DiverterValveDefaultPositionConfiguration**|O3EByteVal|1||ro||
|**1792**|**ResetElectricalEnergyHistory**|RawCodec|1||ro||
|**1793**|**BurnerPreconditions**|RawCodec|1||ro||
|**1794**|**HeatingCircuitHeatDeficit**|RawCodec|4||ro||
|**1795**|**FuelCellRuntimePrediction**|O3EInt8|1||ro||
|**1796**|**DomesticElectricalEnergyConsumption**|RawCodec|2||ro||
|**1797**|**PredictionDomesticElectricalEnergyConsumptionNextHour**|RawCodec|2||ro||
|**1798**|**FuelCellHoursTillNextStart**|O3EInt8|1||ro||
|**1799**|[**PrimaryCircuitCurrentTemperatureSetpoint**](## "Heating Circuit 1: Temperature Setpoint")|O3EInt16|2|[°C](## "°C or °F (system configuration)")|**rw**||
|**1800**|**ResetTimeSeriesRecordingGroups**|RawCodec|4||ro||
|**1801**|[**ElectricalEnergyStorageEnergyTransferStatistic**](## "Statistics of Transfered Electrical Energy")|*O3EComplexType*|40||ro|[Link](https://github.com/open3e/open3e/wiki/036-DoI-%E2%80%90-Data-points-of-Interest/#data-points-of-vx3)|
|**1802**|[**EnergyProductionPhotovoltaic**](## "Statistics of Photovoltaic Production")|*O3EComplexType*|80||ro|[Link](https://github.com/open3e/open3e/wiki/036-DoI-%E2%80%90-Data-points-of-Interest/#data-points-of-vx3)|
|**1807**|**ElectricalEnergyInverterDcInputOne**|RawCodec|10||ro||
|**1808**|**ElectricalEnergyInverterDcInputTwo**|RawCodec|10||ro||
|**1809**|**ElectricalEnergyInverterDcInputThree**|RawCodec|10||ro||
|**1810**|**ElectricalEnergyInverterPowerAc**|*O3EComplexType*|4||ro||
|**1811**|**ElectricalEnergyStorageModuleSetUpCheck**|RawCodec|1||ro||
|**1812**|**PointOfCommonCouplingConfiguredEnergyMeter**|RawCodec|2||ro||
|**1813**|**EnhancedVapourInjectionValve**|O3EInt8|1||ro||
|**1814**|**ReceiverLiquidLevelSensor**|RawCodec|5||ro||
|**1815**|**ElectricalHeaterPhaseOne**|O3EInt8|1||ro||
|**1816**|**ElectricalHeaterPhaseTwo**|O3EInt8|1||ro||
|**1817**|**ElectricalHeaterPhaseThree**|O3EInt8|1||ro||
|**1819**|**SolarPumpConfigurationSelection**|O3EByteVal|1||ro||
|**1822**|**ThreePhaseInverterCurrent**|RawCodec|51||ro||
|**1823**|**ThreePhaseInverterVoltage**|RawCodec|27||ro||
|**1824**|**ThreePhaseInverterCurrentPower**|*O3EComplexType*|16||ro||
|**1825**|**ThreePhaseInverterCurrentApparentPower**|*O3EComplexType*|16||ro||
|**1826**|**ThreePhaseInverterMaximunNominalPower**|*O3EComplexType*|4||ro||
|**1827**|[**InverterElectricalEnergyStorageMaximumNominalChargePower**](## "Nominal Electrical Power of Inverter for Charging")|*O3EComplexType*|4||ro||
|**1828**|[**InverterElectricalEnergyStorageCurrentMaximumlChargePower**](## "Maximum Electrical Power of Inverter for Charging")|*O3EComplexType*|4||ro||
|**1829**|[**InverterElectricalEnergyStorageMaximumNominalDischargePower**](## "Nominal Electrical Power of Inverter for Discharging")|*O3EComplexType*|4||ro||
|**1830**|[**InverterElectricalEnergyStorageCurrentMaximumlDishargePower**](## "Maximum Electrical Power of Inverter for Discharging")|*O3EComplexType*|4||ro||
|**1831**|[**PhotovoltaicCurrentStringPower**](## "Current Photovoltaic Power per String")|*O3EComplexType*|12||ro||
|**1832**|[**PhotovoltaicStringCurrent**](## "Current Photovoltaic Current per String (resolution is 1 Ampere)")|*O3EComplexType*|12||ro||
|**1833**|[**PhotovoltaicStringVoltage**](## "Current Photovoltaic Voltage per String")|*O3EComplexType*|12||ro|[Link](https://github.com/open3e/open3e/wiki/036-DoI-%E2%80%90-Data-points-of-Interest/#data-points-of-vx3)|
|**1834**|[**ElectricalEnergyStorageStateOfEnergy**](## "SoC of Battery")|*O3EComplexType*|4||ro||
|**1835**|**ManufacturerProperties**|RawCodec|20||ro||
|**1836**|[**ElectricalEnergyStorageCurrentPower**](## "Current Power for Battery Discharging (positive values) and Charging (negative values)")|O3EInt32|4|W|ro||
|**1837**|**ElectricalEnergyStorageCurrent**|*O3EComplexType*|4||ro||
|**1838**|**ElectricalEnergyStorageVoltage**|O3EInt16|2||ro||
|**1839**|**ElectricalEnergyStorageUsableEnergy**|RawCodec|4||ro||
|**1840**|**ElectricalEnergyStorageUsableNominalEnergy**|RawCodec|4||ro||
|**1841**|**PointOfCommonCouplingOverview**|RawCodec|32||ro||
|**1842**|[**SecondaryCircuitFourThreeWayValve**](## "Circuit 2: Position of Four Three Way Valve")|*O3EComplexType*|2||ro||
|**1843**|**MixerOneCircuitHumidityProtection**|RawCodec|2||ro||
|**1844**|**MixerTwoCircuitHumidityProtection**|RawCodec|2||ro||
|**1845**|**HeatPumpCompressorEnvelope**|RawCodec|36||ro||
|**1846**|**HeatPumpCompressorCurrentOperatingPoint**|RawCodec|4||ro||
|**1847**|**CustomerDetailsExtensions**|RawCodec|81||ro||
|**1848**|**ApartmentOneProperty**|RawCodec|27||ro||
|**1849**|**ApartmentOneSetpoints**|RawCodec|50||**rw**||
|**1850**|**ApartmentOneTimeScheduleMonday**|RawCodec|57||**rw**||
|**1851**|**ApartmentOneTimeScheduleTuesday**|RawCodec|57||**rw**||
|**1852**|**ApartmentOneTimeScheduleWednesday**|RawCodec|57||**rw**||
|**1853**|**ApartmentOneTimeScheduleThursday**|RawCodec|57||**rw**||
|**1854**|**ApartmentOneTimeScheduleFriday**|RawCodec|57||**rw**||
|**1855**|**ApartmentOneTimeScheduleSaturday**|RawCodec|57||**rw**||
|**1856**|**ApartmentOneTimeScheduleSunday**|RawCodec|57||**rw**||
|**1884**|**RoomOneProperty**|RawCodec|84||ro||
|**1884**|**RoomOneProperty**|*O3EComplexType*|85||ro||
|**1885**|**RoomOneSetpoints**|RawCodec|30||**rw**||
|**1886**|**RoomOneCurrentValues**|RawCodec|46||ro||
|**1887**|**RoomTwoProperty**|RawCodec|84||ro||
|**1887**|**RoomTwoProperty**|*O3EComplexType*|85||ro||
|**1888**|**RoomTwoSetpoints**|RawCodec|30||**rw**||
|**1889**|**RoomTwoCurrentValues**|RawCodec|46||ro||
|**1890**|**RoomThreeProperty**|RawCodec|84||ro||
|**1890**|**RoomThreeProperty**|*O3EComplexType*|85||ro||
|**1891**|**RoomThreeSetpoints**|RawCodec|30||**rw**||
|**1892**|**RoomThreeCurrentValues**|RawCodec|46||ro||
|**1893**|**RoomFourProperty**|RawCodec|84||ro||
|**1893**|**RoomFourProperty**|*O3EComplexType*|85||ro||
|**1894**|**RoomFourSetpoints**|RawCodec|30||**rw**||
|**1895**|**RoomFourCurrentValues**|RawCodec|46||ro||
|**1896**|**RoomFiveProperty**|RawCodec|84||ro||
|**1896**|**RoomFiveProperty**|*O3EComplexType*|85||ro||
|**1897**|**RoomFiveSetpoints**|RawCodec|30||**rw**||
|**1898**|**RoomFiveCurrentValues**|RawCodec|46||ro||
|**1899**|**RoomSixProperty**|RawCodec|84||ro||
|**1899**|**RoomSixProperty**|*O3EComplexType*|85||ro||
|**1900**|**RoomSixSetpoints**|RawCodec|30||**rw**||
|**1901**|**RoomSixCurrentValues**|RawCodec|46||ro||
|**1902**|**RoomSevenProperty**|RawCodec|84||ro||
|**1902**|**RoomSevenProperty**|*O3EComplexType*|85||ro||
|**1903**|**RoomSevenSetpoints**|RawCodec|30||**rw**||
|**1904**|**RoomSevenCurrentValues**|RawCodec|46||ro||
|**1905**|**RoomEightProperty**|RawCodec|84||ro||
|**1905**|**RoomEightProperty**|*O3EComplexType*|85||ro||
|**1906**|**RoomEightSetpoints**|RawCodec|30||**rw**||
|**1907**|**RoomEightCurrentValues**|RawCodec|46||ro||
|**1908**|**RoomNineProperty**|RawCodec|84||ro||
|**1908**|**RoomNineProperty**|*O3EComplexType*|85||ro||
|**1909**|**RoomNineSetpoints**|RawCodec|30||**rw**||
|**1910**|**RoomNineCurrentValues**|RawCodec|46||ro||
|**1911**|**RoomTenProperty**|RawCodec|84||ro||
|**1911**|**RoomTenProperty**|*O3EComplexType*|85||ro||
|**1912**|**RoomTenSetpoints**|RawCodec|30||**rw**||
|**1913**|**RoomTenCurrentValues**|RawCodec|46||ro||
|**1914**|**RoomElevenProperty**|RawCodec|84||ro||
|**1915**|**RoomElevenSetpoints**|RawCodec|30||**rw**||
|**1916**|**RoomElevenCurrentValues**|RawCodec|46||ro||
|**1917**|**RoomTwelveProperty**|RawCodec|84||ro||
|**1918**|**RoomTwelveSetpoints**|RawCodec|30||**rw**||
|**1919**|**RoomTwelveCurrentValues**|RawCodec|46||ro||
|**1920**|**RoomThirteenProperty**|RawCodec|84||ro||
|**1920**|**RoomThirteenProperty**|*O3EComplexType*|85||ro||
|**1921**|**RoomThirteenSetpoints**|RawCodec|30||**rw**||
|**1922**|**RoomThirteenCurrentValues**|RawCodec|46||ro||
|**1923**|**RoomFourteenProperty**|RawCodec|84||ro||
|**1923**|**RoomFourteenProperty**|*O3EComplexType*|85||ro||
|**1924**|**RoomFourteenSetpoints**|RawCodec|30||**rw**||
|**1925**|**RoomFourteenCurrentValues**|RawCodec|46||ro||
|**1926**|**RoomFifteenProperty**|RawCodec|84||ro||
|**1926**|**RoomFifteenProperty**|*O3EComplexType*|85||ro||
|**1927**|**RoomFifteenSetpoints**|RawCodec|30||**rw**||
|**1928**|**RoomFifteenCurrentValues**|RawCodec|46||ro||
|**1929**|**RoomSixteenProperty**|RawCodec|84||ro||
|**1929**|**RoomSixteenProperty**|*O3EComplexType*|85||ro||
|**1930**|**RoomSixteenSetpoints**|RawCodec|30||**rw**||
|**1931**|**RoomSixteenCurrentValues**|RawCodec|46||ro||
|**1932**|**RoomSeventeenProperty**|RawCodec|84||ro||
|**1932**|**RoomSeventeenProperty**|*O3EComplexType*|85||ro||
|**1933**|**RoomSeventeenSetpoints**|RawCodec|30||**rw**||
|**1934**|**RoomSeventeenCurrentValues**|RawCodec|46||ro||
|**1935**|**RoomEighteenProperty**|RawCodec|84||ro||
|**1935**|**RoomEightteenProperty**|*O3EComplexType*|85||ro||
|**1936**|**RoomEighteenSetpoints**|RawCodec|30||**rw**||
|**1937**|**RoomEighteenCurrentValues**|RawCodec|46||ro||
|**1938**|**RoomNineteenProperty**|RawCodec|84||ro||
|**1938**|**RoomNineteenProperty**|*O3EComplexType*|85||ro||
|**1939**|**RoomNineteenSetpoints**|RawCodec|30||**rw**||
|**1940**|**RoomNineteenCurrentValues**|RawCodec|46||ro||
|**1941**|**RoomTwentyProperty**|RawCodec|84||ro||
|**1941**|**RoomTwentyProperty**|*O3EComplexType*|85||ro||
|**1942**|**RoomTwentySetpoints**|RawCodec|30||**rw**||
|**1943**|**RoomTwentyCurrentValues**|RawCodec|46||ro||
|**1944**|**RoomOneTimeScheduleMonday**|RawCodec|57||**rw**||
|**1945**|**RoomOneTimeScheduleTuesday**|RawCodec|57||**rw**||
|**1946**|**RoomOneTimeScheduleWednesday**|RawCodec|57||**rw**||
|**1947**|**RoomOneTimeScheduleThursday**|RawCodec|57||**rw**||
|**1948**|**RoomOneTimeScheduleFriday**|RawCodec|57||**rw**||
|**1949**|**RoomOneTimeScheduleSaturday**|RawCodec|57||**rw**||
|**1950**|**RoomOneTimeScheduleSunday**|RawCodec|57||**rw**||
|**1951**|**RoomTwoTimeScheduleMonday**|RawCodec|57||**rw**||
|**1952**|**RoomTwoTimeScheduleTuesday**|RawCodec|57||**rw**||
|**1953**|**RoomTwoTimeScheduleWednesday**|RawCodec|57||**rw**||
|**1954**|**RoomTwoTimeScheduleThursday**|RawCodec|57||**rw**||
|**1955**|**RoomTwoTimeScheduleFriday**|RawCodec|57||**rw**||
|**1956**|**RoomTwoTimeScheduleSaturday**|RawCodec|57||**rw**||
|**1957**|**RoomTwoTimeScheduleSunday**|RawCodec|57||**rw**||
|**1958**|**RoomThreeTimeScheduleMonday**|RawCodec|57||**rw**||
|**1959**|**RoomThreeTimeScheduleTuesday**|RawCodec|57||**rw**||
|**1960**|**RoomThreeTimeScheduleWednesday**|RawCodec|57||**rw**||
|**1961**|**RoomThreeTimeScheduleThursday**|RawCodec|57||**rw**||
|**1962**|**RoomThreeTimeScheduleFriday**|RawCodec|57||**rw**||
|**1963**|**RoomThreeTimeScheduleSaturday**|RawCodec|57||**rw**||
|**1964**|**RoomThreeTimeScheduleSunday**|RawCodec|57||**rw**||
|**1965**|**RoomFourTimeScheduleMonday**|RawCodec|57||**rw**||
|**1966**|**RoomFourTimeScheduleTuesday**|RawCodec|57||**rw**||
|**1967**|**RoomFourTimeScheduleWednesday**|RawCodec|57||**rw**||
|**1968**|**RoomFourTimeScheduleThursday**|RawCodec|57||**rw**||
|**1969**|**RoomFourTimeScheduleFriday**|RawCodec|57||**rw**||
|**1970**|**RoomFourTimeScheduleSaturday**|RawCodec|57||**rw**||
|**1971**|**RoomFourTimeScheduleSunday**|RawCodec|57||**rw**||
|**1972**|**RoomFiveTimeScheduleMonday**|RawCodec|57||**rw**||
|**1973**|**RoomFiveTimeScheduleTuesday**|RawCodec|57||**rw**||
|**1974**|**RoomFiveTimeScheduleWednesday**|RawCodec|57||**rw**||
|**1975**|**RoomFiveTimeScheduleThursday**|RawCodec|57||**rw**||
|**1976**|**RoomFiveTimeScheduleFriday**|RawCodec|57||**rw**||
|**1977**|**RoomFiveTimeScheduleSaturday**|RawCodec|57||**rw**||
|**1978**|**RoomFiveTimeScheduleSunday**|RawCodec|57||**rw**||
|**1979**|**RoomSixTimeScheduleMonday**|RawCodec|57||**rw**||
|**1980**|**RoomSixTimeScheduleTuesday**|RawCodec|57||**rw**||
|**1981**|**RoomSixTimeScheduleWednesday**|RawCodec|57||**rw**||
|**1982**|**RoomSixTimeScheduleThursday**|RawCodec|57||**rw**||
|**1983**|**RoomSixTimeScheduleFriday**|RawCodec|57||**rw**||
|**1984**|**RoomSixTimeScheduleSaturday**|RawCodec|57||**rw**||
|**1985**|**RoomSixTimeScheduleSunday**|RawCodec|57||**rw**||
|**1986**|**RoomSevenTimeScheduleMonday**|RawCodec|57||**rw**||
|**1987**|**RoomSevenTimeScheduleTuesday**|RawCodec|57||**rw**||
|**1988**|**RoomSevenTimeScheduleWednesday**|RawCodec|57||**rw**||
|**1989**|**RoomSevenTimeScheduleThursday**|RawCodec|57||**rw**||
|**1990**|**RoomSevenTimeScheduleFriday**|RawCodec|57||**rw**||
|**1991**|**RoomSevenTimeScheduleSaturday**|RawCodec|57||**rw**||
|**1992**|**RoomSevenTimeScheduleSunday**|RawCodec|57||**rw**||
|**1993**|**RoomEightTimeScheduleMonday**|RawCodec|57||**rw**||
|**1994**|**RoomEightTimeScheduleTuesday**|RawCodec|57||**rw**||
|**1995**|**RoomEightTimeScheduleWednesday**|RawCodec|57||**rw**||
|**1996**|**RoomEightTimeScheduleThursday**|RawCodec|57||**rw**||
|**1997**|**RoomEightTimeScheduleFriday**|RawCodec|57||**rw**||
|**1998**|**RoomEightTimeScheduleSaturday**|RawCodec|57||**rw**||
|**1999**|**RoomEightTimeScheduleSunday**|RawCodec|57||**rw**||
|**2000**|**RoomNineTimeScheduleMonday**|RawCodec|57||**rw**||
|**2001**|**RoomNineTimeScheduleTuesday**|RawCodec|57||**rw**||
|**2002**|**RoomNineTimeScheduleWednesday**|RawCodec|57||**rw**||
|**2003**|**RoomNineTimeScheduleThursday**|RawCodec|57||**rw**||
|**2004**|**RoomNineTimeScheduleFriday**|RawCodec|57||**rw**||
|**2005**|**RoomNineTimeScheduleSaturday**|RawCodec|57||**rw**||
|**2006**|**RoomNineTimeScheduleSunday**|RawCodec|57||**rw**||
|**2007**|**RoomTenTimeScheduleMonday**|RawCodec|57||**rw**||
|**2008**|**RoomTenTimeScheduleTuesday**|RawCodec|57||**rw**||
|**2009**|**RoomTenTimeScheduleWednesday**|RawCodec|57||**rw**||
|**2010**|**RoomTenTimeScheduleThursday**|RawCodec|57||**rw**||
|**2011**|**RoomTenTimeScheduleFriday**|RawCodec|57||**rw**||
|**2012**|**RoomTenTimeScheduleSaturday**|RawCodec|57||**rw**||
|**2013**|**RoomTenTimeScheduleSunday**|RawCodec|57||**rw**||
|**2014**|**RoomElevenTimeScheduleMonday**|RawCodec|57||**rw**||
|**2015**|**RoomElevenTimeScheduleTuesday**|RawCodec|57||**rw**||
|**2016**|**RoomElevenTimeScheduleWednesday**|RawCodec|57||**rw**||
|**2017**|**RoomElevenTimeScheduleThursday**|RawCodec|57||**rw**||
|**2018**|**RoomElevenTimeScheduleFriday**|RawCodec|57||**rw**||
|**2019**|**RoomElevenTimeScheduleSaturday**|RawCodec|57||**rw**||
|**2020**|**RoomElevenTimeScheduleSunday**|RawCodec|57||**rw**||
|**2021**|**RoomTwelveTimeScheduleMonday**|RawCodec|57||**rw**||
|**2022**|**RoomTwelveTimeScheduleTuesday**|RawCodec|57||**rw**||
|**2023**|**RoomTwelveTimeScheduleWednesday**|RawCodec|57||**rw**||
|**2024**|**RoomTwelveTimeScheduleThursday**|RawCodec|57||**rw**||
|**2025**|**RoomTwelveTimeScheduleFriday**|RawCodec|57||**rw**||
|**2026**|**RoomTwelveTimeScheduleSaturday**|RawCodec|57||**rw**||
|**2027**|**RoomTwelveTimeScheduleSunday**|RawCodec|57||**rw**||
|**2028**|**RoomThirteenTimeScheduleMonday**|RawCodec|57||**rw**||
|**2029**|**RoomThirteenTimeScheduleTuesday**|RawCodec|57||**rw**||
|**2030**|**RoomThirteenTimeScheduleWednesday**|RawCodec|57||**rw**||
|**2031**|**RoomThirteenTimeScheduleThursday**|RawCodec|57||**rw**||
|**2032**|**RoomThirteenTimeScheduleFriday**|RawCodec|57||**rw**||
|**2033**|**RoomThirteenTimeScheduleSaturday**|RawCodec|57||**rw**||
|**2034**|**RoomThirteenTimeScheduleSunday**|RawCodec|57||**rw**||
|**2035**|**RoomFourteenTimeScheduleMonday**|RawCodec|57||**rw**||
|**2036**|**RoomFourteenTimeScheduleTuesday**|RawCodec|57||**rw**||
|**2037**|**RoomFourteenTimeScheduleWednesday**|RawCodec|57||**rw**||
|**2038**|**RoomFourteenTimeScheduleThursday**|RawCodec|57||**rw**||
|**2039**|**RoomFourteenTimeScheduleFriday**|RawCodec|57||**rw**||
|**2040**|**RoomFourteenTimeScheduleSaturday**|RawCodec|57||**rw**||
|**2041**|**RoomFourteenTimeScheduleSunday**|RawCodec|57||**rw**||
|**2042**|**RoomFifteenTimeScheduleMonday**|RawCodec|57||**rw**||
|**2043**|**RoomFifteenTimeScheduleTuesday**|RawCodec|57||**rw**||
|**2044**|**RoomFifteenTimeScheduleWednesday**|RawCodec|57||**rw**||
|**2045**|**RoomFifteenTimeScheduleThursday**|RawCodec|57||**rw**||
|**2046**|**RoomFifteenTimeScheduleFriday**|RawCodec|57||**rw**||
|**2047**|**RoomFifteenTimeScheduleSaturday**|RawCodec|57||**rw**||
|**2048**|**RoomFifteenTimeScheduleSunday**|RawCodec|57||**rw**||
|**2049**|**RoomSixteenTimeScheduleMonday**|RawCodec|57||**rw**||
|**2050**|**RoomSixteenTimeScheduleTuesday**|RawCodec|57||**rw**||
|**2051**|**RoomSixteenTimeScheduleWednesday**|RawCodec|57||**rw**||
|**2052**|**RoomSixteenTimeScheduleThursday**|RawCodec|57||**rw**||
|**2053**|**RoomSixteenTimeScheduleFriday**|RawCodec|57||**rw**||
|**2054**|**RoomSixteenTimeScheduleSaturday**|RawCodec|57||**rw**||
|**2055**|**RoomSixteenTimeScheduleSunday**|RawCodec|57||**rw**||
|**2056**|**RoomSeventeenTimeScheduleMonday**|RawCodec|57||**rw**||
|**2057**|**RoomSeventeenTimeScheduleTuesday**|RawCodec|57||**rw**||
|**2058**|**RoomSeventeenTimeScheduleWednesday**|RawCodec|57||**rw**||
|**2059**|**RoomSeventeenTimeScheduleThursday**|RawCodec|57||**rw**||
|**2060**|**RoomSeventeenTimeScheduleFriday**|RawCodec|57||**rw**||
|**2061**|**RoomSeventeenTimeScheduleSaturday**|RawCodec|57||**rw**||
|**2062**|**RoomSeventeenTimeScheduleSunday**|RawCodec|57||**rw**||
|**2063**|**RoomEighteenTimeScheduleMonday**|RawCodec|57||**rw**||
|**2064**|**RoomEighteenTimeScheduleTuesday**|RawCodec|57||**rw**||
|**2065**|**RoomEighteenTimeScheduleWednesday**|RawCodec|57||**rw**||
|**2066**|**RoomEighteenTimeScheduleThursday**|RawCodec|57||**rw**||
|**2067**|**RoomEighteenTimeScheduleFriday**|RawCodec|57||**rw**||
|**2068**|**RoomEighteenTimeScheduleSaturday**|RawCodec|57||**rw**||
|**2069**|**RoomEighteenTimeScheduleSunday**|RawCodec|57||**rw**||
|**2070**|**RoomNineteenTimeScheduleMonday**|RawCodec|57||**rw**||
|**2071**|**RoomNineteenTimeScheduleTuesday**|RawCodec|57||**rw**||
|**2072**|**RoomNineteenTimeScheduleWednesday**|RawCodec|57||**rw**||
|**2073**|**RoomNineteenTimeScheduleThursday**|RawCodec|57||**rw**||
|**2074**|**RoomNineteenTimeScheduleFriday**|RawCodec|57||**rw**||
|**2075**|**RoomNineteenTimeScheduleSaturday**|RawCodec|57||**rw**||
|**2076**|**RoomNineteenTimeScheduleSunday**|RawCodec|57||**rw**||
|**2077**|**RoomTwentyTimeScheduleMonday**|RawCodec|57||**rw**||
|**2078**|**RoomTwentyTimeScheduleTuesday**|RawCodec|57||**rw**||
|**2079**|**RoomTwentyTimeScheduleWednesday**|RawCodec|57||**rw**||
|**2080**|**RoomTwentyTimeScheduleThursday**|RawCodec|57||**rw**||
|**2081**|**RoomTwentyTimeScheduleFriday**|RawCodec|57||**rw**||
|**2082**|**RoomTwentyTimeScheduleSaturday**|RawCodec|57||**rw**||
|**2083**|**RoomTwentyTimeScheduleSunday**|RawCodec|57||**rw**||
|**2084**|**ZigBeeOneDeviceProperty**|*O3EComplexType*|84||ro||
|**2085**|**ZigBeeOneDeviceSetpoint**|*O3EComplexType*|13||**rw**||
|**2086**|**ZigBeeOneDeviceCurrentValues**|RawCodec|57||ro||
|**2086**|**ZigBeeOneDeviceCurrentValues**|*O3EComplexType*|68||ro||
|**2087**|**ZigBeeTwoDeviceProperty**|*O3EComplexType*|84||ro||
|**2088**|**ZigBeeTwoDeviceSetpoint**|*O3EComplexType*|13||**rw**||
|**2089**|**ZigBeeTwoDeviceCurrentValues**|RawCodec|57||ro||
|**2089**|**ZigBeeTwoDeviceCurrentValues**|*O3EComplexType*|68||ro||
|**2090**|**ZigBeeThreeDeviceProperty**|*O3EComplexType*|84||ro||
|**2091**|**ZigBeeThreeDeviceSetpoint**|*O3EComplexType*|13||**rw**||
|**2092**|**ZigBeeThreeDeviceCurrentValues**|RawCodec|57||ro||
|**2092**|**ZigBeeThreeDeviceCurrentValues**|*O3EComplexType*|68||ro||
|**2093**|**ZigBeeFourDeviceProperty**|*O3EComplexType*|84||ro||
|**2094**|**ZigBeeFourDeviceSetpoint**|*O3EComplexType*|13||**rw**||
|**2095**|**ZigBeeFourDeviceCurrentValues**|RawCodec|57||ro||
|**2095**|**ZigBeeFourDeviceCurrentValues**|*O3EComplexType*|68||ro||
|**2096**|**ZigBeeFiveDeviceProperty**|*O3EComplexType*|84||ro||
|**2097**|**ZigBeeFiveDeviceSetpoint**|*O3EComplexType*|13||**rw**||
|**2098**|**ZigBeeFiveDeviceCurrentValues**|RawCodec|57||ro||
|**2098**|**ZigBeeFiveDeviceCurrentValues**|*O3EComplexType*|68||ro||
|**2099**|**ZigBeeSixDeviceProperty**|*O3EComplexType*|84||ro||
|**2100**|**ZigBeeSixDeviceSetpoint**|*O3EComplexType*|13||**rw**||
|**2101**|**ZigBeeSixDeviceCurrentValues**|RawCodec|57||ro||
|**2101**|**ZigBeeSixDeviceCurrentValues**|*O3EComplexType*|68||ro||
|**2102**|**ZigBeeSevenDeviceProperty**|*O3EComplexType*|84||ro||
|**2103**|**ZigBeeSevenDeviceSetpoint**|*O3EComplexType*|13||**rw**||
|**2104**|**ZigBeeSevenDeviceCurrentValues**|RawCodec|57||ro||
|**2104**|**ZigBeeSevenDeviceCurrentValues**|*O3EComplexType*|68||ro||
|**2105**|**ZigBeeEightDeviceProperty**|*O3EComplexType*|84||ro||
|**2106**|**ZigBeeEightDeviceSetpoint**|*O3EComplexType*|13||**rw**||
|**2107**|**ZigBeeEightDeviceCurrentValues**|RawCodec|57||ro||
|**2107**|**ZigBeeEightDeviceCurrentValues**|*O3EComplexType*|68||ro||
|**2108**|**ZigBeeNineDeviceProperty**|*O3EComplexType*|84||ro||
|**2109**|**ZigBeeNineDeviceSetpoint**|*O3EComplexType*|13||**rw**||
|**2110**|**ZigBeeNineDeviceCurrentValues**|RawCodec|57||ro||
|**2110**|**ZigBeeNineDeviceCurrentValues**|*O3EComplexType*|68||ro||
|**2111**|**ZigBeeTenDeviceProperty**|*O3EComplexType*|84||ro||
|**2112**|**ZigBeeTenDeviceSetpoint**|*O3EComplexType*|13||**rw**||
|**2113**|**ZigBeeTenDeviceCurrentValues**|RawCodec|57||ro||
|**2113**|**ZigBeeTenDeviceCurrentValues**|*O3EComplexType*|68||ro||
|**2114**|**ZigBeeElevenDeviceProperty**|*O3EComplexType*|84||ro||
|**2115**|**ZigBeeElevenDeviceSetpoint**|*O3EComplexType*|13||**rw**||
|**2116**|**ZigBeeElevenDeviceCurrentValues**|RawCodec|57||ro||
|**2116**|**ZigBeeElevenDeviceCurrentValues**|*O3EComplexType*|68||ro||
|**2117**|**ZigBeeTwelveDeviceProperty**|*O3EComplexType*|84||ro||
|**2118**|**ZigBeeTwelveDeviceSetpoint**|*O3EComplexType*|13||**rw**||
|**2119**|**ZigBeeTwelveDeviceCurrentValues**|RawCodec|57||ro||
|**2119**|**ZigBeeTwelveDeviceCurrentValues**|*O3EComplexType*|68||ro||
|**2120**|**ZigBeeThirteenDeviceProperty**|*O3EComplexType*|84||ro||
|**2121**|**ZigBeeThirteenDeviceSetpoint**|*O3EComplexType*|13||**rw**||
|**2122**|**ZigBeeThirteenDeviceCurrentValues**|RawCodec|57||ro||
|**2122**|**ZigBeeThirteenDeviceCurrentValues**|*O3EComplexType*|68||ro||
|**2123**|**ZigBeeFourteenDeviceProperty**|*O3EComplexType*|84||ro||
|**2124**|**ZigBeeFourteenDeviceSetpoint**|*O3EComplexType*|13||**rw**||
|**2125**|**ZigBeeFourteenDeviceCurrentValues**|RawCodec|57||ro||
|**2125**|**ZigBeeFourteenDeviceCurrentValues**|*O3EComplexType*|68||ro||
|**2126**|**ZigBeeFifteenDeviceProperty**|*O3EComplexType*|84||ro||
|**2127**|**ZigBeeFifteenDeviceSetpoint**|*O3EComplexType*|13||**rw**||
|**2128**|**ZigBeeFifteenDeviceCurrentValues**|RawCodec|57||ro||
|**2128**|**ZigBeeFifteenDeviceCurrentValues**|*O3EComplexType*|68||ro||
|**2129**|**ZigBeeSixteenDeviceProperty**|*O3EComplexType*|84||ro||
|**2130**|**ZigBeeSixteenDeviceSetpoint**|*O3EComplexType*|13||**rw**||
|**2131**|**ZigBeeSixteenDeviceCurrentValues**|RawCodec|57||ro||
|**2131**|**ZigBeeSixteenDeviceCurrentValues**|*O3EComplexType*|68||ro||
|**2132**|**ZigBeeSeventeenDeviceProperty**|*O3EComplexType*|84||ro||
|**2133**|**ZigBeeSeventeenDeviceSetpoint**|*O3EComplexType*|13||**rw**||
|**2134**|**ZigBeeSeventeenDeviceCurrentValues**|RawCodec|57||ro||
|**2134**|**ZigBeeSeventeenDeviceCurrentValues**|*O3EComplexType*|68||ro||
|**2135**|**ZigBeeEighteenDeviceProperty**|*O3EComplexType*|84||ro||
|**2136**|**ZigBeeEighteenDeviceSetpoint**|*O3EComplexType*|13||**rw**||
|**2137**|**ZigBeeEighteenDeviceCurrentValues**|RawCodec|57||ro||
|**2137**|**ZigBeeEighteenDeviceCurrentValues**|*O3EComplexType*|68||ro||
|**2138**|**ZigBeeNineteenDeviceProperty**|*O3EComplexType*|84||ro||
|**2139**|**ZigBeeNineteenDeviceSetpoint**|*O3EComplexType*|13||**rw**||
|**2140**|**ZigBeeNineteenDeviceCurrentValues**|RawCodec|57||ro||
|**2140**|**ZigBeeNineteenDeviceCurrentValues**|*O3EComplexType*|68||ro||
|**2141**|**ZigBeeTwentyDeviceProperty**|*O3EComplexType*|84||ro||
|**2142**|**ZigBeeTwentyDeviceSetpoint**|*O3EComplexType*|13||**rw**||
|**2143**|**ZigBeeTwentyDeviceCurrentValues**|RawCodec|57||ro||
|**2143**|**ZigBeeTwentyDeviceCurrentValues**|*O3EComplexType*|68||ro||
|**2144**|**PointOfCommonCouplingAcActiveCurrent**|RawCodec|16||ro||
|**2145**|**ObjectTopology**|RawCodec|38||ro||
|**2146**|**ZigBeeApartmentOneProperty**|RawCodec|8||ro||
|**2147**|**ZigBeeApartmentOneTopology**|RawCodec|106||ro||
|**2158**|**ActivatedFeatures**|RawCodec|16||ro||
|**2159**|**ApartmentOneCurrentValues**|RawCodec|84||ro||
|**2164**|**DeviceDigitalInputSixValue**|O3EByteVal|1||ro||
|**2165**|**DevicePwmOutputThreeValue**|O3EInt8|1||ro||
|**2166**|**MixerOneCircuitExternalHookupDemandInput**|RawCodec|1||ro||
|**2167**|**MixerTwoCircuitExternalHookupDemandInput**|RawCodec|1||ro||
|**2168**|**MixerThreeCircuitExternalHookupDemandInput**|RawCodec|1||ro||
|**2169**|**MixerFourCircuitExternalHookupDemandInput**|RawCodec|1||ro||
|**2182**|**SupportedApartmentFeatures**|RawCodec|15||ro||
|**2183**|**ActivatedApartmentFeatures**|RawCodec|15||ro||
|**2184**|**BackupBoxTest**|RawCodec|2||ro||
|**2185**|**BatteryStateOfChargeHistogram**|RawCodec|40||ro||
|**2188**|**PointOfCommonCouplingSetActivePowerTotal**|RawCodec|6||ro||
|**2189**|**EebusDeviceListTwo**|RawCodec|104||ro||
|**2190**|**EebusDeviceListThree**|RawCodec|104||ro||
|**2191**|**EebusDeviceListFour**|RawCodec|104||ro||
|**2192**|**EebusDeviceListFive**|RawCodec|104||ro||
|**2193**|**ApartmentOneSupplyChannelTwoTimeScheduleMonday**|RawCodec|57||**rw**||
|**2194**|**ApartmentOneSupplyChannelTwoTimeScheduleTuesday**|RawCodec|57||**rw**||
|**2195**|**ApartmentOneSupplyChannelTwoTimeScheduleWednesday**|RawCodec|57||**rw**||
|**2196**|**ApartmentOneSupplyChannelTwoTimeScheduleThursday**|RawCodec|57||**rw**||
|**2197**|**ApartmentOneSupplyChannelTwoTimeScheduleFriday**|RawCodec|57||**rw**||
|**2198**|**ApartmentOneSupplyChannelTwoTimeScheduleSaturday**|RawCodec|57||**rw**||
|**2199**|**ApartmentOneSupplyChannelTwoTimeScheduleSunday**|RawCodec|57||**rw**||
|**2200**|**ApartmentOneSupplyChannelThreeTimeScheduleMonday**|RawCodec|57||**rw**||
|**2201**|**ApartmentOneSupplyChannelThreeTimeScheduleTuesday**|RawCodec|57||**rw**||
|**2202**|**ApartmentOneSupplyChannelThreeTimeScheduleWednesday**|RawCodec|57||**rw**||
|**2203**|**ApartmentOneSupplyChannelThreeTimeScheduleThursday**|RawCodec|57||**rw**||
|**2204**|**ApartmentOneSupplyChannelThreeTimeScheduleFriday**|RawCodec|57||**rw**||
|**2205**|**ApartmentOneSupplyChannelThreeTimeScheduleSaturday**|RawCodec|57||**rw**||
|**2206**|**ApartmentOneSupplyChannelThreeTimeScheduleSunday**|RawCodec|57||**rw**||
|**2207**|**ApartmentOneSupplyChannelFourTimeScheduleMonday**|RawCodec|57||**rw**||
|**2208**|**ApartmentOneSupplyChannelFourTimeScheduleTuesday**|RawCodec|57||**rw**||
|**2209**|**ApartmentOneSupplyChannelFourTimeScheduleWednesday**|RawCodec|57||**rw**||
|**2210**|**ApartmentOneSupplyChannelFourTimeScheduleThursday**|RawCodec|57||**rw**||
|**2211**|**ApartmentOneSupplyChannelFourTimeScheduleFriday**|RawCodec|57||**rw**||
|**2212**|**ApartmentOneSupplyChannelFourTimeScheduleSaturday**|RawCodec|57||**rw**||
|**2213**|**ApartmentOneSupplyChannelFourTimeScheduleSunday**|RawCodec|57||**rw**||
|**2214**|[**BackupBoxConfiguration**](## "Configuration for Backup Box")|*O3EComplexType*|2||**rw**||
|**2217**|**InputDemandSideManagementlReceiver**|RawCodec|1||ro||
|**2218**|**RemoteLimitValueDemandSideManagement**|RawCodec|4||ro||
|**2219**|**BatteryCalibration**|RawCodec|1||ro||
|**2220**|**BatteryReactivePowerMode**|RawCodec|1||ro||
|**2221**|**BatteryReactivePowerFixCosinusPhi**|RawCodec|3||ro||
|**2222**|**BatteryReactivePower**|RawCodec|18||ro||
|**2223**|**BatteryReactivePowerCosinusPhi**|RawCodec|15||ro||
|**2224**|**PhotovoltaicsActivePowerLimitation**|RawCodec|16||ro||
|**2225**|**ElectricEnergyStorageSetpoint**|RawCodec|12||**rw**||
|**2226**|**ElectricEnergyStorageMaximum**|RawCodec|12||ro||
|**2229**|**ThermostatTerminalOneFunction**|RawCodec|1||ro||
|**2230**|**ThermostatTerminalTwoFunction**|RawCodec|1||ro||
|**2231**|**ThermostatTerminalThreeFunction**|RawCodec|1||ro||
|**2233**|**PersistentStorageStatus**|O3EByteVal|1||ro||
|**2234**|**PowerGridCodeSettingsNormOne**|RawCodec|27||ro||
|**2235**|**CascadeSystemConfiguration**|RawCodec|65||ro||
|**2236**|**CascadeDeviceSetpoint**|RawCodec|10||**rw**||
|**2237**|**CascadeDeviceStatus**|RawCodec|18||ro||
|**2239**|**ElectricEnergyStorageControlMode**|RawCodec|1||ro||
|**2240**|**BatteryTemperatureSensor**|*O3EComplexType*|9||ro||
|**2241**|**OutsideTemperatureSensorSource**|RawCodec|1||ro||
|**2242**|**PowerGridCodeSettingsNormTwo**|RawCodec|27||ro||
|**2244**|**PowerGridCodeSettingsNormFour**|RawCodec|27||ro||
|**2246**|**FixReactivePowerIn**|RawCodec|26||ro||
|**2247**|**FilterRuntime**|*O3EComplexType*|12||ro||
|**2248**|**CurrentVentilationHeatRecovery**|O3EByteVal|1||ro||
|**2249**|**DigitalSwitchSettingOne**|RawCodec|8||ro||
|**2250**|**DigitalSwitchSettingTwo**|RawCodec|8||ro||
|**2251**|**LedStatusOne**|RawCodec|8||ro||
|**2252**|**LedStatusTwo**|RawCodec|8||ro||
|**2253**|**DeviceDigitalInputSevenValue**|O3EByteVal|1||ro||
|**2254**|**PowerGridCodeSettingConfiguration**|RawCodec|1||ro||
|**2255**|**MinimumSecondaryReturnTemperatureRefrigerantCircuit**|O3EInt16|2||ro||
|**2256**|[**DesiredThermalEnergyDefrost**](## "Target value of thermal energy to perform next defrosting")|O3EInt16|2|Wh|ro||
|**2257**|**DomesticHotWaterTemperatureSetpointOffset**|O3EInt16|2||**rw**||
|**2259**|**RefrigerationCircuitStatus**|O3EByteVal|1||ro||
|**2260**|**ZigBeeTwentyOneDeviceProperty**|*O3EComplexType*|84||ro||
|**2261**|**ZigBeeTwentyOneDeviceSetpoint**|*O3EComplexType*|13||**rw**||
|**2262**|**ZigBeeTwentyOneDeviceCurrentValues**|RawCodec|57||ro||
|**2262**|**ZigBeeTwentyOneDeviceCurrentValues**|*O3EComplexType*|68||ro||
|**2263**|**ZigBeeTwentyTwoDeviceProperty**|*O3EComplexType*|84||ro||
|**2264**|**ZigBeeTwentyTwoDeviceSetpoint**|*O3EComplexType*|13||**rw**||
|**2265**|**ZigBeeTwentyTwoDeviceCurrentValues**|RawCodec|57||ro||
|**2265**|**ZigBeeTwentyTwoDeviceCurrentValues**|*O3EComplexType*|68||ro||
|**2266**|**ZigBeeTwentyThreeDeviceProperty**|*O3EComplexType*|84||ro||
|**2267**|**ZigBeeTwentyThreeDeviceSetpoint**|*O3EComplexType*|13||**rw**||
|**2268**|**ZigBeeTwentyThreeDeviceCurrentValues**|RawCodec|57||ro||
|**2268**|**ZigBeeTwentyThreeDeviceCurrentValues**|*O3EComplexType*|68||ro||
|**2269**|**ZigBeeTwentyFourDeviceProperty**|*O3EComplexType*|84||ro||
|**2270**|**ZigBeeTwentyFourDeviceSetpoint**|*O3EComplexType*|13||**rw**||
|**2271**|**ZigBeeTwentyFourDeviceCurrentValues**|RawCodec|57||ro||
|**2271**|**ZigBeeTwentyFourDeviceCurrentValues**|*O3EComplexType*|68||ro||
|**2272**|**ZigBeeTwentyFiveDeviceProperty**|*O3EComplexType*|84||ro||
|**2273**|**ZigBeeTwentyFiveDeviceSetpoint**|*O3EComplexType*|13||**rw**||
|**2274**|**ZigBeeTwentyFiveDeviceCurrentValues**|RawCodec|57||ro||
|**2274**|**ZigBeeTwentyFiveDeviceCurrentValues**|*O3EComplexType*|68||ro||
|**2275**|**ZigBeeTwentySixDeviceProperty**|*O3EComplexType*|84||ro||
|**2276**|**ZigBeeTwentySixDeviceSetpoint**|*O3EComplexType*|13||**rw**||
|**2277**|**ZigBeeTwentySixDeviceCurrentValues**|RawCodec|57||ro||
|**2277**|**ZigBeeTwentySixDeviceCurrentValues**|*O3EComplexType*|68||ro||
|**2278**|**ZigBeeTwentySevenDeviceProperty**|*O3EComplexType*|84||ro||
|**2279**|**ZigBeeTwentySevenDeviceSetpoint**|*O3EComplexType*|13||**rw**||
|**2280**|**ZigBeeTwentySevenDeviceCurrentValues**|RawCodec|57||ro||
|**2280**|**ZigBeeTwentySevenDeviceCurrentValues**|*O3EComplexType*|68||ro||
|**2281**|**ZigBeeTwentyEightDeviceProperty**|*O3EComplexType*|84||ro||
|**2282**|**ZigBeeTwentyEightDeviceSetpoint**|*O3EComplexType*|13||**rw**||
|**2283**|**ZigBeeTwentyEightDeviceCurrentValues**|RawCodec|57||ro||
|**2283**|**ZigBeeTwentyEightDeviceCurrentValues**|*O3EComplexType*|68||ro||
|**2284**|**ZigBeeTwentyNineDeviceProperty**|*O3EComplexType*|84||ro||
|**2285**|**ZigBeeTwentyNineDeviceSetpoint**|*O3EComplexType*|13||**rw**||
|**2286**|**ZigBeeTwentyNineDeviceCurrentValues**|RawCodec|57||ro||
|**2286**|**ZigBeeTwentyNineDeviceCurrentValues**|*O3EComplexType*|68||ro||
|**2287**|**ZigBeeThirtyDeviceProperty**|*O3EComplexType*|84||ro||
|**2288**|**ZigBeeThirtyDeviceSetpoint**|*O3EComplexType*|13||**rw**||
|**2289**|**ZigBeeThirtyDeviceCurrentValues**|RawCodec|57||ro||
|**2289**|**ZigBeeThirtyDeviceCurrentValues**|*O3EComplexType*|68||ro||
|**2290**|**ZigBeeThirtyOneDeviceProperty**|*O3EComplexType*|84||ro||
|**2291**|**ZigBeeThirtyOneDeviceSetpoint**|*O3EComplexType*|13||**rw**||
|**2292**|**ZigBeeThirtyOneDeviceCurrentValues**|RawCodec|57||ro||
|**2292**|**ZigBeeThirtyOneDeviceCurrentValues**|*O3EComplexType*|68||ro||
|**2293**|**ZigBeeThirtyTwoDeviceProperty**|*O3EComplexType*|84||ro||
|**2294**|**ZigBeeThirtyTwoDeviceSetpoint**|*O3EComplexType*|13||**rw**||
|**2295**|**ZigBeeThirtyTwoDeviceCurrentValues**|RawCodec|57||ro||
|**2295**|**ZigBeeThirtyTwoDeviceCurrentValues**|*O3EComplexType*|68||ro||
|**2296**|**ZigBeeThirtyThreeDeviceProperty**|*O3EComplexType*|84||ro||
|**2297**|**ZigBeeThirtyThreeDeviceSetpoint**|*O3EComplexType*|13||**rw**||
|**2298**|**ZigBeeThirtyThreeDeviceCurrentValues**|RawCodec|57||ro||
|**2298**|**ZigBeeThirtyThreeDeviceCurrentValues**|*O3EComplexType*|68||ro||
|**2299**|**ZigBeeThirtyFourDeviceProperty**|*O3EComplexType*|84||ro||
|**2300**|**ZigBeeThirtyFourDeviceSetpoint**|*O3EComplexType*|13||**rw**||
|**2301**|**ZigBeeThirtyFourDeviceCurrentValues**|RawCodec|57||ro||
|**2301**|**ZigBeeThirtyFourDeviceCurrentValues**|*O3EComplexType*|68||ro||
|**2302**|**ZigBeeThirtyFiveDeviceProperty**|*O3EComplexType*|84||ro||
|**2303**|**ZigBeeThirtyFiveDeviceSetpoint**|*O3EComplexType*|13||**rw**||
|**2304**|**ZigBeeThirtyFiveDeviceCurrentValues**|RawCodec|57||ro||
|**2304**|**ZigBeeThirtyFiveDeviceCurrentValues**|*O3EComplexType*|68||ro||
|**2305**|**ZigBeeThirtySixDeviceProperty**|*O3EComplexType*|84||ro||
|**2306**|**ZigBeeThirtySixDeviceSetpoint**|*O3EComplexType*|13||**rw**||
|**2307**|**ZigBeeThirtySixDeviceCurrentValues**|RawCodec|57||ro||
|**2307**|**ZigBeeThirtySixDeviceCurrentValues**|*O3EComplexType*|68||ro||
|**2308**|**ZigBeeThirtySevenDeviceProperty**|*O3EComplexType*|84||ro||
|**2309**|**ZigBeeThirtySevenDeviceSetpoint**|*O3EComplexType*|13||**rw**||
|**2310**|**ZigBeeThirtySevenDeviceCurrentValues**|RawCodec|57||ro||
|**2310**|**ZigBeeThirtySevenDeviceCurrentValues**|*O3EComplexType*|68||ro||
|**2311**|**ZigBeeThirtyEightDeviceProperty**|*O3EComplexType*|84||ro||
|**2312**|**ZigBeeThirtyEightDeviceSetpoint**|*O3EComplexType*|13||**rw**||
|**2313**|**ZigBeeThirtyEightDeviceCurrentValues**|RawCodec|57||ro||
|**2313**|**ZigBeeThirtyEightDeviceCurrentValues**|*O3EComplexType*|68||ro||
|**2314**|**ZigBeeThirtyNineDeviceProperty**|*O3EComplexType*|84||ro||
|**2315**|**ZigBeeThirtyNineDeviceSetpoint**|*O3EComplexType*|13||**rw**||
|**2316**|**ZigBeeThirtyNineDeviceCurrentValues**|RawCodec|57||ro||
|**2316**|**ZigBeeThirtyNineDeviceCurrentValues**|*O3EComplexType*|68||ro||
|**2317**|**ZigBeeFourtyDeviceProperty**|*O3EComplexType*|84||ro||
|**2318**|**ZigBeeFourtyDeviceSetpoint**|*O3EComplexType*|13||**rw**||
|**2319**|**ZigBeeFourtyDeviceCurrentValues**|RawCodec|57||ro||
|**2319**|**ZigBeeFourtyDeviceCurrentValues**|*O3EComplexType*|68||ro||
|**2320**|[**DomesticHotWaterStatus**](## "Status of domestic hot water preparation {0: Idle, 1: Active, 2: Postrun}")|O3EEnum|1||ro||
|**2321**|**ZigBeeApartmentOneDecoupleList**|RawCodec|91||ro||
|**2327**|**VentilationTargetVolumeFlow**|*O3EComplexType*|4||**rw**||
|**2328**|**VentilationCurrentVolumeFlow**|*O3EComplexType*|4||ro||
|**2329**|**BatteryEnergyUsedAverage**|RawCodec|14||ro||
|**2330**|[**GenericDigitalInputConfigurationOnBoardTwo**](## "{0: Nothing, 1: FaultSignal, 2: DhwCirculation, 3: FaultSignalAndLocked, 4: ExternalHeatDemand, 5: ExternalLocked, 6: ExternalThermostat, 7: RoomTemperatureLimiter, 8: CallForHeat, 9: SmartGridReadyInputOne, 10: SmartGridReadyInputTwo, 11: PowerSupplierLock, 12: ExternalCoolingDemand, 13: PrioritizedDemandDeactivationOtherCircuits, 14: LockCircuitOne, 15: LockCircuitTwo, 16: ExternalDemandAutomatic, 17: FanControl, 18: FanRpmControl, 19: DefrostHeaterControlOne, 20: DefrostHeaterControlTwo, 21: DayNigthOperation, 22: DayNigthOperationPlusDirectControlDigitalOutputOne, 23: PermanentHeating, 24: DirectControlDryContactOne, 25: DirectControlDryContactTwo, 26: DirectControlDryContactThree, 27: DirectControlDigitalOutputTwentyFourVolt}")|O3EEnum|1||ro||
|**2331**|[**GenericDigitalInputConfigurationOnBoardThree**](## "{0: Nothing, 1: FaultSignal, 2: DhwCirculation, 3: FaultSignalAndLocked, 4: ExternalHeatDemand, 5: ExternalLocked, 6: ExternalThermostat, 7: RoomTemperatureLimiter, 8: CallForHeat, 9: SmartGridReadyInputOne, 10: SmartGridReadyInputTwo, 11: PowerSupplierLock, 12: ExternalCoolingDemand, 13: PrioritizedDemandDeactivationOtherCircuits, 14: LockCircuitOne, 15: LockCircuitTwo, 16: ExternalDemandAutomatic, 17: FanControl, 18: FanRpmControl, 19: DefrostHeaterControlOne, 20: DefrostHeaterControlTwo, 21: DayNigthOperation, 22: DayNigthOperationPlusDirectControlDigitalOutputOne, 23: PermanentHeating, 24: DirectControlDryContactOne, 25: DirectControlDryContactTwo, 26: DirectControlDryContactThree, 27: DirectControlDigitalOutputTwentyFourVolt}")|O3EEnum|1||ro||
|**2332**|[**GenericDigitalInputConfigurationOnBoardFour**](## "{0: Nothing, 1: FaultSignal, 2: DhwCirculation, 3: FaultSignalAndLocked, 4: ExternalHeatDemand, 5: ExternalLocked, 6: ExternalThermostat, 7: RoomTemperatureLimiter, 8: CallForHeat, 9: SmartGridReadyInputOne, 10: SmartGridReadyInputTwo, 11: PowerSupplierLock, 12: ExternalCoolingDemand, 13: PrioritizedDemandDeactivationOtherCircuits, 14: LockCircuitOne, 15: LockCircuitTwo, 16: ExternalDemandAutomatic, 17: FanControl, 18: FanRpmControl, 19: DefrostHeaterControlOne, 20: DefrostHeaterControlTwo, 21: DayNigthOperation, 22: DayNigthOperationPlusDirectControlDigitalOutputOne, 23: PermanentHeating, 24: DirectControlDryContactOne, 25: DirectControlDryContactTwo, 26: DirectControlDryContactThree, 27: DirectControlDigitalOutputTwentyFourVolt}")|O3EEnum|1||ro||
|**2333**|[**EconomizerLiquidTemperatureSensor**](## "Actual temperature economizer inlet")|*O3EComplexType*|9||ro|[Link](https://github.com/open3e/open3e/wiki/036-DoI-%E2%80%90-Data-points-of-Interest/#data-points-of-vitocal-250)|
|**2334**|[**EvaporatorVaporTemperatureSensor**](## "Actual temperature avaporator inlet")|*O3EComplexType*|9||ro|[Link](https://github.com/open3e/open3e/wiki/036-DoI-%E2%80%90-Data-points-of-Interest/#data-points-of-vitocal-250)|
|**2335**|**BatteryModuleCoulombCounters**|RawCodec|8||ro||
|**2336**|**ControllerBoardTemperatureSensor**|*O3EComplexType*|9||ro||
|**2337**|**UltraLowNitroOxideStatusActive**|RawCodec|1||ro||
|**2338**|**HighLimitTestMode**|RawCodec|3||ro||
|**2339**|**SafetyLimiterThresholdTemperature**|RawCodec|2||ro||
|**2340**|**ElectricalHeaterConfiguration**|RawCodec|2||ro||
|**2341**|**CoefficientOfPerformanceConfiguration**|RawCodec|4||ro||
|**2342**|**NominalThermalCapacityHeating**|O3EInt32|4||ro||
|**2343**|**NominalThermalCapacityCooling**|O3EInt32|4||ro||
|**2344**|**CombustionAirInterlockSettings**|RawCodec|1||ro||
|**2345**|[**CompressorSetpointPercent**](## "Setpoint of speed of heat pump compressor")|O3EInt8|1|%|**rw**||
|**2346**|[**CompressorSpeedPercent**](## "Actual speed of heat pump compressor")|O3EInt8|1|%|ro|[Link](https://github.com/open3e/open3e/wiki/036-DoI-%E2%80%90-Data-points-of-Interest/#data-points-of-vitocal-250)|
|**2348**|**PhotovoltaicsActivePowerLimitationEnergyManagementSystem**|RawCodec|8||ro||
|**2349**|**PhotovoltaicsActivePowerLimitationFallbackEnergyManagementSystem**|RawCodec|8||ro||
|**2350**|**EnergyManagmentSystemResultingControlState**|O3EByteVal|1||ro||
|**2351**|[**HeatPumpCompressor**](## "Actual state of the heat pump compressor")|*O3EComplexType*|2||ro||
|**2352**|[**AdditionalElectricHeater**](## "Actual state of the electric auxiliary heating")|*O3EComplexType*|2||ro||
|**2353**|**TargetDemandHeatProducer**|*O3EComplexType*|4||**rw**||
|**2355**|**MinimumVentilationSupplyAirTemperature**|*O3EComplexType*|4||ro||
|**2356**|**CurrentSystemHeatingCoolingLevel**|O3EInt8|1||ro||
|**2369**|[**HeatPumpCompressorStatistical**](## "Statistics for heat pump compressor starts")|*O3EComplexType*|14||ro||
|**2370**|**AdditionalElectricHeaterStatistical**|*O3EComplexType*|11||ro||
|**2371**|**VentilationControlMode**|*O3EComplexType*|2||ro||
|**2372**|**VentilationControllerOperationState**|*O3EComplexType*|2||**rw**||
|**2373**|**VentilationAirVolumeFlowBalancingOffset**|RawCodec|2||**rw**||
|**2374**|**VentilationExternalLockFunctionSetting**|O3EByteVal|1||ro||
|**2375**|**NarrowBandInternetOfThingsConfiguration**|RawCodec|7||ro||
|**2376**|**NarrowBandInternetOfThingsRadio**|RawCodec|132||ro||
|**2377**|**EvolvedUniversalTerrestrialRadioAccessDataLinkInfo**|RawCodec|45||ro||
|**2378**|**EvolvedUniversalTerrestrialRadioAccessNeighborCells**|RawCodec|48||ro||
|**2379**|**EvolvedUniversalTerrestrialRadioAccessServingCellInfo**|RawCodec|22||ro||
|**2380**|**EvolvedUniversalTerrestrialRadioAccessServingCellMeasurements**|RawCodec|17||ro||
|**2382**|**PaddleSwitch**|RawCodec|2||ro||
|**2403**|**BypassOperationLevel**|O3EInt8|1||ro||
|**2404**|**BivalenceControlMode**|*O3EComplexType*|6||ro||
|**2405**|**MixerOneCircuitConstantFlowSetTemperatureCooling**|*O3EComplexType*|6||ro||
|**2406**|**MixerTwoCircuitConstantFlowSetTemperatureCooling**|*O3EComplexType*|6||ro||
|**2407**|**MixerThreeCircuitConstantFlowSetTemperatureCooling**|*O3EComplexType*|6||ro||
|**2408**|**MixerFourCircuitConstantFlowSetTemperatureCooling**|*O3EComplexType*|6||ro||
|**2409**|**MixerOneCircuitMinimumMaximumFlowSetTemperatureCooling**|RawCodec|12||ro||
|**2410**|**MixerTwoCircuitMinimumMaximumFlowSetTemperatureCooling**|RawCodec|12||ro||
|**2411**|**MixerThreeCircuitMinimumMaximumFlowSetTemperatureCooling**|RawCodec|12||ro||
|**2412**|**MixerFourCircuitMinimumMaximumFlowSetTemperatureCooling**|RawCodec|12||ro||
|**2413**|**MixerOneCircuitThresholdCooling**|*O3EComplexType*|4||ro||
|**2414**|**MixerTwoCircuitThresholdCooling**|*O3EComplexType*|4||ro||
|**2415**|**MixerThreeCircuitThresholdCooling**|*O3EComplexType*|4||ro||
|**2416**|**MixerFourCircuitThresholdCooling**|*O3EComplexType*|4||ro||
|**2417**|**MixerOneCircuitTargetValueRelativeHumidityCooling**|RawCodec|6||**rw**||
|**2418**|**MixerTwoCircuitTargetValueRelativeHumidityCooling**|RawCodec|6||**rw**||
|**2419**|**MixerThreeCircuitTargetValueRelativeHumidityCooling**|RawCodec|6||**rw**||
|**2420**|**MixerFourCircuitTargetValueRelativeHumidityCooling**|RawCodec|6||**rw**||
|**2421**|**MixerOneCircuitTemperatureOffsetCooling**|RawCodec|2||**rw**||
|**2422**|**MixerTwoCircuitTemperatureOffsetCooling**|RawCodec|2||**rw**||
|**2423**|**MixerThreeCircuitTemperatureOffsetCooling**|RawCodec|2||**rw**||
|**2424**|**MixerFourCircuitTemperatureOffsetCooling**|RawCodec|2||**rw**||
|**2425**|**BatteryModuleTypeId**|RawCodec|2||ro||
|**2426**|**MixerOneCircuitRoomEcoFunctionSettings**|*O3EComplexType*|6||ro||
|**2427**|**MixerTwoCircuitRoomEcoFunctionSettings**|*O3EComplexType*|6||ro||
|**2428**|**MixerThreeCircuitRoomEcoFunctionSettings**|*O3EComplexType*|6||ro||
|**2429**|**MixerFourCircuitRoomEcoFunctionSettings**|*O3EComplexType*|6||ro||
|**2442**|**HeatPumpFrostProtection**|O3EInt8|1||ro||
|**2444**|**LogLevelEmbbededApplication**|O3EInt8|1||ro||
|**2445**|**SupplementalHeatEngineConfiguration**|RawCodec|2||ro||
|**2446**|**HmiWakeupTrigger**|RawCodec|4||ro||
|**2447**|**SupplyAirVolumeFlowDeviceLimit**|*O3EComplexType*|4||ro||
|**2448**|**ExhaustAirVolumeFlowDeviceLimit**|*O3EComplexType*|4||ro||
|**2449**|**CustomerSpecificDeviceName**|RawCodec|2||ro||
|**2450**|**CascadeSequenceCurrentBoiler**|RawCodec|16||ro||
|**2451**|**CascadeEmergencyOperationMode**|RawCodec|3||ro||
|**2452**|**MixerOneCircuitRoomTemperatureThresholdCooling**|*O3EComplexType*|4||ro||
|**2453**|**MixerTwoCircuitRoomTemperatureThresholdCooling**|*O3EComplexType*|4||ro||
|**2454**|**MixerThreeCircuitRoomTemperatureThresholdCooling**|*O3EComplexType*|4||ro||
|**2455**|**MixerFourCircuitRoomTemperatureThresholdCooling**|*O3EComplexType*|4||ro||
|**2457**|**CalculatedOutsideTemperature**|*O3EComplexType*|9||ro||
|**2458**|**CascadeDeviceStatusLead**|RawCodec|18||ro||
|**2459**|**CascadeDeviceStatusLagOne**|RawCodec|18||ro||
|**2460**|**CascadeDeviceStatusLagTwo**|RawCodec|18||ro||
|**2461**|**CascadeDeviceStatusLagThree**|RawCodec|18||ro||
|**2462**|**CascadeDeviceStatusLagFour**|RawCodec|18||ro||
|**2463**|**CascadeDeviceStatusLagFive**|RawCodec|18||ro||
|**2464**|**CascadeDeviceStatusLagSix**|RawCodec|18||ro||
|**2465**|**CascadeDeviceStatusLagSeven**|RawCodec|18||ro||
|**2466**|**CascadeDeviceStatusLagEight**|RawCodec|18||ro||
|**2467**|**CascadeDeviceStatusLagNine**|RawCodec|18||ro||
|**2468**|**CascadeDeviceStatusLagTen**|RawCodec|18||ro||
|**2469**|**CascadeDeviceStatusLagEleven**|RawCodec|18||ro||
|**2470**|**CascadeDeviceStatusLagTwelve**|RawCodec|18||ro||
|**2471**|**CascadeDeviceStatusLagThirteen**|RawCodec|18||ro||
|**2472**|**CascadeDeviceStatusLagFourteen**|RawCodec|18||ro||
|**2473**|**CascadeDeviceStatusLagFifteen**|RawCodec|18||ro||
|**2474**|**CascadeCommonFlowTemperatureSensor**|RawCodec|9||ro||
|**2475**|**CascadeCommonFlowCurrentTemperatureSetpoint**|O3EInt16|2||**rw**||
|**2476**|**EnvironmentAirQualityTargetValues**|RawCodec|21||**rw**||
|**2477**|**EnvironmentAirQualitySensor**|O3EByteVal|1||ro||
|**2479**|**MixerOneCircuitRoomAirHumiditySensor**|RawCodec|5||ro||
|**2480**|**MixerTwoCircuitRoomAirHumiditySensor**|RawCodec|5||ro||
|**2481**|**MixerThreeCircuitRoomAirHumiditySensor**|RawCodec|5||ro||
|**2482**|**MixerFourCircuitRoomAirHumiditySensor**|RawCodec|5||ro||
|**2484**|**ElectricalPowerRangeMetaData**|RawCodec|8||ro||
|**2486**|[**CurrentElectricalPowerConsumptionRefrigerantCircuit**](## "Actual electrical power consumption of the refrigeration circuit")|O3EInt32|4|W|ro||
|**2487**|[**CurrentElectricalPowerConsumptionElectricHeater**](## "Actual electrical power consumption of the auxiliary heater")|O3EInt32|4|W|ro||
|**2488**|[**CurrentElectricalPowerConsumptionSystem**](## "Actual total electrical power consumption of the system")|O3EInt32|4|W|ro||
|**2489**|**FrostProtectionStatus**|RawCodec|3||ro||
|**2490**|**StartUpWizardState**|RawCodec|1||ro||
|**2491**|**DomesticHotWaterDemandInput**|RawCodec|1||ro||
|**2493**|**VentilationBypassPosition**|RawCodec|2||ro||
|**2494**|[**CurrentThermalCapacityRefrigerantCircuit**](## "Actual thermal power output of the refrigeration circuit")|O3EInt32|4|W|ro||
|**2495**|[**CurrentThermalCapacityElectricHeater**](## "Actual thermal power output of the auxiliary heater")|O3EInt32|4|W|ro||
|**2496**|[**CurrentThermalCapacitySystem**](## "Actual thermal power output of the system")|O3EInt32|4|W|ro||
|**2497**|**ResetStatisticalValuesDate**|RawCodec|3||ro||
|**2498**|**CentralHeatingPumpType**|O3EByteVal|1||ro||
|**2499**|**MixerOneCircuitPumpType**|O3EByteVal|1||ro||
|**2500**|**MixerTwoCircuitPumpType**|O3EByteVal|1||ro||
|**2501**|**MixerThreeCircuitPumpType**|O3EByteVal|1||ro||
|**2502**|**MixerFourCircuitPumpType**|O3EByteVal|1||ro||
|**2515**|**EnergyConsumptionDomesticHotWaterMonthMatrixElectricHeater**|*O3EComplexType*|124||ro||
|**2516**|**EnergyConsumptionDomesticHotWaterYearMatrixElectricHeater**|*O3EComplexType*|96||ro||
|**2517**|**EnergyConsumptionDomesticHotWaterElectricHeater**|*O3EComplexType*|24||ro||
|**2524**|**EnergyConsumptionCentralHeatingMonthMatrixElectricHeater**|*O3EComplexType*|124||ro||
|**2525**|**EnergyConsumptionCentralHeatingYearMatrixElectricHeater**|*O3EComplexType*|96||ro||
|**2526**|**EnergyConsumptionCentralHeatingElectricHeater**|*O3EComplexType*|24||ro||
|**2527**|**GeneratedCoolingOutputMonthMatrix**|*O3EComplexType*|124||ro||
|**2528**|**GeneratedCoolingOutputYearMatrix**|*O3EComplexType*|96||ro||
|**2529**|**GeneratedCoolingOutput**|*O3EComplexType*|24||ro||
|**2533**|**PowerGridCodeSettingsNormSix**|RawCodec|27||ro||
|**2534**|**BusTopologyMatrixSix**|RawCodec|181||ro||
|**2535**|**BusTopologyMatrixSeven**|RawCodec|181||ro||
|**2536**|**BusTopologyMatrixEight**|RawCodec|181||ro||
|**2537**|**BusTopologyMatrixNine**|RawCodec|181||ro||
|**2538**|**BusTopologyMatrixTen**|RawCodec|181||ro||
|**2539**|**AlternatingCurrentEnergyStatistic**|RawCodec|40||ro||
|**2540**|**NoiseReductionSettings**|RawCodec|6||ro||
|**2541**|**SupplyAirVolumeFlowConfigurationLimit**|*O3EComplexType*|4||ro||
|**2542**|**ExhaustAirVolumeFlowConfigurationLimit**|*O3EComplexType*|4||ro||
|**2543**|**SmartGridTemperatureOffsets**|*O3EComplexType*|10||**rw**||
|**2544**|**EnableElectricalHeaterSmartGridLock**|O3EByteVal|1||ro||
|**2545**|**EnableElectricalHeaterSmartGridIncreaseMaxDemand**|O3EByteVal|1||ro||
|**2546**|**MixerOneCircuitRoomTemperatureSetpointCooling**|*O3EComplexType*|9||**rw**||
|**2547**|**MixerTwoCircuitRoomTemperatureSetpointCooling**|*O3EComplexType*|9||**rw**||
|**2548**|**MixerThreeCircuitRoomTemperatureSetpointCooling**|*O3EComplexType*|9||**rw**||
|**2549**|**MixerFourCircuitRoomTemperatureSetpointCooling**|*O3EComplexType*|9||**rw**||
|**2551**|**FlameBurnerTwo**|RawCodec|6||ro||
|**2552**|**ModulationCurrentValueBurnerTwo**|RawCodec|2||ro||
|**2553**|**HeatEngineStatisticalBurnerTwo**|RawCodec|12||ro||
|**2554**|**CellularModemIdentification**|RawCodec|62||ro||
|**2555**|**ElectricalPowerSetPoint**|RawCodec|4||**rw**||
|**2556**|**ElectricalEnergyRemainingCapacity**|RawCodec|4||ro||
|**2557**|**HeatPumpState**|O3EByteVal|1||ro||
|**2558**|**HeatPumpSupportedStates**|RawCodec|3||ro||
|**2559**|**VentilationFanModbusId**|RawCodec|2||ro||
|**2560**|**SmartGridFeatureSelection**|O3EByteVal|1||ro||
|**2563**|**ZigBeeDeviceDecoupleList**|RawCodec|91||ro||
|**2564**|**HydraulicFlapState**|RawCodec|1||ro||
|**2566**|**VentilationSupplyFanRuntime**|O3EInt32|4||ro||
|**2567**|**VentilationExhaustFanRuntime**|O3EInt32|4||ro||
|**2568**|**RefrigerantType**|O3EInt8|1||ro||
|**2569**|[**CompressorSpeedRps**](## "Actual speed of the heat pump compressor")|O3EInt16|2|rps|ro||
|**2570**|**CompressorModulType**|O3EInt16|2||ro||
|**2571**|**CompressorSuctionSuperheat**|O3EInt16|2||ro||
|**2572**|**ActualCompressorInletMassflow**|RawCodec|4||ro||
|**2573**|**CompressorOnTimer**|RawCodec|2||ro||
|**2574**|**NominalPowerElectricalHeater**|*O3EComplexType*|8||ro||
|**2575**|**RefrigerationCycleApplicationState**|O3EInt16|2||ro||
|**2576**|**FuelCellTestModeOne**|RawCodec|2||ro||
|**2577**|**FuelCellTestModeTwo**|RawCodec|6||ro||
|**2578**|**RefrigerationCircuitDesiredOperatingMode**|O3EInt8|1||ro||
|**2579**|**CompressorMinMaxAllowedPrimaryTemperatureHeating**|RawCodec|4||ro||
|**2580**|**CompressorSetpointRps**|O3EInt16|2||**rw**||
|**2581**|**CompressorCalculatedSetpointRps**|O3EInt16|2||**rw**||
|**2582**|**CompressorOffTimer**|RawCodec|2||ro||
|**2583**|**OxygenProbeProcessValuesBurnerOne**|RawCodec|15||ro||
|**2584**|**OxygenProbeProcessValuesBurnerTwo**|RawCodec|15||ro||
|**2586**|**DigitalOutputCooling**|RawCodec|2||ro||
|**2587**|**BatteryModuleWarrantyDataListLastEntry**|RawCodec|5||ro||
|**2588**|**BatteryModuleWarrantyDataListOne**|RawCodec|197||ro||
|**2589**|**BatteryModuleWarrantyDataListTwo**|RawCodec|197||ro||
|**2590**|**HeatPumpCommonSettingsHeating**|RawCodec|8||ro||
|**2591**|**HeatPumpCommonSettingsCooling**|RawCodec|8||ro||
|**2592**|**ExpansionValveTheoreticalSetpoint**|RawCodec|4||**rw**||
|**2593**|**ProductMatrix**|*O3EList*|181||ro||
|**2594**|**ElectricalPreHeaterMonthMatrix**|RawCodec|124||ro||
|**2595**|**ElectricalPreHeaterYearMatrix**|RawCodec|96||ro||
|**2598**|**VentilationFanAssignmentAvailable**|O3EByteVal|1||ro||
|**2599**|**VentilationFanAssignmentSwitch**|O3EByteVal|1||ro||
|**2600**|**ElectricalHeaterActivation**|RawCodec|2||ro||
|**2601**|**ElectricalHeaterVentilationConfiguration**|RawCodec|2||ro||
|**2602**|**PrimaryHeatExchangerStatus**|RawCodec|10||ro||
|**2603**|**PrimaryHeatExchangerCommonSettings**|RawCodec|4||ro||
|**2604**|**LevelSwitchActivation**|O3EByteVal|1||ro||
|**2605**|**QuickModeRuntime**|*O3EComplexType*|4||ro||
|**2606**|**ExternalTriggerActivation**|O3EByteVal|1||ro||
|**2607**|**ExternalTriggerSettings**|O3EByteVal|1||ro||
|**2608**|**FilterSettings**|RawCodec|28||ro||
|**2609**|**CommissioningStatus**|RawCodec|6||ro||
|**2610**|**SetDeliveryStateExpert**|RawCodec|1||ro||
|**2611**|**NominalThermalCapacityIndoorUnit**|O3EInt32|4||ro||
|**2612**|**PrimarySourceCommonSettingsHeating**|*O3EComplexType*|7||ro||
|**2613**|**PrimarySourceCommonSettingsCooling**|*O3EComplexType*|7||ro||
|**2621**|**MaximumOperatingPressureActualTemperatureSetpoint**|O3EInt16|2||**rw**||
|**2622**|**SeasonalCoefficientOfPerformanceHeating**|*O3EComplexType*|9||ro||
|**2623**|**SeasonalEnergyEfficiencyRatioCooling**|*O3EComplexType*|9||ro||
|**2624**|**SeasonalCoefficientOfPerformanceDomesticHotWater**|*O3EComplexType*|9||ro||
|**2625**|**SeasonalCoefficientOfPerformanceHeatingAndDomesticHotWater**|*O3EComplexType*|9||ro||
|**2626**|**MaximumPowerElectricalHeater**|O3EInt32|4||ro||
|**2627**|**CompressorStartUpTimer**|O3EInt16|2||ro||
|**2629**|**DesiredThermalCapacity**|O3EInt32|4||ro||
|**2630**|**CompressorMinMaxSpeedHeating**|*O3EComplexType*|4||ro||
|**2631**|**CompressorMinMaxSpeedCooling**|*O3EComplexType*|4||ro||
|**2632**|**CompressorMinMaxSpeedDefrost**|*O3EComplexType*|4||ro||
|**2633**|**MaxSpeedNoiseReductionMode**|RawCodec|12||ro||
|**2634**|**NoiseReductionMode**|O3EByteVal|1||ro||
|**2635**|**BurnerProcessDataFlags**|RawCodec|8||ro||
|**2636**|**BurnerTwoProcessDataFlags**|RawCodec|8||ro||
|**2637**|**BurnerThreeProcessDataFlags**|RawCodec|8||ro||
|**2638**|**SupportedCountryCodes**|RawCodec|4||ro||
|**2643**|**MaximumRechargePower**|O3EInt16|2||ro||
|**2733**|**InstallationConfirmation**|RawCodec|3||ro||
|**2735**|[**FourThreeWayValveValveCurrentPosition**](## "Current position of the four/three-way valve {0: Heating/Cooling, 1: Internal Buffer, 2: Domestic Hot Water, 3: Heating/Cooling and Internal Buffer, 4: Domestic Hot Water and Internal Buffer}")|O3EEnum|1||ro||
|**2741**|**ComfortEnsuringMode**|RawCodec|3||ro||
|**2742**|**DiagnosticHydraulicFilterInterval**|O3EInt8|1||ro||
|**2743**|**DiagnosticElectricalHeaterSafetyTemperatureLimiter**|O3EInt8|1||ro||
|**2744**|**DiagnosticSecondaryFourThreeWayValve**|O3EInt8|1||ro||
|**2745**|**DiagnosticHydraulicFilterContamination**|O3EInt8|1||ro||
|**2746**|**DiagnosticHydraulicSafetyValve**|O3EInt8|1||ro||
|**2748**|**DiagnosticControlledLowPressureShutDown**|O3EInt8|1||ro||
|**2749**|**DiagnosticControlledHighPressureShutDown**|O3EInt8|1||ro||
|**2750**|**DiagnosticHydraulicTemperatureSensors**|O3EInt8|1||ro||
|**2751**|**DiagnosticElectronicExpansionValve**|O3EInt8|1||ro||
|**2752**|**DiagnosticFanOperation**|O3EInt8|1||ro||
|**2753**|**DiagnosticHeatExchangerConstraints**|O3EInt8|1||ro||
|**2758**|**GasPressureSwitchErrorReaction**|RawCodec|1||ro||
|**2759**|**EnergyRecoveredCrossHeatExchanger**|RawCodec|24||ro||
|**2760**|[**EnergyOwnConsumption**](## "Own Energy Consumption")|*O3EComplexType*|24||ro||
|**2767**|**DiagnosticMonitoringPressureDrop**|O3EInt8|1||ro||
|**2768**|**DiagnosticMonitoringPressurePeaks**|O3EInt8|1||ro||
|**2772**|**EnergyRecoveredCrossHeatExchangerMonthMatrix**|RawCodec|124||ro||
|**2773**|**EnergyRecoveredCrossHeatExchangerYearMatrix**|RawCodec|96||ro||
|**2774**|**EnergyOwnConsumptionMonthMatrix**|RawCodec|124||ro||
|**2775**|**EnergyOwnConsumptionYearMatrix**|RawCodec|96||ro||
|**2776**|**ProductMatrixTwo**|RawCodec|181||ro||
|**2777**|**PrimaryBootLoaderVersion**|RawCodec|8||ro||
|**2778**|**ErrorMessageInputSelection**|RawCodec|2||ro||
|**2779**|**DeltaTemperaturePumpControlSetpoint**|RawCodec|2||**rw**||
|**2780**|**DomesticHotWaterFlowRangeDwellDuration**|RawCodec|1||ro||
|**2781**|**AirVolumeFlowSetpoint**|RawCodec|7||**rw**||
|**2782**|**AirVolumeFlowStatus**|RawCodec|24||ro||
|**2783**|**VentilationSelfCheckDuration**|RawCodec|4||ro||
|**2784**|**SecondaryHeatExchangerVaporPressureSensor**|*O3EComplexType*|9||ro||
|**2785**|**ElectricalHeaterStarts**|RawCodec|16||ro||
|**2786**|**ElectricalPreheaterCurrentPowerConsumption**|RawCodec|2||ro||
|**2791**|**CentralHeatingPumpStatus**|*O3EComplexType*|5||ro||
|**2792**|**MixerOneCircuitPumpStatus**|*O3EComplexType*|5||ro||
|**2793**|**MixerTwoCircuitPumpStatus**|*O3EComplexType*|5||ro||
|**2794**|**MixerThreeCircuitPumpStatus**|*O3EComplexType*|5||ro||
|**2795**|**MixerFourCircuitPumpStatus**|*O3EComplexType*|5||ro||
|**2796**|**ExternalHeaterConfiguration**|*O3EComplexType*|2||ro||
|**2797**|**VentilationBypassFlapAvailableCount**|O3EByteVal|1||ro||
|**2798**|**RelativeHumiditySensorSelection**|O3EByteVal|1||ro||
|**2799**|**ElectricalHeatersShutdownDelay**|O3EByteVal|1||ro||
|**2800**|**VentilationHeatExchangerType**|O3EByteVal|1||ro||
|**2801**|**VentilationFanAssignmentSwitchManufacturing**|O3EByteVal|1||ro||
|**2802**|**InverterSelfTestStatus**|RawCodec|6||ro||
|**2804**|**InverterSelfTestResultTwo**|RawCodec|151||ro||
|**2805**|**InverterSelfTestResultThree**|RawCodec|151||ro||
|**2806**|[**RefrigerationCircuitOperationMode**](## "Actual operating mode of the refrigeration circuit")|*O3EComplexType*|2||ro||
|**2807**|**InverterHousingTemperature**|RawCodec|9||ro||
|**2808**|**InverterInternalPowerModuleTemperature**|RawCodec|9||ro||
|**2809**|**PumpMinSpeedConfiguration**|RawCodec|1||ro||
|**2810**|**CentralHeatingPumpFeedbackSignalHandlingMode**|RawCodec|1||ro||
|**2826**|**FuelCellNetworkSystemProtectionErrorHistory**|RawCodec|40||ro||
|**2827**|**FuelCellNetworkSystemProtectionParameters**|RawCodec|48||ro||
|**2828**|**FuelCellSdCardRecording**|RawCodec|2||ro||
|**2829**|**ProductIdentification**|RawCodec|20||ro||
|**2830**|**EmergencyMode**|RawCodec|1||ro||
|**2831**|**BivalenceControlAlternativeTemperature**|O3EInt16|2||ro||
|**2832**|**BaseHeaterTimer**|RawCodec|4||ro||
|**2833**|**BaseHeaterTimerMode**|O3EInt8|1||ro||
|**2834**|**BaseHeaterTimerDuration**|O3EInt16|2||ro||
|**2835**|**BaseHeaterTemperatureThreshold**|O3EInt16|2||ro||
|**2836**|**SecondaryHeatExchangerMinimumVolumeFlowThreshold**|O3EInt16|2||ro||
|**2837**|**SecondaryHeatExchangerOptimumTemperatureSpreadExponent**|O3EInt16|2||ro||
|**2838**|**SecondaryHeatExchangerOptimumTemperatureSpreadHeating**|RawCodec|4||ro||
|**2839**|**SecondaryHeatExchangerOptimumTemperatureSpreadCooling**|RawCodec|4||ro||
|**2840**|**SecondaryHeatExchangerOptimumVolumeFlowDefrost**|O3EInt16|2||ro||
|**2842**|**SecondaryHeatExchangerHxSubcooling**|O3EInt16|2||ro||
|**2843**|**SecondaryHeatExchangerMinimumVolumeFlow**|O3EInt16|2||ro||
|**2844**|**SecondaryHeatExchangerMinimumOutletTemperature**|O3EInt16|2||ro||
|**2845**|**SecondaryHeatExchangerMaximumOutletTemperature**|O3EInt16|2||ro||
|**2847**|**CrankCaseHeaterStatistics**|RawCodec|8||ro||
|**2848**|**CrankCaseHeaterTemperatureStatistics**|O3EInt16|2||ro||
|**2849**|**CrankCaseHeaterOnTimer**|RawCodec|27||ro||
|**2850**|**InstalledHeater**|*O3EComplexType*|3||ro||
|**2851**|**PreStartDuration**|O3EInt16|2||ro||
|**2852**|**FanDuctHeater**|O3EByteVal|1||ro||
|**2853**|**ExternalHeaterTimeIntegralThershold**|O3EInt16|2||ro||
|**2855**|**MixerOneCircuitFrostProtectionConfiguration**|*O3EComplexType*|3||ro||
|**2856**|**MixerTwoCircuitFrostProtectionConfiguration**|*O3EComplexType*|3||ro||
|**2857**|**MixerThreeCircuitFrostProtectionConfiguration**|*O3EComplexType*|3||ro||
|**2858**|**MixerFourCircuitFrostProtectionConfiguration**|*O3EComplexType*|3||ro||
|**2874**|**PrimarySourceRpsOne**|O3EInt16|2||ro||
|**2875**|**PrimarySourceRpsTwo**|O3EInt16|2||ro||
|**2876**|**PrimaryPumpCommonSetpoint**|O3EInt16|2||**rw**||
|**2877**|**SuctionSuperheatSetpoint**|O3EInt16|2||**rw**||
|**2878**|**SubcoolingSetpoint**|O3EInt16|2||**rw**||
|**2879**|**MixerOneCircuitHeatingBlocked**|RawCodec|2||ro||
|**2880**|**MixerTwoCircuitHeatingBlocked**|RawCodec|2||ro||
|**2881**|**ExpansionValveOneTimer**|RawCodec|4||ro||
|**2882**|**ExpansionValveTwoTimer**|RawCodec|4||ro||
|**2883**|**ExpansionValveMaximumOperatingPressureTemperatureSetpoint**|O3EInt16|2||**rw**||
|**2884**|**ExpansionValveOneStatus**|O3EInt16|2||ro||
|**2885**|**ExpansionValveTwoStatus**|O3EInt16|2||ro||
|**2886**|**RefrigerantCyclePostStopDuration**|O3EInt16|2||ro||
|**2887**|**RefrigerantCycleAlarmPauseDuration**|O3EInt16|2||ro||
|**2888**|**RefrigerantCyclePumpdownStoppingDelay**|O3EInt16|2||ro||
|**2889**|**RefrigerantCycleTimers**|RawCodec|6||ro||
|**2890**|**RefrigerantCyclePumpdownHoldTimer**|O3EInt16|2||ro||
|**2891**|**RefrigerantCycleDefrostTimers**|RawCodec|6||ro||
|**2892**|**RefrigerantCycleTransitionToHeatingTimer**|O3EInt16|2||ro||
|**2893**|**RefrigerantCycleTransitionToCoolingTimer**|O3EInt16|2||ro||
|**2894**|**RefrigerantCycleAvailability**|O3EByteVal|1||ro||
|**2895**|**PrimaryPumpSettings**|RawCodec|5||ro||
|**2896**|**PrimaryPumpOneStatus**|O3EInt8|1||ro||
|**2897**|**PrimaryPumpTwoStatus**|O3EInt8|1||ro||
|**2908**|**InverterModuleType**|O3EInt8|1||ro||
|**2909**|**CompressorMinMaxRequestedSecondaryReturnTemperatureCooling**|RawCodec|4||ro||
|**2910**|**CompressorMinMaxRequestedSecondaryReturnTemperaturePreStartDefrost**|RawCodec|4||ro||
|**2911**|**CompressorMaximumRequestedSecondaryReturnTempDefrost**|O3EInt16|2||ro||
|**2912**|**CompressorMaximumDischargeTemperature**|O3EInt16|2||ro||
|**2913**|**CompressorMinimumAllowedSecondaryOutletTemperatureHeating**|O3EInt16|2||ro||
|**2914**|**CompressorMinMaxAllowedPrimaryTemperatureCooling**|RawCodec|4||ro||
|**2915**|**CompressorMaximumCondensingPressure**|O3EInt16|2||ro||
|**2916**|**CompressorMaximumEvaporatingPressure**|O3EInt16|2||ro||
|**2917**|**CompressorMinimumEvaporatingPressureHeating**|O3EInt16|2||ro||
|**2918**|**CompressorMinimumEvaporatingPressureCooling**|O3EInt16|2||ro||
|**2920**|**ExternalHeaterSpecification**|RawCodec|2||ro||
|**2921**|**DiagnosticHydraulicFilterIntervalSettings**|RawCodec|2||ro||
|**2922**|**DiagnosticHydraulicFilterIntervalTemporalSettings**|RawCodec|2||ro||
|**2923**|**DiagnosticSecondaryFourThreeWayValveSettings**|RawCodec|6||ro||
|**2924**|**DiagnosticHydraulicFilterContaminationSettings**|RawCodec|4||ro||
|**2925**|**DiagnosticMonitoringPressurePeaksSettings**|RawCodec|2||ro||
|**2926**|**DiagnosticMonitoringPressureDropSettings**|RawCodec|6||ro||
|**2927**|**DiagnosticElectronicExpansionValveSettings**|O3EInt8|1||ro||
|**2928**|**DiagnosticHeatExchangerConstraintsSettings**|O3EInt16|2||ro||
|**2929**|**DiagnosticRefrigerantCircuitPressureSensors**|O3EInt8|1||ro||
|**2930**|**DiagnosticRefrigerantCircuitFourTwoWayValve**|O3EInt8|1||ro||
|**2931**|**DiagnosticRefrigerantCircuitTemperatureSensors**|O3EInt8|1||ro||
|**2932**|**TimeCounterSinceLastReset**|RawCodec|4||ro||
|**2934**|**CurrentElectricalSystemPowerSetpoint**|O3EInt32|4||**rw**||
|**2936**|**ElectricalEnergyStorageSystemState**|RawCodec|3||ro||
|**2937**|**SystemPumpConfiguration**|RawCodec|2||ro||
|**2938**|**CascadeSystemPump**|RawCodec|4||ro||
|**2939**|**PrimaryHeatExchangerLowEvaporatingTemperatureAlarmDelay**|O3EInt16|2||ro||
|**2940**|**ExternalHeaterDelayTimer**|*O3EComplexType*|3||ro||
|**2942**|**ListOfLayerSettingServiceDevices**|RawCodec|137||ro||
|**2944**|**NodeIdOnExternalCan**|O3EByteVal|1||ro||
|**2945**|**PointOfCommonCouplingEnergyMeterConnectedPhases**|RawCodec|1||ro||
|**2946**|**EnergyConsumptionElectricalPreHeater**|RawCodec|24||ro||
|**2947**|**SleepModePrevention**|RawCodec|5||ro||
|**2952**|**ListOfLayerSettingServiceDevicesTwo**|RawCodec|137||ro||
|**2953**|**CascadeSystemConfigurationArray**|RawCodec|10||ro||
|**2956**|**DeviceDigitalInputEightValue**|O3EInt8|1||ro||
|**2957**|**DeviceDigitalInputNineValue**|O3EInt8|1||ro||
|**2969**|**ElectronicControlUnitSafeStateStatus**|O3EByteVal|1||ro||
|**2985**|**ExternalHeaterTemperatureSetpoint**|O3EInt16|2||**rw**||
|**2986**|**ExternalHeaterOperationState**|O3EByteVal|1||**rw**||
|**2987**|**RefrigerantCycleUnlock**|O3EInt8|1||ro||
|**2996**|**BatteryAmbientTemperatureHistogramTwoPointFour**|RawCodec|40||ro||
|**2997**|**BatteryTemperatureHistogramTwoPointFour**|RawCodec|56||ro||
|**2998**|**HardwareSignalCheckCsc**|RawCodec|8||ro||
|**2999**|**ElectricalHeatersOperationHours**|RawCodec|16||ro||
|**3000**|**EcuResetInformationList**|RawCodec|115||ro||
|**3001**|**LowEvaporatingLowCondensingDriveDuration**|RawCodec|196||ro||
|**3002**|**MidEvaporatingLowCondensingDriveDuration**|RawCodec|196||ro||
|**3003**|**HighEvaporatingLowCondensingDriveDuration**|RawCodec|196||ro||
|**3004**|**LowEvaporatingHighCondensingDriveDuration**|RawCodec|196||ro||
|**3005**|**MidEvaporatingHighCondensingDriveDuration**|RawCodec|196||ro||
|**3006**|**HighEvaporatingHighCondensingDriveDuration**|RawCodec|196||ro||
|**3008**|**FanDuctHeaterOnDuration**|O3EInt16|2||ro||
|**3009**|**FanDuctHeaterOnTimer**|RawCodec|4||ro||
|**3013**|**MixerHybridThreeWayValvePositionPercent**|RawCodec|2||ro||
|**3014**|**OutdoorMiddleCoilTemperatureSensor**|*O3EComplexType*|9||ro||
|**3015**|**HeatSinkTemperatureSensor**|*O3EComplexType*|9||ro||
|**3016**|[**HeatingBufferTemperatureSensor**](## "Actual temperature of the heating buffer")|*O3EComplexType*|9||ro||
|**3017**|**CoolingBufferTemperatureSensor**|*O3EComplexType*|9||ro||
|**3018**|**HeatingCoolingBufferTemperatureSensor**|*O3EComplexType*|9||ro||
|**3019**|**CompressorOutletTargetTemperature**|*O3EComplexType*|9||**rw**||
|**3029**|**DomesticHotWaterEfficiencyMode**|O3EByteVal|1||ro||
|**3030**|**DomesticHotWaterEfficiencyModeAvailability**|RawCodec|2||ro||
|**3031**|**ExternalHeater**|RawCodec|2||ro||
|**3032**|**PrimaryEnergyFactorElectricity**|O3EInt16|2||ro||
|**3034**|**DomesticHotWaterReturnTemperaturTankLoadSystem**|*O3EComplexType*|9||ro||
|**3035**|**DomesticHotWaterFlowTemperaturTankLoadSystem**|*O3EComplexType*|9||ro||
|**3036**|**PrimaryEnergyFactorExternalHeater**|O3EInt16|2||ro||
|**3037**|**ElectricityPriceTimeScheduleMonday**|RawCodec|57||**rw**||
|**3038**|**ElectricityPriceTimeScheduleTuesday**|RawCodec|57||**rw**||
|**3039**|**ElectricityPriceTimeScheduleWednesday**|RawCodec|57||**rw**||
|**3040**|**ElectricityPriceTimeScheduleThursday**|RawCodec|57||**rw**||
|**3041**|**ElectricityPriceTimeScheduleFriday**|RawCodec|57||**rw**||
|**3042**|**ElectricityPriceTimeScheduleSaturday**|RawCodec|57||**rw**||
|**3043**|**ElectricityPriceTimeScheduleSunday**|RawCodec|57||**rw**||
|**3056**|**NarrowBandInternetOfThingsNetworkStatus**|O3EInt8|1||ro||
|**3057**|**NarrowBandInternetOfThingsCloudStatus**|O3EInt8|1||ro||
|**3066**|**DomesticHotWaterHighDemandDetection**|RawCodec|4||ro||
|**3067**|**AirVolumeFlowValue**|RawCodec|9||ro||
|**3068**|[**DomesticHotWaterTemperatureSetpointComfort**](## "Temperature setpoint domestic hot water comfort")|O3EInt16|2|[°C](## "°C or °F (system configuration)")|**rw**||
|**3069**|**DomesticHotWaterSensorForDemand**|O3EByteVal|1||ro||
|**3070**|**BufferTargetOperationMode**|O3EByteVal|1||**rw**||
|**3085**|**ElectricalEnergyStorageModuleOneInformation**|RawCodec|18||ro||
|**3086**|**ElectricalEnergyStorageModuleTwoInformation**|RawCodec|18||ro||
|**3087**|**ElectricalEnergyStorageModuleThreeInformation**|RawCodec|18||ro||
|**3088**|**ElectricalEnergyStorageModuleFourInformation**|RawCodec|18||ro||
|**3089**|**ElectricalEnergyStorageModuleFiveInformation**|RawCodec|18||ro||
|**3090**|**ElectricalEnergyStorageModuleSixInformation**|RawCodec|18||ro||
|**3091**|**GatewayEthernetTwoEnable**|O3EByteVal|1||ro||
|**3092**|**GatewayEthernetTwoConfig**|RawCodec|21||ro||
|**3093**|**GatewayEthernetTwoIp**|RawCodec|20||ro||
|**3094**|**GatewayEthernetTwoNetworkStatus**|O3EByteVal|1||ro||
|**3095**|**MacAddressLanTwo**|RawCodec|6||ro||
|**3096**|**GatewayWifiStationEnable**|O3EByteVal|1||ro||
|**3097**|**GatewayInternetAccess**|O3EByteVal|1||ro||
|**3098**|**ExternalHeaterTemperatureOffset**|*O3EComplexType*|2||**rw**||
|**3103**|**IsCountryModeLoadInformation**|RawCodec|6||ro||
|**3106**|**BufferMinimumMaximumSetTemperature**|*O3EComplexType*|4||**rw**||
|**3107**|**BatteryModuleExchangeAssistent**|RawCodec|7||ro||
|**3108**|**PhotovoltaicsActivePowerLimitationRampRate**|RawCodec|9||ro||
|**3109**|**PrimaryHeatExchangerBaseHeaterStatistical**|RawCodec|8||ro||
|**3113**|**DeviceDigitalOutputOneValueStatistical**|RawCodec|8||ro||
|**3114**|**DeviceDigitalOutputTwoValueStatistical**|RawCodec|8||ro||
|**3115**|**DeviceDigitalOutputThreeValueStatistical**|RawCodec|8||ro||
|**3116**|**DeviceDigitalOutputFourValueStatistical**|RawCodec|8||ro||
|**3117**|**DeviceDigitalOutputFiveValueStatistical**|RawCodec|8||ro||
|**3119**|**RefrigerantCircuitFourWayValveStatistical**|RawCodec|8||ro||
|**3120**|**CompressorCrankCaseHeaterStatistical**|RawCodec|8||ro||
|**3129**|**FanDuctHeaterStatistical**|RawCodec|8||ro||
|**3134**|**DomesticHotWaterCirculationPumpStatistical**|RawCodec|8||**rw**||
|**3146**|**ElectricalHeaterPhaseOneStatistical**|RawCodec|8||ro||
|**3147**|**ElectricalHeaterPhaseTwoStatistical**|RawCodec|8||ro||
|**3148**|**ElectricalHeaterPhaseThreeStatistical**|RawCodec|8||ro||
|**3155**|**DomesticHotWaterShiftLoadPumpStatus**|RawCodec|5||ro||
|**3156**|**DomesticHotWaterShiftLoadPumpType**|O3EByteVal|1||ro||
|**3190**|**RefrigerantCircuitFourWayValvePosition**|O3EByteVal|1||ro||
|**3191**|**ExtendedEventLoggingHistory**|RawCodec|199||ro||
|**3212**|**BivalentMixerDomesticHotWaterTemperatureOffset**|*O3EComplexType*|2||**rw**||
|**3213**|**ExternalHeaterTemperatureSensor**|*O3EComplexType*|9||ro||
|**3215**|**ExternalHeaterSeparatorTemperatureSensor**|*O3EComplexType*|9||ro||
|**3228**|**EnergyMeterOne**|*O3EComplexType*|73||ro||
|**3229**|**EnergyMeterTwo**|*O3EComplexType*|73||ro||
|**3230**|**EnergyMeterThree**|*O3EComplexType*|73||ro||
|**3231**|**EnergyMeterFour**|*O3EComplexType*|73||ro||
|**3232**|**DomesticHotWaterBufferBottomTemperatureSensor**|*O3EComplexType*|9||ro||
|**3233**|**DomesticHotWaterBufferMidTemperatureSensor**|*O3EComplexType*|9||ro||
|**3234**|**DomesticHotWaterBufferTopTemperatureSensor**|*O3EComplexType*|9||ro||
|**3235**|**BufferLoadingTimeLimit**|O3EInt16|2||**rw**||
|**3282**|**DomesticHotWaterMinimumComfortTemperatureSetpoint**|O3EInt16|2|[°C](## "°C or °F (system configuration)")|**rw**||
|**3335**|**HeatingCoolingHysteresisHeatingCircuitOne**|*O3EComplexType*|8||ro||
|**3336**|**HeatingCoolingHysteresisHeatingCircuitTwo**|*O3EComplexType*|8||ro||
|**3337**|**HeatingCoolingHysteresisHeatingCircuitThree**|*O3EComplexType*|8||ro||
|**3338**|**HeatingCoolingHysteresisHeatingCircuitFour**|*O3EComplexType*|8||ro||
|**3366**|**ElectricalActivePowerStatusReport**|*O3EComplexType*|16||ro||
|**3384**|**ElectricalActivePowerConsumptionLimitationDefaultValue**|*O3EComplexType*|4||ro||

