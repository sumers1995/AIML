from fastapi import FastAPI, HTTPException, status, Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

users = {
    1: {
        "name":"Sumer",
        "website":"mywebsite.com",
        "age":30,
        "role":"developer"
    },
    2: {
        "name":"Prabhakar",
        "website":"www.prabhkar.com",
        "age":28,
        "role":"Accounts"
    }
}

# define pydantic base model
class User(BaseModel):
    name:str
    website:str
    age:int
    role:str
    
# will be used for making changes in user
class UpdateUser(BaseModel):
    name: Optional[str] = None
    website: Optional[str] = None
    age: Optional[int] = None
    role: Optional[str] = None

@app.get("/")
def root():
    return {"message":"Welcome"}

@app.get("/users/")
def get_all_users():
    return users

@app.get("/users/{user_id}")
def get_user(user_id: int = Path(..., description="Id you want to get", gt=0,lt=100)):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found!")
    return users[user_id]

# create a user
@app.post("/users/{user_id}", status_code=status.HTTP_201_CREATED)
def create_user(user_id: int, user:User):
    if user_id in users:
        raise HTTPException(status_code=400, detail="User already exists")
    users[user_id] = user.dict()
    return user

# update a user
@app.put("/users/{user_id}", status_code=status.HTTP_202_ACCEPTED)
def update_user(user_id: int, user:UpdateUser):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User is not here")
    current_user = users[user_id]
    if user.name is not None:
        current_user["name"] = user.name
    if user.website is not None:
        current_user["website"] = user.website
    if user.age is not None:
        current_user["age"] = user.age
    if user.role is not None:
        current_user["role"] = user.role
        
    return current_user

# delete a user
@app.delete("/users/{user_id}")
def delete_user(user_id:int):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User is not here")
    deleted_user = users.pop(user_id)
    return {"message":"User has been deleted", "deleted_user": deleted_user}

@app.get("/users/search/")
def search_by_name(name: Optional[str] = None):
    if not name:
        return {"message":"Name parameter is required"}
    for user in users.values():
        if user["name"] == name:
            return user
    raise HTTPException(status_code=404, detail="user not found")