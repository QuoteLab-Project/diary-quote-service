from dotenv import load_dotenv
from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from app.database import TORTOISE_ORM
from fastapi.staticfiles import StaticFiles

from app.api.v1.auth import router as auth_router
from app.api.v1.quote import router as quotes_router
from app.api.v1.diary import router as diary_router
from app.api.v1.questions import router as questions_router
from app.api.v1.frontend import router as frontend_router

load_dotenv()
app = FastAPI()

# static
app.mount("/static", StaticFiles(directory="frontend/static/"), name="static")

# Tortoise ORM
register_tortoise(
    app,
    config=TORTOISE_ORM,
    generate_schemas=False,
    add_exception_handlers=True,
)


# DB Connection test
@app.get("/")
async def root():
    return {"status": "db connected"}


# Router
app.include_router(frontend_router, tags=["Frontend"])
app.include_router(auth_router, prefix="/auth", tags=["Auth"])
app.include_router(quotes_router, prefix="/quotes", tags=["Quotes"])
app.include_router(diary_router, prefix="/diary", tags=["Diary"])
app.include_router(questions_router, prefix="/questions", tags=["Questions"])
