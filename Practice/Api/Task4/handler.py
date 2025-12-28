from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from repo import EmployeeServiceDep
from models import EmployeeCreate, EmployeeRead
from security import oauth2_scheme
from utils import decode_token

emp_router = APIRouter(prefix="/employee", tags=["Employee"])

@emp_router.post("/signup", response_model=EmployeeRead)
def emp_signup(emp: EmployeeCreate, service: EmployeeServiceDep):
    return service.add(emp)

@emp_router.post("/login")
def emp_login(request_form: Annotated[OAuth2PasswordRequestForm, Depends()],
              service: EmployeeServiceDep):
    return {"access_token": service.login(request_form.username, request_form.password),
            "type": "jwt"}

@emp_router.post("/all/")
def get_all(token: Annotated[str, Depends(oauth2_scheme)]):
    data = decode_token(token)
    if data is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Invalid access token")
    return {"detail": "Successfully Authenticated!"}