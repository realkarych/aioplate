from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from app.core.navigations import reply


class ResizedReplyKeyboard(ReplyKeyboardMarkup):
    """
    I prefer override default ReplyKeyboardMarkup to avoid passing the resizer parameter
    every time.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.resize_keyboard = True


# Customize your keyboard here
default_menu = ResizedReplyKeyboard(
    keyboard=[
        [
            KeyboardButton(reply.some_text)
        ],
    ]
)
