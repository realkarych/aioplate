from __future__ import annotations

from dataclasses import dataclass

from aiogram import types as tg
from aiogram.types import Message

from app.models import database


@dataclass
class User:
    """User DTO: database & telegram user."""

    id: int
    username: str | None = None
    firstname: str | None = None
    lastname: str | None = None

    @classmethod
    def from_aiogram(cls, user: tg.User) -> User:
        """
        :param user: Telegram user
        :return: DTO
        """

        return cls(
            id=user.id,
            username=user.username,
            firstname=user.first_name,
            lastname=user.last_name
        )

    @classmethod
    def from_db(cls, user: database.User) -> User:
        """
        :param user: Database user
        :return: DTO
        """

        return cls(
            id=user.id,
            username=user.username,
            firstname=user.firstname,
            lastname=user.lastname
        )


def get_user_from_message(message: Message) -> User:
    """Returns user obj from aiogram message."""

    return User(
        id=message.from_user.id,
        username=message.from_user.username,
        firstname=message.from_user.first_name,
        lastname=message.from_user.last_name
    )
