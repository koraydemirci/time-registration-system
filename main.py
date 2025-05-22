from fastapi import FastAPI
from routers import project, timeblock
from db import models
from db.database import engine
from auth.authentication import router as auth_router
from routers import project, timeblock
from routers.customer import router as customer_router



app = FastAPI()
app.include_router(project.router)
app.include_router(timeblock.router)
app.include_router(auth_router)
app.include_router(customer_router)

@app.get('/', summary="this is our home", description="this is home description",
 response_description="this is description")
def home_index():
    return{"message": "this is home page"}

models.Base.metadata.create_all(engine)