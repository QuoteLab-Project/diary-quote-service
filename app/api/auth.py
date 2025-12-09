from fastapi import APIRouter, Depends, HTTPException
from jose import jwt, JWTError
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from app.models.user import User
from app.models.token_blacklist import TokenBlacklist
from app.schemas.user import UserCreate, UserLogin
from app.core.security import hash_password, verify_password, create_access_token, SECRET_KEY, ALGORITHM

router = APIRouter()
security = HTTPBearer()

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


@router.post("/login")
async def login(data: UserLogin):
    user = await User.filter(email=data.email).first()
    if not user:
        raise HTTPException(status_code=400, detail="Invalid credentials")

    if not verify_password(data.password, user.password_hash):
        raise HTTPException(status_code=400, detail="Invalid credentials")

    token = create_access_token({"user_id": user.id})
    return {"access_token": token, "token_type": "bearer"}


@router.post("/logout")
async def logout(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials

    await TokenBlacklist.create(token=token)
    return {"message": "Logged out successfully"}
