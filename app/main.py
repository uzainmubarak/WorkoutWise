from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.db import create_db_and_tables

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup code (previously in @app.on_event("startup"))
    create_db_and_tables()
    print("Application startup complete")
    
    yield  # This is where the application runs
    
    # Shutdown code (previously in @app.on_event("shutdown"))
    print("Application shutdown complete")

app = FastAPI(lifespan=lifespan)

# Your routes go here

@app.get("/")
def get_root():
    return {"message": "Hello World"}