import os
import pydantic


class BaseAppSettings(pydantic.BaseSettings):
    app_env: str = os.environ["ENVIRONMENT"]

    class Config:
        env_file = ".env"
