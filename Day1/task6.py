from sqlalchemy import create_engine, Integer, String, Column
from sqlalchemy.ext.declarative import declarative_base

user = "postgres"
password = "12345"
host = "localhost"
port = 5432
database = "postgres"

def get_connection():
    return create_engine(url="postgresql://{0}:{1}@{2}:{3}/{4}".format(user, password, host, port, database))

engine = get_connection()
# print(f"connection to the {host} for user {user} created successfully.")

Base = declarative_base()

class Employee(Base):
    __tablename__ = 'employees'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    salary = Column(Integer)
    
# print("Table Defined.")

# Base.metadata.create_all(engine)

# print("All good")

from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

# new_emp = Employee(id=10331152, name="Sumer Sadawarti", salary=50000)
# new_emp1 = Employee(id=10338774, name="Prabhakar Gangwar", salary=48000)
# session.add(new_emp)
# session.add(new_emp1)
# session.commit()
# print("Data inserted successfully")

def print_all():
    employees = session.query(Employee).all()
    for employee in employees:
        print(f"ID: {employee.id}, Name: {employee.name}, Salary: {employee.salary}")

print_all()

def update(salary):
    update = session.query(Employee).filter_by(id=10331152).first()
    update.salary = 60000
    session.commit()
    print("Updated.")

print_all()
    