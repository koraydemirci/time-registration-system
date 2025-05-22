from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas import CustomerCreate, CustomerUpdate, CustomerOut
from db.database import get_db
from db import crud_customer

router = APIRouter(
    prefix="/customers",
    tags=["Customers"]
)

@router.post("/", response_model=CustomerOut)
def create(customer: CustomerCreate, db: Session = Depends(get_db)):
    return crud_customer.create_customer(db, customer)

@router.get("/", response_model=list[CustomerOut])
def read_all(db: Session = Depends(get_db)):
    return crud_customer.get_customers(db)

@router.get("/{customer_id}", response_model=CustomerOut)
def read(customer_id: int, db: Session = Depends(get_db)):
    db_customer = crud_customer.get_customer(db, customer_id)
    if not db_customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    return db_customer

@router.put("/{customer_id}", response_model=CustomerOut)
def update(customer_id: int, customer: CustomerUpdate, db: Session = Depends(get_db)):
    updated = crud_customer.update_customer(db, customer_id, customer)
    if not updated:
        raise HTTPException(status_code=404, detail="Customer not found")
    return updated

@router.delete("/{customer_id}")
def delete(customer_id: int, db: Session = Depends(get_db)):
    deleted = crud_customer.delete_customer(db, customer_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Customer not found")
    return {"message": "Customer deleted"}
