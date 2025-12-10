from typing import List
from pydantic import BaseModel, constr

# 질문 응답
class QuestionResponse(BaseModel):
    id: int
    text: str
    category: str

    class Config:
        orm_mode = True