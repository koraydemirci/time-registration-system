from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas import EmployerCreate,EmployerOut
from db.database import get_db
from db import crud_employer

router = APIRouter(
    prefix="/employer",
    tags=["Employers"]
)

@router.post("/", response_model=EmployerOut)
def create(employer: EmployerCreate, db: Session = Depends(get_db)):
    return crud_employer.create_employer(db, employer)

@router.get("/", response_model=list[EmployerOut])
def read_all(db: Session = Depends(get_db)):
    return crud_employer.get_employers(db)

@router.get("/{employer_id}", response_model=EmployerOut)
def read(employer_id: int, db: Session = Depends(get_db)):
    db_employer = crud_employer.get_employer(db, employer_id)
    if not db_employer:
        raise HTTPException(status_code=404, detail="Employer not found")
    return db_employer