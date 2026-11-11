from fastapi import FastAPI, HTTPException 
from pydantic import BaseModel, EmailStr

app = FastAPI()

class StudentCreate(BaseModel):
    name: str
    email: EmailStr

class StudentUpdate(BaseModel):
    name: str | None = None
    email: EmailStr | None = None

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

@app.post("/students", status_code=201)
def create_student(student_data: StudentCreate):

    # 1. Generate a new ID
    new_id = max(student["id"] for student in students) + 1
    # new_id = len(students) + 1

    # 2. Create a dictionary containing:
    #    id, name and email
    new_student = {
        "id": new_id,
        "name": student_data.name,
        "email": student_data.email
    }

    # 3. Add the new student to the students list
    students.append(new_student)

    # 4. Return the new student
    return new_student

@app.put("/students/{student_id}")
def update_student(student_id: int, student_data: StudentCreate):

    for student in students:

        if student["id"] == student_id:

            # 1. Update the student's name
            student["name"] = student_data.name

            # 2. Update the student's email
            student["email"] = student_data.email
            # 3. Return the updated student
            return student

    # 4. If the student is not found, raise a 404 error
    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )

@app.patch("/students/{student_id}")
def partially_update_student(student_id: int, student_data: StudentUpdate):

    for student in students:

        if student["id"] == student_id:

            # 1. Get only the fields submitted by the client
            update_data = student_data.model_dump(exclude_unset=True)

            # 2. Update the existing student dictionary
            for key, value in update_data.items():
                student[key] = value
            # student.update(update_data)

            # 3. Return the updated student
            return student
    # 4. Raise a 404 error if student doesn't exist
    raise HTTPException(
        status_code=404, 
        detail=f"Student with ID {student_id} not found"
    )

@app.delete("/students/{student_id}")
def delete_student(student_id: int):

    for student in students:

        if student["id"] == student_id:

            # 1. Remove the student from the list
            students.remove(student)

            # 2. Return a success response
            return {
                "message": "Student deleted successfully"
            }

    # 3. Raise a 404 error if the student doesn't exist
    raise HTTPException(
        status_code=404, 
        detail=f"Student with ID {student_id} not found"
    )