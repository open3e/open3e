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

# +++++++++++++++++++++++++++++++++++++++++++++++
# please adjust! 
# +++++++++++++++++++++++++++++++++++++++++++++++ 
interface = "can0"

# cob scan, default 0x680 to 0x6ff  
startcob = 0x680
lastcob = 0x6ff

# did scan, default 256 to 3500
startdid = 256
lastdid = 3500

# write files for virtualE3 
writesimul = True

# end of adjusts 
# +++++++++++++++++++++++++++++++++++++++++++++++ 




import time
import binascii
import json

import udsoncan
from udsoncan.connections import IsoTPSocketConnection
from udsoncan.client import Client
from udsoncan.services import ReadDataByIdentifier

import Open3Edatapoints
from Open3Edatapoints import *
import Open3Eenums



# scan methods ~~~~~~~~~~~~~~~~~~~~~~
def scan_cobs(startcob:int, lastcob:int) -> tuple:  # list of responding cobs tuples (cobid,devprop)
    lstfounds = []
    lstskips =[]  # skip respond cobs    
    chkdid = 256

    print(f"scan COB-IDs {hex(startcob)} to {hex(lastcob)} ...") 
    for tx in range(startcob, lastcob + 1):
        if(tx in lstskips):
            continue
        rx = tx + 0x10
        conn = IsoTPSocketConnection(interface, rxid=rx, txid=tx)
        conn.tpsock.set_opts(txpad=0x00)
        
        with Client(conn) as client:
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
    #            else:
    #                print(f"{hex(tx)}:nothing")
            except Exception as e:
                pass
        client.close()
        time.sleep(0.1)

    print(f"{len(lstfounds)} responding COB-IDs found.")
    return lstfounds


def scan_dids(ecutx:int, startdid:int, lastdid:int) -> tuple:  # list of tuples (did,len,data)
    print(f"scan DIDs {startdid} to {lastdid} ...") 
    lstfounds = []
    rx = ecutx + 0x10

    conn = IsoTPSocketConnection(interface, rxid=rx, txid=ecutx)
    conn.tpsock.set_opts(txpad=0x00)

    with Client(conn) as client:
        for did in range(startdid, lastdid+1):
            try:
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
    #            else:
    #                print(f"{did}:0")
            except Exception as e:
                # print(f"# DID {did}: Fehler: {e}")
                pass
            time.sleep(0.02)
    client.close()
    print(f"{len(lstfounds)} DIDs found.")
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
        shead =  'import Open3Ecodecs\n'
        shead += 'from Open3Ecodecs import *\n\n'
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


# +++++++++++++++++++++++++++++++++
# Main
# +++++++++++++++++++++++++++++++++

# peparations
dataIdentifiers = dict(Open3Edatapoints.dataIdentifiers["dids"])
e3Devices = Open3Eenums.E3Enums['Devices']
dicDidEnums = read_didenums("DidEnums.txt")

# scan ECUs/COB-IDs
lstEcus = scan_cobs(startcob, lastcob)

# generate devices.json
write_devices_json(lstEcus)

# scan dids of each responding ECU
for cob,prop in lstEcus:
    lstdids = scan_dids(cob, startdid, lastdid)
    # write sumilation data in case
    if(writesimul):
        write_simul_datafile(lstdids, cob, prop)
    # write ECU specific datapoints_did.py
    write_datapoints_file(lstdids, cob, prop)
# report
print("\nconfiguration:")
with open('devices.json', 'r') as file:
    lines = file.readlines()
for line in lines:
    line = line.replace('\n','')
    print(line)
print("\nrun Open3Eclient with -mqtt and -a to get EVERYTHING on your MQTT app.")
    
