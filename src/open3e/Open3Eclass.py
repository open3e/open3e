
import udsoncan
from doipclient import DoIPClient
from doipclient.connectors import DoIPClientUDSConnector
#from udsoncan.client import Client
from open3e.Open3EudsClient import Open3EudsClient
from udsoncan.exceptions import *
from udsoncan.services import *

from can.interface import Bus
from udsoncan.connections import PythonIsoTpConnection
from can.interfaces.socketcan import SocketcanBus
from can.interfaces.slcan import slcanBus
import isotp

from typing import Optional, Any
import logging
import importlib
import binascii
import os
import sys
#import time

import open3e.Open3Edatapoints
import open3e.Open3Ecodecs
from open3e.Open3Ecodecs import *

# import arbitrary python files as modules
def import_path(path):
    module_name = os.path.basename(path).replace('-', '_').replace('.py', '')
    spec = importlib.util.spec_from_loader(
        module_name,
        importlib.machinery.SourceFileLoader(module_name, path)
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    sys.modules[module_name] = module
    return module


class O3Eclass():
    def __init__(self, ecutx:int=0x680, ecurx:int=0,
                 doip:str=None, # doip mode if not empty  
                 can:str='can0',
                 slcan:str=None,
                 dev=None
                ):

        self.tx = ecutx 
        self.dev = dev  # not necessary
        self.numdps = 0
        self.slcan = slcan

        # ECU addresses ~~~~~~~~~~~~~~~~~~
        if(ecurx == 0):
            ecurx = ecutx + 0x10

        # load general datapoints table from open3e.Open3Edatapoints.py
        self.dataIdentifiers = dict(open3e.Open3Edatapoints.dataIdentifiers["dids"])            

        # overlay dids if certain device is selected ~~~~~~~~~~~~~~~~~~
        if(dev != None):  #!?! was kommt aus config.json?!?
            if(dev != ''):  #!?! was kommt aus config.json?!?
                if('.py' in dev):
                    didmoduledev = import_path(dev)
                else:
                    module_name = "open3e.Open3Edatapoints" + dev.capitalize()
                    didmoduledev = importlib.import_module(module_name)

                # load datapoints for selected device
                
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
        if(doip != None): #DoIP
            self.conn = DoIPClientUDSConnector(DoIPClient(doip, ecutx))
        elif(slcan != None): #SLCAN Serial CAN Interface either locally via USB or remote via Telnet
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
            bus = slcanBus(channel=slcan, tty_baudrate=115200, bitrate=250000)
            tp_addr = isotp.Address(isotp.AddressingMode.Normal_11bits, txid=ecutx, rxid=ecurx) # Network layer addressing scheme
            stack = isotp.CanStack(bus=bus, address=tp_addr, params=isotp_params)               # Network/Transport layer (IsoTP protocol)
            stack.set_sleep_timing(0.01, 0.01)                                                  # Balancing speed and load
            self.conn = PythonIsoTpConnection(stack)   
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
            bus = SocketcanBus(channel=can, bitrate=250000)                                     # Link Layer (CAN protocol)
            tp_addr = isotp.Address(isotp.AddressingMode.Normal_11bits, txid=ecutx, rxid=ecurx) # Network layer addressing scheme
            stack = isotp.CanStack(bus=bus, address=tp_addr, params=isotp_params)               # Network/Transport layer (IsoTP protocol)
            stack.set_sleep_timing(0.01, 0.01)                                                  # Balancing speed and load
            self.conn = PythonIsoTpConnection(stack)                                            # interface between Application and Transport layer

        # UDS setup ~~~~~~~~~~~~~~~~~~
        udsoncan.setup_logging()
        loglevel = logging.ERROR
        self.conn.logger.setLevel(loglevel)  #?? hier? s.u.

        # configuration for udsoncan client
        config = dict(udsoncan.configs.default_client_config)
        config['data_identifiers'] = self.dataIdentifiers
        # increase default timeout
        config['request_timeout'] = 3  # default 5, never appeared
        config['p2_timeout'] = 3       # default 1
        config['p2_star_timeout'] = 3  # default 5, never appeared
        
        # run uds client
        self.uds_client = Open3EudsClient(self.conn, config=config)
        self.uds_client.open()
        self.uds_client.logger.setLevel(loglevel)
        self.bus = bus


    # utils -----------------------
    def get_did_as_int(self, v):
        try:
            did = int(eval(str(v)))
            return did
        except:
            for did,cdc in self.dataIdentifiers.items():
                if(cdc.id.lower() == str(v).lower()):
                    return did
            raise ValueError(f"No DID found according to {v} on ECU {hex(self.tx)}")

    def get_sub_as_int(self, did:int, v):
        try:
            sub = int(eval(str(v)))
            return sub
        except:
            for sub in range(len(self.dataIdentifiers[did].subTypes)):
                if(self.dataIdentifiers[did].subTypes[sub].id.lower() == str(v).lower()):
                    return sub
            raise ValueError(f"No Sub found according to {v} with DID {did}")


    #++++++++++++++++++++++++++++++
    # 'global' methods
    #++++++++++++++++++++++++++++++

    def readByDid(self, did, raw:bool, sub=None):
        try:
            idid = self.get_did_as_int(did)

            if(sub is None):
                return self._readByDid(idid, raw)

            if(idid not in self.dataIdentifiers):
                raise ValueError(f"No Codec specified for DID {idid}")
            
            selectedDid = self.dataIdentifiers[idid]

            if(not isinstance(selectedDid, open3e.Open3Ecodecs.O3EComplexType)):
                raise TypeError(f"DID {idid} is not complex")   
            
            isub = self.get_sub_as_int(idid, sub)

            if (isub >= len(selectedDid.subTypes) or isub < 0):
                raise IndexError(f"Sub-Item with Index {isub} does not exist with DID {idid}")
                
            selectedSub = selectedDid.subTypes[isub]

            startIndexSub = 0
            for i in range(isub):
                startIndexSub += selectedDid.subTypes[i].string_len
            stopIndexSub = startIndexSub + selectedSub.string_len

            # receive bin data directly, no codec, no conversion
            string_bin,_ = self.readPure(idid, binary=True)
            string_bin_sub = string_bin[startIndexSub:stopIndexSub]

            open3e.Open3Ecodecs.flag_rawmode = raw
            decodedData = selectedSub.decode(string_bin_sub)

            return decodedData,selectedSub.id
        except NegativeResponseException as e:
            return f'Device rejected this read access. Probably DID {idid} is not available. {e}', f'ERR/{hex(self.tx)}.{idid}'
        except Exception as e:
            return str(e), f'ERR/{hex(self.tx)}.{did}'
        
                        
    # not global anymore... ;-)
    def _readByDid(self, did:int, raw:bool):
        if(did in self.dataIdentifiers): 
            open3e.Open3Ecodecs.flag_rawmode = raw
            response = self.uds_client.read_data_by_identifier([did])
            # return value and idstr
            return response.service_data.values[did],self.dataIdentifiers[did].id
        else:
            return self.readPure(did)


    def writeByDid(self, did, val, raw:bool, useService77=False, sub=None, readecu=None):
        #print( did, val, raw, useService77, sub)

        try:
            idid = self.get_did_as_int(did)

            if(sub is None):
                return self._writeByDid(idid, val, raw, useService77)

            if(idid not in self.dataIdentifiers):
                raise ValueError(f"No Codec specified for DID {idid}")
            
            selectedDid = self.dataIdentifiers[idid]

            if(not isinstance(selectedDid, open3e.Open3Ecodecs.O3EComplexType)):
                raise TypeError(f"DID {idid} is not complex")   
            
            isub = self.get_sub_as_int(idid, sub)

            if (isub >= len(selectedDid.subTypes) or isub < 0):
                raise IndexError(f"Sub Index {isub} does not exist in DID {idid}")
            
            selectedSub = selectedDid.subTypes[isub]

            startIndexSub = 0
            for i in range(isub):
                startIndexSub += selectedDid.subTypes[i].string_len
            stopIndexSub = startIndexSub + selectedSub.string_len

            # receive bin data directly, no codec, no conversion
            string_bin = None  # noetig?
            if(readecu is not None):
                string_bin,_ = readecu.readPure(idid, binary=True)
            else:
                string_bin,_ = self.readPure(idid, binary=True)

            # encode value to bytes
            open3e.Open3Ecodecs.flag_rawmode = raw 
            string_bin_sub = selectedSub.encode(val)

            # replace bytes in did data bytes   #TODO ggf. noch Laenge pruefen!
            string_bin = string_bin[:startIndexSub] + bytes(string_bin_sub) + string_bin[stopIndexSub:]

            # write back #TODO hier waere binaeres Schreiben wuenschenswert ohne Umweg ueber Codecs
            open3e.Open3Ecodecs.flag_binary = True
            ret1,ret2 = self._writeByDid(idid, string_bin, True, useService77)        
            open3e.Open3Ecodecs.flag_binary = False   
            return ret1,ret2
        except NegativeResponseException as e:
            return f'Device rejected this write access. {e}', f'ERR/{hex(self.tx)}.{idid}'
        except Exception as e:
            return str(e), f'ERR/{hex(self.tx)}.{did}'

    # not global anymore... ;-)
    def _writeByDid(self, did:int, val, raw:bool, useService77=False):
        open3e.Open3Ecodecs.flag_rawmode = raw
        response = self.uds_client.write_data_by_identifier(did, val, useService77)
        succ = (response.valid & response.positive)
        return succ, response.code


    def readAll(self, raw:bool):
        lst = []
        for did,cdc in self.dataIdentifiers.items():
            value,idstr = self._readByDid(int(did), raw=raw)
            lst.append([did, value, idstr])
        return lst 


    # reading without knowing length / codec
    def readPure(self, did:int, binary:bool=False):
        # ref https://github.com/pylessard/python-udsoncan/issues/188#issuecomment-1913654033
        response = self.uds_client.test_data_identifier([did])
        if(response.positive):
            diddata = response.data[2:]
            if(binary):
                return diddata,f"DID_{did}"
            else:
                return binascii.hexlify(diddata).decode('utf-8'),f"DID_{did}:len={len(response)-3}"
        else:
            return f"negative response, {response.code}:{response.invalid_reason}","DID_{did}"
    

    def close(self):
        self.uds_client.close()
        if (self.slcan != None):
            self.bus.shutdown()