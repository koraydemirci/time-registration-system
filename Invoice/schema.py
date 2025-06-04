from pydantic import BaseModel
from datetime import date
from typing import Optional

class InvoiceBase(BaseModel):
    customer_id: int
    project_id: int
    amount: float
    issue_date: date
    due_date: date
    status: str

class InvoiceCreate(InvoiceBase):
    pass

class InvoiceUpdate(BaseModel):
    amount: Optional[float]
    issue_date: Optional[date]
    due_date: Optional[date]
    status: Optional[str]

class InvoiceOut(InvoiceBase):
    id: int

    class Config:
        orm_mode = True
