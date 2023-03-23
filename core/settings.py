import json
import os
import pathlib
import typing as t


class AppSettings:
    def __init__(self) -> None:
        # defaults
        self.__host = "0.0.0.0"
        self.__port = 5000
        self.__debug = True
        self.__option_dicts: t.List[dict] = []

        return

    def load_setting_file(self) -> 'AppSettings':
        root_dir_path = str(pathlib.Path(__file__).parent.parent)
        path = os.path.join(root_dir_path, "settings/settings.json")

        with open(path, "r", encoding="utf-8") as f:
            app_settings: dict = json.load(f)

        self.__host = app_settings.get("FlaskHost", self.__host)
        self.__port = int(app_settings.get("FlaskPort", self.__port))
        self.__debug = app_settings.get("FlaskDebug", self.__debug)
        self.__option_dicts = app_settings.get("CronTaskOptions", self.__option_dicts)

        return self

    def load_environment(self) -> 'AppSettings':
        self.__host = os.environ.get("FLASK_HOST", self.__host)
        self.__port = int(os.environ.get("FLASK_PORT", self.__port))

        debug = os.environ.get("FLASK_DEBUG", "")
        if debug.lower() == "true":
            self.__debug = True
        if debug.lower() == "false":
            self.__debug = False

        return self

    @property
    def host(self) -> str:
        return self.__host

    @property
    def port(self) -> int:
        return self.__port

    @property
    def debug(self) -> bool:
        return self.__debug

    @property
    def option_dicts(self) -> t.List[dict]:
        return self.__option_dicts
