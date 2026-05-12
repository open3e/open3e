"""
  Copyright 2025 MyHomeMyData
  
  Licensed under the Apache License, Version 2.0 (the "License");
  you 05_may not use this file except in compliance with the License.
  You 05_may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License.
"""

#
# Convert Open3E datapoint list to JSON format, e.g. for use in ioBroker adapter ioBroker.e3oncan.
#
# There is no need to use this tool when using open3e. The resulting files are not used by open3e.
#
# 08.02.2024: Added Version-String to Open3Edatapoints.json
#
# 14.01.2026: Deactivated generation of list of writables. Now based on vddList
# 14.01.2026: Added creation of list of variant dids.

import argparse
import json
import os
from datetime import date

import open3e.Open3Edatapoints
import open3e.Open3EdatapointsVariants

from open3e.Open3Ecodecs import *

tool_version_string = '1.0.0'

def get_package_version_string():
    package_name = "open3e"

    try:
        from importlib.metadata import version
        package_version = version(package_name)
    except ImportError:
        package_version = "unknown"

    try:
        from open3e import _scm_version as scm_version
        git_ref = scm_version.git_ref
    except ImportError:
        git_ref = "unknown"

    return f'{tool_version_string} based on open3e {package_version} ({git_ref})'

def main():
    help_version_string = get_package_version_string()

    parser = argparse.ArgumentParser(fromfile_prefix_chars='@', epilog=f'open3e_dids2json {help_version_string}')
    parser.add_argument("-p", "--path", type=str, help="optional path to store output files")
    args = parser.parse_args()

    dataIdentifiers = dict(open3e.Open3Edatapoints.dataIdentifiers)
    variants = dict(open3e.Open3EdatapointsVariants.dataIdentifiers)

    didsDict = {}
    didsDictVars = {}

    if args.path != None:
        fpath = os.path.join(args.path, '')
    else:
        fpath = ''

    print('This tool converts data points for use in the ioBroker adapter ioBroker.e3oncan. It is not used by open3e.')
    print('Start conversion of data points to json format.')

    cntDps = 0
    cntVars = 0
    cntWrt = 0

    for dp in dataIdentifiers["dids"]:
        didsDict[dp] = dataIdentifiers["dids"][dp].getCodecInfo()
        cntDps += 1

    didsDict['Version'] = dataIdentifiers['Version']

    with open(fpath+'Open3Edatapoints.json', 'w') as json_file:
        json.dump(didsDict, json_file, indent=2)

    for dp in variants["dids"]:
        didsDictVars[dp] = {}
        for v in variants["dids"][dp]:
            didsDictVars[dp][v] = variants["dids"][dp][v].getCodecInfo()
        cntVars += 1

    didsDictVars['Version'] = variants["Version"]

    with open(fpath+'Open3EdatapointsVariants.json', 'w') as json_file:
        json.dump(didsDictVars, json_file, indent=2)

    print(f'{str(cntDps)} dids converted to JSON format. See file "{fpath}Open3Edatapoints.json"')
    print(f'{str(cntVars)} variant dids converted to JSON format. See file "{fpath}Open3EdatapointsVariants.json"')

if __name__ == "__main__":
    main()