from db.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey,Boolean, Float
from sqlalchemy.orm import relationship
from sqlalchemy.types import DateTime as Datetime
from sqlalchemy import Enum

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
    customer_id = Column(Integer, ForeignKey("customer.id"))
    employer_id = Column(Integer, ForeignKey("employer.id"))

#    relationships
    customer = relationship(
        "Customer",
        back_populates="projects_as_customer",
        foreign_keys=[customer_id])
 
    employer = relationship(
        "Employer",
        back_populates="projects_as_employer",
        foreign_keys=[employer_id]
    )
    employee_links = relationship("DbProjectEmployee", back_populates="project")
    timeblocks = relationship("DbTimeBlock", back_populates="project")
    
class DbProjectEmployee(Base):
    __tablename__ = "project_employee"
    id = Column(Integer, primary_key=True, index=True)
    project_id = Column(Integer, ForeignKey("projects.id"))
    employee_id = Column(Integer, ForeignKey("employee.id"))

    project = relationship("DbProjects", back_populates="employee_links")
    employee = relationship("Employee", back_populates="project_links")

# class DbTimeBlock(Base): 
#     __tablename__ = "timeblocks"