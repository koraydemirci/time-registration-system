from pydantic import BaseModel

class InvoiceBase(BaseModel):
    customer: str
    amount: float
    description: str

class InvoiceCreate(InvoiceBase):
    pass

class InvoiceUpdate(InvoiceBase):
    pass

class InvoiceOut(InvoiceBase):
    id: int

    class Config:
        orm_mode = True
