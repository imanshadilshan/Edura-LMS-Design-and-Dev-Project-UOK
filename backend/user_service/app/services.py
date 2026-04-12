from schema import TeacherCreate
from db import get_db as db
from utility import password_hash , password_compare
from models import Teacher

# teacher (create , update, )

def create_teacher(data: TeacherCreate):
    data.password = password_hash(data.password)
    teacher = Teacher(
        teacher_username= data.teacher_username,
        
    )