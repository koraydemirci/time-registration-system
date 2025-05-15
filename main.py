from fastapi import FastAPI
from auth.routes import router as auth_router

app = FastAPI()

# Include the authentication routes under the /auth prefix
app.include_router(auth_router, prefix="/auth")

@app.get("/")
async def root():
    return {"message": "Hello, FastAPI!"}