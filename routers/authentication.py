from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.database import get_db
from pydantic import BaseModel, EmailStr
from db import db_authentication  

router = APIRouter(
    tags=['authentication']
)

class UserSignup(BaseModel):
    email: EmailStr
    password: str
    name: str

@router.post('/signup')
def signup(request: UserSignup, db: Session = Depends(get_db)):
    return db_authentication.signup(request, db)

class UserLogin(BaseModel):
    email: EmailStr
    password: str

@router.post('/login')
def login(request: UserLogin, db: Session = Depends(get_db)):
    return db_authentication.login(request, db)