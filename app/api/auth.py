from fastapi import APIRouter, Depends, HTTPException
from jose import jwt, JWTError
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from models.user import User
from models.token_blacklist import TokenBlacklist
from schemas.user import UserCreate, UserLogin
from core.security import hash_password, verify_password, create_access_token, SECRET_KEY, ALGORITHM

router = APIRouter()
security = HTTPBearer()


# ✅ 회원가입
@router.post("/signup")
async def signup(data: UserCreate):
    exists = await User.filter(email=data.email).first()
    if exists:
        raise HTTPException(status_code=400, detail="Email already exists")

    user = await User.create(
        email=data.email,
        password_hash=hash_password(data.password),
    )

    return {"id": user.id, "email": user.email}


# ✅ 로그인 (JWT 발급)
@router.post("/login")
async def login(data: UserLogin):
    user = await User.filter(email=data.email).first()
    if not user:
        raise HTTPException(status_code=400, detail="Invalid credentials")

    if not verify_password(data.password, user.password_hash):
        raise HTTPException(status_code=400, detail="Invalid credentials")

    token = create_access_token({"user_id": user.id})
    return {"access_token": token, "token_type": "bearer"}


# ✅ 로그아웃 (토큰 블랙리스트)
@router.post("/logout")
async def logout(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials

    await TokenBlacklist.create(token=token)
    return {"message": "Logged out successfully"}
