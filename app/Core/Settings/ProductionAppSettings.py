from app.Core.Settings.AppSettings import AppSettings


class ProductionAppSettings(AppSettings):
    debug: bool = False

    title: str = "[Production] Finn Url Shortner"

    class Config(AppSettings.Config):
        env_file = ".env"
