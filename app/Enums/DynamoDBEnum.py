from enum import Enum


class DynamoDBEnum(str, Enum):
    DECODE: str = "DECODE"
    ENCODE: str = "ENCODE"
