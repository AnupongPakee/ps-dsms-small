import os
from dotenv import load_dotenv
load_dotenv()

from typing import Optional
from jose import JWTError, ExpiredSignatureError, jwt
from datetime import datetime, timedelta, timezone

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = 60

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None, secret_key = SECRET_KEY, algorithm = "HS256"):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt =  jwt.encode(to_encode, secret_key, algorithm=algorithm)

    return encoded_jwt

def verify_token(token: str, secret_key = SECRET_KEY, algorithm = ALGORITHM):
    try:
        payload = jwt.decode(token, secret_key, algorithms=[algorithm])
        
        return payload
    except ExpiredSignatureError:
        return "Token expired"
    except JWTError:
        return "Invalid token"
        