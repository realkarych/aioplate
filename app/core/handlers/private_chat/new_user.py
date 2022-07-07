from aiogram import types, Dispatcher
from aiogram.types import ChatType

from app.core.messages.private_chat import new_user as msgs
from app.core.middlewares.throttling import throttle
from app.core.navigations.command import Commands
from app.models.dto import get_user_from_message
from app.services.database.dao.user import UserDAO


@throttle(limit=2)
async def cmd_start(m: types.Message):
    """/start command handling"""

    user = get_user_from_message(message=m)
    session = UserDAO(session=m.bot.get("db"))
    await session.add_user(user)

    await m.answer(msgs.welcome(user_firsname=user.firstname), reply_markup=None)


def register_handlers(dp: Dispatcher) -> None:
    """Register handlers for newcomers"""

    dp.register_message_handler(cmd_start, commands=str(Commands.start), chat_type=ChatType.PRIVATE)
