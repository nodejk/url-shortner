import os
import typing

from app.Core.Settings.BaseAppSettings import BaseAppSettings


class AppSettings(BaseAppSettings):
    debug: bool = False
    docs_url: str = "/docs"
    openapi_prefix: str = "/"
    openapi_url: str = "/openapi.json"
    redoc_url: str = "/redoc"
    title: str = "Finn Url Shortner"
    version: str = os.environ["VERSION"]

    max_connection_count: int = 10
    min_connection_count: int = 10

    api_prefix: str = ""

    jwt_token_prefix: str = "Token"

    allowed_hosts: typing.List[str] = ["*"]

    class Config:
        validate_assignment = True

    @property
    def fastapi_kwargs(self) -> typing.Dict[str, typing.Any]:
        return {
            "debug": self.debug,
            "docs_url": self.docs_url,
            "openapi_prefix": self.openapi_prefix,
            "openapi_url": self.openapi_url,
            "redoc_url": self.redoc_url,
            "title": self.title,
            "version": self.version,
        }
