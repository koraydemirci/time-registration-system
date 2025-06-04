from fastapi import APIRouter, Depends, HTTPException
from schemas import TimeBlockCreate, TimeBlockDisplay
from sqlalchemy.orm import Session
from db.database import get_db
from TimeBlock.db_timeblock import (create_timeblock as db_create_timeblock,
    get_timeblocks_by_employee as db_get_timeblocks_by_employee, get_timeblocks_by_project as db_get_timeblocks_by_project , update_timeblock as put_update_timeblock)


router = APIRouter(prefix='/timeblocks', tags=['TimeBlocks'])


@router.post('/', response_model=TimeBlockDisplay)
def create_timeblock(request: TimeBlockCreate, db: Session = Depends(get_db)):
    return db_create_timeblock(db, request)

@router.get('/employee/{employee_id}', response_model=list[TimeBlockDisplay])
def get_timeblocks_by_employee(employee_id: int, db: Session = Depends(get_db)):
    return db_get_timeblocks_by_employee(db, employee_id)

@router.get('/project/{project_id}', response_model=list[TimeBlockDisplay])
def get_timeblocks_by_project(project_id: int, db: Session = Depends(get_db)):
    return db_get_timeblocks_by_project(db, project_id)

@router.put('/{timeblock_id}', response_model=TimeBlockDisplay)
def update_timeblock(timeblock_id: int, request: TimeBlockCreate, db: Session = Depends(get_db)):
    tb = put_update_timeblock(db, timeblock_id, request)
    if not tb:
        raise HTTPException(status_code=404, detail="TimeBlock not found")
    return tb