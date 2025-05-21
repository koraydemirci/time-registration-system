from fastapi import APIRouter, Depends
from schemas import TimeBlockCreate, TimeBlockDisplay
from sqlalchemy.orm import Session
from db.database import get_db
from db import db_timeblock
from fastapi import HTTPException

router = APIRouter(prefix='/timeblocks', tags=['TimeBlocks'])

# Create a new timeblock
@router.post('/', response_model=TimeBlockDisplay)
def create_timeblock(request: TimeBlockCreate, db: Session = Depends(get_db)):
    return db_timeblock.create_timeblock(db, request)

# Get all timeblocks by employee
@router.get('/employee/{employee_id}', response_model=list[TimeBlockDisplay])
def get_timeblocks_by_employee(employee_id: int, db: Session = Depends(get_db)):
    return db_timeblock.get_timeblocks_by_employee(db, employee_id)

# Get all timeblocks by project
@router.get('/project/{project_id}', response_model=list[TimeBlockDisplay])
def get_timeblocks_by_project(project_id: int, db: Session = Depends(get_db)):
    return db_timeblock.get_timeblocks_by_project(db, project_id)

