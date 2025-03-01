"""
  Copyright 2025 MojoOli

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
import json
from typing import Callable

import paho.mqtt.client as paho

from open3e.Open3Eclass import O3Eclass
from open3e.system.Device import Device
from open3e.system.DeviceFeature import DeviceFeature


class System:
    devices: list[Device]

    def __init__(self):
        self.devices = []

    @staticmethod
    def send_config(
            mqtt_client: paho.Client,
            mqtt_topic: str,
            ecus: dict[str, O3Eclass],
            get_mqtt_topic_callback: Callable[[int, str, str], str],
    ):
        system = System()

        for did, ecu in ecus.items():
            if 256 in ecu.dataIdentifiers.keys():
                bus_identification = ecu.readByDid(256, False)
                name = bus_identification[0]["DeviceProperty"]["Text"]
                serial_number = bus_identification[0]["VIN"]
                software_version = bus_identification[0]["SW-Version"]
                hardware_version = bus_identification[0]["HW-Version"]
            else:
                continue

            features: list[DeviceFeature] = []
            for k, v in ecu.dataIdentifiers.items():
                features.append(
                    DeviceFeature(
                        id=k,
                        topic=get_mqtt_topic_callback(ecu.tx, k, v.id)
                    )
                )

            system.devices.append(
                Device(
                    name=name,
                    id=ecu.tx,
                    serial_number=serial_number,
                    software_version=software_version,
                    hardware_version=hardware_version,
                    features=features
                )
            )

        json_config = json.dumps(system, default=lambda config: config.__dict__)
        mqtt_client.publish(
            topic=f"{mqtt_topic}/system",
            payload=json_config
        )
