# ViGuide Demo App Analysis — Approach and Results

## Source Material

File: `Viguide.Demo.V3.36.0.zip` (dated 2024-02-07)  
Extracted: Angular single-page application with one large bundled JavaScript file (`main.3260291c81ee1e8d.js`, 19 MB).

The app was the public demo version of ViGuide, Viessmann's installer/diagnostics tool.
It is no longer publicly accessible.

---

## Analysis Approach

### Step 1 — Identify what the app communicates with

The app uses the **Viessmann IoT Cloud REST API**
(`api.viessmann.com` / `api-integration.viessmann.com`).
It does **not** speak raw UDS/CAN — it consumes a high-level semantic API that abstracts
the underlying device protocol.

The API model: every piece of device state is a **feature** (dot-separated path, e.g.
`heating.circuits.0.heating.curve`). Each feature has named **properties** (sub-fields with
typed values) and optional **commands** (write actions with typed parameters).

### Step 2 — Extract embedded mock data

The demo app contains hardcoded mock API responses for several virtual device configurations
(timestamps: 2020-02, 2022-10, 2023-03). These are JavaScript object literals embedded
directly in the bundle.

Each mock object has the shape:
```javascript
{
    properties: {
        slope:  { value: 1.2, type: "number" },
        shift:  { value: 0,   type: "number" }
    },
    commands: { ... },
    feature:   "heating.circuits.0.heating.curve",
    deviceId:  "0",
    isEnabled: true,
    isReady:   true
}
```

### Step 3 — Systematic extraction

A Python script parsed all occurrences of `feature: "..."` in the bundle, walked backwards
to find the preceding `properties: { ... }` block for each, and extracted property names
and types. The same was done for `commands` blocks to identify writable features.

**Results:**
- **709 unique features** with at least one named property
- **138 features** with write commands (including parameter types)

The full extraction is reproduced at the end of this document. For details see [here](vg-features.txt).

---

## Key Findings

### What the Viguide data is good for

| Use case | Quality |
|----------|---------|
| Confirming semantic purpose of a DID | ✓ Good |
| Learning property/sub-field names for complex DIDs | ✓ Good |
| Identifying writable DIDs and their parameter types | ✓ Good |
| Determining byte-level structure (Int8/Int16/Float?) | ✗ Not possible |
| Determining scale factors | ✗ Not possible |
| 1:1 mapping of feature path → DID number | ✗ Not directly available |

### Limitation: abstraction layer

The cloud API shows semantic field names (`slope`, `shift`, `hours`, `starts`) but abstracts
away all byte-level encoding. One cloud feature may correspond to one or several CAN DIDs,
and the granularity differs from what open3e exposes.

### Relationship to existing open3e code

The comment at the top of `Open3Edatapoints.py` already references the ViGuide demo URL,
confirming the open3e team previously used it as a source. Many DID names in open3e
(e.g. `FlowTemperatureSensor`, `DomesticHotWaterSensor`) match the enum strings found in
the Viguide JS (`O.FlowTemperatureSensor`, `O.OutsideTemperatureSensor`, …).

---

## Notable Feature → DID Correlations

| Viguide feature | Properties | open3e DID(s) |
|---|---|---|
| `heating.sensors.temperature.outside` | `value: number`, `status: string` | 274 OutsideTemperatureSensor |
| `heating.circuits.0.heating.curve` | `slope: number`, `shift: number` | 880–883 MixerXCircuitCentralHeatingCurve |
| `heating.burners.0.statistics` | `hours: number`, `starts: number` | 1346 HeatEngineStatistical (partially) |
| `heating.compressors.0.statistics` | `hours: number`, `starts: number` | (unresolved) |
| `heating.compressors.0.statistics.load` | `hoursLoadClassOne..Five: number` | (unresolved) |
| `heating.gas.consumption.fuelCell` | `day[], month[], week[], year[]` | 1348 FuelCellGasConsumption + 1349/1350 matrices |
| `pcc.ac.active.current` | `phaseOne`, `phaseTwo`, `phaseThree`, `total: number` | 2144 PointOfCommonCouplingAcActiveCurrent |
| `device.timeseries.water.pressure.peaks` | `countOne..Four`, `timestampOne..Four` | 1787 TimeSeriesRecordedWaterPressurePeaks |
| `heating.noise.reduction` | `active: boolean`, `changeableByEndCustomer: boolean` | 2540 NoiseReductionSettings |

---

## Writable Features (selection)

| Feature | Command | Parameters |
|---|---|---|
| `heating.circuits.N.operating.modes.active` | `setMode` | `mode: string` |
| `heating.circuits.N.heating.curve` | `setCurve` | `slope: number` |
| `heating.circuits.N.operating.programs.normal` | `setTemperature` | `targetTemperature: number` |
| `heating.circuits.N.operating.programs.comfort` | `setTemperature`, `activate` | `temperature: number` |
| `heating.dhw.temperature` | `setTargetTemperature` | `temperature: number` |
| `heating.dhw.operating.modes.active` | `setMode` | `mode: string` |
| `ventilation.operating.modes.active` | `setMode` | `mode: string` |
| `heating.configuration.pressure.total` | `setNormalRange` | `defaultPressure: number` |

---

## RawCodec DIDs Not Resolved

The following Matrix-named RawCodec DIDs have no matching template because their sizes do
not fit any known pattern:

| DID | Name | Bytes | Reason |
|-----|------|-------|--------|
| 449 | ElectricalEnergyMatrix | 141 | Unusual size, no template |
| 952 | HydraulicMatrix | 51 | Different data type (hydraulic config) |
| 1549 | HydraulicMatrixConfiguration | 97 | Different data type |
| 1550 | FunctionMatrix | 22 | Different data type |
