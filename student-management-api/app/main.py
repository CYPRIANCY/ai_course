from fastapi import FastAPI, HTTPException 

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to Student Management API"}

students = [
    {
        "id": 1,
        "name": "Ada",
        "email": "ada@gmail.com"
    },
    {
        "id": 2,
        "name": "John",
        "email": "john@gmail.com"
    }
]

@app.get("/students")
def get_students():
    return students

@app.get("/students/{student_id}")
def get_student_by_id(student_id: int):

    for student in students:
        if student["id"] == student_id:
            return student
            
    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )