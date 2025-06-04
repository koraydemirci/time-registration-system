
from Project.model import DbProjects, DbProjectEmployee
from Customer.model import Customer
from Employer.model import Employer
from Employee.model import Employee
from sqlalchemy.orm import Session
from schemas import ProjectCreate
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
def assign_employee_to_project(
    db: Session,
    project_id: int,
    employee_id: int,
    employer_id: int
):
    # Check if the employer exists
    employer = db.query(Employer).filter(Employer.id == employer_id).first()
    if not employer:
        raise HTTPException(status_code=403, detail="Employer not found")
    
    # Check if the project exists
    project = db.query(DbProjects).filter(DbProjects.id == project_id).first()
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    
    # Check if the employee exists
    employee = db.query(Employee).filter(Employee.id == employee_id).first()
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")
        
    if not any(link.employee_id == employee_id for link in project.employee_links):
        project.employee_links.append(DbProjectEmployee(employee_id=employee_id))
        db.commit()
        db.refresh(project)
        return {"detail": "Employee assigned to project successfully"}
    else:
        return {"detail": "Employee already assigned to project"}