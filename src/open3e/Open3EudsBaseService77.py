from udsoncan.BaseService import BaseService

class Open3EudsBaseService(BaseService):

    @classmethod  # Returns the service ID used for a server response
    def response_id(cls) -> int:
        return cls._sid         # Service 77 returns SID instead of SID+0x40
