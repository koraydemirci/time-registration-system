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
    status: Optional[str]
    customer: Optional[Customer] = None
    employer: Optional[Employer] = None
   # timeblocks: Optional[List['TimeBlockDisplay']] = None
    class Config():
        from_attributes = True


#timeblock schema
class TimeBlockBase(BaseModel):
    start_date: datetime
    end_date: datetime
    note: Optional[str] = None
    hours: Optional[float] = None

    
    @field_validator("end_date")
    def end_after_start(cls, v, info):
        start_date = info.data.get("start_date")
        if start_date and v <= start_date:
            raise ValueError(f"end_date ({v}) must be after start_date ({start_date})")
        return v

class TimeBlockCreate(TimeBlockBase):
    project_id: int
    employee_id: int

class TimeBlockDisplay(TimeBlockBase):
    id: int
    project_id: int
    employee_id: int
    project: Optional[ProjectDisplay] = None 
    class Config():
        from_attributes = True


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


# Schema class for employees 
class EmployeeBase(BaseModel):
    name: str
    email: str

class EmployeeCreate(EmployeeBase):
    pass

class EmployeeOut(EmployeeBase):
    id: int
    class Config:
        orm_mode = True


ProjectDisplay.update_forward_refs()
TimeBlockDisplay.update_forward_refs()