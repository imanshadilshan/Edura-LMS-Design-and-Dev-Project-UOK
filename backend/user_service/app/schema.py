from pydantic import BaseModel
import datetime
from uuid import UUID

class AdminCreate(BaseModel):
    admin_username: str
    password: str
    first_name: str
    last_name: str

class AdminResponse(BaseModel):
    admin_id: UUID
    admin_username: str
    first_name: str
    last_name: str

class TeacherCreate(BaseModel):
    teacher_username: str
    first_name : str
    last_name: str
    password: str

class TeacherResponse(BaseModel):
    teacher_id: UUID
    teacher_username: str
    first_name: str
    last_name: str
    status: bool


class StudentCreate(BaseModel):
    student_username: str
    first_name: str
    last_name: str
    password: str
    date_of_birth: datetime.datetime

class StudentResponse(BaseModel):
    student_id : UUID
    student_username: str
    first_name: str
    last_name: str
    date_of_birth: datetime.datetime
    status: bool