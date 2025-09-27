from passlib.hash import pbkdf2_sha512

def hash_password(password: str) -> str:
    return pbkdf2_sha512.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pbkdf2_sha512.verify(plain_password, hashed_password)