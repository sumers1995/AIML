from fastapi import FastAPI

app = FastAPI()

@app.get("/items/foo")
async def root():
    return {"message": "Hello World",
            "New_message":{
                "message1":"Sumer",
                "message2":"Sadawarti"
            }}