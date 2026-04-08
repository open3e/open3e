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

import struct
from udsoncan.Request import Request
from udsoncan.Response import Response
from udsoncan import DidCodec, check_did_config, make_did_codec_from_definition, fetch_codec_definition_from_config, DIDConfig
from udsoncan.exceptions import *
from udsoncan.BaseService import BaseResponseData
from open3e.Open3EudsBaseService77 import Open3EudsBaseService
from udsoncan.ResponseCode import ResponseCode
from udsoncan.services.WriteDataByIdentifier import WriteDataByIdentifier
import udsoncan.tools as tools

from typing import Any, cast

class WriteDataByIdentifier77(Open3EudsBaseService):
    _sid = 0x77
    _use_subfunction = False

    supported_negative_response = [ResponseCode.IncorrectMessageLengthOrInvalidFormat,
                                   ResponseCode.ConditionsNotCorrect,
                                   ResponseCode.RequestOutOfRange,
                                   ResponseCode.SecurityAccessDenied,
                                   ResponseCode.GeneralProgrammingFailure
                                   ]

    class ResponseData(BaseResponseData):
        """
        .. data:: did_echo

                The DID echoed back by the server
        """

        did_echo: int

        def __init__(self, did_echo: int):
            super().__init__(WriteDataByIdentifier)

            self.did_echo = did_echo

    class InterpretedResponse(Response):
        service_data: "WriteDataByIdentifier.ResponseData"

    @classmethod
    def make_request(cls, did: int, value: Any, didconfig: DIDConfig) -> Request:
        """
        Generates a request for WriteDataByIdentifier

        :param did: The data identifier to write
        :type did: int

        :param value: Value given to the :ref:`DidCodec <DidCodec>`.encode method. If involved codec is defined with a pack string (default codec), multiple values may be passed with a tuple.
        :type value: object

        :param didconfig: Definition of DID codecs. Dictionary mapping a DID (int) to a valid :ref:`DidCodec <DidCodec>` class or pack/unpack string 
        :type didconfig: dict[int] = :ref:`DidCodec <DidCodec>`

        :raises ValueError: If parameters are out of range, missing or wrong type
        :raises ConfigError: If ``didlist`` contains a DID not defined in ``didconfig``
        """

        tools.validate_int(did, min=0, max=0xFFFF, name='Data Identifier')
        req = Request(cls)
        didconfig = check_did_config(did, didconfig=didconfig)  # Make sure all DIDs are correctly defined in client config
        codec_definition = fetch_codec_definition_from_config(did, didconfig)
        codec = make_did_codec_from_definition(codec_definition)

        if codec.__class__ == DidCodec and isinstance(value, tuple):
            req.data = codec.encode(*value)    # Fixes issue #29
        else:
            req.data = codec.encode(value)

        # Assemble prefix data for service 0x77:
        prefix = struct.pack('>H', did)     # encode DID number
        len_code = 0xb0+ len(req.data)      # encode length: 0xb0 + data length
        prefix77 = [prefix[0], prefix[1], 0x43, 0x01, 0x82, prefix[1], prefix[0], len_code];
                    # Use did as ID code (first two bytes)

        # Assemble req.data:
        req.data = bytearray(prefix77) + req.data

        return req

    @classmethod
    def interpret_response(cls, response: Response) -> InterpretedResponse:
        """
        Populates the response ``service_data`` property with an instance of :class:`WriteDataByIdentifier.ResponseData<udsoncan.services.WriteDataByIdentifier.ResponseData>`

        :param response: The received response to interpret
        :type response: :ref:`Response<Response>`

        :raises InvalidResponseException: If length of ``response.data`` is too short
        """
        if response.data is None:
            raise InvalidResponseException(response, "No data in response")

        if len(response.data) < 2:
            raise InvalidResponseException(response, "Response must be at least 2 bytes long")

        response.service_data = cls.ResponseData(
            did_echo=struct.unpack(">H", response.data[0:2])[0]
        )

        return cast(WriteDataByIdentifier.InterpretedResponse, response)