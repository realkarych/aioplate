from sqlalchemy.ext.asyncio import AsyncSession

from app.dtos.user import UserDTO
from app.models.user import User
from app.services.database.dao.base import BaseDAO


class UserDAO(BaseDAO[User]):
    """ORM queries for users table"""

    def __init__(self, session: AsyncSession):
        super().__init__(User, session)

    async def add_user(self, user: UserDTO) -> None:
        await self._session.merge(user.to_db_model())
