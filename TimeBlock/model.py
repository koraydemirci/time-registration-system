from db.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from sqlalchemy.types import DateTime as Datetime

class DbTimeBlock(Base):
    __tablename__ = "timeblocks"
    id = Column(Integer, primary_key=True, index=True)
    start_date = Column(Datetime, nullable=False)
    end_date = Column(Datetime, nullable=False)
    note = Column(String, nullable=True)
    hours = Column(Float, nullable=True) 
    project_id = Column(Integer, ForeignKey("projects.id"), nullable=False)
    employee_id = Column(Integer, ForeignKey("employee.id"), nullable=False)
    project = relationship("DbProjects", back_populates="timeblocks")