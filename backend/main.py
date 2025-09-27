from fastapi import FastAPI
from routes.auth import routes

app = FastAPI(
    description="Mini Debt & Saving Management System (ระบบจัดการหนี้และการออมขนาดเล็ก)"
)

app.include_router(routes, prefix="/api")