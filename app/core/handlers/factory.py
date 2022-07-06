import logging
import types
from abc import ABC, abstractmethod

from aiogram import Dispatcher


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

        for handler in handlers:

            if isinstance(handler, types.ModuleType):
                try:
                    handler.register_handlers(dp=self._dp)
                except AttributeError as error:
                    logging.error("register_handlers() method wasn't implemented "
                                  "in %s", str(error.obj))

            else:
                logging.error("%s from submitted args to `register_handlers()` "
                              "is not a .py module", handler)
