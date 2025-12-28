from fastapi import FastAPI
from scalar_fastapi import get_scalar_api_reference
from handler import emp_router

from repo import create_db_table

app = FastAPI()
app.include_router(router=emp_router)
create_db_table()

@app.get("/")
def root():
    return {"message": "Task 4 initiated."}

@app.get("/scalar", include_in_schema=False)
def get_scalar_docs():
    return get_scalar_api_reference(openapi_url=app.openapi_url, title="Task 4")
