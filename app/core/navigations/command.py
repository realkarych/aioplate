from dataclasses import dataclass
from enum import Enum, unique

from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeAllPrivateChats


@dataclass
class Command:
    """
    Command object is dto for organize the same interface to access /command
    data in handlers & in commands-factory & in registrator.
    """

    name: str
    description: str

    def to_bot_command(self) -> BotCommand:
        """Map Command object to BotCommand object"""

        return BotCommand(command=self.name, description=self.description)


@unique
class BaseCommandList(Enum):
    """Base list of commands."""

    def __str__(self) -> str:
        return self.value.name

    def __call__(self, *args, **kwargs) -> Command:
        return self.value


class PrivateChatCommands(BaseCommandList):
    """
    List of commands with public access & submission to Telegram menu list.
    Do not implement here admin commands because of submission to menu.
    For this case, create another commands list & factory.
    """

    start = Command(name='start', description='Start Bot')


async def set_bot_commands(bot: Bot) -> None:
    """
    Creates a commands' lists (shortcuts) in Telegram app menu.
    """

    # Private chat commands
    await bot.set_my_commands(
        commands=[command().to_bot_command() for command in PrivateChatCommands],
        scope=BotCommandScopeAllPrivateChats()  # pyright: ignore
    )
