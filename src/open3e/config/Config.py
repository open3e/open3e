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
from open3e.config.Device import Device
from open3e.config.DeviceFeature import DeviceFeature


class Config:
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
        config = Config()

        for did, ecu in ecus.items():
            name = None
            serial_number = None
            software_version = None
            hardware_version = None
            if 256 in ecu.dataIdentifiers.keys():
                bus_identification = ecu.readByDid(256, False)
                print(bus_identification)
                name = bus_identification["DeviceProperty"]["Text"]
                serial_number = bus_identification["VIN"]
                software_version = bus_identification["SW-Version"]
                hardware_version = bus_identification["HW-Version"]
            else:
                continue

            # if 377 in ecu.dataIdentifiers.keys():
            #     serial_number, _ = ecu.readByDid(377, False)
            # if 580 in ecu.dataIdentifiers.keys():
            #     software_version, _ = ecu.readByDid(580, False)
            # if 581 in ecu.dataIdentifiers.keys():
            #     hardware_version, _ = ecu.readByDid(581, False)

            features: list[DeviceFeature] = []
            for k, v in ecu.dataIdentifiers.items():
                features.append(
                    DeviceFeature(
                        id=k,
                        topic=get_mqtt_topic_callback(ecu.tx, k, v.id)
                    )
                )

            config.devices.append(
                Device(
                    name=name,
                    id=ecu.tx,
                    serial_number=serial_number,
                    software_version=software_version,
                    hardware_version=hardware_version,
                    features=features
                )
            )

        print("sending config")
        json_config = json.dumps(config, default=lambda config: config.__dict__)
        print(json_config)

        mqtt_client.publish(
            topic=f"{mqtt_topic}/config",
            payload=json_config
        )
