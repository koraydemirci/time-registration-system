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
    password = Column(String, nullable=False)
    type = Column(Enum("employee", "customer","employer",name="user_type"), nullable=False)
    name = Column(String, nullable=False)

#relationships
    projects = relationship("DbProjects", back_populates="customer", primaryjoin="and_(DbUser.id==DbProjects.customer_id , DbUser.type=='customer')")
    employers = relationship("DbProjects", back_populates="employer", primaryjoin="and_(DbUser.id==DbProjects.employer_id , DbUser.type=='employer')")
    project_assignment = relationship("DbProjectAssigned", back_populates="users", primaryjoin="and_(DbUser.id==DbProjectAssigned.user_id , DbUser.type=='employee')")
    # timeblocks = relationship("DbTimeBlock", back_populates="employee", primaryjoin="and_(DbUser.id==DbTimeBlock.employee_id , DbUser.type=='employee')")


class DbProjects(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True) 
    name = Column(String)
    description = Column(String)
    start_date = Column(Datetime)
    end_date = Column(Datetime)
    budget = Column(Float)
    status = Column(Enum("active", "inactive", "completed", "on hold", name="project_status"), default="active")
    hour_rate = Column(Float)

#    foreign keys
    customer_id = Column(Integer, ForeignKey("users.id"))
    employer_id = Column(Integer, ForeignKey("users.id"))

#    relationships
    customer = relationship(
        "DbUser",
        back_populates="projects",
        foreign_keys=[customer_id],
        primaryjoin="and_(DbUser.id==DbProjects.customer_id , DbUser.type=='customer')")
    employer = relationship(
        "DbUser",
        back_populates="employers",
        foreign_keys=[employer_id],
        primaryjoin="and_(DbUser.id==DbProjects.employer_id , DbUser.type=='employer')")
    project_assignment = relationship("DbProjectAssigned", back_populates="projects")
    timeblocks = relationship("DbTimeBlock", back_populates="project")


class DbTimeBlock(Base):
    '''
        This class represents the timeblocks table in the database. 
        It contains information about the time blocks, including the date, hours worked, and a note.
        It also has a foreign key relationship with the projects table, allowing us to associate each time block with a project.
        The employee_id attribute is commented out, but it could be used to associate each time block with an employee.
    '''
    __tablename__ = "timeblocks"

    id = Column(Integer, primary_key=True, index=True)
    start_date = Column(Datetime)
    end_date = Column(Datetime)
    note = Column(String, nullable=True)

#    foreign keys
    project_id = Column(Integer, ForeignKey("projects.id"))
    # employee_id = Column(Integer, ForeignKey("users.id"))

#    relationships
    project = relationship("DbProjects", back_populates="timeblocks")
 #   employee = relationship("DbUser", back_populates="timeblocks", foreign_keys=[employee_id])


#project_assigned table
'''
    This class represents the project_assigned table in the database. 
    It contains information about the projects assigned to users.
    It has foreign key relationships with the projects and users tables, allowing us to associate each project assignment with a project and a user.
'''
class DbProjectAssigned(Base):
    __tablename__ = "project_assigned"

    id = Column(Integer, primary_key=True, index=True)
    project_id = Column(Integer, ForeignKey("projects.id"))
    user_id = Column(Integer, ForeignKey("users.id"))

    projects = relationship("DbProjects", back_populates="project_assignment")
    users = relationship("DbUser", back_populates="project_assignment", foreign_keys=[user_id],
                            primaryjoin="and_(DbUser.id==DbProjectAssigned.user_id , DbUser.type=='employee')")
    
    
class Customer(Base):
    __tablename__ = "customers"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True)