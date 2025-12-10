from pydantic import BaseModel
from datetime import datetime

class TokenBlacklistCreate(BaseModel):
    token: str
    expired_at: datetime
    user_id: int   # ForeignKey는 일반적으로 id로 보냄


class TokenBlacklistResponse(BaseModel):
    id: int
    token: str
    expired_at: datetime
    user_id: int

    class Config:
        orm_mode = True
