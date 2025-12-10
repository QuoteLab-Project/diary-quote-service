from pydantic import BaseModel
from datetime import datetime

# 일기 요청 (작성)
class  DiaryCreateRequest(BaseModel):
    title: str
    text: str

# 일기 응답
class DiaryResponse(BaseModel):
    id: int
    title: str
    text: str
    created_at: datetime
    updated_at: datetime

class DiaryCreate(BaseModel):
    title: str
    text: str

class DiaryUpdate(BaseModel):
    title: str | None = None
    text: str | None = None

class DiaryOut(BaseModel):
    id: int
    title: str
    text: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True