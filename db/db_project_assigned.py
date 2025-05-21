from db.models import DbProjectAssigned
from sqlalchemy.orm import Session
from schemas import ProjectAssignedCreate, ProjectAssignedDisplay
from typing import List
from datetime import datetime


def create_project_assigned(db: Session, project_assigned: ProjectAssignedCreate):
    new_project_assigned = DbProjectAssigned(
        user_id=project_assigned.user_id,
        project_id=project_assigned.project_id)
    
    db.add(new_project_assigned)
    db.commit()
    db.refresh(new_project_assigned)
    return new_project_assigned

def get_project_assigned_by_user(db: Session, user_id: int) -> List[ProjectAssignedDisplay]:
    project_assigned = db.query(DbProjectAssigned).filter(DbProjectAssigned.user_id == user_id).all()
    return project_assigned


