from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from typing import Optional
from datetime import datetime, timedelta
from jose import jwt, JWTError
from sqlalchemy.orm import Session
from db.database import get_db
from db import models
from Employer.model import Employer


oauth2_schema = OAuth2PasswordBearer(tokenUrl="/auth/login")

SECRET_KEY = '2d34ce59a41ce49d3d9e6b2d886b127c7db7b06e6021ee596f4e3c3555ddabb1'
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def get_current_user(token: str = Depends(oauth2_schema), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail='Could not validate credentials',
        headers={"WWW-Authenticate": "Bearer"}
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = db.query(models.DbUser).filter(models.DbUser.email == email).first()
    if user is None:
        raise credentials_exception
    # Determine user type
    if db.query(models.Employer).filter(models.Employer.id == user.id).first():
        user.user_type = "employer"
    elif db.query(models.Employee).filter(models.Employee.id == user.id).first():
        user.user_type = "employee"
    elif db.query(models.Customer).filter(models.Customer.id == user.id).first():
        user.user_type = "customer"
    else:
        user.user_type = None
    return user
