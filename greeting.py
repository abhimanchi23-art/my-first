
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to abhi"}

@app.get("/hello")
def greet(name: str):
    return {"message": "Hello " + name}
