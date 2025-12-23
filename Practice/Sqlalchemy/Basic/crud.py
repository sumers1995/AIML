from models import User, engine
from sqlalchemy import select
from sqlalchemy.orm import sessionmaker
from typing import Optional

Session = sessionmaker(bind=engine)
session = Session()

def create_users():
    user = User(name="Sumer", age=30)
    user1 = User(name="Mantis", age=14)
    user2 = User(name="Jarvis", age=26)
    user3 = User(name="Noah", age=8)
    session.add(user)
    session.add_all([user1, user2, user3])
    session.commit()

def add_user(name: str, age: int):
    user = User(name=name, age=age)
    session.add(user)
    session.commit()
    return user

def get_all_users():
    stmt = select('*').select_from(User)
    result = session.execute(stmt).mappings()
    # first_user = result.fetchone()
    # n_users = result.fetchmany(2)
    # users = result.fetchall()
    users = result.fetchall()
    return users

def get_user(id: int):
    stmt = select(User).where(User.id == id)
    result = session.execute(stmt).mappings()
    user = result.first().User
    return user

def update_user(id: int, name: str):
    stmt = select(User).where(User.id == id)
    result = session.execute(stmt).mappings()
    user = result.first().User
    user.name = name
    session.commit()
    return user

def filter_by_age(age: int):
    stmt = select(User).where(User.age >= 10)
    result = session.execute(stmt).mappings()
    return result.fetchall()

def check_exists(id: Optional[int] = None, name: Optional[str] = None) -> bool:
    if id is not None and session.execute(select(User).where(User.id == id)).mappings().first() is not None:
        return True
    if name is not None and session.execute(select(User).where(User.name == name)).mappings().first() is not None:
        return True
    return False

# create_users()
# print(get_all_users())
print(get_user(3))
# print(update_user(3, "Jonny"))
# print(add_user("Ramesh", 37))
# print(check_exists(name="Sumer"))
# print(filter_by_age(30))