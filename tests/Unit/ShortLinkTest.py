from tests.TestEnvironment import TestEnvironment
from app.Finn.ShortLink.Models.ShortLink import ShortLink


class ShortLinkTest(TestEnvironment):
    def __init__(self, methodName: str) -> None:
        super().__init__(methodName)

    @property
    def valid_url(self) -> str:
        return "http://finn.com"

    def test_encoded_url_same_for_one_url(self) -> None:
        short_link: ShortLink = ShortLink(link=self.valid_url)  # type: ignore

        encoded_1: ShortLink = short_link.encode()
        encoded_2: ShortLink = short_link.encode()

        self.assertEqual(encoded_1.link, encoded_2.link)

    def test_decoded_url_same_for_one_encoded_url(self) -> None:
        short_link: ShortLink = ShortLink(link=self.valid_url)  # type: ignore

        encoded_shortlink: ShortLink = short_link.encode()

        decoded_shortlink: ShortLink = encoded_shortlink.decode()

        self.assertEqual(short_link.link, decoded_shortlink.link)
