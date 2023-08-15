# Open3E interface

* Connects E3 boiler (vcal or vdens) controller through CAN UDS or doip
* Read known datapoints
* Experimental (!) write support (untested)

# Requirements
    pip3 install -r requirements.txt

# Setup CAN Bus
    sudo ip link set can0 up type can bitrate 250000

# Usage
    usage: Open3Eclient.py [-h] [-c CAN] [-d DOIP] [-dev DEV] [-a] [-r READ] [-raw] [-w WRITE] [-t TIMESTEP] [-m MQTT] [-mfstr MQTTFORMATSTRING] [-muser MQTTUSER]
                           [-mpass MQTTPASS] [-v]

    options:
    -h, --help            show this help message and exit
    -c CAN, --can CAN     use can device, e.g. can0
    -d DOIP, --doip DOIP  use doip access, e.g. 192.168.1.1
    -dev DEV, --dev DEV   boiler type --dev vdens or --dev vcal
    -a, --scanall         dump all dids
    -r READ, --read READ  read did, e.g. 0x173,0x174
    -raw, --raw           return raw data for all dids
    -w WRITE, --write WRITE
                            write did, e.g. 0x173=0x1000 (raw data only!)
    -t TIMESTEP, --timestep TIMESTEP
                            read continuous with delay in s
    -m MQTT, --mqtt MQTT  publish to server, e.g. 192.168.0.1:1883:topicname
    -mfstr MQTTFORMATSTRING, --mqttformatstring MQTTFORMATSTRING
                            mqtt formatstring e.g. {didNumber}_{didName}
    -muser MQTTUSER, --mqttuser MQTTUSER
                            mqtt username
    -mpass MQTTPASS, --mqttpass MQTTPASS
                            mqtt password
    -v, --verbose         verbose info

# Read dids
    python3 Open3Eclient.py -c can0 -dev vdens -r 268 -v
    0x10c FlowTempSensor 27.2

    python3 Open3Eclient.py -c can0 -dev vcal -r 318 -v
    0x13e WaterPressureSensor 1.8

    python3 Open3Eclient.py -c can0 -dev vcal -r 377 -v
    0x179 IdentNumber XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

    python3 Open3Eclient.py -c can0 -dev vcal -r 1043 -v
    0x413 FlowMeterSensor 2412.0

# Interval Readout
    python3 Open3Eclient.py -c can0 -dev vcal -r 1043 -t 1
    2412.0
    2413.0
    2411.0
    2412.0
    ...

# Write did (experimental)
    python3 Open3Eclient.py -c can0 -dev vdens -raw -w 396=D601
    -> sets domestic hot water setpoint to 48degC

# Publish datapoints to mqtt
    python Open3Eclient.py -c can0 -dev vcal -r 268,269,271,274,318,1043 -m 192.168.0.5:1883:open3e -t 1
    -> will periodically scan datapoints and publish data to broker 192.168.0.5

    python Open3Eclient.py -c can0 -dev vcal -r 268,269,271,274,318,1043 -m 192.168.0.5:1883:open3e -t 1 -mfstr "{didNumber}_{didName}"
    -> will publish with custom identifier format: e.g. open3e/268_FlowTemperatureSensor
