from dotenv import load_dotenv
from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from app.database import TORTOISE_ORM
from fastapi.staticfiles import StaticFiles

# 라우터 모듈들 (API 엔드포인트 구성)
from app.api.v1.auth import router as auth_router
from app.api.v1.quote import router as quotes_router
from app.api.v1.diary import router as diary_router
from app.api.v1.questions import router as questions_router
from app.api.v1.frontend import router as frontend_router

# .env 파일 로드 (환경 변수 불러오기)
load_dotenv()

# FastAPI 앱 생성
app = FastAPI()

# 정적 파일 제공 (/static 경로로 매핑)
# 중요: HTML/CSS/JS 파일을 Frontend에서 불러올 때 사용됨
app.mount("/static", StaticFiles(directory="frontend/static/"), name="static")

# Tortoise ORM 초기화
# 중요:
# - config=TORTOISE_ORM: DB 연결 + 모델 등록 정보
# - generate_schemas=False: 마이그레이션은 Aerich로 관리하므로 스키마 자동 생성 비활성화
# - add_exception_handlers=True: ORM 관련 예외를 FastAPI 스타일로 처리
register_tortoise(
    app,
    config=TORTOISE_ORM,
    generate_schemas=False,
    add_exception_handlers=True,
)

# root API: DB 연결 테스트용
@app.get("/")
async def root():
    return {"status": "db connected"}


# -------- Router 등록 --------
# 각 기능별 라우터를 FastAPI에 연결
# prefix: URL 앞부분
# tags: Swagger 문서에서 그룹으로 표시됨

app.include_router(frontend_router, tags=["Frontend"])         # 화면 렌더링 라우터
app.include_router(auth_router, prefix="/auth", tags=["Auth"])  # 회원가입/로그인/로그아웃
app.include_router(quotes_router, prefix="/quotes", tags=["Quotes"])  # 명언 API
app.include_router(diary_router, prefix="/diary", tags=["Diary"])      # 일기 API
app.include_router(questions_router, prefix="/questions", tags=["Questions"])  # 질문 API
