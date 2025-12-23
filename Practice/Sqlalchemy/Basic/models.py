from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base

dialect = "postgresql"
user = "postgres"
pwd = "12345"
host = "localhost"
port = "5432"
db_name = "postgres"

engine = create_engine(f"{dialect}://{user}:{pwd}@{host}:{port}/{db_name}")
Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

Base.metadata.create_all(engine) 