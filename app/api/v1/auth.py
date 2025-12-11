
# 회원가입, 로그인, 로그아웃 라우터

from fastapi import APIRouter, Request, Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt, JWTError

from app.core.auth import get_current_user
from app.core.templates import templates
from app.models.user import User
from app.models.token_blacklist import TokenBlacklist
from app.schemas.user import UserCreate, UserLogin
from app.core.security import hash_password, verify_password, create_access_token

router = APIRouter()
security = HTTPBearer()


# 회원가입 페이지

@router.get("/signup")
async def signup_page(request: Request):
    return templates.TemplateResponse("signup.html", {"request": request})

@router.post("/signup")
async def signup(data: UserCreate):
    email_exists = await User.filter(email=data.email).exists()
    if email_exists:
        raise HTTPException(status_code=400, detail="Email already exists")

    nickname_exists = await User.filter(nickname=data.nickname).exists()
    if nickname_exists:
        raise HTTPException(status_code=400, detail="Nickname already exists")

    user = await User.create(
        email=data.email,
        nickname=data.nickname,
        hashed_password=hash_password(data.password),
    )

    return {
        "id": user.id,
        "email": user.email,
        "nickname": user.nickname,
    }

@router.get("/login")
async def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@router.post("/login")
async def login(data: UserLogin):
    user = await User.filter(email=data.email).first()
    if not user:
        raise HTTPException(status_code=400, detail="Invalid credentials")

    if not verify_password(data.password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid credentials")

    token = create_access_token({"user_id": user.id})
    return {"access_token": token, "token_type": "bearer"}

  
@router.post("/logout")
async def logout(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials

    await TokenBlacklist.create(token=token)

    return {"message": "Logged out successfully"}

@router.get("/me")
async def me(user: User = Depends(get_current_user)):
    return {
        "id": user.id,
        "email": user.email,
        "nickname": user.nickname,
    }


