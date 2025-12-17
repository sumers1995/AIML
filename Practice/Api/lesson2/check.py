from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import select, create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

from pydantic import BaseModel
from typing import Optional, List

engine = create_engine("sqlite:///users.db", connect_args={"check_same_thread":False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = SessionLocal()
Base = declarative_base()

class User(Base):
    __tablename__ = "Users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    role = Column(String(100), nullable=False)
    
Base.metadata.create_all(engine)

select_user = session.execute(select(User).where(User.id == 1)).first()[0]
query_user = session.query(User).filter(User.id == 1).first()
print("Select: ", select_user)
print("Query: ", query_user)
print("Truth: ", select_user is query_user)