from pydantic import BaseModel, EmailStr

class UserSignin(BaseModel):
    email: EmailStr
    password: str

class UserSignup(BaseModel):
    name: str
    email: EmailStr
    password: str