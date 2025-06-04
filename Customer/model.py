from sqlalchemy import Column, Integer, String, ForeignKey,Boolean, Float
from db.models import DbUser
from sqlalchemy.orm import relationship


class Customer(DbUser):
    __tablename__ = "customer"
    id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    projects_as_customer = relationship(
    "DbProjects",
    back_populates="customer",
    foreign_keys="DbProjects.customer_id"
    )