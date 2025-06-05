import json


def _load_test_data_file(file_path):
    with open(file_path, "r") as file:
        return json.load(file)


def dataset(file_path):
    dataset_dict = _load_test_data_file(file_path)
    return DeviceDataset(dataset_dict)


class DeviceDataset:
    def __init__(self, devices):
        self.devices = devices

    def ecus(self):
        return self.devices.keys()

    def ecu(self, ecu):
        ecu_data = self.devices.get(ecu, None)
        if ecu_data is None:
            raise KeyError(f"ecu {ecu} not found in dataset.")
        return DeviceEntry(ecu, ecu_data)

    def get(self, ecu, did, sub_did=None):
        did_entry = self.ecu(ecu).did(did)
        if sub_did is None:
            return did_entry
        return did_entry.sub_did(sub_did)

    def fixtures(self):
        fixtures = []
        for ecu in self.ecus():
            device_entry = self.ecu(ecu)
            for did in device_entry.dids():
                did_entry = device_entry.did(did)
                fixtures.append((did_entry.ecu, int(did_entry.did), did_entry))
        return fixtures


class DeviceEntry:
    def __init__(self, ecu, device_data):
        self.ecu = ecu
        self.device_data = device_data

    def dids(self):
        return self.device_data.keys()

    def did(self, did):
        did_data = self.device_data.get(str(did), None)
        if did_data is None:
            raise KeyError(f"did {did} not found in device data (ecu: {self.ecu}).")
        return DidEntry(self.ecu, did, did_data)


class DidEntry:
    def __init__(self, ecu, did, did_data):
        self.ecu = ecu
        self.did = did
        self.did_data = did_data

    def sub_did(self, sub_did):
        if not isinstance(self.did_data, dict):
            raise KeyError(f"sub-did {sub_did} not found in did data (ecu: {self.ecu}, did: {self.did}, value: {self.did_data}).")

        complex_sub_did_value = self.did_data.get(sub_did, None)
        if complex_sub_did_value is None:
            raise KeyError(f"sub-did {sub_did} not found in did data (ecu: {self.ecu}, did: {self.did}, value: {self.did_data}).")

        return DidEntry(self.ecu, sub_did, complex_sub_did_value)

    def __str__(self):
        if not isinstance(self.did_data, dict):
            return str(self.did_data)
        else:
            return json.dumps(self.did_data)