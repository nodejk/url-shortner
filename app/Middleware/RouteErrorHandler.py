import pydantic

from typing import Callable

from fastapi import Request, Response
from fastapi.routing import APIRoute
from app.Errors.ItemNotFoundException import ItemNotFoundException
from app.Errors.InternalServerError import InternalServerError


class RouteErrorHandler(APIRoute):
    def get_route_handler(self) -> Callable:
        original_route_handler = super().get_route_handler()

        async def custom_route_handler(request: Request) -> Response:
            try:
                return await original_route_handler(request)
            except Exception as exception:
                if isinstance(exception, (pydantic.ValidationError, ItemNotFoundException)):
                    raise exception
                raise InternalServerError()

        return custom_route_handler
