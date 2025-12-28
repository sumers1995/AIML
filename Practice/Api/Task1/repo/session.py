from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlmodel import SQLModel
from config import DatabaseSettings

db_settings = DatabaseSettings()
engine = create_engine(
    url = db_settings.POSTGRES_URL,
)

Session = sessionmaker(bind=engine, expire_on_commit=False)

def get_session():
    with Session() as session:
        yield session

def create_db_tables():
    SQLModel.metadata.create_all(engine)

