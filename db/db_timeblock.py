from db.models import  DbTimeBlock
from sqlalchemy.orm import Session
from schemas import TimeBlockCreate


# timeblock functions
def create_timeblock(db: Session, timeblock: TimeBlockCreate):
    new_tb = DbTimeBlock(
        start_date=timeblock.start_date,
        end_date=timeblock.end_date,
        note=timeblock.note,
        project_id=timeblock.project_id,
        employee_id=timeblock.employee_id
    )
    db.add(new_tb)
    db.commit()
    db.refresh(new_tb)
    return new_tb

def get_timeblocks_by_employee(db: Session, employee_id: int):
    return db.query(DbTimeBlock).filter(DbTimeBlock.employee_id == employee_id).all()

def get_timeblocks_by_project(db: Session, project_id: int):
    return db.query(DbTimeBlock).filter(DbTimeBlock.project_id == project_id).all()