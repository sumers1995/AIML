from fastapi import FastAPI

app = FastAPI()

# conflict with param and endpoint
@app.get("/items/{num}")
def read_item(num: int):
    return {"square": num*num}

@app.get("/items/25")
def read_item():
    return {"square": "no square"}

# api with same endpoints
@app.get("/items/new/")
def return_new():
    return ['new1','new2']

@app.get("/items/new/")
def return_items():
    return ["item1","item2"]





