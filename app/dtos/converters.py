from datetime import datetime

from app.dtos.user import UserDTO
from app.models.user import User


def db_user_to_dto(user: User) -> UserDTO:
    return UserDTO(
        id=int(str(user.id)),
        username=str(user.username),
        firstname=str(user.firstname),
        lastname=str(user.lastname),
        language_code=str(user.language_code),
        registered_time=datetime.fromisoformat(str(user.registered_date))
    )
