import os
import typing

from app.Enums.DynamoDBEnum import DynamoDBEnum
from app.Core.Settings.DynamoDBSettings import DynamoDBSettings


class DatabaseSettings:
    decode_tablename: str = os.environ["DECODE_TABLE_NAME"]
    encode_tablename: str = os.environ["ENCODE_TABLE_NAME"]

    @property
    def database_settings_mapping(self) -> typing.Dict[str, typing.Any]:
        return {
            DynamoDBEnum.ENCODE: DynamoDBSettings(table_name=self.encode_tablename).dict(),
            DynamoDBEnum.DECODE: DynamoDBSettings(table_name=self.decode_tablename).dict(),
        }
