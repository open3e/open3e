**_New: List of data points now available as [table](https://github.com/open3e/open3e/blob/dids_to_markdown/src/open3e/Open3Edatapoints.md)_**

**_New: Tool `open3e_dids2md` can create your own list of data points in markdown format. `open3e_dids2md -h` for options._**

**_New: All info about data points available as json files for [general dids](https://github.com/open3e/open3e/blob/dids_to_markdown/src/open3e/Open3Edatapoints.md) and [variant dids](https://github.com/open3e/open3e/blob/dids_to_markdown/src/open3e/Open3EdatapointsVariants.md)_**

**_New: Web UI for browser-based configuration and monitoring_**

<BR>

# Open3E interface

* Connects E3 'OneBase' device through CAN UDS or doip
* Read data points
* Listen to commands on mqtt
* Write data points in raw and json data format
* Experimental write support for service 77
* **Web UI** for configuration, live monitoring, and Home Assistant integration

# Web UI

open3e includes a browser-based management interface for configuring and monitoring Viessmann heat pumps. All configuration (CAN interface, MQTT broker, Home Assistant discovery, datapoint polling) is done through the web UI — no CLI arguments needed.

## Features

* **Dashboard** with live data cards and time-series charts (uPlot)
* **Datapoints browser** with search, filter by ECU/priority, bulk enable/disable
* **Priority-based polling** — High (every cycle), Medium (every 4th), Low (every 12th), Off
* **Write values** with categorized DIDs, enum dropdowns, sub-field support
* **MQTT publishing** with JSON or split mode, retained state messages, change detection
* **Home Assistant MQTT auto-discovery** with 100+ typed entity inference rules
* **Per-sub-field HA entities** for ComplexType DIDs (e.g., PowerState/ErrorState separately)
* **50+ writable HA entities** — number sliders, select dropdowns, switches, buttons
* **Operation Mode control** — set mixer circuits and DHW to Off/Heating/Cooling from HA
* **System depiction** (ECU/DID scan) with live progress bar and console output
* **CAN interface discovery** and configuration (simple + advanced parameters)
* **Database backup/restore/download** via web interface
* **Optional password authentication**
* **System status** with CAN bus counters, engine state, MQTT connection info

## Installation

### Prerequisites

* Linux host with SocketCAN (Raspberry Pi, any Linux with CAN adapter)
* Python 3.9+
* CAN interface connected to the Viessmann heat pump's internal bus

### Option 1: pip install (recommended)

Create a virtual environment and install with web dependencies:

    python3 -m venv .venv
    source .venv/bin/activate
    pip install git+https://github.com/open3e/open3e.git[web]

### Option 2: From source (for development)

    git clone https://github.com/open3e/open3e.git
    cd open3e
    python3 -m venv .venv
    source .venv/bin/activate
    pip install --editable ".[dev,web]"

### Option 3: Docker Compose

    git clone https://github.com/open3e/open3e.git
    cd open3e/docker
    docker compose up -d

Uses host networking for SocketCAN access. See `docker/docker-compose.yml` for details.

## Starting the Web UI

    source .venv/bin/activate
    open3e-web

The server starts on port 8080. Open `http://<your-ip>:8080` in your browser.

## Auto-start with systemd

Create `/etc/systemd/system/open3e-web.service`:

```ini
[Unit]
Description=open3e Web UI
After=network-online.target

[Service]
Type=simple
User=<your-user>
WorkingDirectory=/home/<your-user>/open3e
ExecStart=/home/<your-user>/open3e/.venv/bin/open3e-web
Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target
```

Replace `<your-user>` with your Linux username, then:

    sudo systemctl daemon-reload
    sudo systemctl enable open3e-web
    sudo systemctl start open3e-web

## First-Run Setup

1. **CAN interface** — Settings > CAN tab: select interface (e.g., `can0`), set bitrate (250000), apply
2. **System Depiction** — scan for ECUs and datapoints (takes 10-20 minutes)
3. **Datapoints** — enable polling for the values you need, set priorities (High/Medium/Low)
4. **MQTT** (optional) — Settings > MQTT tab: configure broker host/port/credentials, test, save
5. **Home Assistant** (optional) — Settings > HA tab: apply suggested defaults, publish discovery

After first run, all settings are persisted in `open3e_web.db` and auto-restored on next launch.

## Home Assistant Integration

The web UI publishes MQTT auto-discovery messages that Home Assistant picks up automatically. Entities include:

* **Sensors** — temperatures, pressures, energy, power, flow rates, compressor stats
* **Number sliders** — temperature setpoints (Comfort/Standard/Reduced), pump limits
* **Select dropdowns** — operation modes (Off/Heating/Cooling) for each mixer circuit and DHW
* **Switches** — one-time DHW heating, external control enable

All entity types, units, and icons are inferred from the datapoint names using 100+ pattern-matching rules. ComplexType DIDs get separate entities for each sub-field (e.g., `HeatPumpCompressor` splits into `PowerState` and `ErrorState`).

# Smart Home Integrations and Add Ons

The following integrations and add ons are available to use open3e functionality within smart home applications:
* **HomeAssistant Integration**: Automatically connects to the Open3e server and handles automatic device/integration/entity setup based on configuration sent by Open3e. Data is then automatically refreshed. Refer to https://github.com/MojoOli/open3e-ha and https://github.com/open3e/open3e/wiki/090-Homeassistant
* **HomeAssistant Add-On**: If you have your CAN Adapter attached to the device which is running HomeAssistant you can run this Add-on to read the data from CAN. It is working good together with the HomeAssistant Integration mentioned above. Refer to https://github.com/flecke-m/ha-addons/tree/main/open3e Please note the HomeAssistant dependency that the Add-On only works with HAOS and Supervised installations see: https://www.home-assistant.io/installation/
* **Adapter for ioBroker**: Adapter ioBroker.e3oncan is based on open3e and completely replaces open3e. Thus, no installation of open3e is needed when using the adapter. Refer to https://github.com/MyHomeMyData/ioBroker.e3oncan and https://github.com/open3e/open3e/wiki/095-ioBroker-Adapter
* Open3E is also available for **docker** environment. Refer to https://hub.docker.com/u/fleckem
* Using **Smart Grid Ready Function** of Vitocal 250: Refer to https://github.com/open3e/open3e/wiki/099-%C3%9Cber-openE3-hinaus-%E2%80%90-Smart-Grid-Ready

You created your own extension based on open3e? Great! Please let us know! Just add a new [discission topic](https://github.com/open3e/open3e/discussions).

# Installation
There is a [Video Tutorial](https://youtu.be/u_fkwtIARug) (German languge) available from CRYDTEAM - thank you very much for it! Find the according web site [here](https://crydteam.de/2025/04/27/viessmann-vx3-in-homeassistant/). The final 1/3 is related to Home Assistant, but the first part shows the complete installation process of open3e and hardware very vividly.

For a **detailed step-by-step installation guide** (German language) see [Wiki, chapt. 030](https://github.com/open3e/open3e/wiki/030-Installation-und-Inbetriebnahme-von-open3E).

<br>

For a fresh Raspberry PI install git, python3 and python-pip first:

    sudo apt install git python3 python3-pip  

Optional, but highly recommended is creating a virtual environment before the installation. Basic instructions, see here: https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#create-and-use-virtual-environments

Now install the latest version of open3e via

    pip install git+https://github.com/open3e/open3e.git

or for the develop branch

    pip install git+https://github.com/open3e/open3e.git@develop

This will install open3e along with all dependencies.

If you get the error "error: externally-managed-environment" you could add *--break-system-packages* to the previous command, but better install using a virtual environment - venv<br>
(please see: https://stackoverflow.com/questions/75608323/how-do-i-solve-error-externally-managed-environment-every-time-i-use-pip-3)  

## Update/upgrade to latest Version (later)
Please see Wiki
https://github.com/open3e/open3e/wiki/030-Installation-und-Inbetriebnahme-von-open3E#open3e-aktualisieren 

# Setup CAN Bus
    sudo ip link set can0 up type can bitrate 250000

# Depict System
In advance of first time starting the client and after every firmware update, run 
    
    open3e_depictSystem -s
    
to scan the system and generate devices.json and Open3Edatapoints_6yz.py files.<br>
Use `open3e` with cmd line argument `-cnfg devices.json` afterwards.<br>
Pls. make sure to use same working directory for `open3e` as used for running `open3e_depictSystem`.<br>
By using the optional switch `-s` data files for simulation get created. 

To refer to a specific device, you have to use "complex addressing mode", e.g. to read dids 268 and 269 of device 0x680 use `-cnfg devices.json -r 0x680.268,0x680.269`.
Do not use option `-dev` in this context.

It's possible to change naming of devices by editing `devices.json`:
When you change `"0x680": {` to `"vitocal": {` you can use read commands like `-r vitocal.268,vitocal.269`.
New naming will also be used for paramter `{device}`within MQTT topics (see below).

Further information is available [here](https://github.com/open3e/open3e/wiki/032-Command-Line-Arguments).

The depicting scans take several minutes (usually 10..20) - please be patient!

Infos about data points are available [here](https://github.com/open3e/open3e/blob/dids_to_markdown/src/open3e/Open3Edatapoints.md).

# Usage

For more detailed description of the command line arguments see also the [according section](https://github.com/open3e/open3e/wiki/032-Command-Line-Arguments) in the Wiki.

    usage: open3e [-h] [@argsfile] [-c CAN] [-d DOIP] [-dev DEV] [-a] [-r READ] [-raw] [-w WRITE] [-f77] [-t TIMESTEP] [-m MQTT] [-mfstr MQTTFORMATSTRING] [-muser MQTTUSER:PASSW] [-mcid mqtt-client-id] [-j] [-v] [-l CMND-TOPIC] [-tx ECUADDR] [-cnfg DEVICES.JSON]

    options:
    -h, --help              show this help message and exit
    -c CAN, --can CAN       use can device, e.g. can0. `-c can0` is default, can be omitted.
    -d DOIP, --doip DOIP    use doip access, e.g. 192.168.1.1
    (*)-dev DEV, --dev DEV     boiler type --dev vdens or --dev vcal || pv/battery --dev vx3, --dev vair(*)
    -a, --scanall           dump all dids
    -r READ, --read READ    read did, e.g. 257,258
    -raw, --raw             return raw data for all dids
    -w WRITE, --write WRITE
                            write did, e.g. `-w 396=D601 -raw` 
    -f77, --forcesid77      force the use of serive 0x77 for writing of a did
    -t TIMESTEP, --timestep TIMESTEP (seconds)
                            read continuous with delay in s
    -m MQTT, --mqtt MQTT  publish to server, e.g. 192.168.0.1:1883:TOPICNAME
    -mfstr MQTTFORMATSTRING, --mqttformatstring MQTTFORMATSTRING
                            mqtt formatstring e.g. {ecuAddr:03X}_{device}_{didNumber:04d}_{didName}
    -muser MQTTUSER:PASSW, --mqttuser MQTTUSER:PASSW
                            mqtt username:password
    -mcid MQTT-CLENT-ID, --mqttclientid MQTT-CLENT-ID
                            set mqtt client id of open3e
    -tx ECUADDR, --ecuaddr ECUADDR
                            sets the default ECU Address different from 0x680
    -cnfg DEVICES.JSON, --config DEVICES.JSON 
                            use multi-ECU configuration file. `-cnfg devices.json` created by Open3E_depictSystem is default, can be omitted.
    -j, --json              send JSON structure via MQTT
    -v, --verbose           verbose info
    -l, --listen            mqtt topic to listen for commands, e.g. `open3e/cmnd`
    @argsfile               use arguments given in a file. Seperate line for each argument. No linebreak after final entry. 

(*) **Attention!** The option `-dev DEV, --dev DEV` is deprecated and may be removed in future versions. 

Since V0.4.0 `-cnfg devices.json` is default and does not need to get specified.

Since V0.5.0 all data point codecs definitions are checked for correct length values. If you get an assert error please check you customer specific data point codec definitions!

<br>

**IMPORTANT: When addressing sub-items of data points, ALWAYS use `ecu.did.sub` format (including ecu!)**
otherwise intended `did.sub` will get interpreted as `ecu.did` and cause unintended access or failure!

**For details regarding the different ways of addressing data points (complex, named) [refer to the Wiki](https://github.com/open3e/open3e/wiki/032-Command-Line-Arguments#komplexe-adressierung)**

**Remark: Do not start more than one instance of open3e!** Doing so, could lead to conflicts on CAN bus causing open3e to stop with errors.
If you want to read several lists of data points with diffetent time schedules or you want to read and write data points in parallel, pls. use listener mode of open3e (see below). It's possible to add a read command when starting the listener mode.

**_regarding the following examples: Please be aware of that not all data points exist with every device._**

# Read DIDs

    open3e -c can0 -cnfg devices.json -r 268 -v
    268 FlowTempSensor 27.2

    open3e -c can0 -cnfg dev -r 318 -v
    318 WaterPressureSensor 1.8 

    open3e -c can0 -r 377 -v
    377 IdentNumber 7XXXXXXXXXXXXX 

    open3e -r 1043 -v
    1043 FlowMeterSensor 2412.0 

    open3e -r 1664 -v
    1664 ElectricalEnergyStorageStateOfCharge 44 

    open3e @myargs
        with content of file myargs:
        -c
        can0
        -cnfg
        devices.jsom
        -r
        1664
        -v
    
    open3e -r 424 -v
    0x680 424 MixerOneCircuitRoomTemperatureSetpoint {"Comfort": 23.0, "Standard": 21.0, "Reduced": 15.0, "Increased": 0.0, "Duration": 0}
    
    open3e -r MixerOneCircuitRoomTemperatureSetpoint
    {"Comfort": 23.0, "Standard": 21.0, "Reduced": 15.0, "Increased": 0.0, "Duration": 0}

    open3e -r 0x680.MixerOneCircuitRoomTemperatureSetpoint.Comfort
    22.0


# Interval Readout
    open3e -r 1043 -t 1
    2412.0
    2413.0
    2411.0
    2412.0
    ...
  

# Write DID
(more details [on Wiki](https://github.com/open3e/open3e/wiki/032-Command-Line-Arguments#lesen--schreiben-per-kommandozeile))
## Using raw data format
    open3e -raw -w 396=D601
    -> sets domestic hot water setpoint to 47degC

## Using encoder data format     
    open3e -w 396=47.5

    open3e -w TimeSettingSource=NetworkTimeProtocol

    open3e -w 0x680.MixerOneCircuitRoomTemperatureSetpoint.Comfort=23

    open3e -w 0x680.ExternalDomesticHotWaterTargetOperationMode.Mode=1

## Using json data format
**Remark on using JSON data format:** In open3e the order of the data elements is relevant. E.g. passing `{"Mode": 1, "State": 0}` will work for DID 538, passing `{"State": 0, "Mode": 1}` will not. We recommend first reading a data point in JSON format and then using the result as a template to create the write access command.

    open3e -j -w 396=47.5
    -> sets domestic hot water setpoint to 47.5degC

    open3e -j -w 538='{"Mode": 1, "State": 0}'
    -> sets ExternalDomesticHotWaterTargetOperationMode.Mode to 1 and .State to 0
    -> Use -j -r to read data point in json format as template for writing. Always provide valid and complete json data for writing, enclosed in single quotes.
 
    open3e -j -w 0x6a1.2214='{"DischargeLimit": 20.0, "Unknown": 0.0}'
    -> sets BackupBoxConfiguration.DischargeLimit to 20% on VX3 on ECU-address 0x6a1

## Using complex addressing

    open3e -w 0x6a1.BackupBoxConfiguration.DischargeLimit=20.0
    -> sets BackupBoxConfiguration.DischargeLimit to 20% on VX3 on ECU-address 0x6a1

## Extended writing service (internal can bus only, experimental)
In case of a "negative response" code when writing data, you may try to use the command line option -f77. However, this is experimental. Always verify the result!

# Publish data points to mqtt
    open3e -r 268,269,271,274,318,1043 -m 192.168.0.5:1883:open3e -t 1
    -> will periodically scan data points and publish data to broker 192.168.0.5 

    open3e -r 268,269,271,274,318,1043 -m 192.168.0.5:1883:open3e -t 1 -mfstr "{didNumber}_{didName}"
    -> will publish with custom identifier format: e.g. open3e/268_FlowTemperatureSensor 

# Listener mode
    open3e -m localhost:1883:open3e -mfstr "{didNumber}_{didName}" -l open3e/cmnd
    
    will listen for commands on topic open3e/cmnd with payload in json format:
    {"mode":"read"|"read-raw"|"read-pure"|"read-all"|"write"|"write-raw"|"write-sid77"|"write-raw-sid77"|"system", "data":[list of data], "addr":"ECU_addr"}
    rem: "addr" is optional, otherwise default ECU address used
    
    open3e -m localhost:1883:open3e -mfstr "{didNumber}_{didName}" -l open3e/cmnd -r 0x6a1.1603,0x6a1.1831 -t 15 -m localhost:1883:open3e

    will listen for commands on topic open3e/cmnd and read & publish dids 1603 and 1831 of device 0x6a1 every 15 seconds

    Examples for commands sent via mqtt:

    to read dids 271 and 274:
    {"mode": "read", "data":[271,274]}
    
    to read dids 265 and 266 as JSON-objects (even w/o option -json):
    {"mode": "read-json", "data":[265,266]}
    
    it's possible to use complex addressing mode:
    {"mode": "read-json", "data":[256,257,396,"0x6a1.[257,259,261]","0x6a1.256.BusType"]}
    IMPORTANT REMARK: Quotes must be used for complex addressing. The ECU-address must be specified in Python hex format (leading 0x), e.g. 0x680

    to read dids 265 and 266 as raw data (even w/o option -raw):
    {"mode": "read-raw", "data":[265,266]}
    
    to write value of 21.5 to did 395 and value of 45.0 to did 396 (Use a list of tuples to write data):
    {"mode": "write", "data":[[395,21.5],[396,45.0]]}

    to write a discharge limit of 20% to did 2214 (BackupBoxConfiguration) to VX3 on ECU address 0x6a1 as json object:
    {"mode":"write", "data":[[2214,{"DischargeLimit": 20.0, "Unknown": 0.0}]], "addr":"0x6a1"}

    doing the same thing using Sub-DID addressing:
    {"mode":"write", "data":[["2214.DischargeLimit",20.0]], "addr":"0x6a1"}

    doing the same thing again using complex addressing:
    {"mode":"write", "data":[["0x6a1.2214.DischargeLimit",20.0]]}

    to write value of 45.0 to did 396 using service 0x77 (internal can bus only, experimental):
    {"mode": "write-sid77", "data":[[396,45.0]]}

    to write value of 45.0 to did 396 in raw data format using service 0x77 (internal can bus only, experimental):
    {"mode": "write-raw-sid77", "data":[[396,"C201"]]}

    to set frost protect threshold to -9°C in complex did
    (A6FF lsb..msb -> 0xFFA6 -> -90 -> -9.0°C; Byte 0 unchanged):
    {"mode": "write-raw", "data":[[2855,"01A6FF"]]}

    to set frost protect threshold and eco function threshold to -9°C (complex dids):
    {"mode": "write-raw", "data":[[2855,"01A6FF"],[2426,"01A6FF000A00"]]}

    to request system information which is then published on the system topic, e.g. open3e/system, as json:
    {"mode": "system"}

 
    Option -m is mandatory for this mode.
    Options -r, -t, -j, -v may be used in parallel.

# Convert list of data points to json format
Use
```
open3e_dids2json
```
to convert common list of data points (Open3Edatapoints.py, Open3EdatapointsVariants.py) to json format.
This tool converts data points for use in the ioBroker adapter ioBroker.e3oncan. It is not used by open3e.

# Convert list of data points to markdown format
Use
```
open3e_dids2md -h
```
to see the options for creating your own list of data points. Use a viewer for markdown format to view it.

**Hint**: Choose a viewer supporting mouser-over feature of markdown.

# For developers

If you want to work on the codebase you can clone the repository and work in "editable" mode as follows. The editable mode allows you to modify and test changes in the source code without the need of a re-installation.

    git clone https://github.com/open3e/open3e.git  
    cd open3e
    pip install --editable ".[dev,web]"

**Hint: If you get an error like "A "pyproject.toml" file was found, but editable mode currently requires a setup.py based build." you are running an old pip version. Editable mode requires pip version >= 21.1.**

# Changelog

### 0.7.0 (2026-04-07)
* **New: Web UI** — browser-based management interface (`open3e-web`)
* Dashboard with live data cards and uPlot time-series charts
* Datapoints browser with search, filter, priority control, bulk actions
* Priority-based CAN polling: High (every cycle), Medium (every 4th), Low (every 12th), Off
* MQTT publishing with change detection, retained state messages, JSON/split mode
* Home Assistant MQTT auto-discovery with smart type inference (100+ rules)
* Per-sub-field HA entities for ComplexType DIDs
* 50+ writable HA entities (number, select, switch, button)
* CAN interface auto-discovery and configuration via web
* System depiction with live progress bar, cancel, and auto-load results
* Write values from the web UI with confirmation dialog
* Database backup/restore/download
* Optional password authentication
* Docker Compose deployment with host networking for SocketCAN
* Systemd service support for auto-start on boot

### 0.6.1 (2026-02-24)
* Introduced list of data points in markdown format.
* Added meta data to several data points, e.g. description, unit, link to further info
* Added tool to create user defined list of data points in markdown format
* Added meta data to json formated data points as well

### 0.6.0 (2026-02-07)
* Introduced list of data points (Open3EdatapointsVariants.py) with lengths different from common data points. Via open3e_depictSystem open3e can handle those device specific data points.

### 0.5.10 (2025-12-10)
* Added support for data points 511-520
* Added support for complex addressing mode for listener mode
* Bugfix: Writing of time value (e.g. "11:30") via MQTT did not work
* Added infos about Smart Home integrations to Readme

### 0.5.9 (2025-09-19)
* Fixed issue #274 (addressing mode `0x068c.[505,506]`)

### 0.5.8 (2025-07-08)
* Added support for data points 2405-2408, 2643, 3335-3338
* Improved support for sub-dids
* Improved handling for undefined codecs

### 0.5.7 (2025-06-15)
* Added support for data points 2413-2416 & 2452-2455

### 0.5.6 (2025-06-04)
* Added support for data points of energy meters, DIDs 3228 to 3231

### 0.5.5 (2025-04-22)
* Output on command line always uses json data format

### 0.5.x (2025-03-14)
* Reading and writing of subs and using plain text implemented:<br>
`open3e -r 0x680.256.2` returns `{'ID': 31, 'Text': 'HPMUMASTER'}`<br>
`open3e -r 0x680.BusIdentification.DeviceProperty` returns the same result,<br>
`open3e -r Vical.BusIdentification.DeviceProperty` also the same if you named your 0x680 ECU to 'Vical' in devices.json.<br>
Same way working with writing values. Text and numeric form can get mixed. Case not sensitive. Can be used with 'complete' datapoints as well.
* Defaults `-c can0` and `-cnfg devices.json` implemented so no need to specify 'usually' (except you use different settings). If devices.json not found arg default will be ignored.
* All data point codecs defined are checked for correct length values. If you get an assert error please check you customer specific data point definitions!
* System information, specifically connected devices and their features, is now published when requesting it via the command `{"mode": "system"}`.
