from fastapi import APIRouter

from app.Finn.ShortLink.Controllers.ApiShortLinkController import ApiShortLinkController
from app.Middleware.RouteErrorHandler import RouteErrorHandler

router = APIRouter(route_class=RouteErrorHandler)

router.include_router(ApiShortLinkController().router)
