from pydantic import BaseModel
from typing import List
from datetime import datetime
from app.schemas.quote import QuoteOut

# 북마크 생성 요청
class BookmarkCreateRequest(BaseModel):
    quote_ids: List[int]  # 북마크에 추가할 quote ID 목록

# --- Bookmark 응답용 스키마 ---
class BookmarkResponse(BaseModel):
    id: int
    user_id: int
    quote_ids: List[int]  # 북마크에 포함된 quote ID 목록
    created_at: datetime

    class Config:
        orm_mode = True  # Tortoise 모델을 Pydantic으로 변환 가능하게

class BookmarkItemOut(BaseModel):
    id: int
    quote: QuoteOut

    model_config = {"from_attributes": True}