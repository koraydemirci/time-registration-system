from db.models import DbProjects
from sqlalchemy.orm import Session
from schemas import ProjectCreate
from typing import List
from datetime import datetime


def create_project(db: Session, request: ProjectCreate):
    # Check if the customer exists
    # Check if the employer exists
    new_project = DbProjects(
        name=request.name,
        description=request.description,
        start_date=request.start_date,
        end_date=request.end_date,
        budget=request.budget,
        status=request.status.value,
        hour_rate=request.hour_rate,
        customer_id=request.customer_id,
        employer_id=request.employer_id
    )
    db.add(new_project)
    db.commit()
    db.refresh(new_project)
    # Check if the project was created successfully
    if not new_project:
        db.rollback()
        raise Exception("Error creating project")
    
    # Automatically assign the customer to the project
    # project_assigned = DbProjectAssigned(
    #     project_id=new_project.id,
    #     user_id=request.customer_id
    # )
    return new_project


def get_projects(db: Session):
    return db.query(DbProjects).all()

def get_project_by_id(db: Session, project_id: int):
    return db.query(DbProjects).filter(DbProjects.id == project_id).first()

#assign employee to project