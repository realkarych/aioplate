import configparser
import os
from dataclasses import dataclass

from app.settings import paths


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


def get_parse_mode(bot_section: configparser.SectionProxy) -> str:
    """
    Get & return parse mode. Provides to bot instance.
    :param bot_section: configparser section
    """

    try:
        if bot_section["parse_mode"] in ("HTML", "MarkdownV2"):
            return bot_section["parse_mode"]
        return "HTML"
    # Param parse_mode isn't set in app.ini. HTML will be set.
    except KeyError:
        return "HTML"


def load_config() -> Config:
    """Load and return bot configuration data"""

    config_file_path = paths.ROOT_DIR / "app.ini"

    # If developer wasn't created app.ini configuration file, raising an exception
    if not os.path.exists(config_file_path):
        raise ValueError("app.ini wasn't created!")

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
