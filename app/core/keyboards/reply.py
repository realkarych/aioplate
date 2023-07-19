from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from fluentogram import TranslatorRunner


class ResizedReplyKeyboard(ReplyKeyboardMarkup):
    """
    I prefer override default ReplyKeyboardMarkup to avoid passing the resizer parameter
    every time.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.resize_keyboard = True


# Customize your keyboard here
def default_menu(i18n: TranslatorRunner):
    return ResizedReplyKeyboard(
        keyboard=[
            [
                KeyboardButton(text=str(i18n.button.something))
            ],
        ]
    )
