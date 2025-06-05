from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas import EmployeeCreate, EmployeeOut
from db.database import get_db
from Employee.crud_employee import Create_Employee , get_employee 
from Employee.model import Employee

router = APIRouter(
    prefix="/employee",
    tags=["Employees"]
)

@router.post("/", response_model=EmployeeOut)
def create(employee: EmployeeCreate, db: Session = Depends(get_db)):
    return Create_Employee(db, employee)

@router.get("/", response_model=list[EmployeeOut])
def read_all(db: Session = Depends(get_db)):
    return get_employee(db)

@router.get("/{employee_id}", response_model=EmployeeOut)
def read(employee_id: int, db: Session = Depends(get_db)):
    db_employee = get_employee(db, employee_id)
    if not db_employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    return db_employee