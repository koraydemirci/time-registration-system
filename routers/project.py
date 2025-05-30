from fastapi import APIRouter, Depends, Body
from schemas import ProjectCreate, ProjectDisplay, UserBase
from sqlalchemy.orm import Session
from db.database import get_db
from db import db_project
from fastapi import HTTPException
from auth.oauth2 import oauth2_schema, get_current_user

router = APIRouter(prefix='/projects', tags=['Projects'])

# Create a new project
@router.post('/', response_model=ProjectDisplay)
def create_project(request: ProjectCreate, db: Session = Depends(get_db),  current_user: UserBase = Depends(get_current_user)):
    return db_project.create_project(db, request, current_user.id)

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


@router.put("/{project_id}", response_model=ProjectDisplay)
def update_project(project_id: int, request: ProjectCreate, db: Session = Depends(get_db),  current_user: UserBase = Depends(get_current_user)):
    return db_project.update_project(db, project_id, request, current_user.id)

@router.delete("/{project_id}")
def delete_project(project_id: int, db: Session = Depends(get_db), current_user: UserBase = Depends(get_current_user)):
    return db_project.delete_project(db, project_id, current_user.id)