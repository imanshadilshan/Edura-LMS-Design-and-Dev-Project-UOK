from uuid import UUID

from fastapi import FastAPI

from app.models import Teacher, Student
from app.schema import TeacherCreate, TeacherResponse, AdminCreate, AdminResponse, StudentCreate, StudentResponse

app = FastAPI()

@app.get("/")
async def main():
    return {"message": "fastapi user_services"}

# admin endpoints
@app.get("/admin/{admin_id}")
async def admin(admin_id: UUID):
    return {"message": "admin-data"}

@app.put("/admin/{admin_id}")
async def admin(admin_id: UUID):
    return {"message": "admin-update"}


# teacher endpoints

@app.post("/teacher")
async def teacher(teacher: TeacherCreate):
    return {"message": "teacher-data teacher create success fully"}
@app.get("/teacher/{teacher_id}")
async def teacher(teacher_id: UUID):
    return {"message": "teacher-create"}

@app.put("/teacher/{teacher_id}")
async def teacher(teacher_id: UUID, teacher: TeacherCreate):
    return {"message": "teacher-update"}

@app.delete("/teacher/{teacher_id}")
async def teacher(teacher_id: UUID):
    return {"message": "teacher-delete"}

# student endpoints

@app.post("/student")
async def student(student: StudentCreate):
    return {"message": "student-created"}
@app.get("/student/{student_id}")
async def student(student_id: UUID):
    return {"message": "student-data "}

@app.put("/student/{student_id}")
async def student(student_id: UUID):
    return {"message": "student-update"}

@app.delete("/student/{student_id}")
async def student(student_id: UUID):
    return {"message": "student-delete"}