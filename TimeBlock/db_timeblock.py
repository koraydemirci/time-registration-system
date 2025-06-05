from db.database import get_db
from TimeBlock.model import DbTimeBlock
from sqlalchemy.orm import Session
from schemas import TimeBlockCreate, TimeBlockDisplay

def create_timeblock(db: Session, request):
    new_tb = DbTimeBlock(
        start_date=request.start_date,
        end_date=request.end_date,
        note=request.note,
        hours=request.hours,
        project_id=request.project_id,
        employee_id=request.employee_id
    )
    db.add(new_tb)
    db.commit()
    db.refresh(new_tb)
    return new_tb

def get_timeblocks_by_employee(db: Session, employee_id):
    return db.query(DbTimeBlock).filter(DbTimeBlock.employee_id == employee_id).all()

def get_timeblocks_by_project(db: Session, project_id):
    return db.query(DbTimeBlock).filter(DbTimeBlock.project_id == project_id).all()

def update_timeblock(db: Session, timeblock_id, request):
    tb = db.query(DbTimeBlock).filter(DbTimeBlock.id == timeblock_id).first()
    if not tb:
        return None
    tb.start_date = request.start_date
    tb.end_date = request.end_date
    tb.note = request.note
    tb.project_id = request.project_id
    tb.employee_id = request.employee_id
    db.commit()
    db.refresh(tb)
    return tb