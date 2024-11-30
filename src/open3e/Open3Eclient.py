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

import argparse
import time
import json
import paho.mqtt.client as paho
from udsoncan.exceptions import *

import open3e.Open3Eclass

def main():
    # default ECU address
    deftx = 0x680

    # ECUs and their addresses
    dicEcus = {}      # addr:ecu
    dicDevAddrs = {}  # devstr:addr

    cmnd_queue = []   # command queue to serialize MQTT requests

    # utils ~~~~~~~~~~~~~~~~~~~~~~~
    def getint(v) -> int:
        if type(v) is int:
            return v
        else:
            return int(eval(str(v)))

    def addr_of_dev(v) -> int: 
        if(v in dicDevAddrs):
            return int(dicDevAddrs[v])
        return getint(v)

    def dev_of_addr(addr:int):
        for key, val in dicDevAddrs.items():
            if val == addr:
                return key
        return hex(addr)
            
    def get_ecudid(v):
        s = str(v)
        parts = s.split(".")
        if(len(parts) > 1):
            return getint(parts[0]),getint(parts[1])
        else:
            return deftx,getint(parts[0])

    # complex addressing: 0x680.[257,258,259] or 0x680.256 or 257,259,261 or 256 ...
    # also possibel 0x680.[257.0,258.1,259]  or 0x680.256.1 ...
    # also Vcal.BusIdentification.BusAddress or Vcal.256.BusAddress ...
    # if sub gets addressed, ecu must be given, otherwiese not clear if ecu.did or did.sub
    def eval_complex(v) -> list: 
        """ 
        this is the 'inner evaluation', called by eval_complex_list() only. 
        returns list of [ecu,did,sub] items (i.a. sub=None). 
        did and sub may be string now!! to be evaluated in class!
        """
        s = str(v).replace(' ','')
        parts = s.split(".")
        if(len(parts) == 1):
            # only did
            return [[deftx, parts[0], None]]
        
        # ecu.[...] or ecu.did or ecu.did.sub
        ecu = addr_of_dev(parts[0])
        
        if(len(parts) == 2):
            # only ecu.did
            return [[ecu,parts[1],None]]
            
        if("[" in parts[1]):
            # ecu.[...]
            parts.pop(0)
            s = '.'.join(parts)
            s = s.replace('[','').replace(']','')
            parts = s.split(",")
            lst = []
            for part in parts:
                did,sub = get_didsub(part)
                lst.append([ecu,did,sub])
            return lst

        # ecu.did.sub
        return [[ecu,parts[1],parts[2]]]

    def eval_complex_list(v) -> list:  
        """
        :param v: enum of complex addressing separated by ','
        :return: list of items [ecu,did,sub]
        """
        sl = list(str(v).replace(' ',''))
        open = 0
        for i in range(len(sl)):
            if sl[i] == '[':
                open += 1   # max 1, no nested brackets
            elif sl[i] == ']':
                open -= 1
            elif open <= 0:
                if sl[i] == ",":
                    sl[i] = ';'
        s = ''.join(sl)
        parts = s.split(';')
        lst = []
        for part in parts:
            plst = eval_complex(part)
            for itm in plst:
                lst.append(itm)
        return lst

    # gets did and sub from fraction tailing 'ecu.'
    def get_didsub(s):
        parts = s.split(".")
        if(len(parts) == 1):
            # only did
            return parts[0], None
        else:
            return parts[0], parts[1]      
          

    def ensure_ecu(addr:int):
        if(not (addr in dicEcus)):
            # make ecu with no name str
            ecu = open3e.Open3Eclass.O3Eclass(ecutx=addr, doip=args.doip, can=args.can, dev=None) 
            dicEcus[addr] = ecu


    # listen events ~~~~~~~~~~~~~~~~~~~~~~~
    def on_connect(client, userdata, flags, reason_code, properties):
        if args.listen != None:
            client.subscribe(args.listen)
        
    def on_disconnect(client, userdata, flags, reason_code, properties):
        if reason_code != 0:
            print('mqtt broker disconnected. reason_code = ' + str(reason_code))

    def on_message(client, userdata, msg):
        topic = str(msg.topic)            # Topic in String umwandeln
        if topic == args.listen:
            try:
                payload = json.loads(msg.payload.decode())  # Payload in Dict umwandeln
                cmnd_queue.append(payload)
            except:
                print('bad payload: ' + str(msg.payload)+'; topic: ' + str(msg.topic))
                payload = ''


    # subs  ~~~~~~~~~~~~~~~~~~~~~~~
    def listen(readdids=None, timestep=0):
        if(args.mqtt == None):
            raise Exception('mqtt option is mandatory for listener mode')

        def getaddr(cd) -> int:
            if 'addr' in cd: 
                return getint(addr_of_dev(cd['addr']))
            else: 
                return deftx 

        def cmnd_loop():
            cmnds = ['read','read-json','read-raw','read-pure','read-all','write','write-raw','write-sid77','write-raw-sid77']
            if(readdids != None):
                jobs =  eval_complex_list(readdids)
                next_read_time = time.time()

            while True:
                if len(cmnd_queue) > 0:
                    cd = cmnd_queue.pop(0)

                    if not cd['mode'] in cmnds:
                        print('bad mode value = ' + str(cd['mode']) + '\nSupported commands are: ' + json.dumps(cmnds)[1:-1])

                    elif cd['mode'] in ['read','read-json','read-raw']:
                        addr = getaddr(cd)
                        dids = cd['data']
                        ensure_ecu(addr) 
                        for did in dids:
                            readbydid(addr, getint(did), json=(cd['mode']=='read-json'), raw=(cd['mode']=='read-raw'))
                            time.sleep(0.01)            # 10 ms delay before next request

                    elif cd['mode'] == 'read-pure':
                        addr = getaddr(cd)
                        dids = cd['data']
                        ensure_ecu(addr) 
                        for did in dids:
                            readpure(addr, getint(did))
                            time.sleep(0.01)            # 10 ms delay before next request

                    elif cd['mode'] == 'read-all':
                        addr = getaddr(cd)
                        if(args.verbose == True):
                            print(f"reading {hex(addr)}, {dicEcus[addr].numdps} datapoints, please be patient...")
                        lst = dicEcus[addr].readAll(args.raw)
                        for itm in lst:
                            showread(addr=addr, did=itm[0], value=itm[1], idstr=itm[2])

                    elif cd['mode'] == 'write':
                        addr = getaddr(cd)
                        ensure_ecu(addr)
                        for wd in cd['data']:
                            didKey = getint(wd[0])    # key: convert numeric or string parameter to numeric value
                            if type(wd[1]) == str:
                                didVal = json.loads(wd[1])    # value: if string parse as json
                            else:
                                didVal = wd[1]  # value: if mqtt payload already parsed
                            dicEcus[addr].writeByDid(didKey, didVal, raw=False) 
                            time.sleep(0.1)
                        
                    elif cd['mode'] == 'write-raw':
                        addr = getaddr(cd)
                        ensure_ecu(addr)
                        for wd in cd['data']:
                            didKey = getint(wd[0])                  # key is submitted as numeric value
                            didVal = str(wd[1]).replace('0x','')    # val is submitted as hex string
                            dicEcus[addr].writeByDid(didKey, didVal, raw=True)
                            time.sleep(0.1)
                            
                    elif cd['mode'] == 'write-sid77':
                        addr = getaddr(cd)
                        ensure_ecu(addr)
                        for wd in cd['data']:
                            didKey = getint(wd[0])    # key: convert numeric or string parameter to numeric value
                            if type(wd[1]) == str:
                                didVal = json.loads(wd[1])    # value: if string parse as json
                            else:
                                didVal = wd[1]  # value: if mqtt payload already parsed
                            ecu77 = open3e.Open3Eclass.O3Eclass(ecutx=addr+2, doip=args.doip, can=args.can, dev=args.dev)
                            ecu77.writeByDid(didKey, didVal, raw=False, useService77=True)
                            ecu77.close() 
                            time.sleep(0.1)
                        
                    elif cd['mode'] == 'write-raw-sid77':
                        addr = getaddr(cd)
                        ensure_ecu(addr)
                        for wd in cd['data']:
                            didKey = getint(wd[0])                  # key is submitted as numeric value
                            didVal = str(wd[1]).replace('0x','')    # val is submitted as hex string
                            ecu77 = open3e.Open3Eclass.O3Eclass(ecutx=addr+2, doip=args.doip, can=args.can, dev=args.dev)
                            ecu77.writeByDid(didKey, didVal, raw=True, useService77=True)
                            ecu77.close()
                            time.sleep(0.1)
                else:
                    if (readdids != None):
                        if (next_read_time > 0) and (time.time() > next_read_time):
                            # add dids to read to command queue
                            for ecudid in jobs:
                                cmnd_queue.append({'mode':'read', 'addr': ecudid[0], 'data': [ecudid[1]]})
                            if(timestep != None):
                                next_read_time = next_read_time + int(timestep)
                            else:
                                next_read_time = 0    # Don't do it again
                        
                time.sleep(0.01)

        print("Enter listener mode, waiting for commands on mqtt...")
        # and go...
        cmnd_loop() 


    def readbydid(addr:int, did:any, json=None, raw=None, msglvl=0, sub=None):
        if(raw == None): 
            raw = args.raw
        value,idstr =  dicEcus[addr].readByDid(did, raw, sub)
        showread(addr, did, value, idstr, json, msglvl)    

        
    def readpure(addr:int, did:int, json=None, msglvl=0):
        value,idstr =  dicEcus[addr].readPure(did)
        showread(addr, did, value, idstr, json, msglvl)    


    def showread(addr, did, value, idstr, fjson=None, msglvl=0):   # msglvl: bcd, 1=didnr, 2=didname, 4=ecuaddr
        def mqttdump(topic, obj):
            if (type(obj)==dict):
                for k,itm in obj.items():
                    mqttdump(topic+'/'+str(k),itm)
            elif (type(obj)==list):
                for k in range(len(obj)):
                    mqttdump(topic+'/'+str(k),obj[k])
            else:
                ret = mqtt_client.publish(topic, str(obj))     

        if(fjson == None): 
            fjson = args.json

        if(mqtt_client != None):
            publishStr = mqttformatstring.format(
                ecuAddr = addr,
                device = dev_of_addr(addr),
                didName = idstr,
                didNumber = did
            )
            
            if(fjson):
                # Send one JSON message
                ret = mqtt_client.publish(mqttTopic + "/" + publishStr, json.dumps(value))    
            else:
                # Split down to scalar types
                mqttdump(mqttTopic + "/" + publishStr, value)
            
            if(args.verbose == True):
                print (dev_of_addr(addr), did, idstr, json.dumps(value))
        else:
            if(args.verbose == True):
                print (dev_of_addr(addr), did, idstr, json.dumps(value))
            else:
                mlst = []
                if((msglvl & 4) != 0):
                    mlst.append(str(hex(addr)))
                if((msglvl & 1) != 0):
                    mlst.append(str(did))
                if((msglvl & 2) != 0):
                    mlst.append(idstr)
                mlst.append(str(value))
                msg = " ".join(mlst)
                print(msg)


    #~~~~~~~~~~~~~~~~~~~~~~
    # Main
    #~~~~~~~~~~~~~~~~~~~~~~
    parser = argparse.ArgumentParser(fromfile_prefix_chars='@')
    parser.add_argument("-c", "--can", type=str, help="use can device, e.g. can0")
    parser.add_argument("-d", "--doip", type=str, help="use doip access, e.g. 192.168.1.1")
    parser.add_argument("-dev", "--dev", type=str, help="boiler type --dev vdens or --dev vcal || pv/battery --dev vx3")
    parser.add_argument("-tx", "--ecuaddr", type=str, help="ECU Address")
    parser.add_argument("-cnfg", "--config", type=str, help="json configuration file")
    parser.add_argument("-a", "--scanall", action='store_true', help="dump all dids")
    parser.add_argument("-r", "--read", type=str, help="read did, e.g. 0x173,0x174")
    parser.add_argument("-w", "--write", type=str, help="write did, e.g. -w 396=D601 (raw data only!)")
    parser.add_argument("-f77", "--forcesid77", action='store_true', help="force the use of serive 0x77 for writing of a did")
    parser.add_argument("-raw", "--raw", action='store_true', help="return raw data for all dids")
    parser.add_argument("-t", "--timestep", type=str, help="read continuous with delay in s")
    parser.add_argument("-l", "--listen", type=str, help="mqtt topic to listen for commands, e.g. open3e/cmnd")
    parser.add_argument("-m", "--mqtt", type=str, help="publish to server, e.g. 192.168.0.1:1883:topicname")
    parser.add_argument("-mfstr", "--mqttformatstring", type=str, help="mqtt formatstring e.g. {didNumber}_{didName}")
    parser.add_argument("-muser", "--mqttuser", type=str, help="mqtt username:password")
    parser.add_argument("-mcid", "--mqttclientid", type=str, help="mqtt client id of open3e")
    parser.add_argument("-j", "--json", action='store_true', help="send JSON structure")
    parser.add_argument("-v", "--verbose", action='store_true', help="verbose info")
    args = parser.parse_args()


    if(args.can == None):
        args.can = 'can0' 

    if(args.ecuaddr != None):
        deftx = getint(args.ecuaddr)

    # list of ECUs ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    if(args.config != None):
        if(args.config == 'dev'):  # short
            args.config = 'devices.json'
        # get configuration from file
        with open(args.config, 'r') as file:
            devjson = json.load(file)
        # make ECU list
        for device, config in devjson.items():
            addrtx = getint(config.get("tx"))
            dplist = config.get("dpList")
            # make ecu
            ecu = open3e.Open3Eclass.O3Eclass(ecutx=addrtx, doip=args.doip, can=args.can, dev=dplist)
            dicEcus[addrtx] = ecu
            dicDevAddrs[device] = addrtx
    else:
        # only default device
        ecu = open3e.Open3Eclass.O3Eclass(ecutx=deftx, doip=args.doip, can=args.can, dev=args.dev)
        dicEcus[deftx] = ecu
        dicDevAddrs[args.dev] = deftx
        

    # MQTT setup ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    mqtt_client = None
    if(args.mqtt != None):
        if (args.mqttclientid != None):
            open3e_client_id = args.mqttclientid
        else:
            open3e_client_id = "Open3E" + '_' + str(int(time.time()*1000))
        mqtt_client = paho.Client(paho.CallbackAPIVersion.VERSION2, open3e_client_id)  # Unique mqtt id using timestamp
        if(args.mqttuser != None):
            mlst = args.mqttuser.split(':')
            mqtt_client.username_pw_set(mlst[0], password=mlst[1])
        mlst = args.mqtt.split(':')
        mqttTopic = mlst[2] 
        if(args.mqttformatstring == None):
            mqttformatstring = "{didName}" # default
        else:
            mqttformatstring = args.mqttformatstring
        mqtt_client.on_connect = on_connect
        mqtt_client.on_disconnect = on_disconnect
        mqtt_client.on_message = on_message
        mqtt_client.connect(mlst[0], int(mlst[1]))
        mqtt_client.reconnect_delay_set(min_delay=1, max_delay=30)
        mqtt_client.loop_start()
        
    print("hallo!")

    # do what has to be done  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    try:
        # listener mode
        if(args.listen != None):
            listen(args.read, args.timestep)

        # read cmd line reads
        elif(args.read != None):
            jobs = eval_complex_list(args.read)
            mlvl = 0  # only val 
            if(len(jobs) > 1): mlvl |= 1  # show did nr
            while(True):
                for ecudidsub in jobs:
                    ensure_ecu(ecudidsub[0])
                    if(len(dicEcus) > 1): mlvl |= 4  # show ecu addr
                    try:
                        readbydid(addr=ecudidsub[0], did=ecudidsub[1], raw=args.raw, msglvl=mlvl, sub=ecudidsub[2])
                    except NegativeResponseException as e:
                        print(f'Device rejected this read access. Probably DID {ecudidsub[1]} is not available.\nErr: {e}')
                    time.sleep(0.02)
                if(args.timestep != None):
                    time.sleep(float(eval(args.timestep)))
                else:
                    break

        # experimental write to did
        elif(args.write != None):
            if(args.raw == True):
                jobs = args.write.split(",")
                for job in jobs:
                    writeArg = job.split("=")
                    #ecu,didkey = get_ecudid(writeArg[0])
                    lsteds = eval_complex(writeArg[0])
                    ecu = lsteds[0][0]  # int
                    did = lsteds[0][1]  # may be string
                    sub = lsteds[0][2]  # may be None or string
                    val=str(writeArg[1]).replace("0x","")     #!?!?!?
                    if args.forcesid77:
                        print(f"write raw: {ecu}.{did}.{sub} = {val}")
                        ecu77 = open3e.Open3Eclass.O3Eclass(ecutx=dicEcus[ecu].tx+2, doip=args.doip, can=args.can, dev=args.dev)
                        succ,code = ecu77.writeByDid(did, val, raw=True, useService77=True, sub=sub)
                        ecu77.close()
                    else:
                        ensure_ecu(ecu)
                        print(f"write raw: {ecu}.{did}.{sub} = {val}")
                        succ,code = dicEcus[ecu].writeByDid(did, val, raw=True, useService77=False, sub=sub)
                    print(f"success: {succ}, code: {code}")
            elif(args.json == True):
                writeArg = args.write.split("=")
                #ecu,didkey = get_ecudid(writeArg[0])
                lsteds = eval_complex(writeArg[0])
                ecu = lsteds[0][0]
                did = lsteds[0][1]
                sub = lsteds[0][2]
                val = json.loads(writeArg[1])
                if args.forcesid77:
                    print(f"write: {ecu}.{did}.{sub} = {val}")
                    ecu77 = open3e.Open3Eclass.O3Eclass(ecutx=dicEcus[ecu].tx+2, doip=args.doip, can=args.can, dev=args.dev)
                    succ,code = ecu77.writeByDid(did, val, raw=False, useService77=True)
                    ecu77.close()
                else:
                    ensure_ecu(ecu)
                    print(f"write: {ecu}.{did}.{sub} = {val}")
                    succ,code = dicEcus[ecu].writeByDid(did, val, raw=False, useService77=False)
                print(f"success: {succ}, code: {code}")  
            else:
                jobs = args.write.split(",")
                for job in jobs:
                    writeArg = job.split("=")
                    #ecu,didkey = get_ecudid(writeArg[0])
                    lsteds = eval_complex(writeArg[0])
                    ecu = lsteds[0][0]  # int
                    did = lsteds[0][1]  # may be string
                    sub = lsteds[0][2]  # may be None or string
                    val = writeArg[1]   # must be decoded form
                    if args.forcesid77:
                        print(f"write raw: {ecu}.{did}.{sub} = {val}")
                        ecu77 = open3e.Open3Eclass.O3Eclass(ecutx=dicEcus[ecu].tx+2, doip=args.doip, can=args.can, dev=args.dev)
                        succ,code = ecu77.writeByDid(did, val, raw=False, useService77=True, sub=sub)
                        ecu77.close()
                    else:
                        ensure_ecu(ecu)
                        print(f"write raw: {ecu}.{did}.{sub} = {val}")
                        succ,code = dicEcus[ecu].writeByDid(did, val, raw=False, useService77=False, sub=sub)
                    print(f"success: {succ}, code: {code}")
            time.sleep(0.1)

        # scanall
        elif(args.scanall == True):
            msglvl = 1  # show did nr
            if(len(dicEcus) > 1):
                msglvl = 5  # show ECU addr also
            for addr,ecu in dicEcus.items():
                #? if(args.verbose == True):
                print(f"reading {hex(addr)}, {dicEcus[addr].numdps} datapoints, please be patient...")
                lst = ecu.readAll(args.raw)
                for itm in lst:
                    showread(addr=addr, did=itm[0], value=itm[1], idstr=itm[2], msglvl=msglvl)

    except (KeyboardInterrupt, InterruptedError):
        # <STRG-C> oder SIGINT to stop
        # Use <kill -s SIGINT pid> to send SIGINT
        pass
                    
    # close all connections before exit
    for ecu in dicEcus.values():
        if(args.verbose):
            print(f"closing {hex(ecu.tx)} - bye!")
        ecu.close()

    if(mqtt_client != None):
        if(args.verbose):
            print("closing MQTT client")
        mqtt_client.disconnect()


if __name__ == "__main__":
    main()