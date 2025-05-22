from sqlmodel import SQLModel, create_engine

from app.config import settings

engine = create_engine(settings.db_url, echo=True)
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)