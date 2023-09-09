from sqlalchemy.ext.asyncio import AsyncSession

from app.dtos.user import UserDTO


class UserDAO:
    """ORM queries for users table"""

    def __init__(self, session: AsyncSession):
        self._session = session

    async def add_user(self, user: UserDTO) -> None:
        await self._session.merge(user.to_db_model())
