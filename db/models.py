from db.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey,Boolean
from sqlalchemy.orm import relationship

'''
    This file contains the database models for the application.
    It uses SQLAlchemy ORM to define the structure of the database tables.
    Each class represents a table in the database, and each attribute of the class represents a column in the table.
'''

class DbCustomers(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True)

    projects = relationship("DbProjects", back_populates="customer")
    assignements = relationship("DbAssignments", back_populates="customers")

class DbProjects(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True) 
    name = Column(String, nullable=False)
    description = Column(String)
    start_date = Column(Date)
    end_date = Column(Date)
    budget = Column(Integer)

    customer_id = Column(Integer, ForeignKey("customers.id"))
    customer = relationship("DbCustomers", back_populates="projects")

    assignements = relationship("DbAssignments", back_populates="projects")
    time_block = relationship("DbTimeBlock", back_populates="projects")


class DbTimeBlock(Base):
    '''
        This class represents the timeblocks table in the database. 
        It contains information about the time blocks, including the date, hours worked, and a note.
        It also has a foreign key relationship with the projects table, allowing us to associate each time block with a project.
        The employee_id attribute is commented out, but it could be used to associate each time block with an employee.
    '''
    __tablename__ = "timeblocks"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date)
    hours = Column(Integer)
    note = Column(String)

    project_id = Column(Integer, ForeignKey("projects.id"))
   # employee_id = Column(Integer, ForeignKey("users.id"))

    project = relationship("DbProjects", back_populates="timeblocks")
   # employee = relationship("DbUser", back_populates="timeblocks")