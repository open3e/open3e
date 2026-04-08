"""
  Copyright 2026 MyHomeMyData
  
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
# Convert Open3E datapoint list from JSON back to python file and adds info about writablility of data points.
#
# There is no need to use this tool when using open3e.
#
# 10.02.2026: Initial version
#

import json
from datetime import date

import open3e.Open3Eenums
import open3e.Open3Edatapoints
import open3e.Open3EdatapointsVariants

from open3e.Open3Ecodecs import *

try:
    with open('Open3Edatapoints_writables.json', 'r') as file:
        dids_writable = json.load(file)
except:
    dids_writable = {}

def collectComments(fn):
    # Collect all comments in file named fn and return a dict
    # Only works with dids in a single line
    # did is expected in columns 8 to 12
    comments = {}
    with open(fn, 'r') as f:
        for line in f:
            try:
                did = int(line[8:12])
                p = line.find('#',14)
                if p>0:
                    comments[did] = line[p:-1]  # remove \n
            except:
                pass
    return comments

def dids2string(dids,comments):
    # Collect all data points
    # return a string containing one line of text per data point
    didsStr = ''
    for dp in dids:
        codecStr = dids[dp].getCodecString()
        if codecStr.find('acc="') == -1:
            # Access info not yet included. Add it:
            if str(dp) in dids_writable:
                codecStr = f'{codecStr[:-1]}, acc="rw")'
            else:
                codecStr = f'{codecStr[:-1]}, acc="ro")'
        codecStr += ',' # Add final comma of this list element
        if dp in comments:
            # Add comment
            codecStr += '    '+comments[dp]
        # Data point completed, add to the string:
        didsStr += f"        {dp} : {codecStr}\n"
    return didsStr

def main():
    dataIdentifiers = dict(open3e.Open3Edatapoints.dataIdentifiers)
    comments = collectComments('Open3Edatapoints.py')
    print(dids2string(dataIdentifiers["dids"],comments))

if __name__ == "__main__":
    main()
