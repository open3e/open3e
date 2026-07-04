import json
from unittest.mock import MagicMock

import pytest
import udsoncan

import open3e.Open3Edatapoints
from open3e.Open3E_depictSysDev import (
    EcuInfo,
    DepictDashboard,
    did_info,
    prop_str,
    shex,
    probe_ecu,
    scan_ecu_dids,
    write_devices_json,
    write_datapoints_file,
    write_simul_datafile,
)


def _vcan_available() -> bool:
    try:
        import can
        b = can.interface.Bus(channel="vcan0", interface="socketcan")
        b.shutdown()
        return True
    except Exception:
        return False


# ~~~~~~~~~~~~~~~~~~~~~~ pure-logic tests ~~~~~~~~~~~~~~~~~~~~~~

def test_shex():
    assert shex(0x681) == "681"
    assert shex(0x6) == "006"


def test_prop_str_known_and_unknown():
    e3_devices = {2: "HMUMASTER"}
    assert prop_str(2, e3_devices) == "HMUMASTER"
    assert prop_str(99, e3_devices) == "99"


def test_did_info_general_did():
    data_identifiers = dict(open3e.Open3Edatapoints.dataIdentifiers["dids"])
    didlen, idstr = did_info(256, data_identifiers, {})
    assert idstr == "BusIdentification"
    assert didlen > 0


def test_did_info_unknown_did_with_enum_name():
    didlen, idstr = did_info(999999, {}, {999999: "SomeEnumName"})
    assert (didlen, idstr) == (0, "SomeEnumName")


def test_did_info_fully_unknown():
    assert did_info(999999, {}, {}) == (0, "Unknown")


def test_devices_json_sorted_and_formatted(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    ecus = [EcuInfo(tx=0x6a1, devprop="HMUMASTER"), EcuInfo(tx=0x681, devprop="MCUMASTER")]
    write_devices_json(ecus)
    data = json.loads((tmp_path / "devices.json").read_text())
    # ascending order despite input order (parallel discovery may complete out of order)
    assert list(data.keys()) == [hex(0x681), hex(0x6a1)]
    assert data[hex(0x681)] == {"tx": hex(0x681), "dpList": "Open3Edatapoints_681.py", "prop": "MCUMASTER"}


def test_datapoints_file_same_length_writes_none(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    data_identifiers = dict(open3e.Open3Edatapoints.dataIdentifiers["dids"])
    genlen = data_identifiers[256].string_len
    write_datapoints_file([(256, genlen, b"\x00" * genlen)], 0x681, "MCUMASTER", {},
                           data_identifiers, {})
    text = (tmp_path / "Open3Edatapoints_681.py").read_text()
    assert "dataIdentifiers = {" in text
    assert f"256 : None," in text


def test_datapoints_file_different_length_writes_rawcodec(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    data_identifiers = dict(open3e.Open3Edatapoints.dataIdentifiers["dids"])
    write_datapoints_file([(256, 999, b"\x00" * 999)], 0x681, "MCUMASTER", {},
                           data_identifiers, {})
    text = (tmp_path / "Open3Edatapoints_681.py").read_text()
    assert '256 : RawCodec(999, "BusIdentification"),' in text


def test_simul_datafile_format(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    write_simul_datafile([(256, 2, b"\x01\x02")], 0x681, "MCUMASTER")
    text = (tmp_path / "virtdata_681.txt").read_text()
    lines = text.splitlines()
    assert lines[0] == "# 0x681:MCUMASTER"
    assert lines[1] == "256 0102"


# ~~~~~~~~~~~~~~~~~~~~~~ dashboard ~~~~~~~~~~~~~~~~~~~~~~

def test_dashboard_progress_and_done():
    dash = DepictDashboard()
    dash.add_ecu(0x681, "MCUMASTER")
    cb = dash.make_callback(0x681)
    cb(0x681, 10, 3)
    row = dash._rows[0x681]
    assert (row.dids_queried, row.dids_found, row.status) == (10, 3, "scanning")
    dash.mark_done(0x681)
    assert dash._rows[0x681].status == "done"


# ~~~~~~~~~~~~~~~~~~~~~~ mocked-Client unit tests ~~~~~~~~~~~~~~~~~~~~~~

def test_probe_ecu_parses_devprop(monkeypatch):
    # data[2+2]=data[4] is devprop: DID-echo(2) + PCI/DL-ish lead bytes(2) + devprop(1)
    fake_response = MagicMock(positive=True, data=b'\x00\x00\x00\x00\x02')  # iprop=2 -> HMUMASTER
    fake_client = MagicMock()
    fake_client.__enter__.return_value = fake_client
    fake_client.send_request.return_value = fake_response

    monkeypatch.setattr("open3e.Open3E_depictSysDev.Client", lambda *a, **k: fake_client)
    monkeypatch.setattr("open3e.Open3E_depictSysDev.DoIPClientUDSConnector", lambda *a, **k: MagicMock())
    monkeypatch.setattr("open3e.Open3E_depictSysDev.DoIPClient", lambda *a, **k: MagicMock())

    info = probe_ecu(shared=None, doip_ip="1.2.3.4", tx=0x681, e3_devices={2: "HMUMASTER"})
    assert info == EcuInfo(tx=0x681, devprop="HMUMASTER")


def test_probe_ecu_malformed_response_returns_none(monkeypatch):
    fake_response = MagicMock(positive=True, data=b'\x00\x00')  # too short, no devprop byte
    fake_client = MagicMock()
    fake_client.__enter__.return_value = fake_client
    fake_client.send_request.return_value = fake_response

    monkeypatch.setattr("open3e.Open3E_depictSysDev.Client", lambda *a, **k: fake_client)
    monkeypatch.setattr("open3e.Open3E_depictSysDev.DoIPClientUDSConnector", lambda *a, **k: MagicMock())
    monkeypatch.setattr("open3e.Open3E_depictSysDev.DoIPClient", lambda *a, **k: MagicMock())

    info = probe_ecu(shared=None, doip_ip="1.2.3.4", tx=0x681, e3_devices={})
    assert info is None


def test_scan_ecu_dids_continues_after_setup_exception(monkeypatch):
    # bug #1 regression: connection setup failure must not raise, must return []
    monkeypatch.setattr(
        "open3e.Open3E_depictSysDev.DoIPClientUDSConnector",
        MagicMock(side_effect=RuntimeError("bus error")),
    )
    result = scan_ecu_dids(shared=None, doip_ip="1.2.3.4", tx=0x681,
                            startdid=256, lastdid=257, progress_cb=lambda *a, **k: None, delay_ms=0)
    assert result == []


def test_scan_ecu_dids_skips_empty_positive_response(monkeypatch):
    # bug #5 regression: a positive response with dlen==0 must not be counted as found
    empty_response = MagicMock(positive=True, data=b'\x00\x00')
    empty_response.__len__.return_value = 3   # len(response) - 3 == 0

    fake_client = MagicMock()
    fake_client.__enter__.return_value = fake_client
    fake_client.send_request.return_value = empty_response

    monkeypatch.setattr("open3e.Open3E_depictSysDev.Client", lambda *a, **k: fake_client)
    monkeypatch.setattr("open3e.Open3E_depictSysDev.DoIPClientUDSConnector", lambda *a, **k: MagicMock())
    monkeypatch.setattr("open3e.Open3E_depictSysDev.DoIPClient", lambda *a, **k: MagicMock())

    progress_calls = []
    result = scan_ecu_dids(shared=None, doip_ip="1.2.3.4", tx=0x681,
                            startdid=256, lastdid=256,
                            progress_cb=lambda *a: progress_calls.append(a), delay_ms=0)
    assert result == []
    assert progress_calls == [(0x681, 1, 0)]


def test_scan_ecu_dids_paces_requests_when_delay_set(monkeypatch):
    fake_response = MagicMock(positive=False)
    fake_client = MagicMock()
    fake_client.__enter__.return_value = fake_client
    fake_client.send_request.side_effect = udsoncan.exceptions.NegativeResponseException(fake_response)

    monkeypatch.setattr("open3e.Open3E_depictSysDev.Client", lambda *a, **k: fake_client)
    monkeypatch.setattr("open3e.Open3E_depictSysDev.DoIPClientUDSConnector", lambda *a, **k: MagicMock())
    monkeypatch.setattr("open3e.Open3E_depictSysDev.DoIPClient", lambda *a, **k: MagicMock())

    sleeps = []
    monkeypatch.setattr("open3e.Open3E_depictSysDev.time.sleep", lambda s: sleeps.append(s))

    scan_ecu_dids(shared=None, doip_ip="1.2.3.4", tx=0x681,
                  startdid=256, lastdid=258, progress_cb=lambda *a, **k: None, delay_ms=20)
    assert sleeps == [0.02, 0.02, 0.02]


# ~~~~~~~~~~~~~~~~~~~~~~ real vcan0 smoke test ~~~~~~~~~~~~~~~~~~~~~~

@pytest.mark.skipif(not _vcan_available(), reason="vcan0 not available")
def test_shared_context_discovery_against_fake_ecu():
    import threading
    import time as _time

    import can
    import isotp
    from open3e.Open3E_depictSysDev import SharedCanContext

    tx, rx = 0x681, 0x691   # from the scanning tool's POV: it sends to tx, receives on rx
    stop = threading.Event()

    def fake_ecu():
        # Responder: listens on 'tx' (what the scanner sends to), replies on 'rx'.
        # isotp's CanStack.start() spawns its own internal rx/tx threads; calling
        # process() manually afterwards is not supported in this isotp version.
        bus = can.interface.Bus(channel="vcan0", interface="socketcan")
        addr = isotp.Address(isotp.AddressingMode.Normal_11bits, txid=rx, rxid=tx)
        stack = isotp.CanStack(bus=bus, address=addr)
        stack.start()
        request = bytes([0x22]) + (256).to_bytes(2, 'big')   # SID 0x22 (ReadDataByIdentifier) + DID 256
        try:
            while not stop.is_set():
                payload = stack.recv(block=True, timeout=0.2)
                if payload == request:
                    # positive response: SID 0x62, DID echo(2), leadbyte(2), devprop
                    stack.send(bytes([0x62, 0x01, 0x00, 0x00, 0x00, 0x02]))
        finally:
            stack.stop()
            bus.shutdown()

    t = threading.Thread(target=fake_ecu, daemon=True)
    t.start()
    _time.sleep(0.2)

    shared = SharedCanContext("vcan0")
    try:
        info = probe_ecu(shared, None, tx, e3_devices={2: "HMUMASTER"})
        assert info == EcuInfo(tx=tx, devprop="HMUMASTER")
    finally:
        shared.close()
        stop.set()
        t.join(timeout=2)
        assert len(shared.notifier.listeners) == 0
