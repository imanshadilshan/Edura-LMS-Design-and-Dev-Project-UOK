from sqlalchemy import Column, Integer, String, UUID, DateTime
from db import Base


class Admin(Base):
    __tablename__ = "admins"

    id = Column(UUID, primary_key=True, index=True, unique=True)
    username = Column(String, index=True, unique=True)
    first_name = Column(String)
    last_name = Column(String)
    password = Column(String)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

class Teacher(Base):
    __tablename__ = "teachers"

    id = Column(UUID, primary_key=True, index=True, unique=True)
    teacher_username = Column(String , index=True, unique=True)
    first_name = Column(String)
    last_name = Column(String)
    password = Column(String)
    created_at = Column(String)
    updated_at = Column(String)
