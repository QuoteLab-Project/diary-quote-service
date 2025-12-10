import random
from fastapi import APIRouter, HTTPException, Depends
from starlette.responses import JSONResponse

from app.core.auth import get_current_user
from app.models import User, Question
from app.schemas.question import QuestionResponse

router = APIRouter()

@router.get("/", response_model=QuestionResponse)
async def get_question(current_user: User = Depends(get_current_user)):
    total = await Question.all().count()
    if total == 0:
        raise HTTPException(status_code=404, detail="등록된 질문이 없습니다.")

    random_index = random.randrange(total)
    question = await Question.all().offset(random_index).limit(1).first()

    return question