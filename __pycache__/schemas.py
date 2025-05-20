from pydantic import BaseModel
from typing import List, Optional
from datetime import date
        
#customer schema
class Customer(BaseModel):
    id: int
    name: str
    email: str
    class Config():
        orm_mode = True

#Project schema
class ProjectBase(BaseModel):
    name: str
    description: Optional[str] = None
    start_date: Optional[date]
    end_date: Optional[date]
    budget: int

class ProjectCreate(ProjectBase):
    customer_id: int

class ProjectDisplay(BaseModel):
    name: str
    description: str
    start_date: str
    end_date: str
    budget: int
    customer: Customer
    class Config():
        orm_mode = True


#timeblock schema
class TimeBlockBase(BaseModel):
    date: date
    hours: int
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

