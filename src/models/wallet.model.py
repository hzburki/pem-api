from sqlalchemy import DateTime, Column, Float, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy import func

from ..config.database import Base


class Wallet(Base):
    __tablename__ = "wallets"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String)
    balance = Column(Float)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    user_wallets = relationship(
        "UserWallet", back_populates="wallet", cascade="all, delete-orphan")
