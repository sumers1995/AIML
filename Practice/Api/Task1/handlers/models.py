from pydantic import BaseModel, Field, EmailStr

class BaseUser(BaseModel):
    name: str = Field(max_length=30, min_length=3)
    email: EmailStr = Field()

class 
