from sqlalchemy import Column, Integer, String, UUID, DateTime, Boolean
from db import Base


class Admin(Base):
    __tablename__ = "admins"

    admin_id = Column(UUID, primary_key=True, index=True, unique=True)
    admin_username = Column(String, index=True, unique=True)
    first_name = Column(String)
    last_name = Column(String)
    password = Column(String)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

class Teacher(Base):
    __tablename__ = "teachers"

    teacher_id = Column(UUID, primary_key=True, index=True, unique=True)
    teacher_username = Column(String , index=True, unique=True)
    first_name = Column(String)
    last_name = Column(String)
    password = Column(String)
    status = Column(Boolean, default=False)
    activate_account = Column(Boolean, default=False)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

class Student(Base):
    __tablename__ = "students"

    student_id = Column(UUID, primary_key=True, index=True, unique=True)
    student_username = Column(String, unique=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    password = Column(String)
    date_of_birth = Column(DateTime)
    status = Column(Boolean, default=False) # account blocked  or unblocked
    activate_account = Column(Boolean, default=False)  # otp validation
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
