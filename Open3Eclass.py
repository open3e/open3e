
import udsoncan
from doipclient import DoIPClient
from doipclient.connectors import DoIPClientUDSConnector
from udsoncan.connections import IsoTPSocketConnection
from udsoncan.client import Client
from udsoncan.exceptions import *
from udsoncan.services import *

from typing import Optional, Any
import logging
import importlib
import binascii
import time
import isotp

import Open3Edatapoints
import Open3Ecodecs
from Open3Ecodecs import *


class O3Eclass():
    def __init__(self, ecutx:int=0x680, ecurx:int=0,
                 doip:str=None, # doip mode if not empty  
                 can:str='can0', 
                 dev=None
                ):

        self.tx = ecutx 
        self.dev = dev  # not necessary
        self.numdps = 0

        # ECU addresses ~~~~~~~~~~~~~~~~~~
        if(ecurx == 0):
            ecurx = ecutx + 0x10

        # load general datapoints table from Open3Edatapoints.py
        self.dataIdentifiers = dict(Open3Edatapoints.dataIdentifiers["dids"])            

        # overlay dids if certain device is selected ~~~~~~~~~~~~~~~~~~
        if(dev != None):  #!?! was kommt aus config.json?!?
            if(dev != ''):  #!?! was kommt aus config.json?!?
                if('.py' in dev):
                    module_name = dev.replace('.py', '')
                else:
                    module_name = "Open3Edatapoints" + dev.capitalize()

                # load datapoints for selected device
                didmoduledev = importlib.import_module(module_name)
                dataIdentifiersDev = didmoduledev.dataIdentifiers["dids"]

                # add dids not in general but in device to general
                for key,val in dataIdentifiersDev.items():
                    if not (key in self.dataIdentifiers):
                        if(val != None):
                            self.dataIdentifiers[key] = val

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
                # for info
                self.numdps = len(self.dataIdentifiers)

            
        # select CAN / DoIP ~~~~~~~~~~~~~~~~~~
        if(doip != None):
            conn = DoIPClientUDSConnector(DoIPClient(doip, ecutx))
        else:
            conn = IsoTPSocketConnection(can, isotp.Address(rxid=ecurx, txid=ecutx))
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


    #++++++++++++++++++++++++++++++
    # 'global' methods
    #++++++++++++++++++++++++++++++

    def readByDid(self, did:int, raw:bool):
        if(did in self.dataIdentifiers): 
            retry = 0
            while(True):
                try:
                    Open3Ecodecs.flag_rawmode = raw
                    response = self.uds_client.read_data_by_identifier([did])
                    # return value and idstr
                    return response.service_data.values[did],self.dataIdentifiers[did].id
                except Exception as e:
                    if(type(e) in [TimeoutError, udsoncan.exceptions.TimeoutException]):
                        time.sleep(0.1)
                        retry += 1
                        if(retry == 4):
                            print(did, "ERROR max retry")
                            return None,self.dataIdentifiers[did].id
                    else:
                        raise Exception(e)
        else:
            return self.readPure(did)

    def writeByDid(self, did:int, val, raw:bool):
        Open3Ecodecs.flag_rawmode = raw
        response = self.uds_client.write_data_by_identifier(did, val)
        succ = (response.valid & response.positive)
        return succ, response.code


    def readAll(self, raw:bool):
        lst = []
        for did,cdc in self.dataIdentifiers.items():
            value,idstr = self.readByDid(int(did), raw=raw)
            lst.append([did, value, idstr])
        return lst 

    # reading without knowing length / codec
    def readPure(self, did:int):
        response = udsoncan.Response()
        retry = 0
        while(True):
            try:
                response = self.uds_client.send_request(
                    udsoncan.Request(
                        service=udsoncan.services.ReadDataByIdentifier,
                        data=(did).to_bytes(2, byteorder='big')
                    )
                )
                if(response.positive):
                    return binascii.hexlify(response.data[2:]).decode('utf-8'),f"unknown:len={len(response)-3}"
                else:
                    return f"negative response, {response.code}:{response.invalid_reason}","unknown"
            except Exception as e:
                if(type(e) in [TimeoutError, udsoncan.exceptions.TimeoutException]):
                    time.sleep(0.1)
                    retry += 1
                    if(retry == 4):
                        print(did, "ERROR max retry")
                        return None, "unknown"
                else:
                    return e.args, "unknown"
  

    def close(self):
        self.uds_client.close()


