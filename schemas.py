from pydantic import BaseModel, validator, root_validator
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
    #employer_id: int

    class Config:
        schema_extra = {
            "example": {
                "name": "Project A",
                "description": "Description of Project A",
                "start_date": "2023-01-01T00:00:00Z",
                "end_date": "2023-12-31T00:00:00Z",
                "budget": 100000.0,
                "status": "active",
                "hour_rate": 50.0,
                "customer_id": 1,
                "employer_id": 1
            }
        }

    @validator('name')
    def name_must_not_be_empty(cls, v):
        if not v or v.strip():
            raise ValueError('Project name must not be empty')
        return v
    
    @root_validator
    def check_dates(cls, values):
        start_date = values.get('start_date')
        end_date = values.get('end_date')
        if start_date and end_date and start_date > end_date:
            raise ValueError('Start date must be before end date')
        return values

class ProjectDisplay(BaseModel):
    id: int
    name: str
    description: str
    start_date: datetime
    end_date:  datetime
    budget: float
    customer: Customer
    employer: Employer
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

# add these after your Customer schema

class CustomerBase(BaseModel):
    name: str
    email: str
    type: str
    
  



class CustomerCreate(BaseModel):
   name:str
   email:str


class CustomerUpdate(CustomerBase):
    pass

class CustomerOut(CustomerBase):
    id: int
    class Config:
        orm_mode = True




ProjectDisplay.update_forward_refs()
TimeBlockDisplay.update_forward_refs()