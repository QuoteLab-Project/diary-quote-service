from typing import List
from pydantic import BaseModel, constr

# 카테고리 응답
class CategoryResponse(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True

# 질문 생성
class QuestionCreate(BaseModel):
    text: constr(max_length=255)
    # 클라이언트는 category 이름 목록(또는 id 목록)을 보낼 수 있음.
    # 아래 예시는 이름 목록을 받는 경우
    category_names: List[str]

# 질문 응답
class QuestionResponse(BaseModel):
    id: int
    text: str
    categories: List[CategoryResponse]

    class Config:
        orm_mode = True
