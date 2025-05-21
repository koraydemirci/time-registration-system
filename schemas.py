from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
import enum

#enum for project status
class ProjectStatus(enum.Enum):
    active = "active"
    inactive = "inactive"
    completed = "completed"
    on_hold = "on hold"

#employer schema
class Employer(BaseModel):
    id: int
    class Config():
        orm_mode = True

#employee schema
class Employee(BaseModel):
    id: int
    class Config():
        orm_mode = True

#customer schema
class Customer(BaseModel):
    id: int
    class Config():
        orm_mode = True

#Project schema
class ProjectBase(BaseModel):
    name: str
    description: Optional[str] = None
    start_date: Optional[datetime]
    end_date: Optional[datetime]
    budget: float
    status: ProjectStatus= ProjectStatus.active
    hour_rate: Optional[float] = None

class ProjectCreate(ProjectBase):
    customer_id: int
    employee_id: int
    employer_id: int

class ProjectDisplay(BaseModel):
    name: str
    description: str
    start_date: datetime
    end_date:  datetime
    budget: float
    customer: Customer
    employee: Employee
    employer: Employer
    timeblocks: List['TimeBlockDisplay'] = []
    class Config():
        orm_mode = True

#timeblock schema
class TimeBlockBase(BaseModel):
    start_date: datetime
    end_date: datetime
    note: Optional[str] = None

class TimeBlockCreate(TimeBlockBase):
    project_id: int
    employee_id: int

class TimeBlockDisplay(TimeBlockBase):
    id: int
    hours: int
    project_id: int
    employee_id: int
    project: ProjectDisplay
    class Config():
        orm_mode = True

#Invoice schema



ProjectDisplay.update_forward_refs()
TimeBlockDisplay.update_forward_refs()