from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Float, Text
from sqlalchemy.orm import relationship
from sqlalchemy import func

from ..config.database import Base


class Transaction(Base):
    __table_name__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    user_wallet_id = Column(Integer, ForeignKey("user_wallets.id"))
    amount = Column(Float)
    name = Column(String(255))
    description = Column(Text)
    date = Column(DateTime(timezone=True))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    user_wallet = relationship("UserWallet", back_populates="transactions")
