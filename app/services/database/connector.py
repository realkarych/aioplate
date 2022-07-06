from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

from app.services.database.base import Base


async def setup_get_pool(db_uri: str) -> sessionmaker:
    """
    Setup postgres database, creates tables if not exists. Connect to database.
    :param db_uri: postgres dsn
    :return sessionmaker: provides to bot instance to manage sessions.
    """

    engine = create_async_engine(
        db_uri,
        future=True
    )
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    sessionmaker_ = sessionmaker(
        engine, expire_on_commit=False, class_=AsyncSession
    )
    return sessionmaker_
