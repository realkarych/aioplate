"""App launcher"""

import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from sqlalchemy.ext.asyncio import async_sessionmaker

from app.core.handlers import factory
from app.core.handlers.private_chat import base
from app.core.middlewares.db import DbSessionMiddleware
from app.core.middlewares.i18n import TranslatorRunnerMiddleware
from app.core.navigations.command import set_bot_commands
from app.services.database.connector import setup_get_pool
from app.settings.config import Config, load_config


async def main() -> None:
    """Starts app & polling."""

    # On production, set log-level to ERROR; add `filename=` arg and write your logs to
    # file instead of stdout.
    # Example: filename=f"{ROOT_DIR}/error.log".
    # Another way: checking systemctl logs.
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s"
    )

    config: Config = load_config()

    bot = Bot(config.bot.token, parse_mode=config.bot.parse_mode)
    dp = Dispatcher(bot=bot, storage=MemoryStorage())
    await set_bot_commands(bot=bot)

    _set_middlewares(dp=dp, session_pool=await setup_get_pool(db_uri=config.db.get_uri()))

    # Provide your default handler-modules into register() func.
    factory.register(dp, base, )

    try:
        await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
    finally:
        await dp.storage.close()
        await bot.session.close()


def _set_middlewares(dp: Dispatcher, session_pool: async_sessionmaker) -> None:
    dp.message.middleware(DbSessionMiddleware(session_pool))
    dp.callback_query.middleware(DbSessionMiddleware(session_pool))
    dp.edited_message.middleware(DbSessionMiddleware(session_pool))

    dp.message.middleware(TranslatorRunnerMiddleware())
    dp.callback_query.middleware(TranslatorRunnerMiddleware())
    dp.edited_message.middleware(TranslatorRunnerMiddleware())


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        # Logging this is pointless
        pass
