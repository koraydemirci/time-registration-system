from db.models import DbProjects, DbCustomers, DbTimeBlock
from sqlalchemy.orm import Session
from schemas import ProjectCreate, TimeBlockCreate


def create_project(db: Session, request: ProjectCreate):
    new_project = DbProjects(**project.dict())
    #     name=request.name,
    #     description=request.description,
    #     start_date=request.start_date,
    #     end_date=request.end_date,
    #     budget=request.budget,
    #     customer_id=request.customer_id
    # )
    db.add(new_project)
    db.commit()
    db.refresh(new_project)
    return new_project


def get_projects(db: Session):
    return db.query(DbProjects).all()

def get_project_by_id(db: Session, project_id: int):
    return db.query(DbProject).filter(DbProjects.id == project_id).first()


# timeblock functions
def create_timeblock(db: Session, timeblock: TimeBlockCreate):
    new_tb = DbTimeBlock(**timeblock.dict())
    db.add(new_tb)
    db.commit()
    db.refresh(new_tb)
    return new_tb

def get_timeblocks_by_employee(db: Session, employee_id: int):
    return db.query(DbTimeBlock).filter(DbTimeBlock.employee_id == employee_id).all()

def get_timeblocks_by_project(db: Session, project_id: int):
    return db.query(DbTimeBlock).filter(DbTimeBlock.project_id == project_id).all()