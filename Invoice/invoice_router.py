from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.database import get_db
import Invoice.model
import Invoice.schema

router = APIRouter(
    prefix="/invoices",
    tags=["invoices"]
)

# Create
@router.post("/", response_model=Invoice.schema.InvoiceOut)
def create_invoice(invoice: Invoice.schema.InvoiceCreate, db: Session = Depends(get_db)):
    db_invoice = Invoice.model.Invoice(**invoice.dict())
    db.add(db_invoice)
    db.commit()
    db.refresh(db_invoice)
    return db_invoice

# Read all
@router.get("/", response_model=list[Invoice.schema.InvoiceOut])
def get_invoices(db: Session = Depends(get_db)):
    return db.query(Invoice.model.Invoice).all()

# Read one
@router.get("/{invoice_id}", response_model=Invoice.schema.InvoiceOut)
def get_invoice(invoice_id: int, db: Session = Depends(get_db)):
    invoice = db.query(Invoice.model.Invoice).filter(Invoice.model.Invoice.id == invoice_id).first()
    if not invoice:
        raise HTTPException(status_code=404, detail="Invoice not found")
    return invoice

# Update
@router.put("/{invoice_id}", response_model=Invoice.schema.InvoiceOut)
def update_invoice(invoice_id: int, updated: Invoice.schema.InvoiceUpdate, db: Session = Depends(get_db)):
    invoice = db.query(Invoice.model.Invoice).filter(Invoice.model.Invoice.id == invoice_id).first()
    if not invoice:
        raise HTTPException(status_code=404, detail="Invoice not found")
    for key, value in updated.dict().items():
        setattr(invoice, key, value)
    db.commit()
    db.refresh(invoice)
    return invoice

# Delete
@router.delete("/{invoice_id}")
def delete_invoice(invoice_id: int, db: Session = Depends(get_db)):
    invoice = db.query(Invoice.model.Invoice).filter(Invoice.model.Invoice.id == invoice_id).first()
    if not invoice:
        raise HTTPException(status_code=404, detail="Invoice not found")
    db.delete(invoice)
    db.commit()
    return {"message": "Invoice deleted"}
