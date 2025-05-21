from db.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey,Boolean
from sqlalchemy.orm import relationship, back_populates, 
from sqlalchemy.dialects.postgresql import ENUM as enum
from sqlalchemy.types import DateTime as Datetime

'''
    This file contains the database models for the application.
    It uses SQLAlchemy ORM to define the structure of the database tables.
    Each class represents a table in the database, and each attribute of the class represents a column in the table.
'''

class DbUser(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    type = Column(enum("employee", "customer","employer"), nullable=False)
    name = Column(String, nullable=False)

#relationships
    projects = relationship("DbProjects", back_populates="users", foreign_keys=[DbProjects.customer_id, DbProjects.employee_id, DbProjects.employer_id])
    project_assignment = relationship("DbProjectAssigned", back_populates="users", foreign_keys=[DbProjectAssigned.user_id])
    timeblocks = relationship("DbTimeBlock", back_populates="users", foreign_keys=[DbTimeBlock.employee_id])
    

class DbProjects(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True) 
    name = Column(String)
    description = Column(String)
    start_date = Column(Datetime)
    end_date = Column(Datetime)
    budget = Column(float)
    status = Column(enum("active", "inactive", "completed", "on hold"), default="active")
    hour_rate = Column(float)

#    foreign keys
    customer_id = Column(Integer, ForeignKey("users.id"))
    employee_id = Column(Integer, ForeignKey("users.id"))
    employer_id = Column(Integer, ForeignKey("users.id"))

#    relationships
    customer = relationship("DbUser", back_populates="projects", foreign_keys=[customer_id],
                            primaryjoin="DbUser.id==DbProjects.customer_id and DbUser.type=='customer'")
    employee = relationship("DbUser", back_populates="projects", foreign_keys=[employee_id],
                            primaryjoin="DbUser.id==DbProjects.employee_id and DbUser.type=='employee'")
    employer = relationship("DbUser", back_populates="projects", foreign_keys=[employer_id],
                            primaryjoin="DbUser.id==DbProjects.employer_id and DbUser.type=='employer'")
    project_assignment = relationship("DbProjectAssigned", back_populates="projects")
    time_blocks = relationship("DbTimeBlock", back_populates="projects")


class DbTimeBlock(Base):
    '''
        This class represents the timeblocks table in the database. 
        It contains information about the time blocks, including the date, hours worked, and a note.
        It also has a foreign key relationship with the projects table, allowing us to associate each time block with a project.
        The employee_id attribute is commented out, but it could be used to associate each time block with an employee.
    '''
    __tablename__ = "timeblocks"

    id = Column(Integer, primary_key=True, index=True)
    star_date = Column(Datetime)
    end_date = Column(Datetime)
    note = Column(String, nullable=True)

    project_id = Column(Integer, ForeignKey("projects.id"))
    employee_id = Column(Integer, ForeignKey("users.id"))

    project = relationship("DbProjects", back_populates="timeblocks")
    employee = relationship("DbUser", back_populates="timeblocks", foreign_keys=[employee_id],
                            primaryjoin="DbUser.id==DbTimeBlock.employee_id and DbUser.type=='employee'")


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
                            primaryjoin="DbUser.id==DbProjectAssigned.user_id and DbUser.type=='employee'")