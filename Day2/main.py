from fastapi import FastAPI
from sqlalchemy import create_engine, Integer, String, Column, Boolean, select
from pydantic import BaseModel, field_validator, ValidationError, EmailStr
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class UserCreate(BaseModel):
    id: int
    password: str
    name: str
    email: str
    age: int
    flag: bool
    
    @field_validator('email')
    def check_email(cls, em):
        if not('@' in em and '.com' in em):
            raise ValueError('Invalid Email.')
        return em
    
    @field_validator('age')
    def check_age(cls, ag):
        if ag < 18:
            raise ValueError('Age should be greater than 18')
        return ag
    
    @field_validator('password')
    def check_password(cls, pwd):
        if len(pwd) < 8:
            raise ValueError('Length of the password should be atleast 8 chars')
        return pwd
    
    @field_validator('name')
    def check_name(cls, nam):
        if len(nam) <=0:
            raise ValueError('Enter name')
        return nam

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    password = Column(String)
    name = Column(String)
    email = Column(String)
    age = Column(Integer)
    flag = Column(Boolean)
    
engine = create_engine(url="postgresql://postgres:12345@localhost:5432/postgres")
Base.metadata.create_all(engine)
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = Session()
app = FastAPI()

@app.post("/users")
def create_user(id: int = 0, password: str = "", name: str = "", email: str = "", age: int = 0, flag: bool = False):
    try:
        new = UserCreate(id=id,password=password,name=name,email=email,age=age,flag=flag)
        new_user = User(id=new.id,password=new.password,name=new.name,email=new.email,age=new.age,flag=new.flag)
        session.add(new_user)
        session.commit()
        return new.id
    except ValidationError as e:
        return e.json()

@app.get("/users/{id}")
def get_user(id: int):
    # user = session.query(User).filter_by(id=id).first()
    user = session.execute(select(User).where(User.id==id))
    return user

@app.get("/users/all/")
def get_all_users():
    users = session.query(User).all()
    return users

@app.put("/users/{id}")
def update_password(id: int, password: str = ""):
    user = session.query(User).filter_by(id=id).first()
    user.password = password
    session.commit()
    return id
    
@app.delete("/users/{id}")
def delete_user(id: int):
    user = session.query(User).filter_by(id=id).first()
    user.flag = False
    session.commit()
    return id

