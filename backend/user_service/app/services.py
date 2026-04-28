from sqlalchemy import Column

from schema import TeacherCreate
from db import get_db as db
from utility import password_hash , password_compare
from models import Teacher
import datetime
from sqlalchemy import UUID
# teacher (create , update, )

async def create_teacher(data: TeacherCreate):
    data.password = password_hash(data.password)
    teacher = Teacher(
        teacher_username= data.teacher_username,
        first_name = data.first_name,
        last_name = data.last_name,
        password = data.password,
        created_at = datetime.datetime.now(),
        updated_at = datetime.datetime.now()
        
    )
    db.add(teacher)
    db.commit()
    db.refresh(teacher)
    return {
            "message": "teacher created successfully", 
            "teacher_id": teacher.teacher_id, 
            "otp": "send otp to teacher email"
            }

async def teacher_otp_pool(teacher_id: str):
    otp_pool = {}

#async def send_teacher_otp(teacher_id: str, data: TeacherCreate):

async def update_teacher(data: TeacherCreate, teacher_id: UUID ):

    teacher = db.query(Teacher).filter(Teacher.teacher_id==teacher_id).first()
    if not teacher:
        return {"message" : "teacher not found"}
    
    teacher.teacher_username= data.teacher_username
    teacher.first_name = data.first_name
    teacher.last_name = data.last_name
    teacher.password = data.password
    teacher.updated_at = datetime.datetime.now()
    
    # teacher = Teacher(
    #     teacher_username= data.teacher_username,
    #     first_name = data.first_name,
    #     last_name = data.last_name,
    #     password = data.password,
    #     updated_at = datetime.datetime.now()
        
    # )
    db.commit()
    db.refresh(teacher)
    return {
        "status": "200 OK",
        "message": "update successfully"
    }

async def delete_teacher(teacher_id: UUID):
    db.delete(Teacher).where(Teacher.teacher_id == teacher_id)
    db.commit()
    db.refersh()

    return {
        "status": "200 OK",
        "message": "teacher delete successfully"
    }

