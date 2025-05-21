from fastapi import FastAPI
from routers import project, timeblock
from db import models
from db.database import engine


app = FastAPI()
app.include_router(project.router)
app.include_router(timeblock.router)

@app.get('/', summary="this is our home", description="this is home description",
 response_description="this is description")
def home_index():
    return{"message": "this is home page"}

models.Base.metadata.create_all(engine)