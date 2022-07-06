from dataclasses import dataclass, field

from sqlalchemy.ext.asyncio import AsyncSession

from app.services.database.dao.user import UserDAO


@dataclass
class HolderDao:
    session: AsyncSession
    user: UserDAO = field(init=False)

    def __post_init__(self):
        self.user = UserDAO(self.session)

    async def commit(self):
        await self.session.commit()
