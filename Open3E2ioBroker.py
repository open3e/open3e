#
# Convert Open3E datapoint list to JSON format for use in ioBroker adapter E3onCAN

import argparse
import time
import json

import Open3Edatapoints

import Open3Ecodecs
from Open3Ecodecs import *

dataIdentifiers = dict(Open3Edatapoints.dataIdentifiers["dids"])

didsDict = {}
cnt = 0
for dp in dataIdentifiers:
    didsDict[dp] = dataIdentifiers[dp].getCodecInfo()
    cnt += 1

dpDict = {"common": didsDict,
          "0x680": {}
          }

with open('Open3Edatapoints_ioBroker.json', 'w') as json_file:
    json.dump(dpDict, json_file, indent=2)

print(str(cnt)+' dids converted to JSON format.')
