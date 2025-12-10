from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from app.database import TORTOISE_ORM
from app.api.v1.auth import router as auth_router
# from app.api.v1.quote import quotes_router

# Frontend
from fastapi.staticfiles import StaticFiles     # 정적 파일 서빙

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
# app.include_router(quotes_router, prefix="/api", tags=["Quotes"])

@app.get("/")
async def root():
    return {"status": "db connected"}
