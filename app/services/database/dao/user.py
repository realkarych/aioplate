from sqlalchemy.orm import sessionmaker

from app.models import dto
from app.models.database import User
from app.services.database.dao import mapper
from app.services.database.dao.base import BaseDAO


class UserDAO(BaseDAO[User]):
    """ORM queries for users table"""

    def __init__(self, session: sessionmaker):
        super().__init__(User, session)

    async def add_user(self, user: dto.User) -> None:
        """
        Add user to database if not added yet. If added, tries to update parameters.
        :param user: Telegram user.
        """

        async with self._session() as session:
            await session.merge(mapper.map_to_db_user(user))
            await session.commit()
