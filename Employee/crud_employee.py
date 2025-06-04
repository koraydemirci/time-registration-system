from sqlalchemy.orm import Session
from Employee.model import Employee
from schemas import  EmployeeCreate, EmployeeOut

def Create_Employee(db: Session , employee :EmployeeCreate):
    db_employee = Employee(
        name = employee.name , 
        email = employee.email
    )
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee

def get_employee(db:Session, employee_id: int = None) -> list[EmployeeOut]:
    if employee_id:
        return db.query(Employee).filter(Employee.id == employee_id).first()
    else:
        return "message: Please provide employee_id"