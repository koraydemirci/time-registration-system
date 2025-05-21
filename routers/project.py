from fastapi import APIRouter, Depends
from schemas import ProjectCreate, ProjectDisplay
from sqlalchemy.orm import Session
from db.database import get_db
from db import db_project
from fastapi import HTTPException

router = APIRouter(prefix='/projects', tags=['Projects'])

# Create a new project
@router.post('/', response_model=ProjectDisplay)
def create_project(request: ProjectCreate, db: Session = Depends(get_db)):
    return db_project.create_project(db, request)

# Get all projects
@router.get('/', response_model=list[ProjectDisplay])
def get_projects(db: Session = Depends(get_db)):
    return db_project.get_projects(db)

# Get specific project by id
@router.get('/{id}', response_model=ProjectDisplay)
def get_project_by_id(id: int, db: Session = Depends(get_db)):
    project = db_project.get_project_by_id(db, id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    return project

