from sqlmodel import SQLModel, create_engine
# import os
# from dotenv import load_dotenv, find_dotenv

from app.config import settings


# load_dotenv()
# DATABASE_URL = os.environ.get("DB_LINK")

# ENVIRONMENT = os.environ.get("ENVIRONMENT")
# if ENVIRONMENT == "DEVELOPMENT":
#     DATABASE_URL = os.environ.get("DB_LINK")

print(settings.db_url)

engine = create_engine(settings.db_url, echo=True)
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)