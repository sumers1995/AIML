from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base, validates
from email_validator import validate_email, EmailNotValidError
from pydantic import BaseModel, EmailStr

# ------------------------pydantic models----------------------
class BaseEmployee(BaseModel):
    name: str
    email: EmailStr

class EmployeeRead(BaseEmployee):
    pass

class EmployeeCreate(BaseEmployee):
    password: str

# -------------------------- DB tables ---------------------------
Base = declarative_base()

class Employee(Base):
    __tablename__ = "employees"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    email = Column(String(255), unique=True, nullable=False)
    password_hash = Column(String)

    @validates("email")
    def validate_email(self, key, value):
        try:
            valid = validate_email(value)
            return valid.email
        except EmailNotValidError as e:
            raise ValueError(f"Invalid Email {e}")


    