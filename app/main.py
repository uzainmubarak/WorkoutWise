from fastapi import FastAPI
from app.db import create_db_and_tables

app = FastAPI()
@app.on_event("startup")
def on_startup():
    create_db_and_tables()

# Your routes go here

@app.get("/")
def get_root():
    return {"message": "Hello World"}