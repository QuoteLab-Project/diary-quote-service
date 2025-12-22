from tortoise.contrib.fastapi import register_tortoise


# Tortoise ORM 설정 딕셔너리
# FastAPI와 Tortoise ORM을 연동할 때 사용됨
TORTOISE_ORM = {
    "connections": {
        # DB 연결 설정
        # 형식: postgres://<USER>:<PASSWORD>@<HOST>:<PORT>/<DATABASE>
        # 중요: 이 값이 환경에 따라 달라지므로 .env로 분리하는 것이 일반적
        "default": "postgres://diary_quote_admin:1234@localhost:5432/diary_quote_database"
    },

    "apps": {
        "models": {
            # Tortoise가 로딩할 모델 위치
            # "app.models" 안의 __init__.py에서 모든 모델을 가져오도록 구성되어 있어야 함
            # 중요: 여기 지정된 모델만 마이그레이션 및 ORM 기능에 포함됨
            "models": [
                "app.models"
            ],

            # 이 앱에서 사용할 기본 DB 연결 지정
            "default_connection": "default",
        },
    },
}
