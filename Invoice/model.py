from sqlalchemy import Column, Integer, String, Float
from db.database import Base

class Invoice(Base):
    __tablename__ = "invoices"
    id = Column(Integer, primary_key=True, index=True)
    customer = Column(String, index=True)
    amount = Column(Float)
    description = Column(String)
