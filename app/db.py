from sqlmodel import create_engine

DB_USER: str = "postgres"
DB_PASSWORD: str = "12345678"
DB_HOST: str = "localhost"
DB_NAME: str = "workoutwise"

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"

engine = create_engine(DATABASE_URL, echo=true)
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session