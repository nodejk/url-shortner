from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.Core.config import get_app_settings
from app.Routes.router import router


def create_app() -> FastAPI:
    settings = get_app_settings()

    application = FastAPI(**settings.fastapi_kwargs)

    application.add_middleware(
        CORSMiddleware,
        allow_origins=settings.allowed_hosts,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    application.include_router(router, prefix=settings.api_prefix)

    return application


app = create_app()
