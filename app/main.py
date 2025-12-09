from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from app.db import TORTOISE_ORM

from app.api.auth import router as auth_router   # ✅ 이 줄이 핵심

app = FastAPI()

register_tortoise(
    app,
    config=TORTOISE_ORM,
    generate_schemas=False,
    add_exception_handlers=True,
)

app.include_router(auth_router, prefix="/auth", tags=["Auth"])

@app.get("/")
async def root():
    return {"status": "db connected"}