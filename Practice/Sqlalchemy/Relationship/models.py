from sqlalchemy import Column, Integer, String, create_engine, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship, Mapped, mapped_column

dialect = "postgresql"
driver = ""
user = "postgres"
pwd = "12345"
host = "localhost"
port = "5432"
db_name = "relationship_db"

engine = create_engine(f"{dialect}+{driver}://{user}:{pwd}@{host}:{port}/{db_name}")
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

class BaseModel(Base):
    __abstract__ = True
    __allow_unmapped__ = True
    id = Column(Integer, primary_key=True)

class Address(BaseModel):
    __tablename__ = "addresses"
    city = Column(String)
    state = Column(String)
    zip_code = Column(Integer)
    # user_id = Column(ForeignKey("users.id"))
    # for mapped method
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    # user = relationship("User", back_populates="addresses")
    # for mapped method
    user: Mapped["User"] = relationship(back_populates="addresses")
    # backward relationship access
    # if User has many addresses then each address belongs to a User
    # back_populates handles synchonization automatically

    def __repr__(self):
        return f"<Address(id={self.id}, city='{self.city}')"

class User(BaseModel):
    __tablename__ = "users"
    name = Column(String)
    age = Column(Integer)
    # addresses = relationship(Address)
    # for mapped method
    addresses: Mapped[list["Address"]] = relationship()

    def __repr__(self):
        return f"User(id={self.id}, username='{self.name}')"

Base.metadata.create_all(engine)