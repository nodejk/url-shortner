from enum import Enum


class RequestEnum(str, Enum):
    GET: str = "GET"
    POST: str = "POST"
    PUT: str = "PUT"
    DELETE: str = "DELETE"
    PATCH: str = "PATCH"
