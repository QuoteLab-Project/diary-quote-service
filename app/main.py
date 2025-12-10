from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from app.database import TORTOISE_ORM
from app.api.auth import router as auth_router

# Frontend
from fastapi.staticfiles import StaticFiles     # 정적 파일 서빙
from app.core.templates import templates        # ← 여기서 가져오기만 한다 (생성 X)

app = FastAPI()

app.mount(
    "/static",
    StaticFiles(directory="frontend/static"),
    name="static"
)

# Tortoise ORM 등록
register_tortoise(
    app,
    config=TORTOISE_ORM,
    generate_schemas=False,
    add_exception_handlers=True,
)

# Router 등록
app.include_router(auth_router, prefix="/auth", tags=["Auth"])


@app.get("/")
async def root():
    return {"status": "db connected"}
