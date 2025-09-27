import os

from jose import jwt
from security.token_jwt import create_access_token, verify_token
from security.hash import hash_password, verify_password

secret_key = os.getenv("SECRET_KEY", "test-secret")
algorithm = os.getenv("ALGORITHM", "HS256")

def test_create_access_token():
    data = {
        'name': 'user test',
        'email': 'test@gmail.com',
        'password': '2au8pon4g6'
    }
    token = create_access_token(data=data,secret_key=secret_key, algorithm=algorithm)
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
    token = create_access_token(data=data, secret_key=secret_key, algorithm=algorithm)
    payload = verify_token(token=token, secret_key=secret_key, algorithm=algorithm)

    assert isinstance(payload, dict)
    assert payload["email"] == data["email"]
    assert payload["password"] == data["password"]

def test_hash_and_verify_password():
    hash_pass = hash_password("test hash")

    assert isinstance(hash_pass, str)
    assert verify_password("test hash", hash_pass) == True
    assert verify_password("tes hash", hash_pass) == False