
from db.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey,Boolean, Float
from sqlalchemy.orm import relationship
from sqlalchemy.types import DateTime as Datetime
from sqlalchemy import Enum


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

