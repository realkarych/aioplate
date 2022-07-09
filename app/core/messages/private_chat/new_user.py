from aiogram.utils.markdown import hbold as bold, hlink as link


def welcome(user_firstname: str) -> str:
    """
    :param user_firstname:
    :return: welcome message to user
    """

    return bold(f'Hello, {user_firstname}!') + \
           f"\n\nThis is {link(title='Aioplate', url='https://github.com/devkarych/aioplate')}." \
           f"\nAuthor: @karych."
