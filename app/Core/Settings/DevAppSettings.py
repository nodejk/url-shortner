import logging

from app.Core.Settings.AppSettings import AppSettings


class DevAppSettings(AppSettings):
    debug: bool = True

    title: str = "[Dev] Finn Url Shortner"

    logging_level: int = logging.DEBUG

    class Config(AppSettings.Config):
        env_file = ".env"
