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