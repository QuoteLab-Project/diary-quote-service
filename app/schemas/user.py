# 회원 정보 검증
from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    email: EmailStr
    nickname: str
    password: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str

################
# # 회원 생성 요청 모델 (입력용)
# class UserSignRequest(BaseModel):
#     email: EmailStr
#     name: str
#     password: str

# JWT 토큰 전달용 모델 (데코레이터 할때 사용)
class Token(BaseModel):
    access_token: str
    token_type: str

# 회원 로그인 요청 모델
class UserLoginRequest(BaseModel):
    email: str
    password: str

# 회원 로그인 응답 모델
class UserLoginResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"