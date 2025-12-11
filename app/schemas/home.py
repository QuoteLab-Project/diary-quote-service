from pydantic import BaseModel
from app.schemas.quote import QuoteOut
from app.schemas.question import QuestionOut
from app.schemas.diary import DiaryOut
from typing import List


class HomeResponse(BaseModel):
    quote: QuoteOut
    question: QuestionOut
    diaries: List[DiaryOut]

    model_config = {"from_attributes": True}
