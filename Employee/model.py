
from sqlalchemy import Column, Integer, String, ForeignKey,Boolean, Float
from db.models import DbUser
from sqlalchemy.orm import relationship

class Employee(DbUser):
    __tablename__ = "employee"
    id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    name = Column(String , nullable= True)
    email = Column(String , nullable=True )

    project_links = relationship("DbProjectEmployee", back_populates="employee")