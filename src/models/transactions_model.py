# from sqlalchemy import TEXT, Column, DateTime, Float, Integer, String, func
# from ..config.database import Base


# class Transaction(Base):
#     __tablename__ = "transactions"

#     id = Column(Integer, primary_key=True)
#     name = Column(String(255), nullable=False)
#     amount = Column(Float, nullable=False)
#     description = Column(TEXT, nullable=False)

#     created_at = Column(DateTime(timezone=True),
#                         nullable=False, server_default=func.now()),
#     updated_at = Column(DateTime(timezone=True), nullable=False,
#                         onupdate=func.now())
