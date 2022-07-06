from app.models import dto
from app.models.database import User


def map_to_db_user(user: dto.User) -> User:
    """
    :param user: DTO
    :return: database user object
    """

    return User(
        id=user.id,
        username=user.username,
        firstname=user.firstname,
        lastname=user.lastname
    )
