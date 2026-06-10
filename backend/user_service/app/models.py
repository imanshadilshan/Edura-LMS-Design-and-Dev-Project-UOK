from datetime import datetime
import uuid

from sqlalchemy import Column, Integer, String, UUID, DateTime, Boolean, VARCHAR, func
from app.db import Base


class Admin(Base):
    __tablename__ = "admins"

    admin_id = Column(UUID, primary_key=True, index=True, unique=True, default=lambda: str(uuid.uuid4()))
    admin_username = Column(String(50), index=True, unique=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    password = Column(String(255))
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

class Teacher(Base):
    __tablename__ = "teachers"

    teacher_id = Column(UUID, primary_key=True, index=True, unique=True, default=lambda: str(uuid.uuid4()))
    teacher_username = Column(String (50), index=True, unique=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    password = Column(String(255))
    status = Column(Boolean, default=False)
    activate_account = Column(Boolean, default=False)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

class Student(Base):
    __tablename__ = "students"

    student_id = Column(UUID, primary_key=True, index=True, unique=True, default=lambda: str(uuid.uuid4()))
    student_username = Column(String(50), unique=True, index=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    password = Column(String(50))
    date_of_birth = Column(DateTime)
    status = Column(Boolean, default=False) # account blocked  or unblocked
    activate_account = Column(Boolean, default=False)  # otp validation
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
