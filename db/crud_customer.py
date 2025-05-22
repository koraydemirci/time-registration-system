from sqlalchemy.orm import Session
from db.models import Customer
from schemas import CustomerCreate, CustomerUpdate

def create_customer(db: Session, customer: CustomerCreate):
    db_customer = Customer(name=customer.name, email=customer.email)
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    return db_customer

def get_customers(db: Session):
    return db.query(Customer).all()

def get_customer(db: Session, customer_id: int):
    return db.query(Customer).filter(Customer.id == customer_id).first()

def update_customer(db: Session, customer_id: int, customer_data: CustomerUpdate):
    db_customer = db.query(Customer).filter(Customer.id == customer_id).first()
    if db_customer:
        db_customer.name = customer_data.name
        db_customer.email = customer_data.email
        db.commit()
        db.refresh(db_customer)
    return db_customer

def delete_customer(db: Session, customer_id: int):
    db_customer = db.query(Customer).filter(Customer.id == customer_id).first()
    if db_customer:
        db.delete(db_customer)
        db.commit()
    return db_customer
