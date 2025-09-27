from datetime import datetime, timezone
from fastapi import APIRouter, Response, Request, HTTPException
from security.token_jwt import create_access_token, verify_token
from security.hash import hash_password, verify_password
from models.user import UserLogin, UserRegister
from database.db import mongodb

routes = APIRouter()
db = mongodb("users")

@routes.get("/me")
async def read_me(req: Request):
    token = req.cookies.get("access_token")
    if not token:
        raise HTTPException(status_code=401, detail="Not authenticated")
    
    payload = verify_token(token=token)
    if payload == "Invalid token":
        raise HTTPException(status_code=401, detail="Invalid token")
    if payload == "Token expired":
        raise HTTPException(status_code=401, detail="Token exprired")
    
    return payload

@routes.post("/login")
async def signin(res: Response, user: UserLogin):
    response = db.find_one({"email": user.email})
    if not response:
        raise HTTPException(status_code=401, detail="Invalid email")
    if not verify_password(user.password, response["password"]):
        raise HTTPException(status_code=401, detail="Invalid password")
    
    token = create_access_token({
        "user_id": str(response["_id"]),
        "name": response["name"]    
        })
    res.set_cookie(
        key="access_token",
        value=token,
        httponly=True,
        secure=False,
        samesite="strict",
        max_age=1800,
        path="/"
    )
    
    return {
        "msg": "Login successful"
    }

@routes.post("/register")
async def signup(res: Response, user: UserRegister):
    hash_pass = hash_password(user.password)
    new_user = {
        "name": user.name,
        "email": user.email,
        "password": hash_pass,
        "createdAt": datetime.now(timezone.utc)
    }

    primary = db.insert_one(new_user)
    response = db.find_one({"_id": primary.inserted_id})
    token = create_access_token({
        "user_id": str(response["_id"]),
        "name": response["name"]
    })
    res.set_cookie(
        key="access_token",
        value=token,
        httponly=True,
        secure=False,
        samesite="strict",
        max_age=1800,
        path="/"
    )

    return {"msg": "Create user success"}