import os
from dotenv import load_dotenv
load_dotenv()

from jose import jwt
from security.token import create_access_token, verify_token

def test_create_access_token():
    data = {
        'name': 'user test',
        'email': 'test@gmail.com',
        'password': '2au8pon4g6'
    }
    token = create_access_token(data=data)
    secret_key = os.getenv("SECRET_KEY")
    algorithm = os.getenv("ALGORITHM")
    decoded = jwt.decode(token, secret_key, algorithms=[algorithm])

    assert isinstance(token, str)
    assert decoded["email"] == data["email"]
    assert decoded["password"] == data["password"]

def test_verify_token():
    data = {
        'name': 'user test',
        'email': 'test@gmail.com',
        'password': '2au8pon4g6'
    }
    token = create_access_token(data=data)
    payload = verify_token(token=token)

    assert isinstance(payload, dict)
    assert payload["email"] == data["email"]
    assert payload["password"] == data["password"]