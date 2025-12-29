from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, select
from config import db_settings
from models import Base, Employee, EmployeeCreate
from typing import Annotated
from fastapi import Depends, HTTPException, status
from argon2 import PasswordHasher

from utils import generate_token


engine = create_engine(url=db_settings.POSTGRES_URL)
Session = sessionmaker(bind=engine, expire_on_commit=False)
pH = PasswordHasher()

def get_session():
    with Session() as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]

class EmployeeService:
    def __init__(self, session: Session):
        self.session = session

    def add(self, employee: EmployeeCreate) -> Employee:
        emp = Employee(
            name=employee.name,
            email=employee.email,
            password_hash=pH.hash(employee.password),
        )
        self.session.add(emp)
        self.session.commit()
        self.session.refresh(emp)
        return emp
    
    def login(self, email, password) -> str:
        # first validate credentials
        result = self.session.execute(select(Employee).where(Employee.email == email))
        emp = result.scalar()

        if emp is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail="Email or Password is incorrect.")
        
        if not pH.verify(emp.password_hash, password):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                detail="password is incorrect")

        return generate_token(emp)
        

def create_db_table():
    Base.metadata.create_all(engine)

def get_employee_service(session: SessionDep):
    return EmployeeService(session)

EmployeeServiceDep = Annotated[EmployeeService, Depends(get_employee_service)]
