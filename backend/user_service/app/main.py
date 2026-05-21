from uuid import UUID

from fastapi import FastAPI

from app.models import Teacher

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
async def teacher(teacher: Teacher):
    return {"message": "teacher-data teacher create success fully"}
@app.get("/teacher/{teacher_id}")
async def user(teacher_id: UUID):
    return {"message": "teacher-create"}

@app.put("/teacher/{teacher_id}")
async def teacher(teacher_id: UUID, teacher: Teacher):
    return {"message": "teacher-update"}