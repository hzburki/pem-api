from sqlalchemy import Column, DateTime, ForeignKey, Integer, func
from sqlalchemy.orm import relationship

from ..config.database import Base


class UserWallet(Base):
    __tablename__ = "user_wallets"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    wallet_id = Column(Integer, ForeignKey("wallets.id"), nullable=False)
    created_at = Column(DateTime(timezone=True),
                        nullable=False, server_default=func.now())
    updated_at = Column(DateTime(timezone=True), nullable=False,
                        onupdate=func.now())

    user = relationship("User", back_populates="user_wallets")
    wallet = relationship(
        "Wallet", back_populates="user_wallets")
