from aiogram.utils.markdown import hbold as bold, hlink as link


def welcome(user_firstname: str | None) -> str:
    """
    :param user_firstname:
    :return: welcome message to user
    """

    repo_url = link(title='Aioplate', url='https://github.com/devkarych/aioplate')
    return bold(f'Hello, {user_firstname}!') + f"\n\nThis is {repo_url}.\nAuthor: @karych."
