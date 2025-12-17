from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

user = "postgres"
password = "12345"
host = "localhost"
port = 5432
database = "postgres"

def get_connection():
    return create_engine(url="postgresql://{0}:{1}@{2}:{3}/{4}".format(user, password, host, port, database))

engine = get_connection()
print(f"connection to the {host} for user {user} created successfully.")