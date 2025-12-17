from fastapi import FastAPI
import random

from sqlalchemy import create_engine, Integer, String, Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

user = "postgres"
password = "12345"
host = "localhost"
port = 5432
database = "postgres"

engine = create_engine(url="postgresql://{0}:{1}@{2}:{3}/{4}".format(user, password, host, port, database))

Base = declarative_base()
class Item(Base):
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

app = FastAPI()

@app.post("/add/{item}")
def add_item(item):
    i = random.randint(1,1000)
    session.add(Item(id=i,name=item))
    session.commit()
    return i

@app.get("/all/")
def get_all():
    items = session.query(Item).all()
    return items


