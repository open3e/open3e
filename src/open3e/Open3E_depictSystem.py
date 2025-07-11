"""
  Copyright 2023 philippoo66
  
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
# thanks to Hendrik 'surt91' Schawe

import time
import binascii
import json
import argparse
import os

import udsoncan
from udsoncan.client import Client
from udsoncan.services import ReadDataByIdentifier

from can.interface import Bus
from udsoncan.connections import PythonIsoTpConnection
from can.interfaces.socketcan import SocketcanBus
import isotp

from doipclient import DoIPClient
from doipclient.connectors import DoIPClientUDSConnector

import open3e.Open3Edatapoints
from open3e.Open3Edatapoints import *
import open3e.Open3Eenums


def main():
    # cob scan, default 0x680 to 0x6ff  
    startcob = 0x680
    lastcob = 0x6ff

    # did scan, default 256 to 3500
    startdid = 256
    lastdid = 3500

    # connection
    can = "can0"


    # scan methods ~~~~~~~~~~~~~~~~~~~~~~
    def scan_cobs(startcob:int, lastcob:int) -> tuple:  # list of responding cobs tuples (cobid,devprop)
        lstfounds = []
        lstskips = []  # skip respond cobs    
        chkdid = 256

        print(f"scan COB-IDs {hex(startcob)} to {hex(lastcob)} ...") 
        for tx in range(startcob, lastcob + 1):
            try:
                if(tx in lstskips):
                    continue
                print(hex(tx), end='\r')
                rx = tx + 0x10
                if(args.doip != None):
                    conn = DoIPClientUDSConnector(DoIPClient(args.doip, tx))
                else:
                    bus, conn = get_pycan_conn(can=can, ecurx=rx, ecutx=tx)

                # set default timeout
                config = dict(udsoncan.configs.default_client_config)
                #config['request_timeout'] = 3  # default 5
                #config['p2_timeout'] = 3       # default 1
                #config['p2_star_timeout'] = 3  # default 5

                with Client(conn, config=config) as client:
                    try:
                        response = client.send_request(
                            udsoncan.Request(
                                service=ReadDataByIdentifier,
                                data=(chkdid).to_bytes(2, byteorder='big')
                            )
                        )
                        if response.positive:
                            iprop = response.data[2+2]  # PCI,DL, devprop is 3rd byte of diddata
                            devprop = prop_str(iprop)
                            print(f"ECU found: {hex(tx)} : {devprop}")
                            lstfounds.append((tx,devprop))
                            lstskips.append(rx)
                        #else:
                        #    print(f"{hex(tx)}:neg.resp. {response.code}")
                    except Exception as e:
                        if(isinstance(e, udsoncan.exceptions.TimeoutException)):
                            # regular if ECU not present 
                            pass
                        else:
                            #raise Exception(e)
                            if isinstance(e, KeyboardInterrupt):
                                raise  # KeyboardInterrupt erneut werfen
                            print(f"# ECU {hex(tx)}: {e}")  # and continue...
                    # client done
                    client.close()
                    if(args.doip == None):
                        bus.shutdown()
            except Exception as e0:
                # allow exit by KeyboardInterrupt 
                if isinstance(e0, KeyboardInterrupt):
                    raise  # KeyboardInterrupt erneut werfen
                print(f"# ECU {hex(tx)}: {e0}")   # and continue...
            time.sleep(0.1)
        # all addresses done
        print(f"{len(lstfounds)} responding COB-IDs found.")
        return lstfounds


    def scan_dids(ecutx:int, startdid:int, lastdid:int) -> tuple:  # list of tuples (did,len,data)
        print(f"scan {shex(ecutx)} for DIDs {startdid} to {lastdid} ...") 
        lstfounds = []

        if(args.doip != None):
            conn = DoIPClientUDSConnector(DoIPClient(args.doip, ecutx))
        else:
            rx = ecutx + 0x10
            bus, conn = get_pycan_conn(can=can, ecurx=rx, ecutx=ecutx)

        # increase timeout
        config = dict(udsoncan.configs.default_client_config)
        #config['request_timeout'] = 3  # default 5
        config['p2_timeout'] = 3       # default 1
        #config['p2_star_timeout'] = 3  # default 5

        with Client(conn, config=config) as client:
            for did in range(startdid, lastdid+1):
                try:
                    print(did, end='\r')
                    response = client.send_request(
                        udsoncan.Request(
                            service=ReadDataByIdentifier,
                            data=(did).to_bytes(2, byteorder='big')
                        )
                    )
                    if response.positive:
                        dlen = len(response) - 3
                        data = response.data[2:]
                        dstr = "(unknown)"
                        if(did in dicDidEnums):
                            dstr = dicDidEnums[did]
                        print(f"found {did}:{dlen}:{dstr}")
                        lstfounds.append((did,dlen,data))
                except Exception as e:
                    if(isinstance(e, udsoncan.exceptions.NegativeResponseException)):
                        # regular if DID not present 
                        pass
                    else:
                        #raise Exception(e)
                        # allow exit by KeyboardInterrupt 
                        if isinstance(e, KeyboardInterrupt):
                            raise  # KeyboardInterrupt erneut werfen
                        print(f"# DID {did}: {e}")  # and continue...
                # short rest before next did     
                time.sleep(0.05)

            # client done
            client.close()
            if(args.doip == None):
                bus.shutdown()
        print(f"{len(lstfounds)} DIDs found on {shex(ecutx)}.")
        return lstfounds


    # utils ~~~~~~~~~~~~~~~~~~~~~~
    def did_info(did:int) -> tuple:  # (didlen,idstr)
        if(did in dataIdentifiers):
            didlen = vars(dataIdentifiers[did])['string_len']
            idstr = vars(dataIdentifiers[did])['id'] 
            return (didlen,idstr)
        elif(did in dicDidEnums):
            return (0, dicDidEnums[did])
        else:
            return (0, "Unknown")

    def prop_str(devprop:int) -> str:
        if(devprop in e3Devices):
            return e3Devices[devprop]
        else:
            return str(devprop)

    def shex(nbr:int) -> str:
        return format(nbr, '03x')


    def read_didenums(file):
        dicenums = {}
        lines = []
        print("read DID enums ...")
        try:
            with open(file, 'r') as file:
                lines = file.readlines()
        except Exception as ex:
            print(ex)
        
        for line in lines:
            line = line.strip()
            if line:
                parts = line.split('(')
                if len(parts) == 2:
                    name = parts[0].strip()
                    num_str = parts[1].split(')')[0].strip()
                    try:
                        num = int(num_str)
                        dicenums[num] = name
                    except ValueError:
                        print(f"Could not parse '{num_str}' as an integer.")
        print(f"{len(dicenums)} DIDs listed.")
        return dicenums


    # write files methods ~~~~~~~~~~~~~~~~~~~~~~
    def write_devices_json(lstecus:list):
        print("write devices.json ...")
        mylist = []
        # reformat list contents
        for cob,prop in lstecus:
            scob = hex(cob)
            sdplist = "Open3Edatapoints_" + shex(cob) + ".py"
            mylist.append((scob, sdplist, prop))
        # make for dump
        result_dict = {}
        for mytuple in mylist:
            key = mytuple[0]
            values = {'tx': mytuple[0], 'dpList': mytuple[1], 'prop' : mytuple[2]}
            result_dict[key] = values
        # write json
        with open('devices.json', 'w') as json_file:
            json.dump(result_dict, json_file, indent=2)
        print("done.")


    def write_simul_datafile(lstdids:list, cobid:int, devprop:str):
        filename = "virtdata_" + shex(cobid) + ".txt"
        print(f"write simulation data file {filename} ...")
        with open(filename, "w") as file:
            file.write(f"# {hex(cobid)}:{devprop}\n")
            for did,dlen,data in lstdids:
                sdata = binascii.hexlify(data).decode('utf-8')
                file.write(str(did) + " " + sdata + "\n")
        print("done.")


    def write_datapoints_file(lstdids:list, cobid:int, devprop:str):
        filename = "Open3Edatapoints_" + shex(cobid) + ".py"
        print(f"write datapoints file {filename} ...")
        with open(filename, "w") as file:
            shead = 'from open3e.Open3Ecodecs import *\n\n'
            shead += 'dataIdentifiers = {\n'
            shead += '    \"name\": \"' + str(devprop) + '\",\n'
            shead += '    \"dids\" :\n'
            shead += '    {\n'
            file.write(shead)
            for did,dlen,data in lstdids:
                sline = '        ' + str(did) + " : "
                genlen,idstr = did_info(did)
                if(dlen == genlen):
                    sline += 'None,'
                else:
                    sline += 'RawCodec(' + str(dlen) + ', \"' + idstr + '\"),'
                file.write(sline + '\n')
            file.write('    }\n')
            file.write('}\n')
        print("done.")


    def get_isotp_params():
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
        return isotp_params


    def get_pycan_conn(can, ecurx:int, ecutx:int):
        bus = SocketcanBus(channel=can, bitrate=250000)                                     # Link Layer (CAN protocol)
        tp_addr = isotp.Address(isotp.AddressingMode.Normal_11bits, txid=ecutx, rxid=ecurx)       # Network layer addressing scheme
        isotp_params = get_isotp_params()
        stack = isotp.CanStack(bus=bus, address=tp_addr, params=isotp_params)               # Network/Transport layer (IsoTP protocol)
        stack.set_sleep_timing(0.01, 0.01)                                                  # Balancing speed and load
        conn = PythonIsoTpConnection(stack)                                                 # interface between Application and Transport layer
        return bus, conn


# +++++++++++++++++++++++++++++++++
# Main
# +++++++++++++++++++++++++++++++++
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--can", type=str, help="use CAN device, e.g. can0")
    parser.add_argument("-d", "--doip", type=str, help="use DoIP access, e.g. 192.168.1.1")
    parser.add_argument("-s", "--simul", action='store_true', help="write simulation data files")
    args = parser.parse_args()

    if(args.can != None):
        can = args.can

    # peparations
    dataIdentifiers = dict(open3e.Open3Edatapoints.dataIdentifiers["dids"])
    e3Devices = open3e.Open3Eenums.E3Enums['Devices']

    open3e_path = os.path.split(open3e.Open3Eenums.__file__)[0]
    dicDidEnums = read_didenums(os.path.join(open3e_path, "DidEnums.txt"))

    # scan ECUs/COB-IDs
    lstEcus = scan_cobs(startcob, lastcob)

    # generate devices.json
    write_devices_json(lstEcus)

    # scan dids of each responding ECU
    for cob,prop in lstEcus:
        lstdids = scan_dids(cob, startdid, lastdid)
        # write sumilation data for virtualE3in case
        if(args.simul):
            write_simul_datafile(lstdids, cob, prop)
        # write ECU specific datapoints_cob.py
        write_datapoints_file(lstdids, cob, prop)
    # report
    print("\nconfiguration:")
    with open('devices.json', 'r') as file:
        lines = file.readlines()
    for line in lines:
        line = line.replace('\n','')
        print(line)
    print("\nrun open3e with -mqtt and -a to get EVERYTHING on your MQTT app.")
    
if __name__ == "__main__":
    main()
