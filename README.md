**_New: Explicit writing of sub-items of a DID, specifying DIDs and Subs by name instead of number posible._**

<BR>

# Open3E interface

* Connects E3 'OneBase' device through CAN UDS or doip
* Read data points
* Listen to commands on mqtt
* Write data points in raw and json data format
* Experimental write support for service 77 (NOT implemented for listener mode yet)

## What's new with version 0.5.x:
* Reading and writing of subs and using plain text implemented:<br>
`open3e -r 0x680.256.2` returns `{'ID': 31, 'Text': 'HPMUMASTER'}`<br>
`open3e -r 0x680.BusIdentification.DeviceProperty` returns the same result,<br>
`open3e -r Vical.BusIdentification.DeviceProperty` also the same if you named your 0x680 ECU to 'Vical' in devices.json.<br>
Same way working with writing values. Text and numeric form can get mixed. Case not sensitive. Can be used with 'complete' datapoints as well.
* Defaults `-c can0` and `-cnfg devices.json` implemented so no need to specify 'usually' (except you use different settings). If devices.json not found arg default will be ignored.
* All data point codecs defined are checked for correct length values. If you get an assert error please check you customer specific data point definitions!

# Installation
Hint: An installation guide is available also in [German language](https://github.com/open3e/open3e/wiki/030-Installation-und-Inbetriebnahme-von-open3E).

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

# Setup CAN Bus
    sudo ip link set can0 up type can bitrate 250000

# Depict System
In advance of first time starting the client and after every firmware update, run 
    
    open3e_depictSystem [-s]
    
to scan the system and generate devices.json and Open3Edatapoints_678.py files.<br>
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
    0x680 424 MixerOneCircuitRoomTemperatureSetpoint {"Comfort": 22.0, "Standard": 20.0, "Reduced": 18.0, "Unknown2": "0000", "Unknown1": 0}

    open3e -r MixerOneCircuitRoomTemperatureSetpoint
    {'Comfort': 22.0, 'Standard': 20.0, 'Reduced': 18.0, 'Unknown2': '0000', 'Unknown1': 0}

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
    open3e -w 396='47.5'
    -> sets domestic hot water setpoint to 47.5degC

    open3e -j -w 538='{"Mode": 1, "State": 0}'
    -> sets ExternalDomesticHotWaterTargetOperationMode.Mode to 1 and .State to 0
    -> Use -j -r to read data point in json format as template for writing. Always provide valid and complete json data for writing, enclosed in single quotes.
 

## Extended writing service (internal can bus only, experimental)
In case of a "negative response" code when writing data, you may try to use the command line option -f77. However, this is experimental. Always verify the result!

# Publish data points to mqtt
    open3e -r 268,269,271,274,318,1043 -m 192.168.0.5:1883:open3e -t 1
    -> will periodically scan data points and publish data to broker 192.168.0.5 

    open3e -r 268,269,271,274,318,1043 -m 192.168.0.5:1883:open3e -t 1 -mfstr "{didNumber}_{didName}"
    -> will publish with custom identifier format: e.g. open3e/268_FlowTemperatureSensor 

# Listener mode
    open3e -m 192.168.0.5:1883:open3e -mfstr "{didNumber}_{didName}" -l open3e/cmnd
    
    will listen for commands on topic open3e/cmnd with payload in json format:
    {"mode":"read"|"read-raw"|"read-pure"|"read-all"|"write"|"write-raw", "data":[list of data], "addr":"ECU_addr"}
    rem: "addr" is optional, otherwise defaut ECU address used
    
    to read dids 271 and 274:
    {"mode": "read", "data":[271,274]}
    
    to read dids 265 and 266 as JSON-objects (even w/o option -json):
    {"mode": "read-json", "data":[265,266]}
    
    to read dids 265 and 266 as raw data (even w/o option -raw):
    {"mode": "read-raw", "data":[265,266]}
    
    to write value of 21.5 to did 395 and value of 45.0 to did 396:
    {"mode": "write", "data":[[395,21.5],[396,45.0]]}

    to write value of 45.0 to did 396 using service 0x77 (internal can bus only, experimental):
    {"mode": "write-sid77", "data":[[396,45.0]]}

    to write value of 45.0 to did 396 in raw data format using service 0x77 (internal can bus only, experimental):
    {"mode": "write-raw-sid77", "data":[[396,"C201"]]}

    to set frost protect threshold to -9°C in complex did
    (A6FF lsb..msb -> 0xFFA6 -> -90 -> -9.0°C; Byte 0 unchanged):
    {"mode": "write-raw", "data":[[2855,"01A6FF"]]}

    to set frost protect threshold and eco function threshold to -9°C (complex dids):
    {"mode": "write-raw", "data":[[2855,"01A6FF"],[2426,"01A6FF000A00"]]}

 
    Option -m is mandatory for this mode.
    Options -r, -t, -j, -v may be used in parallel.

# Convert list of data points to json format
Use
```
open3e_dids2json
```
to convert common list of data points (Open3Edatapoints.py) to json format.
A white list of writable data points is also created by this tool.

# For developers

If you want to work on the codebase you can clone the repository and work in "editable" mode as follows. The editable mode allows you to modify and test changes in the source code without the need of a re-installation.

    git clone https://github.com/open3e/open3e.git  
    cd open3e
    pip install --editable .[dev]

**Hint: If you get an error like "A "pyproject.toml" file was found, but editable mode currently requires a setup.py based build." you are running an old pip version. Editable mode requires pip version >= 21.1.**

