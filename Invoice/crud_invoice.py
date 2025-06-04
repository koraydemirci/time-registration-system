from sqlalchemy.orm import Session
from Invoice.model import Invoice
from Invoice.schema import InvoiceCreate, InvoiceUpdate

def create_invoice(db: Session, invoice: InvoiceCreate):
    db_invoice = Invoice(**invoice.dict())
    db.add(db_invoice)
    db.commit()
    db.refresh(db_invoice)
    return db_invoice

def get_invoice(db: Session, invoice_id: int):
    return db.query(Invoice).filter(Invoice.id == invoice_id).first()

def get_all_invoices(db: Session):
    return db.query(Invoice).all()

def update_invoice(db: Session, invoice_id: int, invoice_data: InvoiceUpdate):
    db_invoice = db.query(Invoice).filter(Invoice.id == invoice_id).first()
    if db_invoice:
        for key, value in invoice_data.dict(exclude_unset=True).items():
            setattr(db_invoice, key, value)
        db.commit()
        db.refresh(db_invoice)
    return db_invoice

def delete_invoice(db: Session, invoice_id: int):
    db_invoice = db.query(Invoice).filter(Invoice.id == invoice_id).first()
    if db_invoice:
        db.delete(db_invoice)
        db.commit()
    return db_invoice
