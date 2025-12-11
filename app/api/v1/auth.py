# 회원가입, 로그인, 로그아웃 라우터

from fastapi import APIRouter, Request, Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt, JWTError

from app.core.auth import get_current_user   # JWT 검증 후 현재 사용자 반환
from app.core.templates import templates     # HTML 템플릿 렌더링 엔진
from app.models.user import User
from app.models.token_blacklist import TokenBlacklist   # 로그아웃 토큰 저장
from app.schemas.user import UserCreate, UserLogin
from app.core.security import hash_password, verify_password, create_access_token

router = APIRouter()
security = HTTPBearer()   # Authorization: Bearer <token> 방식의 인증 헤더 읽기


# 회원가입 페이지 렌더링
@router.get("/signup")
async def signup_page(request: Request):
    return templates.TemplateResponse("signup.html", {"request": request})


# 회원가입 처리
@router.post("/signup")
async def signup(data: UserCreate):
    # 이메일/닉네임 중복 체크
    if await User.filter(email=data.email).exists():
        raise HTTPException(status_code=400, detail="Email already exists")

    if await User.filter(nickname=data.nickname).exists():
        raise HTTPException(status_code=400, detail="Nickname already exists")

    # 사용자 생성 (중요: 비밀번호 해싱 후 저장)
    user = await User.create(
        email=data.email,
        nickname=data.nickname,
        hashed_password=hash_password(data.password),  # 해싱 필수
    )

    return {"id": user.id, "email": user.email, "nickname": user.nickname}


# 로그인 페이지 렌더링
@router.get("/login")
async def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


# 로그인 처리
@router.post("/login")
async def login(data: UserLogin):
    user = await User.filter(email=data.email).first()
    # 사용자 존재 여부 + 비번 검증
    if not user or not verify_password(data.password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid credentials")

    # JWT 발급 (중요: payload에 user_id 포함)
    token = create_access_token({"user_id": user.id})
    return {"access_token": token, "token_type": "bearer"}


# 로그아웃 → 토큰을 블랙리스트 처리
# (중요: JWT는 상태를 저장하지 않으므로 서버가 직접 차단 관리해야 함)
@router.post("/logout")
async def logout(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    await TokenBlacklist.create(token=token)  # 토큰 저장 후 향후 접근 차단
    return {"message": "Logged out successfully"}


# 현재 로그인된 사용자 정보 조회
# (JWT → get_current_user → DB 사용자 반환)
@router.get("/me")
async def me(user: User = Depends(get_current_user)):
    return {"id": user.id, "email": user.email, "nickname": user.nickname}
