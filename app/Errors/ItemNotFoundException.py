import typing

from fastapi import HTTPException, status


class ItemNotFoundException(HTTPException):
    def __init__(self, detail: typing.Any) -> None:
        super().__init__(status_code=status.HTTP_404_NOT_FOUND, detail=detail)
