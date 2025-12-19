from fastapi import FastAPI
import ollama

app = FastAPI()
model = 'gemma3:270m'

@app.get("/")
def root():
    return {"message": "Ollama with FastAPI!"}

@app.get("/ollama/{prompt}")
def ollama_response(prompt: str):
    try:
        response = ollama.chat(model=model, messages=[
            {
            'role':'user',
            'content': prompt,
            },
        ])
        return {"response": response['message']['content']}
    except Exception as e:
        return {"error": str(e)}
    
@app.get("/ollama_generate/{prompt}")
def ollama_generate(prompt:str):
    try:
        response = ollama.generate(model=model, prompt=prompt)
        return {"response": response['response']}
    except Exception as e:
        return {"error": str(e)}