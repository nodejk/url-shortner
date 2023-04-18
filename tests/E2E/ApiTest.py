import typing

from tests.TestEnvironment import TestEnvironment
from app.Enums.RequestEnum import RequestEnum


class ApiTest(TestEnvironment):
    encode_route: str
    decode_route: str

    def __init__(self, methodName: str) -> None:
        super().__init__(methodName)
        self.encode_route = self._base_route + "/encode"
        self.decode_route = self._base_route + "/decode"

    def test_when_invalid_url_given_to_encode_or_encode(self) -> None:
        payload: typing.Dict[str, str] = {"link": "invali_url"}

        self.assert_response_422(self.encode_route, RequestEnum.POST, payload)
        self.assert_response_422(self.decode_route, RequestEnum.POST, payload)

    def test_when_no_body_is_given(self) -> None:
        self.assert_response_422(self.encode_route, RequestEnum.POST, {})
        self.assert_response_422(self.decode_route, RequestEnum.POST, {})

    def test_invalid_field_types(self) -> None:
        payload: dict[str, typing.Any] = {"link": 123}

        self.assert_single_field_validation_error(self.encode_route, RequestEnum.POST, payload, "link")
        self.assert_single_field_validation_error(self.decode_route, RequestEnum.POST, payload, "link")

    def test_when_no_decode_url_found(self) -> None:
        payload: typing.Dict[str, str] = {"link": "https://finn.service.com"}

        self.assert_response_404(self.decode_route, RequestEnum.POST, payload)
