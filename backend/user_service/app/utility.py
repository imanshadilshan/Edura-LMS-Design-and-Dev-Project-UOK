from fastapi import Depends , HTTPException
from jose import jwt , JWTError
from fastapi.security import HTTPAuthorizationCredentials , HTTPBearer
import os
from dotenv import load_dotenv

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