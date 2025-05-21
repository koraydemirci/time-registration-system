from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

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
    status: enum('active', 'inactive', 'completed', 'on hold') = 'active'
    hour_rate: Optional[float] = None

class ProjectCreate(ProjectBase):
    customer_id: int
    employee_id: int
    employer_id: int

class ProjectDisplay(BaseModel):
    name: str
    description: str
    start_date: str
    end_date: str
    budget: int
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
