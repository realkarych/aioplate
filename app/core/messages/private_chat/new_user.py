from aiogram.utils.markdown import hbold as bold, hlink as link


def welcome(user_firsname: str) -> str:
    """
    :param user_firsname:
    :return: welcome message to user
    """

    return bold(f'Hello, {user_firsname}!') + \
           f"\n\nThis is {link(title='Aioplate', url='https://github.com/devkarych/aioplate')}." \
           f"\nAuthor: @karych."
