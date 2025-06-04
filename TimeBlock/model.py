
from db.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey,Boolean, Float
from sqlalchemy.orm import relationship
from sqlalchemy.types import DateTime as Datetime


class DbTimeBlock(Base):
    __tablename__ = "timeblocks"
    id = Column(Integer, primary_key=True, index=True)
    start_date = Column(Datetime)
    end_date = Column(Datetime)
    note = Column(String, nullable=True)

    project_id = Column(Integer, ForeignKey("projects.id"))
    employee_id = Column(Integer, ForeignKey("employee.id"))
    project = relationship("DbProjects", back_populates="timeblocks")