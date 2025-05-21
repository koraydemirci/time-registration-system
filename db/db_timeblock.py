from db.models import  DbTimeBlock
from sqlalchemy.orm import Session
from schemas import TimeBlockCreate


# timeblock functions
def create_timeblock(db: Session, timeblock: TimeBlockCreate) -> DbTimeBlock:
    try:
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
    except Exception as e:
        db.rollback()
        raise HttpException(
            status_code=500,
            detail=f"Error creating timeblock: {str(e)}"
        )

def get_timeblocks_by_employee(db: Session, employee_id: int) -> list[DbTimeBlock]:
    try:
        return db.query(DbTimeBlock).filter(DbTimeBlock.employee_id == employee_id).all()
    except Exception as e:
        raise HttpException(
            status_code=500,
            detail=f"Error fetching timeblocks for employee {employee_id}: {str(e)}"
        )

def get_timeblocks_by_project(db: Session, project_id: int) -> list[DbTimeBlock]:
    try:
        return db.query(DbTimeBlock).filter(DbTimeBlock.project_id == project_id).all()
    except Exception as e:
        raise HttpException(
            status_code=500,
            detail=f"Error fetching timeblocks for project {project_id}: {str(e)}"
        )