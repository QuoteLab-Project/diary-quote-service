from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from app.database import TORTOISE_ORM
from app.api.auth import router as auth_router

app = FastAPI()

# ✅ Tortoise ORM 등록
register_tortoise(
    app,
    config=TORTOISE_ORM,
    generate_schemas=False,      # ✅ 반드시 False
    add_exception_handlers=True,
)

# ✅ Auth Router 등록
app.include_router(auth_router, prefix="/auth", tags=["Auth"])


@app.get("/")
async def root():
    return {"status": "db connected"}