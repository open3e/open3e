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

import Open3Eclass

# default ECU address
deftx = 0x680

# ECUs and their addresses
lstecus = {}     # addr:ecu
dicdevaddrs = {}  # str:int


# utils ~~~~~~~~~~~~~~~~~~~~~~~
def getint(v) -> int:
    if type(v) is int:
        return v
    else:
        return int(eval(str(v)))

def addr_of_dev(v) -> int: 
    if(v in dicdevaddrs):
        return dicdevaddrs[v]
    return v

def dev_of_addr(addr:int):
    for key, val in dicdevaddrs.items():
        if val == addr:
            return key
    # If the value is not found, you might want to handle this case accordingly
    return None
        
def get_ecudid(v):
    s = str(v)
    parts = s.split(".")
    if(len(parts) > 1):
        return getint(parts[0]),getint(parts[1])
    else:
        return deftx,getint(parts[0])

# complex addressing: 0x680.[257,258,259] or 0x680.256 or 256
def eval_complex(v) -> list: # returns list of [ecu,did] items
    s = str(v).replace(' ','')
    parts = s.split(".")
    if(len(parts) == 1):
        # only did
        return [[deftx,getint(addr_of_dev(parts[0]))]]
    elif(len(parts) == 2):  # maybe later 3: ecu.did.sub... 
        ecu = getint(addr_of_dev((parts[0])))
        parts[1] = parts[1].replace('[','').replace(']','')
        parts = parts[1].split(",")
        if(len(parts) == 1):
            # only ecu.did, no did list
            return [[ecu,getint(parts[0])]]
        else:
            # ecu addr and did list
            lst = []
            for did in parts:
                lst.append([ecu,getint(did)])
            return lst

# enum of complex addressing separated by ','
def eval_complex_list(v) -> list:  # returns list of [ecu,did] items
    sl = list(str(v).replace(' ',''))
    open = 0
    for i in range(len(sl)-1, -1, -1):
        if sl[i] == ']':
            open += 1
        elif sl[i] == '[':
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


def ensure_ecu(addr:int):
    if(not (addr in lstecus)):
        ecu = Open3Eclass.O3Eclass(ecutx=addr, doip=args.doip, can=args.can, 
                                    device=args.dev, raw=args.raw, verbose=args.verbose)
        lstecus[addr] = ecu

    
 

def listen(listento:str, readdids=None, timestep=0):
    if(args.mqtt == None):
        raise Exception('mqtt option is mandatory for listener mode')

    cmnd_queue = []
    
    def on_connect(client, userdata, flags, rc):
        client.subscribe(listento)
        
    def on_disconnect(client, userdata, rc):
        if rc != 0:
            print('mqtt broker disconnected. rc = ' + str(rc))
    
    def on_message(client, userdata, msg):
        topic = str(msg.topic)            # Topic in String umwandeln
        if topic == listento:
            try:
                payload = json.loads(msg.payload.decode())  # Payload in Dict umwandeln
                cmnd_queue.append(payload)
            except:
                print('bad payload: ' + str(msg.payload)+'; topic: ' + str(msg.topic))
                payload = ''

    def getaddr(cd):
        if 'addr' in cd: return getint(addr_of_dev(cd['addr']))
        else: return deftx 

    def cmnd_loop():
        cmnds = ['read','read-json','read-raw','write','write-raw']
        next_read_time = time.time()
        while True:
            if len(cmnd_queue) > 0:
                cd = cmnd_queue.pop(0)

                if not cd['mode'] in cmnds:
                    print('bad mode value = ' + str(cd['mode']) + '\nSupported commands are: ' + json.dumps(cmnds)[1:-1])
                    pass

                if cd['mode'] in ['read','read-json','read-raw']:
                    addr = getaddr(cd)
                    dids = cd['data']
                    ensure_ecu(addr) 
                    for did in dids:
                        readbydid(addr, getint(did), json=(cd['mode']=='read-json'), raw=(cd['mode']=='read-raw'))
                        time.sleep(0.01)            # 10 ms delay before next request

                if cd['mode'] == 'write':
                    # ToDo: Umrechnung über Codec ergänzen. Wechselwirkung mit flag_rawmode beachten!
                    addr = getaddr(cd)
                    ensure_ecu(addr)
                    for wd in cd['data']:
                        didKey = getint(wd[0])    # key: convert numeric or string parameter to numeric value
                        didVal = getint(wd[1])    # value: dto.
                        lstecus[addr].writeByDid(didKey, didVal, raw=False) 
                        time.sleep(0.1)
                    
                if cd['mode'] == 'write-raw':
                    addr = getaddr(cd)
                    ensure_ecu(addr)
                    for wd in cd['data']:
                        didKey = getint(wd[0])                  # key is submitted as numeric value
                        didVal = str(wd[1]).replace('0x','')    # val is submitted as hex string
                        lstecus[addr].writeByDid(didKey, didVal, raw=True)
                        time.sleep(0.1)
            else:
                if (readdids != None):
                    if (next_read_time > 0) and (time.time() > next_read_time):
                        # add dids to read to command queue
                        jobs =  eval_complex_list(readdids)
                        for ecudid in jobs:
                            cmnd_queue.append({'mode':'read', 'addr': ecudid[0], 'data': [ecudid[1]]})
                        if(timestep != None):
                            next_read_time = next_read_time + int(timestep)
                        else:
                            next_read_time = 0    # Don't do it again
                    
            time.sleep(0.01)

    mqtt_client.on_connect = on_connect
    mqtt_client.on_disconnect = on_disconnect
    mqtt_client.on_message = on_message
    print("Enter listener mode, waiting for commands on mqtt...")

    # and go...
    cmnd_loop() 


def readbydid(addr:int, did:int, json=None, raw=None, msglvl=0):
    if(raw == None): 
        raw = args.raw
    try:
        value,idstr =  lstecus[addr].readByDid(did, raw=args.raw)
        showread(addr, did, value, idstr, json, msglvl)    
    except TimeoutError:
        return
    

def showread(addr, did, value, idstr, json=None, msglvl=0):   # msglvl: bcd, 1=didnr, 2=didname, 4=ecuaddr
    def mqttdump(topic, obj):
        if (type(obj)==dict):
            for k, itm in obj.items():
                mqttdump(topic+'/'+str(k),itm)
        elif (type(obj)==list):
            for k in range(len(obj)):
                mqttdump(topic+'/'+str(k),obj[k])
        else:
            ret = mqtt_client.publish(topic, str(obj))     

    if(json == None): 
        json = args.json

    if(mqtt_client != None):
        publishStr = args.mqttformatstring.format(
            ecuAddr = addr,
            device = dev_of_addr(addr),
            didName = idstr,
            didNumber = did
        )
        
        if(json):
            # Send one JSON message
            ret = mqtt_client.publish(mqttTopic + "/" + publishStr, json.dumps(value))    
        else:
            # Split down to scalar types
            mqttdump(mqttTopic + "/" + publishStr, value)
        
        if(args.verbose == True):
            print (hex(addr), did, idstr, value)
    else:
        if(args.verbose == True):
            print (hex(addr), did, idstr, value)
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
parser.add_argument("-muser", "--mqttuser", type=str, help="mqtt username:password")
parser.add_argument("-j", "--json", action='store_true', help="send JSON structure")
parser.add_argument("-v", "--verbose", action='store_true', help="verbose info")
parser.add_argument("-cnfg", "--config", type=str, help="json configuration file")
parser.add_argument("-tx", "--ecuaddr", type=str, help="ECU Address")
args = parser.parse_args()


if(args.dev == None):
    args.dev = "vcal"

if(args.ecuaddr != None):
    deftx = getint(args.ecuaddr)

if(args.verbose == None):
    args.verbose = False   


# list of ECUs ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
if(args.config != None):
    # get configuration from file
    with open(args.config, 'r') as file:
        data = json.load(file)

    # make ECU list
    for entry in data:
#        print("Interval:", entry["timestep"])
        for device in entry["devices"]:
#            print("TX:", device["tx"])
#            print("Device:", device["dev"])
            addr = getint(device['tx'])
            dev = device['dev']
            dicdevaddrs[dev] = addr
            ecu = Open3Eclass.O3Eclass(ecutx=addr, doip=args.doip, can=args.can, 
                                        device=dev, raw=args.raw, verbose=args.verbose)
            lstecus[addr] = ecu
else:
    ecu = Open3Eclass.O3Eclass(ecutx=deftx, doip=args.doip, can=args.can,
                                device=args.dev, raw=args.raw, verbose=args.verbose)
    lstecus[deftx] = ecu
    

# MQTT setup ~~~~~~~~~~~~~~~~~~
mqtt_client = None
if(args.mqtt != None):
    mqtt_client = paho.Client("Open3E" + '_' + str(int(time.time()*1000)))  # Unique mqtt id using timestamp
    if(args.mqttuser != None):
        mlst = args.mqttuser.split(':')
        mqtt_client.username_pw_set(mlst[0], password=mlst[1])
    mlst = args.mqtt.split(':')
    mqttTopic = mlst[2] 
    mqtt_client.connect(mlst[0], int(mlst[1]))
    mqtt_client.reconnect_delay_set(min_delay=1, max_delay=30)
    mqtt_client.loop_start()
    
    
# do what has to be done  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
try:

    if(args.listen != None):
        listen(args.listen, args.read, args.timestep)

    # read cmd line - TODO: lists from config file
    elif(args.read != None):
        jobs =  eval_complex_list(args.read)
        mlvl = 0  # only val 
        if(len(jobs) > 1): mlvl += 1  # show did nr
        while(True):
            for ecudid in jobs:
                ensure_ecu(ecudid[0])
                if(len(lstecus) > 1): mlvl |= 4  # show ecu addr
                val,idstr = lstecus[ecudid[0]].readByDid(ecudid[1])
                showread(addr=ecudid[0], value=val, idstr=idstr, did=ecudid[1])
            if(args.timestep != None):
                time.sleep(float(eval(args.timestep)))
            else:
                break

    # experimental write to did
    elif(args.write != None):
        if(args.raw != True):
            raise Exception("Error: write only accepts raw data, use -raw param")
        writeArg = args.write.split("=")
        ecu,didkey = get_ecudid(writeArg[0])
        didVal=str(writeArg[1]).replace("0x","")
        ensure_ecu(ecu)
        print(f"write {ecu}.{didkey} = {didVal}")
        succ,code = lstecus[ecu].writeByDid(didkey, didVal)
        print(f"success: {succ}, code: {code}")
        time.sleep(0.1)

    # scanall
    elif(args.scanall == True):
        msglvl = 1  # show did nr
        if(len(lstecus) > 1):
            msglvl = 5  # show ECU addr also
        for addr,ecu in lstecus.items():
            lst = ecu.readAll()
            for itm in lst:
                showread(addr=addr, did=itm[0], value=itm[1], idstr=itm[2], msglvl=msglvl)


except (KeyboardInterrupt, InterruptedError):
    # <STRG-C> oder SIGINT to stop
    # Use <kill -s SIGINT pid> to send SIGINT
    pass
                
# close all connections before exit
for ecu in lstecus.values():
    ecu.close()
    
