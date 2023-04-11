from sqlalchemy import func
from sqlalchemy.orm import relationship
from sqlalchemy import DateTime, Column, ForeignKey, Integer, String

from ..config.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    user_wallets = relationship(
        "UserWallet", back_populates="user", cascade="all, delete-orphan")
