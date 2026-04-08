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
# Convert Open3E datapoint list from JSON to markdown format, e.g. for ocumentation purpose.
#
# There is no need to use this tool when using open3e. The resulting files are not used by open3e.
#
# 07.02.2026: Initial version
#

import argparse
import json
from datetime import date

import open3e.Open3Eenums
import open3e.Open3Edatapoints
import open3e.Open3EdatapointsVariants

from open3e.Open3Ecodecs import *

tool_version_string = '0.1.0'

DoI_default = [256,257,258,259,260,261,262,263,264,265,266,268,     # Frequently used Dids
               269,271,274,282,284,318,320,321,322,324,325,355,
               381,389,391,396,491,497,531,535,902,954,987,1043,
               1190,1294,1311,1315,1316,1333,1337,1391,1392,1393,
               1415,1603,1643,1664,1684,1690,1771,1772,1775,1776,
               1799,1801,1802,1828,1830,1831,1832,1833,1834,1836,
               1842,2214,2256,2320,2333,2334,2346,2351,2352,2369,
               2486,2487,2488,2494,2495,2496,2569,2760,2735,2806,
               3016]
md_indent = '- '                                                    # Indentation of sub codecs
meta_codecs = ['O3EList','O3EComplexType']                          # List of meta codecs, show in italic
ignored_ids = ['ListEntries']                                       # List of ids to be ignored (helper ids for json format)
enums = dict(open3e.Open3Eenums.E3Enums)                            # Enumerations known to open3e
enums_excluded = ['Errors','Warnings','States','Infos','Country']   # Do NOT list the entries of enumerations for those keys

def addMouseOver(txt, mouse_over):
    if len(txt) > 0 and txt[0] == '[' and '##' in txt:
        # txt already contains a mouse over. Add another one
        md = txt.replace('## "',f'## "{mouse_over} ')
    else:
        md = f'[{txt}](## "{mouse_over}")'
    return md

def getDescStrTableColumn(codecs):
    if args.showdesc == False:
        return ''
    if 'args' in codecs and 'desc' in codecs['args']:
        return f'{codecs['args']['desc']}|'
    else:
        return ''

def getDescStrMouseOver(codecs):
    if 'args' in codecs and 'desc' in codecs['args']:
        return codecs['args']['desc']
    else:
        return ''

def getIdStr(id, codecs, prefix):
    if prefix == '':
        id_str = f'**{id}**'      # main id in bold
    else:
        id_str = id
    if codecs['codec'] == 'O3EEnum' and codecs['args']['listStr'] in enums and not (codecs['args']['listStr'] in enums_excluded):
        # Add list if enums as mouse over
        id_str = addMouseOver(id_str, json.dumps(enums[codecs['args']['listStr']],indent=None).replace('"',''))
    desc = getDescStrMouseOver(codecs)
    if desc != '':
        # Add description as mouse over
        id_str = addMouseOver(id_str, desc)
    return id_str

def getDescTableHeader(txt):
    if args.showdesc == False:
        return ''
    if txt:
        return ' Description |'
    else:
        return ' :--- |'

def getCodecStr(codec_str):
    if codec_str in meta_codecs:
        return f'*{codec_str}*' # meta codecs in italic
    else:
        return codec_str

def getUniStr(codecs):
    if 'args' in codecs and 'unit' in codecs['args']:
        md = codecs['args']['unit']
        if md == '°C':
            md = f'[°C](## "°C or °F (system configuration)")'
        return md
    else:
        return ''

def getInfoStr(codecs):
    if 'args' in codecs and 'info' in codecs['args']:
        return codecs['args']['info']
    else:
        return ''
    
def getAccesStr(codecs):
    if 'args' in codecs and 'acc' in codecs['args']:
        if codecs['args']['acc'] == 'rw':
            return '**rw**'
        else:
            return 'ro'
    else:
        return '**??**'

def codec2md(codecs, prefix='', accessStr=''):
    md = ''
    if not (codecs['id'] in ignored_ids):
        # skip json helper ids
        md += F'{prefix}{getIdStr(codecs['id'], codecs, prefix)}|{getCodecStr(codecs['codec'])}|{str(codecs['len'])}|{getUniStr(codecs)}|{getDescStrTableColumn(codecs)}{accessStr}|{getInfoStr(codecs)}'
    if not args.compact:
        if 'subTypes' in codecs['args']:
            for codec in codecs['args']['subTypes']:
                if not (codec['id'] in ignored_ids):
                    md += f'|\n| |{codec2md(codec, prefix+md_indent, '')}'
                else:
                    md += f'{codec2md(codec, prefix+md_indent, '')}'
    return md

def did2md(did, codecs):
    return f'|**{str(did)}**|{codec2md(codecs, '', getAccesStr(codecs))}|\n'

def printListOfDoI(DoI):
    dataIdentifiers = dict(open3e.Open3Edatapoints.dataIdentifiers)
    cntDoI = 0
    print('List of Default-DoI:')
    for did in DoI:
        if did in dataIdentifiers['dids']:
            print(f'{did}: {dataIdentifiers['dids'][did].getCodecInfo()['id']}')
            cntDoI += 1
    print(f'{cntDoI} elements.')
    return

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


#~~~~~~~~~~~~~~~~~~~~~~
# Main
#~~~~~~~~~~~~~~~~~~~~~~

help_version_string = get_package_version_string()

parser = argparse.ArgumentParser(fromfile_prefix_chars='@', epilog=f'open3e_dids2md {help_version_string}')
parser.add_argument("-d", "--dids", type=str, help="list specified dids only, e.g. 256,268,269")
parser.add_argument("-f", "--filename", type=str, help="send result to file instead of stdout")
parser.add_argument("-c", "--compact", action='store_true', help="list main data points only, don't list subs")
parser.add_argument("-s", "--showdesc", action='store_true', help="list description as an extra column")
args = parser.parse_args()

# # Print list of default DoI:
# import sys
# printListOfDoI(DoI_default)
# sys.exit(0)

dataIdentifiers = dict(open3e.Open3Edatapoints.dataIdentifiers)
variants = dict(open3e.Open3EdatapointsVariants.dataIdentifiers)

didsDict = {}
didsDictVars = {}

cntDps = 0
cntVars = 0
cntWrt = 0

table_header =  f'|  Did | ID   | Codec | Length | Unit  | {getDescTableHeader(True)}  Access | Further info |\n'
table_header += f'| ---: | :--- | :---  | ---:   | :---: | {getDescTableHeader(False)} :---:  | :---         |\n'

# Convert list of general datapoints to json

for dp in dataIdentifiers["dids"]:
    didsDict[dp] = dataIdentifiers["dids"][dp].getCodecInfo()
    cntDps += 1

didsDict['Version'] = dataIdentifiers['Version']

# Convert list of variant datapoints to json

for dp in variants["dids"]:
    didsDictVars[dp] = {}
    for v in variants["dids"][dp]:
        didsDictVars[dp][v] = variants["dids"][dp][v].getCodecInfo()
    cntVars += 1

didsDictVars['Version'] = variants["Version"]

# Create markdonw formatted version of data points

md = ''
md += '# Open3E - List of data points\n'
md += '- Version of general data points: ' + didsDict['Version'] + '\n'
md += '- Version of variant data points: ' + didsDictVars['Version'] + '\n\n'

md += '### Remarks\n'
md += '* Information on write access to data points (column Access) is based on documents of Viessmann\n'
md += '  * ro => data point is read only\n'
md += '  * rw => data point is read and write. However, device my reject or ignore write access anyway\n\n'

if args.dids == None:
    md += '### Table of contents\n'
    md += '[Frequently used data points including subs](#frequently-used-data-points-including-subs)\n\n'
    md += '[Frequently used data points as compact list](#frequently-used-data-points-in-compact-format)\n\n'
    md += '[All presently known data points including subs](#all-presently-known-data-points-including-subs)\n\n'
    md += '[All presently known data points as compact list](#all-presently-known-data-points-in-compact-format)\n\n'
    md += '## Frequently used data points including subs\n'
else:
    md += '## User defined list of data points\n'

md += table_header

if args.dids != None:
    dids = list(args.dids.replace(' ','').split(','))
else:
    dids = DoI_default

dids.sort()     # Sort data points in ascending order

for did in dids:
    if int(did) in didsDict:
        md += did2md(int(did), didsDict[int(did)])
    if int(did) in didsDictVars:
        for variant in didsDictVars[int(did)]:
            md += did2md(int(did), didsDictVars[int(did)][variant])

if args.dids != None:
    # User specified list of dids. Just print the list and exit:
    if args.filename != None:
        with open(args.filename, 'w') as txt_file:
            print(md, file=txt_file)
    else:
        print(md)
    import sys
    sys.exit(0)

args.compact = True
md += '## Frequently used data points in compact format\n\n'
md += '[Back to table of contents](#table-of-contents)\n\n'
md += table_header
for did in dids:
    if int(did) in didsDict:
        md += did2md(int(did), didsDict[int(did)])
    if int(did) in didsDictVars:
        for variant in didsDictVars[int(did)]:
            md += did2md(int(did), didsDictVars[int(did)][variant])

args.compact = False
md += '## All presently known data points including subs\n\n'
md += '[Back to table of contents](#table-of-contents)\n\n'
md += table_header

for key in didsDict:
    if key != 'Version':
        did = int(key)
        md += did2md(did, didsDict[did])
        if did in didsDictVars:
            for variant in didsDictVars[did]:
                md += did2md(did, didsDictVars[did][variant])

args.compact = True
md += '## All presently known data points in compact format\n\n'
md += '[Back to table of contents](#table-of-contents)\n\n'
md += table_header

for key in didsDict:
    if key != 'Version':
        did = int(key)
        md += did2md(did, didsDict[did])
        if did in didsDictVars:
            for variant in didsDictVars[did]:
                md += did2md(did, didsDictVars[did][variant])

if args.filename != None:
    with open(args.filename, 'w') as txt_file:
        print(md, file=txt_file)
else:
    print(md)
