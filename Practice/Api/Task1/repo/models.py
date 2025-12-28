from typing import Optional
from pydantic import EmailStr
from sqlmodel import SQLModel, Field

class User(SQLModel, table=True):
    __tablename__ = "users"

    id: int = Field(default=10331152, primary_key=True)
    name: str = Field(nullable=False, min_length=3)
    email: EmailStr = Field(unique=True)
    password: str = Field(nullable=False)
    age: int = Field(nullable=False, ge=18)
