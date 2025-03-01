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
from open3e.system.DeviceFeature import DeviceFeature


class Device:
    name: str
    id: int
    serial_number: str | None = None
    software_version: str | None = None
    hardware_version: str | None = None
    features: list[DeviceFeature]

    def __init__(self, name: str, id: int, serial_number: str | None, software_version: str | None,
                 hardware_version: str | None, features: list[DeviceFeature]):
        self.name = name
        self.id = id
        self.features = features
        self.serial_number = serial_number
        self.software_version = software_version
        self.hardware_version = hardware_version
