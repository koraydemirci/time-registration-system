from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.database import get_db
from pydantic import BaseModel, EmailStr
from db import db_authentication  
from fastapi.security import OAuth2PasswordRequestForm
from schemas import UserCreate, UserLogin

router = APIRouter(prefix='/auth',
    tags=['Authentication']
)

@router.post('/signup')
def signup(request: UserCreate, db: Session = Depends(get_db)):
    return db_authentication.signup(request, db, user_type=request.user_type)

@router.post('/login')
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    return db_authentication.login(request, db)
