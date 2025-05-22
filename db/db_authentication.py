from fastapi import HTTPException, status
from auth.hash import Hash
from db import models
from auth import oauth2

def signup(request, db, user_type="customer"):
    user = db.query(models.DbUser).filter(models.DbUser.email == request.email).first()
    if user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already exists")
    hashed_password = Hash.bcrypt(request.password)
    new_user = models.DbUser(
        email=request.email,
        password=hashed_password,
        type=user_type,  # parameterized
        name=request.name
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message": "User created successfully", "user_id": new_user.id}

def login(request, db):
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