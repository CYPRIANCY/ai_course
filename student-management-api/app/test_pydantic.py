from pydantic import BaseModel, EmailStr

class StudentCreate(BaseModel):
    name: str
    email: EmailStr

student = StudentCreate(
    name="Nadoo",
    email="nadoo@gmail.com"
)

print(student)
