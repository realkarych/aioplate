"""App launcher"""

import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from app.core import middlewares
from app.core.handlers.factory import DefaultHandlersFactory
from app.core.handlers.private_chat import base
from app.core.navigations.command import set_bot_commands
from app.core.updates import worker
from app.services.database.connector import setup_get_pool
from app.settings.config import Config, load_config


async def main() -> None:
    """Starts app & polling."""

    # In prod, add `filename=` arg and write your logs to file instead of stdout
    logging.basicConfig(
        level=logging.WARNING,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s"
    )

    config: Config = load_config()

    bot = Bot(config.bot.token, parse_mode=config.bot.parse_mode)
    bot["db"] = await setup_get_pool(db_uri=config.db.get_uri())
    dp = Dispatcher(bot=bot, storage=MemoryStorage())
    await set_bot_commands(bot=bot)

    # Middlewares setup. Register middlewares provided to __init__.py in middlewares package.
    middlewares.setup(dispatcher=dp)
    # Provide your default handler-modules into register() func.
    DefaultHandlersFactory(dp).register(base, )

    try:
        await dp.start_polling(allowed_updates=worker.get_handled_updates(dp))
    finally:
        await dp.storage.close()
        await dp.storage.wait_closed()
        await (await bot.get_session()).close()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        # Log this is pointless
        pass
