from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import ollama

app = FastAPI()
model = 'llama3.2:1b'

class DataInBody(BaseModel):
    prompt: str
    format: object
    options: object

@app.get("/")
def root():
    return {"message": "Ollama with FastAPI!"}

# @app.get("/ollama/{prompt}")
# def ollama_response(prompt: str):
#     try:
#         response = ollama.chat(model=model, messages=[
#             {
#             'role':'user',
#             'content': prompt,
#             },
#         ])
#         return {"response": response['message']['content']}
#     except Exception as e:
#         return {"error": str(e)}
    
# @app.get("/ollama_generate/{prompt}")
# def ollama_generate(prompt:str):
#     try:
#         response = ollama.generate(model=model, prompt=prompt)
#         return {"response": response['response']}
#     except Exception as e:
#         return {"error": str(e)}
    
@app.post("/ollama_generate/")
def ollama_generate(data: DataInBody):
    try:
        response = ollama.generate(model=model, prompt=data.prompt, stream=False)
        return {"response": response['response']}
    except Exception as e:
        return {"error": str(e)}
    
class Message(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    messages: list[Message]
    
@app.post("/ollama_chat/")
def ollama_response(chat_request: ChatRequest):
    try:
        return {"response": chat_request.messages[0]}
        # message_dict = []
        # for message in chat_request.messages:
        #     message_dict.append(message)
        # response = ollama.chat(model=model, messages=message_dict)
        # return {"response": response['response']}
    except Exception as e:
        return {"error": str(e)}