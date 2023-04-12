from sqlalchemy import Column, DateTime, Integer, String, func
from sqlalchemy.orm import relationship

from ..config.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String(255), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    created_at = Column(DateTime(timezone=True),
                        nullable=False, server_default=func.now())
    updated_at = Column(DateTime(timezone=True), nullable=False,
                        onupdate=func.now())

    user_wallets = relationship(
        "UserWallet", back_populates="user", cascade="all, delete-orphan")
