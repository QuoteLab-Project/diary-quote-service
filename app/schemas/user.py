from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    email: EmailStr
    nickname: str
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

# 회원 로그인 응답 모델
class UserLoginResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"

class UserOut(BaseModel):
    id: int
    email: str
    nickname: str

    model_config = {"from_attributes": True}