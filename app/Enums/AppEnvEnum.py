from enum import Enum


class AppEnvEnum(str, Enum):
    PRODUCTION: str = "PROD"
    DEVELOPMENT: str = "DEV"
