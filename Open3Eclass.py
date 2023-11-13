
import udsoncan
from doipclient import DoIPClient
from doipclient.connectors import DoIPClientUDSConnector
from udsoncan.connections import IsoTPSocketConnection
from udsoncan.client import Client
from udsoncan.exceptions import *
from udsoncan.services import *
from typing import Optional, Any
import logging
import time
import paho.mqtt.client as paho
import importlib
import re

import Open3Edatapoints
from Open3Edatapoints import *

import Open3Ecodecs
from Open3Ecodecs import *


class O3Eclass():
    def __init__(self, ecutx:int=0x680, ecurx:int=0,
                 doip:str=None, # doip mode if not empty  
                 can:str='can0', 
                 mqttconstr:str=None,  # IP:port:topic
                 mqttuser:str=None,    # user:pwd 
                 mqttformat:str=None,  
                 device:str='None',
                 json=False,
                 raw=False, 
                 verbose=False,
                ):

        self.device = device
        self.json = json
        self.verbose = verbose
        self.raw = raw
        self.tx = ecutx 

        # MQTT
        self.mqtt_client = None
        self.mqttFormat = mqttformat
        self.mqttTopic = None
        
        # init only, obsolete?!
        Open3Ecodecs.flag_rawmode = self.raw
        

        # load general datapoints table from Open3Edatapoints.py
        self.dataIdentifiers = dict(dataIdentifiers["dids"])

        # overlay dids if certain device is selected ~~~~~~~~~~~~~~~~~~
        if(device != None):  #!?! was kommt aus config.json?!?
            # load datapoints for selected device
            module_name =  "Open3Edatapoints" + device.capitalize()
            didmoduledev = importlib.import_module(module_name)
            dataIdentifiersDev = didmoduledev.dataIdentifiers["dids"]

            # overlay device dids over general table 
            lstpops = []
            for itm in self.dataIdentifiers:
                if not (itm in dataIdentifiersDev):
                    lstpops.append(itm)
                elif not (dataIdentifiersDev[itm] is None):  # None means 'no change', nothing special
                    self.dataIdentifiers[itm] = dataIdentifiersDev[itm]

            # remove dids not existing with the device
            for itm in lstpops:
                self.dataIdentifiers.pop(itm)

            # debug only - see what we have now with this device
            #for itm in dataIdentifiers:
            #    print(f"{itm}:{type(dataIdentifiers[itm]).__name__}, {dataIdentifiers[itm].string_len}")

            # probably useless but to indicate that it's not required anymore
            dataIdentifiersDev = None
            didmoduledev = None
            

        # ECU addresses
        if(ecurx == 0):
            ecurx = ecutx + 0x10

        # select CAN / DoIP ~~~~~~~~~~~~~~~~~~
        if(doip != None):
            conn = DoIPClientUDSConnector(DoIPClient(doip, ecutx))
        else:
            conn = IsoTPSocketConnection(can, rxid=ecurx, txid=ecutx)
            # workaround missing padding for vdens (thanks to Phil, JB and HB!)
            conn.tpsock.set_opts(txpad=0x00)


        # UDS setup ~~~~~~~~~~~~~~~~~~
        udsoncan.setup_logging()
        loglevel = logging.ERROR
        conn.logger.setLevel(loglevel)  #?? hier? s.u.

        # configuration for udsoncan client
        config = dict(udsoncan.configs.default_client_config)
        config['data_identifiers'] = self.dataIdentifiers
        # increase default timeout
        config['request_timeout'] = 20
        config['p2_timeout'] = 20
        config['p2_star_timeout'] = 20
        
        # run uds client
        self.uds_client = Client(conn, config=config)
        self.uds_client.open()
        self.uds_client.logger.setLevel(loglevel)

        
        # MQTT setup ~~~~~~~~~~~~~~~~~~
        if(mqttconstr != None):
            self.mqtt_client = paho.Client("Open3E" + '_' + str(int(time.time()*1000)))  # Unique mqtt id using timestamp
            if(mqttuser != None):
                mlst = mqttuser.split(':')
                self.mqtt_client.username_pw_set(mlst[0] , password=mlst[1])
            mlst = mqttconstr.split(':')
            self.mqttTopic = mlst[2]
            self.mqtt_client.connect(mlst[0], int(mlst[1]))
            self.mqtt_client.reconnect_delay_set(min_delay=1, max_delay=30)
            self.mqtt_client.loop_start()
            if(self.mqttFormat == None):
                self.mqttFormat = "{didName}" # default


    #++++++++++++++++++++++++++++++
    # 'global' methods
    #++++++++++++++++++++++++++++++

    def readByDid(self, did:int, json=None, raw=None, msglvl=0):  # msglvl: bcd, 1=didnr, 2=didname, 4=ecuaddr
        def mqttdump(topic, obj):
            if (type(obj)==dict):
                for k, itm in obj.items():
                    mqttdump(topic+'/'+str(k),itm)
            elif (type(obj)==list):
                for k in range(len(obj)):
                    mqttdump(topic+'/'+str(k),obj[k])
            else:
                ret = self.mqtt_client.publish(topic, str(obj))     

        # flags...
        if(raw==None): raw = self.raw
        if(json==None): json = self.json

        Open3Ecodecs.flag_rawmode = raw

        try:
            response = self.uds_client.read_data_by_identifier([did])
        except TimeoutError:
            return
        
        if(self.mqtt_client != None):
            publishStr = self.mqttFormat.format(
                ecuAddr = self.tx,
                device = self.device,
                didName = self.dataIdentifiers[did].id,
                didNumber = did
            )
            
            if(json):
                # Send one JSON message
                ret = self.mqtt_client.publish(self.mqttTopic + "/" + publishStr, json.dumps(response.service_data.values[did]))    
            else:
                # Split down to scalar types
                mqttdump(self.mqttTopic + "/" + publishStr, response.service_data.values[did])
            
            if(self.verbose == True):
                print (hex(self.tx), did, self.dataIdentifiers[did].id, response.service_data.values[did])
        else:
            if(self.verbose == True):
                print (hex(self.tx), did, self.dataIdentifiers[did].id, response.service_data.values[did])
            else:
                mlst = []
                if((msglvl & 4) != 0):
                    mlst.append(str(hex(self.tx)))
                if((msglvl & 1) != 0):
                    mlst.append(str(did))
                if((msglvl & 2) != 0):
                    mlst.append(self.dataIdentifiers[did].id)
                mlst.append(str(response.service_data.values[did]))
                msg = " ".join(mlst)
                print(msg)


    def writeByDid(self, did:int, val, raw=True):
        if(raw == None): raw = self.raw # for later...
        if(self.verbose):
            print("Write did", did, "with value", val, "...")
        response = self.uds_client.write_data_by_identifier(did, val)
        if(self.verbose):
            # TODO: evaluate response
            print("done.")


    def readAll(self, json=None, raw=None, msglvl=1):
        for did, value in self.dataIdentifiers.items():
            self.readByDid(int(did), json=json, raw=raw, msglvl=msglvl)


    def close(self):
        if(self.verbose):
            print(f"closing {hex(self.tx)} - bye!")
        self.uds_client.close()
        if(self.mqtt_client != None):
            self.mqtt_client.disconnect()


