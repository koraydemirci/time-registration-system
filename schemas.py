from pydantic import BaseModel, field_validator, model_validator
from typing import List, Optional
from datetime import datetime
import enum


class UserBase(BaseModel):
    id: int
    email: str
    name: str

    class Config:
        orm_mode = True

class UserCreate(BaseModel):
    name: str
    email: str
    password: str
    user_type: str = "employer" 

class UserLogin(BaseModel):
    username: str
    password: str
        
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

@model_validator(mode='after')
def validate_dates(self):
    if self.start_date and self.end_date and self.start_date >= self.end_date:
        raise ValueError("Start date must be before end date")
    return self


class ProjectDisplay(BaseModel):
    id: int
    name: str
    description: str
    start_date: datetime
    end_date:  datetime
    budget: float
    customer: Optional[Customer] = None
    employer: Optional[Employer] = None
    timeblocks: List['TimeBlockDisplay'] = []
    class Config():
        from_attributes = True
        
#assign employee to project

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


class CustomerBase(BaseModel):
    name: str
    email: str


class CustomerCreate(BaseModel):
   name:str
   email:str

class CustomerUpdate(CustomerBase):
    pass

class CustomerOut(CustomerBase):
    id: int
    class Config:
        orm_mode = True

class EmployerBase(BaseModel):
    name: str
    email: str

class EmployerCreate(BaseModel):
    name:str
    email:str

class EmployerOut(EmployerBase):
    id: int
    class Config:
        orm_mode = True



ProjectDisplay.update_forward_refs()
TimeBlockDisplay.update_forward_refs()