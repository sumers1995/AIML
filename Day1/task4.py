from fastapi import FastAPI

app = FastAPI()

fake_items_db = [{"item_name": "Apple"}, {"item_name":"Orange"}, {"item_name": "Mango"},
                 {"item_name": "Apple"}, {"item_name":"Orange"}, {"item_name": "Mango"},
                 {"item_name": "Apple"}, {"item_name":"Orange"}, {"item_name": "Mango"},
                 {"item_name": "Apple"}, {"item_name":"Orange"}, {"item_name": "Mango"},
                 {"item_name": "Apple"}, {"item_name":"Orange"}, {"item_name": "Mango"},
                 {"item_name": "Apple"}, {"item_name":"Orange"}, {"item_name": "Mango"},
                 {"item_name": "Apple"}, {"item_name":"Orange"}, {"item_name": "Mango"},]

@app.get("/items/")
def read_item(skip: int = 0, limit: int=10):
    return fake_items_db[skip: skip+limit]

@app.get("/items/{item_id}")
def read_item(item_id: str, q: str | None = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}

@app.get("/search/{item_id}")
def return_search(item_id: int, query: str | None  = None, limit: int | None = None):
    return {"query":query,"limit":limit}