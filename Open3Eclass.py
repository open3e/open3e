
import udsoncan
from doipclient import DoIPClient
from doipclient.connectors import DoIPClientUDSConnector
from udsoncan.client import Client
from udsoncan.exceptions import *
from udsoncan.services import *

from can.interface import Bus
from udsoncan.connections import PythonIsoTpConnection
from can.interfaces.socketcan import SocketcanBus
import isotp

from typing import Optional, Any
import logging
import importlib
import binascii
import time

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
            # Refer to isotp documentation for full details about parameters
            isotp_params = {
                'stmin': 10,                            # Will request the sender to wait 10ms between consecutive frame. 0-127ms or 100-900ns with values from 0xF1-0xF9
                'blocksize': 0,                         # Request the sender to send 8 consecutives frames before sending a new flow control message
                'wftmax': 0,                            # Number of wait frame allowed before triggering an error
                'tx_data_length': 8,                    # Link layer (CAN layer) works with 8 byte payload (CAN 2.0)
                'tx_data_min_length': 8,                # Minimum length of CAN messages. When different from None, messages are padded to meet this length. Works with CAN 2.0 and CAN FD.
                'tx_padding': 0,                        # Will pad all transmitted CAN messages with byte 0x00.
                'rx_flowcontrol_timeout': 1000,         # Triggers a timeout if a flow control is awaited for more than 1000 milliseconds
                'rx_consecutive_frame_timeout': 1000,   # Triggers a timeout if a consecutive frame is awaited for more than 1000 milliseconds
                'override_receiver_stmin': None,        # When sending, respect the stmin requirement of the receiver if set to None.
                'max_frame_size': 4095,                 # Limit the size of receive frame.
                'can_fd': False,                        # Does not set the can_fd flag on the output CAN messages
                'bitrate_switch': False,                # Does not set the bitrate_switch flag on the output CAN messages
                'rate_limit_enable': False,             # Disable the rate limiter
                'rate_limit_max_bitrate': 1000000,      # Ignored when rate_limit_enable=False. Sets the max bitrate when rate_limit_enable=True
                'rate_limit_window_size': 0.2,          # Ignored when rate_limit_enable=False. Sets the averaging window size for bitrate calculation when rate_limit_enable=True
                'listen_mode': False                    # Does not use the listen_mode which prevent transmission.
            }
            bus = SocketcanBus(channel=can, bitrate=250000)                                          # Link Layer (CAN protocol)
            tp_addr = isotp.Address(isotp.AddressingMode.Normal_11bits, txid=ecutx, rxid=ecurx) # Network layer addressing scheme
            stack = isotp.CanStack(bus=bus, address=tp_addr, params=isotp_params)               # Network/Transport layer (IsoTP protocol)
            stack.set_sleep_timing(0.01, 0.01)                                                  # Balancing speed and load
            conn = PythonIsoTpConnection(stack)                                                 # interface between Application and Transport layer

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


