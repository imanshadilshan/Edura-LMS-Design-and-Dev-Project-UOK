from pydantic import BaseModel, EmailStr, Field
from datetime import datetime

class Admin(BaseModel):
    name: str
    user_name: str
    email: EmailStr
    password: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
