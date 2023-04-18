import pydantic
import typing
import random
import string

from app.Utils.DynamoDB import DynamoDB
from app.Errors.ItemNotFoundException import ItemNotFoundException


class ShortLink(pydantic.BaseModel):
    link: pydantic.HttpUrl = pydantic.Field(description="Given url (encoded or decoded)")

    __chars: typing.Final[str] = string.ascii_letters + string.digits
    __base_url: typing.Final[str] = "https://short-link.com/"

    __encode_db: DynamoDB = DynamoDB.encode_dynamoDB()
    __decode_db: DynamoDB = DynamoDB.decode_dynamoDB()

    def encode(self) -> "ShortLink":
        encoded_link_exist: typing.Union[str, None] = self.__encode_db.look_up(self.link)

        if encoded_link_exist != None:
            return ShortLink(link=encoded_link_exist)  # type: ignore

        encoded_link: str = self.get_encode_link()

        while True:
            if self.__decode_db.look_up(encoded_link) != None:
                encoded_link = self.get_encode_link()
            else:
                break

        self.store_encoding(self.link, encoded_link)

        return ShortLink(link=encoded_link)  # type: ignore

    def decode(self) -> "ShortLink":
        decoded_link: typing.Union[str, None] = self.__decode_db.look_up(self.link)

        if decoded_link == None:
            raise ItemNotFoundException({"description": "Encoded URL not found."})
        else:
            return ShortLink(link=decoded_link)  # type: ignore

    def get_encode_link(self) -> str:
        code = "".join(random.choice(self.__chars) for _ in range(6))
        return self.__base_url + code

    def store_encoding(self, original_link: str, encoded_link: str) -> None:
        self.__encode_db.persist(original_link, encoded_link)
        self.__decode_db.persist(encoded_link, original_link)
