from sqlalchemy import Column

from schema import TeacherCreate
from db import get_db as db
from utility import password_hash , password_compare
from models import Teacher
import datetime

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
    return teacher


#async def send_teacher_otp(teacher_id: str, data: TeacherCreate):