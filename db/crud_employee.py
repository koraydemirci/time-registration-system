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
def get_employee(db:Session):
    return db.query(Employee).all()
