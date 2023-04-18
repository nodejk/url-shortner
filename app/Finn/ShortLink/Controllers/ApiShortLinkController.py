from fastapi import APIRouter, status

from app.Enums.RequestEnum import RequestEnum
from app.Finn.ShortLink.Models.ShortLink import ShortLink
from app.Errors.InternalServerError import InternalServerError
from app.Errors.ItemNotFoundException import ItemNotFoundException


class ApiShortLinkController:
    router: APIRouter

    def __init__(self) -> None:
        self.router = APIRouter(
            dependencies=[],
            tags=["URL Shortner"],
        )

        self.router.add_api_route("/encode", self.encode, methods=[RequestEnum.POST], status_code=status.HTTP_200_OK)
        self.router.add_api_route("/decode", self.decode, methods=[RequestEnum.POST], status_code=status.HTTP_200_OK)

    def encode(self, short_link: ShortLink) -> ShortLink:
        try:
            encoded_short_link: ShortLink = short_link.encode()
            return encoded_short_link
        except:
            raise InternalServerError()

    def decode(self, short_link: ShortLink) -> ShortLink:
        try:
            decode_short_link: ShortLink = short_link.decode()
            return decode_short_link
        except BaseException as exception:
            if isinstance(exception, ItemNotFoundException):
                raise exception
            raise InternalServerError()
