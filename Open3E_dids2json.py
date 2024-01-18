#
# Convert Open3E datapoint list to JSON format, e.g. for use in ioBroker adapter E3onCAN
#
# Create white list of writable datapoints based on filter patterns

import json

import Open3Edatapoints

from Open3Ecodecs import *

dataIdentifiers = dict(Open3Edatapoints.dataIdentifiers["dids"])

didsDict = {}
didsWritable = {}
writablesPatterns = ['setpoint',
                     'schedule',
                     'backupboxconfiguration',
                     'target',
                     'offset',
                     'minimummaximumset',
                     'minimummaximumlimit',
                     'domestichotwatercirculationpump'
                     ]

def setToWritable(id):
    res = False
    for pattern in writablesPatterns:
        if pattern in id.lower():
            return True
    return False

print('Start conversion of datapoints "Open3Edatapoints.py" to json format.')
print('Create white list for writable datapoints based on filter patterns.\n')

cntDps = 0
cntWrt = 0

for dp in dataIdentifiers:
    didsDict[dp] = dataIdentifiers[dp].getCodecInfo()
    if setToWritable(didsDict[dp]['id']):
        didsWritable[dp] = didsDict[dp]['id']
        cntWrt += 1
    cntDps += 1

with open('Open3Edatapoints.json', 'w') as json_file:
    json.dump(didsDict, json_file, indent=2)

with open('Open3Edatapoints_writables.json', 'w') as json_file:
    json.dump(didsWritable, json_file, indent=2)

print(str(cntDps)+' dids converted to JSON format. See file "Open3Edatapoints.json"')
print(str(cntWrt)+' dids identified as writable. See file "Open3Edatapoints_writables.json"')
print('Done.')
