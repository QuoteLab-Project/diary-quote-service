from datetime import datetime, timedelta
import bcrypt
from jose import jwt
from passlib.context import CryptContext
import os

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def _normalize_password(password: str) -> bytes:
    # bcrypt는 "바이트 기준 72byte" 제한을 검사함
    password_bytes = password.encode("utf-8")[:72]
    return password_bytes


def hash_password(password: str) -> str:
    # 문자열 비밀번호 → bcrypt가 처리할 수 있도록 바이트로 변환
    password_bytes = password.encode("utf-8")
    print(f"password_bytes : {password_bytes}")

    # bcrypt용 랜덤 salt 생성 (해시마다 다름)
    salt = bcrypt.gensalt()
    print(f"salt : {salt}")

    # 비밀번호 + salt로 bcrypt 해시 생성 → 문자열로 반환
    return bcrypt.hashpw(password_bytes, salt).decode("utf-8") # 바이트로 바꾼 비밀번호와 salt를 이용해 bcrypt 해시 생성.


def verify_password(plain_password: str, hashed_password: str) -> bool:
    password_bytes = plain_password.encode("utf-8")
    hashed_bytes = hashed_password.encode("utf-8")
    return bcrypt.checkpw(password_bytes, hashed_bytes)

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)