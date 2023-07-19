from typing import Callable, Dict, Any, Awaitable

from aiogram import BaseMiddleware
from aiogram.types import Message
from fluentogram import TranslatorHub


class TranslatorRunnerMiddleware(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
            event: Message,
            data: Dict[str, Any]
    ) -> Any:
        hub: TranslatorHub = data.get("_translator_hub")
        data["i18n"] = hub.get_translator_by_locale(event.from_user.language_code)
        return await handler(event, data)
