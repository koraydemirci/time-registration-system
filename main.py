from fastapi import FastAPI
from Project import project
# from TimeBlock import timeblock
from db import models
from db.database import engine
from routers.authentication import router as auth_router

#from Customer.customer import router as customer_router
from Employer import employer
from Employee import employee
from Customer import customer




app = FastAPI()
app.include_router(auth_router)
app.include_router(customer.router)
app.include_router(employer.router)
app.include_router(employee.router)
app.include_router(project.router)

# app.include_router(timeblock.router)




@app.get('/', summary="this is our home", description="this is home description",
 response_description="this is description")
def home_index():
    return {"message": "this is home page"}

models.Base.metadata.create_all(engine)