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

import udsoncan
from doipclient import DoIPClient
from doipclient.connectors import DoIPClientUDSConnector
from udsoncan.connections import IsoTPSocketConnection
from udsoncan.client import Client
from udsoncan.exceptions import *
from udsoncan.services import *
from typing import Optional, Any
import logging
import argparse
import time
import paho.mqtt.client as paho

import Open3EdatapointsVcal
import Open3EdatapointsVdens
import Open3EdatapointsVx3

from Open3EdatapointsVcal import *
from Open3EdatapointsVdens import *

import Open3Ecodecs
from Open3Ecodecs import *

udsoncan.setup_logging()
loglevel = logging.ERROR

parser = argparse.ArgumentParser()
parser.add_argument("-c", "--can", type=str, help="use can device, e.g. can0")
parser.add_argument("-d", "--doip", type=str, help="use doip access, e.g. 192.168.1.1")
parser.add_argument("-dev", "--dev", type=str, help="boiler type --dev vdens or --dev vcal || battery --dev vx3")
parser.add_argument("-a", "--scanall", action='store_true', help="dump all dids")
parser.add_argument("-r", "--read", type=str, help="read did, e.g. 0x173,0x174")
parser.add_argument("-raw", "--raw", action='store_true', help="return raw data for all dids")
parser.add_argument("-w", "--write", type=str, help="write did, e.g. -w 396=D601 (raw data only!)")
parser.add_argument("-t", "--timestep", type=str, help="read continuous with delay in s")
parser.add_argument("-m", "--mqtt", type=str, help="publish to server, e.g. 192.168.0.1:1883:topicname")
parser.add_argument("-mfstr", "--mqttformatstring", type=str, help="mqtt formatstring e.g. {didNumber}_{didName}")
parser.add_argument("-muser", "--mqttuser", type=str, help="mqtt username")
parser.add_argument("-mpass", "--mqttpass", type=str, help="mqtt password")
parser.add_argument("-v", "--verbose", action='store_true', help="verbose info")
args = parser.parse_args()

if(args.dev == None):
    args.dev = "vcal"

if(args.doip != None):
    conn = DoIPClientUDSConnector (DoIPClient(args.doip, 0x680))

if(args.can != None):
    conn = IsoTPSocketConnection(args.can, rxid=0x690, txid=0x680)
    # workaround missing padding for vdens (thanks to Phil, JB and HB!)
    if(args.dev == "vdens"):
        conn.tpsock.set_opts(txpad=0x00)

conn.logger.setLevel(loglevel)

config = dict(udsoncan.configs.default_client_config)

# load datapoints for selected device
dataIdentifiers = None
if(args.dev == "vcal"):
    dataIdentifiers = dataIdentifiersVcal
if(args.dev == "vdens"):
    dataIdentifiers = dataIdentifiersVdens    
if(args.dev == "vdens"):
    dataIdentifiers = dataIdentifiersVx3

config['data_identifiers'] = dataIdentifiers

# increase default timeout
config['request_timeout'] = 20
config['p2_timeout'] = 20
config['p2_star_timeout'] = 20

with Client(conn, config=config) as client:
    client.logger.setLevel(loglevel)

    Open3Ecodecs.flag_rawmode = args.raw

    if(args.read != None):
        if(args.mqtt != None):
            mqttParamas = args.mqtt.split(":")
            client_mqtt = paho.Client("Open3E")
            if((args.mqttuser != None) and (args.mqttpass != None)):
                client_mqtt.username_pw_set(args.mqttuser , password=args.mqttpass)
            client_mqtt.connect(mqttParamas[0], int(mqttParamas[1]))
            client_mqtt.reconnect_delay_set(min_delay=1, max_delay=30)
            client_mqtt.loop_start()
            print("Read dids and publish to mqtt...")
        while(True):
            dids = args.read.split(",")
            for did in dids:
                did = eval(did)
                response = client.read_data_by_identifier([did])
                time.sleep(0.1)
                if(args.mqtt != None):
                    # if no format string is set
                    if(args.mqttformatstring == None):
                        mqttformatstring = "{didName}" # default
                    else:
                        mqttformatstring = args.mqttformatstring
                    publishStr = mqttformatstring.format(
                        didName = dataIdentifiers[did].id,
                        didNumber = did
                    )
                    if(dataIdentifiers[did].complex == True): 
                        # complex datatype
                        for key, value in response.service_data.values[did].items():
                            ret = client_mqtt.publish(mqttParamas[2] + "/" + publishStr + "/" + str(key), str(value))
                    else: 
                        # scalar datatype
                        ret = client_mqtt.publish(mqttParamas[2] + "/" + publishStr, response.service_data.values[did])
                else:
                    if(args.verbose == True):
                        print (did, dataIdentifiers[did].id, response.service_data.values[did])
                    else:
                        print (response.service_data.values[did])
            if(args.timestep != None):
                time.sleep(float(eval(args.timestep)))
            else:
                break
    else:
        if(args.scanall == True):
            for did in dataIdentifiers.keys():
                response = client.read_data_by_identifier([did])
                if(args.verbose == True):
                    print (did, dataIdentifiers[did].id, response.service_data.values[did])
                else:
                    print (did, response.service_data.values[did])
        # experimental write to did
        if(args.write != None):
            if(args.raw == False):
                raise Exception("Error: write only accepts raw data, use -raw param")
            writeArg = args.write.split("=")
            didKey=eval(writeArg[0])
            didVal=str(writeArg[1]).replace("0x","")
            if(args.verbose == True):
                print("Write did", didKey, "with value", didVal, "...")
            response = client.write_data_by_identifier(didKey, didVal)
            if(args.verbose == True):
                print("done.")
            time.sleep(0.1)
