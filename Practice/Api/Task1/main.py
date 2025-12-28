from fastapi import FastAPI
from scalar_fastapi import get_scalar_api_reference

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Task 1 Initiated"}

@app.get("/scalar", include_in_schema=False)
def get():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title="Task 1"
    )