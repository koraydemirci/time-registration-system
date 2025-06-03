from db.models import DbProjects, Customer
from Employer.model import Employer
from sqlalchemy.orm import Session
from schemas import ProjectCreate
from typing import List
from datetime import datetime
from fastapi import HTTPException


def create_project(db: Session, request: ProjectCreate, employer_id: int):
    # Check if the employer exists
    employer = db.query(Employer).filter(Employer.id == employer_id).first()
    if not employer:
        raise HTTPException(status_code=403, detail="Employer not found")
    # Check if the customer exists
    customer = db.query(Customer).filter(Customer.id == request.customer_id).first()
    if not customer:
        raise HTTPException(status_code=422, detail="Customer ID is invalid or does not exist")
    
    new_project = DbProjects(
        name=request.name,
        description=request.description,
        start_date=request.start_date,
        end_date=request.end_date,
        budget=request.budget,
        status=request.status.value,
        hour_rate=request.hour_rate,
        customer_id=request.customer_id,
        employer_id=employer_id
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

def update_project(db: Session, project_id: int, request: ProjectCreate):
    project = db.query(DbProjects).filter(DbProjects.id == project_id).first()
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    for field, value in request.dict().items():
        setattr(project, field, value)
    db.commit()
    db.refresh(project)
    return project

def delete_project(db: Session, project_id: int, employer_id: int):
    employer = db.query(Employer).filter(Employer.id == employer_id).first()
    if not employer:
        raise HTTPException(status_code=403, detail="Employer not found")
    project = db.query(DbProjects).filter(DbProjects.id == project_id).first()
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    db.delete(project)
    db.commit()
    return {"detail": "Project deleted"}
#assign employee to project