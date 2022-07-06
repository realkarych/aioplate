from app.models import dto
from app.models.database import User


def map_to_db_user(user: dto.User) -> User:
    return User(
        id=user.id,
        username=user.username,
        firstname=user.firstname,
        lastname=user.lastname
    )
