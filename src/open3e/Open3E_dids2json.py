#
# Convert Open3E datapoint list to JSON format, e.g. for use in ioBroker adapter ioBroker.e3oncan.
#
# There is no need to use this tool when using open3e. The resulting files are not used by open3e.
#
# 08.02.2024: Added Version-String to Open3Edatapoints.json
#
# 14.01.2026: Deactivated generation of list of writables. Now based on vddList
# 14.01.2026: Added creation of list of variant dids.

import json
from datetime import date

import open3e.Open3Edatapoints
import open3e.Open3EdatapointsVariants

from open3e.Open3Ecodecs import *


def main():
    dataIdentifiers = dict(open3e.Open3Edatapoints.dataIdentifiers["dids"])
    variants = dict(open3e.Open3EdatapointsVariants.dataIdentifiers)

    didsDict = {}
    didsDictVars = {}

    print('This tool converts data points for use in the ioBroker adapter ioBroker.e3oncan. It is not used by open3e.')
    print('Start conversion of data points "open3e.Open3Edatapoints.py" and "open3e.Open3EdatapointsVariants.py" to json format.')

    didsListVersion = date.today().strftime("%Y%m%d")

    cntDps = 0
    cntVars = 0
    cntWrt = 0

    for dp in dataIdentifiers:
        didsDict[dp] = dataIdentifiers[dp].getCodecInfo()
        cntDps += 1

    didsDict['Version'] = didsListVersion

    with open('Open3Edatapoints.json', 'w') as json_file:
        json.dump(didsDict, json_file, indent=2)

    for dp in variants["dids"]:
        didsDictVars[dp] = {}
        for v in variants["dids"][dp]:
            didsDictVars[dp][v] = variants["dids"][dp][v].getCodecInfo()
        cntVars += 1

    didsDictVars['Version'] = variants["Version"]

    with open('Open3EdatapointsVariants.json', 'w') as json_file:
        json.dump(didsDictVars, json_file, indent=2)

    print(str(cntDps)+' dids converted to JSON format. See file "Open3Edatapoints.json"')
    print(str(cntVars)+' variant dids converted to JSON format. See file "Open3EdatapointsVariants.json"')
    print('Done.')

if __name__ == "__main__":
    main()