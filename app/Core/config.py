import functools
import typing

from app.Core.Settings.AppSettings import AppSettings
from app.Core.Settings.BaseAppSettings import BaseAppSettings
from app.Core.Settings.DevAppSettings import DevAppSettings
from app.Core.Settings.ProductionAppSettings import ProductionAppSettings
from app.Enums.AppEnvEnum import AppEnvEnum
from app.Core.Settings.DatabaseSettings import DatabaseSettings

environments_mapping: typing.Dict[str, typing.Type[AppSettings]] = {
    AppEnvEnum.PRODUCTION: ProductionAppSettings,
    AppEnvEnum.DEVELOPMENT: DevAppSettings,
}


@functools.lru_cache
def get_app_settings() -> AppSettings:
    application_env: str = BaseAppSettings().app_env
    config = environments_mapping[application_env]
    return config()


def get_database_settings(database_required: str) -> typing.Dict[str, str]:
    database_settings: DatabaseSettings = DatabaseSettings()
    return database_settings.database_settings_mapping[database_required]
