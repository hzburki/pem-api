from ..config.database import Base
from sqlalchemy import DateTime, Column, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy import func


class UserWallet(Base):
    __tablename__ = "user_wallets"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    wallet_id = Column(Integer, ForeignKey("wallets.id"))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    user = relationship("User", back_populates="user_wallets")
    wallet = relationship("Wallet", back_populates="user_wallets")
