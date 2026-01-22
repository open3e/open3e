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

from udsoncan.BaseService import BaseService

class Open3EudsBaseService(BaseService):

    @classmethod  # Returns the service ID used for a server response
    def response_id(cls) -> int:
        return cls._sid         # Service 77 returns SID instead of SID+0x40
