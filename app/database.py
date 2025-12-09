from tortoise.contrib.fastapi import register_tortoise


TORTOISE_ORM = {
    "connections": {
        "default": "postgres://diary_quote_admin:1234@localhost:5432/diary_quote_database"
    },
    "apps": {
        "models": {
            "models": ["app.db.models"],  # ✅ 실제 모델 위치
            "default_connection": "default",
        },
    },
}
