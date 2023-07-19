from aiogram import types, Router
from aiogram.enums import ChatType
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from fluentogram import TranslatorRunner
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.filters.chat_type import ChatTypeFilter
from app.core.keyboards import reply
from app.core.navigations.command import Commands
from app.models.dto import get_user_from_message
from app.services.database.dao.user import UserDAO


async def cmd_start(m: types.Message, i18n: TranslatorRunner, session: AsyncSession, state: FSMContext):
    """/start command handling. Adds new user to database, finish states"""

    await state.clear()

    user = get_user_from_message(message=m)
    dao = UserDAO(session=session)
    await dao.add_user(user)

    await m.answer(str(i18n.welcome(user_firstname=user.firstname)), reply_markup=reply.default_menu(i18n))


def register() -> Router:
    """Register base handlers: /start and handling events from default menu"""

    router = Router()

    router.message.register(
        cmd_start,
        ChatTypeFilter(chat_type=ChatType.PRIVATE),
        Command(str(Commands.start))
    )

    return router
