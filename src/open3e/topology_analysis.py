"""
Pure E3 bus topology analysis — no open3e I/O.

Input:  topology_data dict collected by Open3Etopology
Output: build_topology_summary() -> {'json': dict, 'html': str, 'text': str}

TOPOLOGY_DIDS: frozenset of DID numbers that carry topology matrix data with a
proper (non-Raw) codec. Extend this set when additional DIDs gain a real codec.
"""

from datetime import datetime, timezone

TOPOLOGY_DIDS = frozenset({954, 1286, 1287, 1288, 1289})

_BUS_COLOR = {
    2:  '#eaf4ea',  # CanInternal
    3:  '#eaeaf4',  # CanExternal
    6:  '#f4f0ea',  # CanRaw
    8:  '#f4eaea',  # ModBus
    14: '#f0eaf4',  # ServiceBus
}

# DeviceProperty IDs for devices that are never UDS-accessible
_KNOWN_DEV_PROP_NAMES = {
    27: 'E380',
}


def _sw_build(sw_str: str) -> int:
    """Extract YYWW build number (3rd segment) from a SW-version string."""
    try:
        return int(str(sw_str).split('.')[2])
    except (IndexError, ValueError):
        return 0


def _s(v) -> str:
    """Return str(v), or an em-dash for None / empty string."""
    return str(v) if v is not None and v != '' else '—'


def _extract_uds_devices(topology_data: dict) -> list:
    devices = []
    for can_addr, dev in (topology_data or {}).items():
        b = dev.get('bus_id')
        if not b:
            continue
        dp = b.get('DeviceProperty', {})
        devices.append({
            'can_addr':    can_addr,
            'dev_type':    dp.get('Text') or str(dp.get('ID', '?')),
            'dev_prop_id': dp.get('ID'),
            'node_id':     b.get('BusAddress'),
            'sw_version':  b.get('SW-Version', ''),
            'hw_version':  b.get('HW-Version', ''),
            'vin':         b.get('VIN', ''),
        })
    return sorted(devices, key=lambda d: int(d['can_addr'], 16))


def _build_dev_prop_names(topology_data: dict) -> dict:
    name_map = {}
    for dev in (topology_data or {}).values():
        dp = (dev.get('bus_id') or {}).get('DeviceProperty', {})
        if dp.get('ID') is not None and dp.get('Text'):
            name_map[dp['ID']] = dp['Text']
    return name_map


def _collect_topology_elements(topology_data: dict, dev_prop_names: dict) -> list:
    element_map = {}
    for can_addr, dev in (topology_data or {}).items():
        for matrix in dev.get('matrices', []):
            if not matrix or matrix.get('Count', 0) == 0:
                continue
            elements = matrix.get('TopologyElement', [])
            if not isinstance(elements, list):
                continue
            for el in elements:
                node_id     = el.get('NodeID', -1)
                dev_prop    = el.get('DeviceProperty', -1)
                bus_type    = el.get('BusType', {})
                bus_type_id = bus_type.get('ID', -1)
                key = f"{bus_type_id}_{node_id}_{dev_prop}"

                if key not in element_map:
                    element_map[key] = {
                        'node_id':     node_id,
                        'bus_type':    bus_type.get('Text') or str(bus_type_id),
                        'bus_type_id': bus_type_id,
                        'dev_prop':    dev_prop,
                        'dev_type':    (dev_prop_names.get(dev_prop)
                                        or _KNOWN_DEV_PROP_NAMES.get(dev_prop)
                                        or str(dev_prop)),
                        'sw_version':  el.get('SW-Version', ''),
                        'hw_version':  el.get('HW-Version', ''),
                        'vin':         el.get('VIN', ''),
                        'reported_by': [can_addr],
                    }
                else:
                    existing = element_map[key]
                    if can_addr not in existing['reported_by']:
                        existing['reported_by'].append(can_addr)
                    if _sw_build(el.get('SW-Version', '')) > _sw_build(existing['sw_version']):
                        existing['sw_version'] = el.get('SW-Version', '')
                        existing['hw_version'] = el.get('HW-Version', '')
                        existing['vin']        = el.get('VIN', '')

    return sorted(element_map.values(), key=lambda e: (e['bus_type_id'], e['node_id']))


def _uds_keys(uds_devices: list) -> set:
    return {
        f"{d['vin']}_{d['devPropId']}"
        for d in uds_devices
        if d.get('vin') and d['vin'] != '0000000000000000' and d.get('devPropId') is not None
    }


def _is_uds(element: dict, keys: set) -> bool:
    """Works with both camelCase JSON result elements and snake_case internal elements."""
    vin      = element.get('vin') or element.get('VIN', '')
    dev_prop = element.get('devProp', element.get('dev_prop', -1))
    return bool(vin and vin != '0000000000000000'
                and f"{vin}_{dev_prop}" in keys)


# ── JSON ──────────────────────────────────────────────────────────────────────

def _build_json(uds_devices: list, topology_elements: list) -> dict:
    return {
        'scanTime': datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%S.000Z'),
        'udsDevices': [
            {
                'canAddr':   d['can_addr'],
                'devType':   d['dev_type'],
                'devPropId': d['dev_prop_id'],
                'nodeId':    d['node_id'],
                'swVersion': d['sw_version'],
                'hwVersion': d['hw_version'],
                'vin':       d['vin'],
            }
            for d in uds_devices
        ],
        'topologyElements': [
            {
                'nodeId':     e['node_id'],
                'busType':    e['bus_type'],
                'busTypeId':  e['bus_type_id'],
                'devProp':    e['dev_prop'],
                'devType':    e['dev_type'],
                'swVersion':  e['sw_version'],
                'hwVersion':  e['hw_version'],
                'vin':        e['vin'],
                'reportedBy': e['reported_by'],
            }
            for e in topology_elements
        ],
    }


# ── HTML ──────────────────────────────────────────────────────────────────────

def _build_html(result: dict) -> str:
    HEADER_BG = '#4a7a9b'

    def th(col):
        return (f'<th style="background:{HEADER_BG};color:#fff;padding:4px 8px;'
                f'text-align:left;border:1px solid #888;white-space:nowrap">{col}</th>')

    def td(val, bg='', extra=''):
        style = 'padding:3px 8px;border:1px solid #ccc'
        if bg:
            style += f';background:{bg}'
        if extra:
            style += f';{extra}'
        return f'<td style="{style}">{val}</td>'

    def row(cells):
        return f'<tr>{"".join(cells)}</tr>'

    def mono(v):
        return f'<span style="font-family:monospace">{v}</span>'

    def badge():
        return ('<span style="background:#2196F3;color:#fff;border-radius:3px;'
                'padding:1px 5px;font-size:10px;vertical-align:middle;margin-left:4px">UDS</span>')

    uds_k = _uds_keys(result['udsDevices'])

    uds_header = row([th(c) for c in ['CAN Addr', 'Type', 'NodeID', 'SW-Version', 'HW-Version', 'VIN']])
    uds_rows = ''.join(
        row([
            td(f"<b>{d['canAddr']}</b>"),
            td(_s(d['devType'])),
            td(_s(d['nodeId'])),
            td(_s(d['swVersion'])),
            td(_s(d['hwVersion'])),
            td(mono(_s(d['vin']))),
        ])
        for d in result['udsDevices']
    )

    topo_header = row([th(c) for c in ['NodeID', 'Bus Type', 'Type', 'SW-Version', 'VIN', 'Reported by']])
    topo_rows = ''.join(
        row([
            td(_s(el['nodeId']),   bg := _BUS_COLOR.get(el['busTypeId'], '#fff')),
            td(_s(el['busType']),  bg),
            td(_s(el['devType']) + (badge() if _is_uds(el, uds_k) else ''), bg),
            td(_s(el['swVersion']), bg),
            td(mono(_s(el['vin'])), bg),
            td(', '.join(el['reportedBy']), bg, 'font-size:11px'),
        ])
        for el in result['topologyElements']
    )

    color_legend = ' '.join(
        f'<span style="background:{_BUS_COLOR[k]};padding:1px 6px;border:1px solid #bbb;'
        f'font-size:11px">{name}</span>'
        for k, name in [(2, 'CanInternal'), (3, 'CanExternal'), (6, 'CanRaw'),
                        (8, 'ModBus'), (14, 'ServiceBus')]
    )

    div = (
        f'<div style="font-family:sans-serif;font-size:13px;padding:8px">\n'
        f'<h3 style="margin:0 0 4px 0">E3 CAN Bus Topology</h3>\n'
        f'<p style="margin:0 0 12px 0;color:#666;font-size:11px">Scan: {result["scanTime"]}'
        f' &nbsp;|&nbsp; UDS devices: {len(result["udsDevices"])}'
        f' &nbsp;|&nbsp; Topology elements: {len(result["topologyElements"])}</p>\n'
        f'<h4 style="margin:0 0 4px 0">UDS-Accessible Devices</h4>\n'
        f'<table style="border-collapse:collapse;width:100%;margin-bottom:16px">'
        f'<thead>{uds_header}</thead><tbody>{uds_rows}</tbody></table>\n'
        f'<h4 style="margin:0 0 4px 0">Internal Bus Topology</h4>\n'
        f'<table style="border-collapse:collapse;width:100%;margin-bottom:8px">'
        f'<thead>{topo_header}</thead><tbody>{topo_rows}</tbody></table>\n'
        f'<p style="margin:4px 0;font-size:11px;color:#555">'
        f'Bus type: {color_legend} &nbsp; {badge()} = also UDS-accessible</p>\n'
        f'</div>'
    )

    return (
        '<!DOCTYPE html>\n'
        '<html lang="en">\n'
        '<head><meta charset="utf-8"><title>E3 CAN Bus Topology</title></head>\n'
        f'<body>{div}\n</body>\n</html>\n'
    )


# ── Text table ────────────────────────────────────────────────────────────────

def _build_text(result: dict) -> str:
    uds_k = _uds_keys(result['udsDevices'])
    lines = []

    lines.append(f"E3 CAN Bus Topology  (Scan: {result['scanTime']})")
    lines.append(
        f"UDS devices: {len(result['udsDevices'])}"
        f"    Topology elements: {len(result['topologyElements'])}"
    )
    lines.append('')

    lines.append('UDS-Accessible Devices:')
    lines.append(
        f"  {'CAN Addr':<10} {'Type':<18} {'NodeID':>6}  "
        f"{'SW-Version':<18} {'HW-Version':<18} VIN"
    )
    lines.append('  ' + '-' * 92)
    for d in result['udsDevices']:
        lines.append(
            f"  {d['canAddr']:<10} {(d['devType'] or '?'):<18} {_s(d.get('nodeId')):>6}  "
            f"{(d['swVersion'] or ''):<18} {(d['hwVersion'] or ''):<18} {d.get('vin', '')}"
        )
    lines.append('')

    lines.append('Internal Bus Topology:')
    lines.append(
        f"  {'NodeID':>6}  {'Bus Type':<14} {'Type':<18} "
        f"{'SW-Version':<18} {'VIN':<18} Reported by"
    )
    lines.append('  ' + '-' * 102)
    for e in result['topologyElements']:
        uds_tag = ' [UDS]' if _is_uds(e, uds_k) else ''
        lines.append(
            f"  {_s(e['nodeId']):>6}  {e['busType']:<14} {(e['devType'] or '?'):<18}"
            f" {(e['swVersion'] or ''):<18} {(e.get('vin') or ''):<18}"
            f" {', '.join(e['reportedBy'])}{uds_tag}"
        )

    return '\n'.join(lines)


# ── Public API ────────────────────────────────────────────────────────────────

def build_topology_summary(topology_data: dict) -> dict:
    """
    Analyse collected topology data.

    :param topology_data: dict keyed by hex CAN address, each value:
        {'can_addr': str, 'bus_id': dict|None, 'matrices': list[dict]}
    :returns: {'json': dict, 'html': str, 'text': str}
        html is a standalone HTML page suitable for writing to a .html file.
    """
    uds_devices       = _extract_uds_devices(topology_data)
    dev_prop_names    = _build_dev_prop_names(topology_data)
    topology_elements = _collect_topology_elements(topology_data, dev_prop_names)
    result            = _build_json(uds_devices, topology_elements)
    return {
        'json': result,
        'html': _build_html(result),
        'text': _build_text(result),
    }
