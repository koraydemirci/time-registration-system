from sqlalchemy.orm import Session
from Employer.model import Employer 
from schemas import  EmployerCreate, EmployerOut

def create_employer(db: Session, employer: EmployerCreate):
    db_employer = Employer(
        name=employer.name, 
        email=employer.email ,
        password = None
          )
    db.add(db_employer)
    db.commit()
    db.refresh(db_employer)
    return db_employer

def get_employers(db: Session):
    return db.query(Employer).all()

def get_employer(db: Session, employer_id: int):
    return db.query(Employer).filter(Employer.id == employer_id).first()