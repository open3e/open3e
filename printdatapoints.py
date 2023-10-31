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

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-dev", "--dev", type=str, help="--dev vdens or vcal or vx3 or vair")
args = parser.parse_args()

if(args.dev == None):
    args.dev = "vcal"

devfile = ""
if(args.dev == "vcal"):
    devfile = "Open3EdatapointsVcal.py"
if(args.dev == "vdens"):
    devfile = "Open3EdatapointsVdens.py"
if(args.dev == "vx3"):
    devfile = "Open3EdatapointsVx3.py"
if(args.dev == "vair"):
    devfile = "Open3EdatapointsVair.py"

def read_enums(file):
    dic = {}
    with open(file, 'r') as file:
        lines = file.readlines()

    for line in lines:
        line = line.strip()
        if line:
            parts = line.split(':')
            if len(parts) > 1:
                did = parts[0].strip()
                stuff = parts[1].strip()
                dic[did] = stuff

    return dic

unifile = "Open3Edatapoints.py"

dicuni = read_enums(unifile)
dicdev = read_enums(devfile)

for did in dicdev:
    if did.isnumeric():
        if dicdev[did].lower().startswith("none"):
            if did in dicuni:
                dicdev[did] = dicuni[did]
        print(f"{did} : {dicdev[did]}")

