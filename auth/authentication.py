from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from db.hash import Hash
from db import models
from db.database import get_db
from auth import oauth2
from pydantic import BaseModel, EmailStr
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column

router = APIRouter(
    tags=['authentication']
)

class UserSignup(BaseModel):
    email: EmailStr
    password: str
    name: str

@router.post('/signup')
def signup(request: UserSignup, db: Session = Depends(get_db)):
    user = db.query(models.DbUser).filter(models.DbUser.email == request.email).first()
    if user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already exists")
    hashed_password = Hash.bcrypt(request.password)
    new_user = models.DbUser(
        email=request.email,
        password=hashed_password,
        type="customer",
        name=request.name
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message": "User created successfully", "user_id": new_user.id}

class UserLogin(BaseModel):
    email: EmailStr
    password: str

@router.post('/login')
def login(request: UserLogin, db: Session = Depends(get_db)):
    user = db.query(models.DbUser).filter(models.DbUser.email == request.email).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    if not Hash.verify(user.password, request.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect password")
    access_token = oauth2.create_access_token(data={'sub': user.email})
    return {
        'access_token': access_token,
        'token_type': 'bearer',
        'user_id': user.id,
        'email': user.email
    }