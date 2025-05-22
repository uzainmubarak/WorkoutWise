from sqlmodel import SQLModel, create_engine
import os
from dotenv import load_dotenv
load_dotenv(".env.local")

DATABASE_URL = os.environ.get("DB_LINK")

# DB_USER: str = "postgres"
# DB_PASSWORD: str = "12345678"
# DB_HOST: str = "localhost"
# DB_NAME: str = "workoutwise"
print(DATABASE_URL)

engine = create_engine(DATABASE_URL, echo=True)
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)