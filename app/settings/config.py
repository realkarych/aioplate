import configparser
import os
from dataclasses import dataclass

from app.settings import paths

parse_mode = str


@dataclass
class Bot:
    """Bot config"""

    token: str
    parse_mode: str


@dataclass
class DB:
    """Database config"""

    host: str
    port: int
    name: str
    user: str
    password: str

    def get_uri(self) -> str:
        """Returns uri of postgres database."""
        return f"postgresql+asyncpg://{self.user}:{self.password}@{self.host}/{self.name}"


@dataclass
class Config:
    """Configurator"""

    bot: Bot
    db: DB


def get_parse_mode(bot_section: configparser.SectionProxy) -> parse_mode:
    """
    Get & return parse mode. Provides to bot instance.
    :param bot_section: configparser section
    """

    _parse_mode: parse_mode

    try:
        _parse_mode = bot_section["parse_mode"] if bot_section["parse_mode"] in \
                                                   ("HTML", "MarkdownV2") else "HTML"

    # Param parse_mode isn't set in app.ini. HTML will be set.
    except KeyError:
        _parse_mode = "HTML"

    return _parse_mode


def load_config() -> Config:
    """Load and return bot configuration data"""

    config_file_path = paths.get_project_root() / "app.ini"

    # If developer wasn't created app.ini configuration file, raising an exception
    if not os.path.exists(config_file_path):
        raise NotImplementedError("app.ini wasn't created!")

    config = configparser.ConfigParser()
    config.read(config_file_path)

    # Get .ini config "blocks"
    bot = config["bot"]
    db = config["db"]

    # Get & return config data instance
    return Config(
        bot=Bot(
            token=bot["token"],
            parse_mode=get_parse_mode(bot_section=bot)
        ),
        db=DB(
            host=db["host"],
            port=int(db["port"]),
            name=db["name"],
            user=db["user"],
            password=db["password"]
        )
    )
