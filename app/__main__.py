"""App launcher"""

import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from app.core.handlers import factory
from app.core.handlers.private_chat import base
from app.core.middlewares.db import DbSessionMiddleware
from app.core.navigations.command import set_bot_commands
from app.services.database.connector import setup_get_pool
from app.settings.config import Config, load_config


async def main() -> None:
    """Starts app & polling."""

    # In prod, set log-level to WARNING; add `filename=` arg and write your logs to
    # file instead of stdout.
    # Example: filename=f"{ROOT_DIR}/error.log".
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s"
    )

    config: Config = load_config()

    bot = Bot(config.bot.token, parse_mode=config.bot.parse_mode)
    await set_bot_commands(bot=bot)

    dp = Dispatcher(bot=bot, storage=MemoryStorage())
    sessionmaker = await setup_get_pool(db_uri=config.db.get_uri())
    dp.message.middleware(DbSessionMiddleware(sessionmaker))
    dp.message.outer_middleware(DbSessionMiddleware(sessionmaker))
    dp.edited_message.outer_middleware(DbSessionMiddleware(sessionmaker))

    # Provide your default handler-modules into register() func.
    factory.register(dp, base, )

    try:
        await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
    finally:
        await dp.storage.close()
        await bot.session.close()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        # Logging this is pointless
        pass
