from fastapi import FastAPI

app = FastAPI()

students = []

@app.get("/")
def home():
    return {"message": "Welcome to my abhi"}


@app.post("/students")
def add_student(name: str, age: int):
    student = {"name": name, "age": age }
    students.append(student)
    return student

@app.get("/students")
def get_students():
    return students