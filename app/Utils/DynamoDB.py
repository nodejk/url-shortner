import typing

from app.Core.config import get_database_settings
from app.Enums.DynamoDBEnum import DynamoDBEnum


class DynamoDB:
    """
    Interface for Database.
    """

    _table_name: str
    _access_key_id: str
    _secret_access_key: str
    _region_name: str
    _service_name: str

    __table: typing.Dict[typing.Any, typing.Any]

    __global_tables: typing.Dict[str, typing.Any] = {
        DynamoDBEnum.ENCODE: {},
        DynamoDBEnum.DECODE: {},
    }

    def __init__(
        self, table_name: str, access_key_id: str, secret_access_key: str, region_name: str, service_name: str
    ) -> None:
        self._table_name = table_name
        self._access_key_id = access_key_id
        self._secret_access_key = secret_access_key
        self.region_name = region_name
        self._secret_access_key = service_name

        self.__table = self.__global_tables[self._table_name]

    def persist(self, key: typing.Any, value: typing.Any) -> None:
        """Used to store data into DynamoDB.

        Args:
            key (typing.Dict[str, typing.Any]): key for DynamoDB Item.
            value (typing.Dict[str, typing.Any]): value for DynamoDB Item.
        """
        self.__table[key] = value

    def look_up(self, key: typing.Any) -> typing.Union[str, None]:
        """Used to look up for item based on key.

        Args:
            key (typing.Dict[str, typing.Dict]): item key to look for in DynamoDB.

        Returns:
            typing.Dict[str, None]: returns the value for encoded url.
        """
        if key in self.__table:
            return self.__table[key]
        return None

    @staticmethod
    def encode_dynamoDB() -> "DynamoDB":
        settings: typing.Dict[str, str] = get_database_settings(DynamoDBEnum.ENCODE)
        return DynamoDB(**settings)

    @staticmethod
    def decode_dynamoDB() -> "DynamoDB":
        settings: typing.Dict[str, str] = get_database_settings(DynamoDBEnum.DECODE)
        return DynamoDB(**settings)
