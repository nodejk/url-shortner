import typing
import unittest
from http import HTTPStatus

from fastapi.testclient import TestClient
from httpx import Response

from app.Enums.RequestEnum import RequestEnum
from app.main import app


class TestEnvironment(unittest.TestCase):
    _app: TestClient
    _base_route: typing.Final[str] = ""

    def __init__(self, methodName: str) -> None:
        super().__init__(methodName)

    def setUp(self) -> None:
        self._app = TestClient(app)

    @typing.final
    def request(
        self,
        route: str,
        method: RequestEnum,
        payload: typing.Dict[typing.Any, typing.Any],
    ) -> Response:
        if method == RequestEnum.POST:
            return self._app.post(route, json=payload, headers=self.api_headers)
        raise Exception("Only POST method implemented")

    @property
    def api_headers(self) -> typing.Dict[str, str]:
        return {"Content-Type": "application/json"}

    def assert_response_200(
        self,
        route: str,
        method: RequestEnum,
        payload: typing.Dict[typing.Any, typing.Any],
    ) -> None:
        self.__assert_response(route, method, payload, HTTPStatus.UNPROCESSABLE_ENTITY)

    def assert_response_422(
        self,
        route: str,
        method: RequestEnum,
        payload: typing.Dict[typing.Any, typing.Any],
    ) -> None:
        self.__assert_response(route, method, payload, HTTPStatus.UNPROCESSABLE_ENTITY)

    def assert_response_404(
        self,
        route: str,
        method: RequestEnum,
        payload: typing.Dict[typing.Any, typing.Any],
    ) -> None:
        self.__assert_response(route, method, payload, HTTPStatus.NOT_FOUND)

    def __assert_response(
        self,
        route: str,
        method: RequestEnum,
        payload: typing.Dict[typing.Any, typing.Any],
        status_code: int,
    ) -> None:
        response: Response = self.request(route, method, payload)

        self.assertEqual(status_code, response.status_code)

    def assert_single_field_validation_error(
        self,
        route: str,
        method: RequestEnum,
        payload: typing.Dict[typing.Any, typing.Any],
        test_field: str,
    ) -> None:
        response: Response = self.request(route, method, payload)

        field_validation_errors: list[typing.Dict[str, typing.Any]] = response.json()["detail"]

        error_fields: list[str] = [validation["loc"][1] for validation in field_validation_errors]

        field_exist: bool = True if (test_field in error_fields and len(error_fields) == 1) else False

        self.assertEqual(True, field_exist)
        self.assertEqual(HTTPStatus.UNPROCESSABLE_ENTITY, response.status_code)
