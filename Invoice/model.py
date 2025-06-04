from sqlalchemy import Column, Integer, Float, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from db.database import Base

class Invoice(Base):
    __tablename__ = "invoices"
    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, ForeignKey("customer.id"))
    project_id = Column(Integer, ForeignKey("project.id"))
    amount = Column(Float)
    issue_date = Column(Date)
    due_date = Column(Date)
    status = Column(String)  # e.g., "paid", "unpaid", "overdue"

    customer = relationship("Customer", back_populates="invoices")
    project = relationship("DbProjects", back_populates="invoices")
