from fastapi import FastAPI

app = FastAPI()

in_memory_db = {}

@app.post("/add/{item}")
def add_item(item):
    in_memory_db[len(in_memory_db)+1] = item
    return len(in_memory_db)

@app.get("/all/")
def get_all():
    return in_memory_db

