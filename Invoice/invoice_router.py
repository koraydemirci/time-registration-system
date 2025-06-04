from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.database import get_db
from Invoice.schema import InvoiceCreate, InvoiceUpdate, InvoiceOut
from Invoice.crud_invoice import create_invoice, get_invoice, get_all_invoices, update_invoice, delete_invoice


router = APIRouter(
    prefix="/invoices",
    tags=["Invoices"]
)

@router.post("/", response_model=InvoiceOut)
def create(invoice: InvoiceCreate, db: Session = Depends(get_db)):
    return create_invoice(db, invoice)

@router.get("/", response_model=list[InvoiceOut])
def read_all(db: Session = Depends(get_db)):
    return get_all_invoices(db)

@router.get("/{invoice_id}", response_model=InvoiceOut)
def read(invoice_id: int, db: Session = Depends(get_db)):
    invoice = get_invoice(db, invoice_id)
    if not invoice:
        raise HTTPException(status_code=404, detail="Invoice not found")
    return invoice

@router.put("/{invoice_id}", response_model=InvoiceOut)
def update(invoice_id: int, invoice: InvoiceUpdate, db: Session = Depends(get_db)):
    updated = update_invoice(db, invoice_id, invoice)
    if not updated:
        raise HTTPException(status_code=404, detail="Invoice not found")
    return updated

@router.delete("/{invoice_id}")
def delete(invoice_id: int, db: Session = Depends(get_db)):
    deleted = delete_invoice(db, invoice_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Invoice not found")
    return {"message": "Invoice deleted"}
