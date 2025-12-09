import os
from dotenv import load_dotenv

load_dotenv()  # ✅ 이 줄이 핵심

TORTOISE_ORM = {
    "connections": {
        "default": os.getenv("DATABASE_URL"),  # ✅ 여기서 None 나오면 지금 에러 발생
    },
    "apps": {
        "models": {
            "models": [
                "app.models.user",
                "app.models.token_blacklist",
            ],
            "default_connection": "default",
        },
    },
}
