from aiogram.types import ReplyKeyboardMarkup


class ResizedReplyKeyboard(ReplyKeyboardMarkup):
    """
    I prefer override default ReplyKeyboardMarkup to avoid passing the resizer parameter
    every time.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.resize_keyboard = True
