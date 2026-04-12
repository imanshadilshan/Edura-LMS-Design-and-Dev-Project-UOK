from fastapi import Depends , HTTPException
from jose import jwt , JWTError
from fastapi.security import HTTPAuthorizationCredentials , HTTPBearer
import os
from dotenv import load_dotenv
from passlib.context import CryptContext

load_dotenv()

SECREAT = os.getenv("JWT_SECREAT")
ALGO = os.getenv("ALGORITHM")

bearer_token = HTTPBearer()

def current_user(token: HTTPAuthorizationCredentials = Depends(bearer_token)):
    try:
        decode_data = jwt.decode(token.credentials, SECREAT, algorithms=[ALGO])
        return decode_data
    except JWTError as e:
        raise HTTPException(401, "invalid jwt")
    

passwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def password_hash(password: str) -> str:
    return passwd_context.hash(password)

def password_compare (current_password: str, hash_passwd: str) -> bool:
    return passwd_context.verify(current_password, hash_passwd)