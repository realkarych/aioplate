from aiogram import types, Router
from aiogram.enums import ChatType
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from fluentogram import TranslatorRunner
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.filters.chat_type import ChatTypeFilter
from app.core.navigations.command import PrivateChatCommands
from app.dtos.user import UserDTO
from app.services.database.dao.user import UserDAO


async def cmd_start(m: types.Message, i18n: TranslatorRunner, session: AsyncSession, state: FSMContext):
    await state.clear()

    user = UserDTO.from_message(message=m)
    dao = UserDAO(session=session)
    await dao.add_user(user)
    await dao.commit()

    await m.answer(
        text=str(i18n.welcome(user_firstname=user.firstname))
    )


def register() -> Router:
    router = Router()

    router.message.register(
        cmd_start,
        ChatTypeFilter(chat_type=ChatType.PRIVATE),
        Command(str(PrivateChatCommands.start))
    )

    return router
