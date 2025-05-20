from fastapi import APIRouter, Depends
from schemas import ProjectCreate, ProjectDisplay
from sqlalchemy.orm import Session
from db.database import get_db
from db import db_project

router = APIRouter(prefix='/timeblocks', tags=['TimeBlocks'])

# Create a new timeblock
@router.post('/new_timeblock', response_model=ProjectDisplay)
def create_timeblock(request: ProjectCreate, db: Session = Depends(get_db)):
    return db_project.create_timeblock(db, request)

# Get all timeblocks by employee
@router.get('/employee/{employee_id}', response_model=list[ProjectDisplay])
def get_timeblocks_by_employee(employee_id: int, db: Session = Depends(get_db)):
    return db_project.get_timeblocks_by_employee(db, employee_id)

# Get all timeblocks by project
@router.get('/project/{project_id}', response_model=list[ProjectDisplay])
def get_timeblocks_by_project(project_id: int, db: Session = Depends(get_db)):
    return db_project.get_timeblocks_by_project(db, project_id)

