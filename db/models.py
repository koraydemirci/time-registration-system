from db.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey,Boolean, Float
from sqlalchemy.orm import relationship
from sqlalchemy.types import DateTime as Datetime
from sqlalchemy import Enum

'''
    This file contains the database models for the application.
    It uses SQLAlchemy ORM to define the structure of the database tables.
    Each class represents a table in the database, and each attribute of the class represents a column in the table.
'''

class DbUser(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=True)
    name = Column(String, nullable=False)
    type = Column(Enum("employer", "employee", "customer", name="user_type"), nullable=False, default="employer")
