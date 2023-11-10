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
import json
import importlib


import Open3Edatapoints
from Open3Edatapoints import *

import Open3Ecodecs
from Open3Ecodecs import *

cmnd_queue = []
cmnds      = ['read','write','write-raw']

def on_connect(client, userdata, flags, rc):
    client.subscribe(args.listen)
	
def on_disconnect(client, userdata, rc):
    if rc != 0:
        print('mqtt broker disconnected. rc = ' + str(rc))
 
def on_message(client, userdata, msg):
    global cmnd_queue
    topic   = str(msg.topic)            # Topic in String umwandeln
    if topic == args.listen:
        try:
            payload = json.loads(msg.payload.decode())  # Payload in Dict umwandeln
            cmnd_queue.append(payload)
        except:
            print('bad payload: '+str(msg.payload)+'; topic: '+str(msg.topic))
            payload = ''

def cmnd_loop(client, client_mqtt, mqttParamas, dataIdentifiers):
    global cmnd_queue
    next_read_time = time.time()
    while True:
        if len(cmnd_queue) > 0:
            cd = cmnd_queue.pop(0)

            if not cd['mode'] in cmnds:
                print('bad mode value = ' + str(cd['mode'])+'\nSupported commands are: '+json.dumps(cmnds)[1:-1])
                pass

            if cd['mode'] == 'read':
                Open3Ecodecs.flag_rawmode = False
                dids = cd['data']
                for did in dids:
                    readByDid(eval(str(did)), client, client_mqtt, mqttParamas, dataIdentifiers)
                    time.sleep(0.01)            # 10 ms delay before next request

            if cd['mode'] == 'write':
                # ToDo: Umrechnung über Codec ergänzen. Wechselwirkung mit flag_rawmode beachten!
                Open3Ecodecs.flag_rawmode = False
                for wd in cd['data']:
                    didKey = eval(str(wd[0]))    # key: convert numeric or string parameter to numeric value
                    didVal = eval(str(wd[1]))    # value: dto.
                    writeByDid(didKey, didVal, client)
                    time.sleep(0.1)
                  
            if cd['mode'] == 'write-raw':
                Open3Ecodecs.flag_rawmode = True
                for wd in cd['data']:
                    didKey = eval(str(wd[0]))               # key is submitted as numeric value
                    didVal = str(wd[1]).replace('0x','')    # val is submitted as hex string
                    writeByDid(didKey, didVal, client)
                    time.sleep(0.1)
        else:
            if (args.read != None):
                if (next_read_time > 0) and (time.time() > next_read_time):
                    # add dids to read to command queue
                    dids = args.read.split(",")
                    cmnd_queue.append({'mode':'read', 'data': dids})
                    if(args.timestep != None):
                        next_read_time = next_read_time + eval(args.timestep)
                    else:
                        next_read_time = 0    # Don't do it again
                  
        time.sleep(0.01)


def readByDid(did, client, client_mqtt, mqttParamas, dataIdentifiers):
    try:
        response = client.read_data_by_identifier([did])
    except TimeoutError:
        return 
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
        if(args.verbose == True):
            print (did, dataIdentifiers[did].id, response.service_data.values[did])
    else:
        if(args.verbose == True):
            print (did, dataIdentifiers[did].id, response.service_data.values[did])
        else:
            print (response.service_data.values[did])

def writeByDid(didKey, didVal, client):
    if(args.verbose == True):
        print("Write did", didKey, "with value", didVal, "...")
    response = client.write_data_by_identifier(didKey, didVal)
    if(args.verbose == True):
        print("done.")

#
# Main
#

udsoncan.setup_logging()
loglevel = logging.ERROR

parser = argparse.ArgumentParser()
parser.add_argument("-c", "--can", type=str, help="use can device, e.g. can0")
parser.add_argument("-d", "--doip", type=str, help="use doip access, e.g. 192.168.1.1")
parser.add_argument("-dev", "--dev", type=str, help="boiler type --dev vdens or --dev vcal || pv/battery --dev vx3")
parser.add_argument("-a", "--scanall", action='store_true', help="dump all dids")
parser.add_argument("-r", "--read", type=str, help="read did, e.g. 0x173,0x174")
parser.add_argument("-raw", "--raw", action='store_true', help="return raw data for all dids")
parser.add_argument("-w", "--write", type=str, help="write did, e.g. -w 396=D601 (raw data only!)")
parser.add_argument("-t", "--timestep", type=str, help="read continuous with delay in s")
parser.add_argument("-l", "--listen", type=str, help="mqtt topic to listen for commands, e.g. open3e/cmnd")
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
    conn.tpsock.set_opts(txpad=0x00)

conn.logger.setLevel(loglevel)

# load datapoints for selected device
module_name =  "Open3Edatapoints" + args.dev.capitalize()
didmoduledev = importlib.import_module(module_name)
dataIdentifiersDev = didmoduledev.dataIdentifiers["dids"]

# load general datapoints table from Open3Edatapoints.py
dataIdentifiers = dataIdentifiers["dids"]

# overlay device dids over general table 
lstpops = []
for itm in dataIdentifiers:
    if not (itm in dataIdentifiersDev):
        lstpops.append(itm)
    elif not (dataIdentifiersDev[itm] is None):  # None means 'no change', nothing special
        dataIdentifiers[itm] = dataIdentifiersDev[itm]

# remove dids not existing with the device
for itm in lstpops:
    dataIdentifiers.pop(itm)

# debug only - see what we have now with this device
#for itm in dataIdentifiers:
#    print(f"{itm}:{type(dataIdentifiers[itm]).__name__}, {dataIdentifiers[itm].string_len}")

# probably useless but to indicate that it's not required anymore
dataIdentifiersDev = None
didmoduledev = None


# configuration for udsoncan client
config = dict(udsoncan.configs.default_client_config)
config['data_identifiers'] = dataIdentifiers
# increase default timeout
config['request_timeout'] = 20
config['p2_timeout'] = 20
config['p2_star_timeout'] = 20


with Client(conn, config=config) as client:
    client.logger.setLevel(loglevel)

    Open3Ecodecs.flag_rawmode = args.raw
    Open3Ecodecs.flag_dev = args.dev

    client_mqtt = None
    mqttParamas = None
    # MQTT setup ~~~~~~~~~~~~~~~~~~
    if(args.mqtt != None):
        mqttParamas = args.mqtt.split(":")
        client_mqtt = paho.Client("Open3E"+'_'+str(int(time.time()*1000)))  # Unique mqtt id using timestamp
        if((args.mqttuser != None) and (args.mqttpass != None)):
            client_mqtt.username_pw_set(args.mqttuser , password=args.mqttpass)
        client_mqtt.connect(mqttParamas[0], int(mqttParamas[1]))
        client_mqtt.reconnect_delay_set(min_delay=1, max_delay=30)
        client_mqtt.loop_start()
        if (args.listen != None):
            client_mqtt.on_connect = on_connect
            client_mqtt.on_disconnect = on_disconnect
            client_mqtt.on_message = on_message
            print("Enter listener mode, waiting for commands on mqtt")
        else:
            print("Read dids and publish to mqtt...")
    # listener mode ~~~~~~~~~~~~~~~~~~
    if (args.listen != None):
        if (args.mqtt == None):
            print('mqtt option is mandatory for listener mode')
            exit(0)
        try:
            cmnd_loop(client, client_mqtt, mqttParamas, dataIdentifiers)
        except (KeyboardInterrupt, InterruptedError):
            # <STRG-C> oder SIGINT to stop
            # Use <kill -s SIGINT pid> to send SIGINT
            pass
    # traditional commands ~~~~~~~~~~~~~~~~~~ 
    else:
        if(args.read != None):
            dids = args.read.split(",")
            while(True):
                for did in dids:
                    readByDid(eval(did), client, client_mqtt, mqttParamas, dataIdentifiers)
                    time.sleep(0.01)
                if(args.timestep != None):
                    time.sleep(float(eval(args.timestep)))
                else:
                    break
        elif(args.scanall == True):
            for did in dataIdentifiers:
                readByDid(did, client, client_mqtt, mqttParamas, dataIdentifiers)
                time.sleep(0.01)
#                for did in dataIdentifiers.keys():
#                    response = client.read_data_by_identifier([did])
#                    if(args.verbose == True):
#                        print (did, dataIdentifiers[did].id, response.service_data.values[did])
#                    else:
#                        print (did, response.service_data.values[did])
        # experimental write to did
        elif(args.write != None):
            if(args.raw == False):
                raise Exception("Error: write only accepts raw data, use -raw param")
            writeArg = args.write.split("=")
            didKey=eval(writeArg[0])
            didVal=str(writeArg[1]).replace("0x","")
            writeByDid(didKey, didVal, client)
            time.sleep(0.1)
