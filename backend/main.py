from fastapi import FastAPI

app = FastAPI(
    description="Mini Debt & Saving Management System (ระบบจัดการหนี้และการออมขนาดเล็ก)"
)

@app.get("/")
def read_root():
    return {"msg": "Hello world"}