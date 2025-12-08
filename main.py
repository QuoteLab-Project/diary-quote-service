from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from db import TORTOISE_ORM

app = FastAPI()

register_tortoise(
    app,
    config=TORTOISE_ORM,
    generate_schemas=False,  # ❗ Aerich 사용 시 반드시 False
    add_exception_handlers=True,
)

@app.get("/")
async def root():
    return {"status": "db connected"}