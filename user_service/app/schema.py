from pydantic import BaseModel

class AdminCreate(BaseModel):
    username: str
    password: str
    first_name: str
    last_name: str

class AdminResponse(BaseModel):
    username: str
    first_name: str
    last_name: str


    