import random
from fastapi import APIRouter, HTTPException, Depends
from starlette.responses import JSONResponse

from app.core.auth import get_current_user
from app.models import User, Question
from app.schemas.question import QuestionResponse

router = APIRouter()

# 랜덤 질문 가져오기 API — 로그인된 사용자만 접근 가능
@router.get("/", response_model=QuestionResponse)
async def get_question(current_user: User = Depends(get_current_user)):
    # 전체 질문 개수 확인
    total = await Question.all().count()
    if total == 0:
        raise HTTPException(status_code=404, detail="등록된 질문이 없습니다.")

    # 0 ~ total-1 사이에서 랜덤 인덱스 선택
    # 중요: DB 레코드를 랜덤하게 가져오는 가장 가벼운 방식
    random_index = random.randrange(total)

    # offset 기반으로 랜덤 레코드 1개 조회
    question = await Question.all().offset(random_index).limit(1).first()

    return question
