import types
from abc import ABC, abstractmethod
from typing import Iterable

from aiogram import Dispatcher

from app.exceptions.handler import RegisterHandlerError


class HandlersFactory(ABC):
    """Declares basic functionality of handlers factory."""

    def __init__(self, dp: Dispatcher) -> None:
        """
        :param dp: Dispatcher for providing it to handlers initializers.
        """

        self._dp = dp

    @abstractmethod
    def register(self, *handlers) -> None:
        """Register handlers here..."""


class DefaultHandlersFactory(HandlersFactory):
    """Implements default handlers registration."""

    def register(self, *handlers) -> None:
        """
        Handlers registering. If `register_handlers()` wasn't implemented in module,
        it skips with error log message.
        :param handlers: .py handler-modules with implemented register_handlers() method.
        """

        handlers: Iterable[types.ModuleType]

        for handler in handlers:
            if isinstance(handler, types.ModuleType):
                try:
                    handler.register_handlers(dp=self._dp)
                except AttributeError as error:
                    raise RegisterHandlerError(
                        f"register_handlers() method wasn't implemented "
                        f"in {str(error.obj)}"
                    )
            else:
                raise RegisterHandlerError(
                    f"{handler} from submitted args to `register_handlers()` "
                    f"is not a .py module"
                )
