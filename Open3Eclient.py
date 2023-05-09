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

import Open3Edatapoints
from Open3Edatapoints import *

import Open3Ecodecs

udsoncan.setup_logging()
loglevel = logging.ERROR

parser = argparse.ArgumentParser()
parser.add_argument("-c", "--can", type=str, help="use can device, e.g. can0")
parser.add_argument("-d", "--doip", type=str, help="use doip access, e.g. 192.168.1.1")
parser.add_argument("-a", "--scanall", action='store_true', help="dump all dids")
parser.add_argument("-r", "--read", type=str, help="read did, e.g. 0x173")
parser.add_argument("-t", "--timestep", type=str, help="read continious with delay in s")
parser.add_argument("-v", "--verbose", action='store_true', help="verbose info")
args = parser.parse_args()

if(args.doip != None):
    conn = DoIPClientUDSConnector (DoIPClient(args.doip, 0x680))

if(args.can != None):
    conn = IsoTPSocketConnection(args.can, rxid=0x690, txid=0x680)

conn.logger.setLevel(loglevel)

config = dict(udsoncan.configs.default_client_config)
config['data_identifiers'] = dataIdentifiers

with Client(conn, request_timeout=10, config=config) as client:
    try:
        client.logger.setLevel(loglevel)

        if(args.read != None):
            while(True):
                did = eval(args.read)
                response = client.read_data_by_identifier([did])
                if(args.verbose == True):
                    print (hex(did), dataIdentifiers[did].id, response.service_data.values[did])
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
                        print (hex(did), dataIdentifiers[did].id, response.service_data.values[did])
                    else:
                        print (hex(did), response.service_data.values[did])

    except NegativeResponseException as e:
        pass

