from sqlalchemy import Column, BigInteger, String, DateTime, func

from app.services.database.base import Base


class User(Base):
    """Implements base table contains all registered in bot users"""

    __tablename__ = "users"

    id = Column(BigInteger, primary_key=True, unique=True, autoincrement=False)  # Telegram id
    username = Column(String, default=None)
    firstname = Column(String, default=None)
    lastname = Column(String, default=None)
    registered_date = Column(DateTime(timezone=True), server_default=func.now())

    def __repr__(self) -> str:
        return f"User: {self.id}, {self.username}, {self.firstname} " \
               f"{self.lastname}, {self.registered_date}"
