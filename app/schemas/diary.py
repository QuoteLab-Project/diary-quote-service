from pydantic import BaseModel
from datetime import datetime

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
    updated_at: datetime | None = None

    model_config = {"from_attributes": True}