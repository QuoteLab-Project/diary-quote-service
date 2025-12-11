from datetime import datetime, timedelta
import bcrypt
from jose import jwt
from passlib.context import CryptContext
import os

# JWT 서명용 비밀키 (환경변수 없으면 기본값 사용)
SECRET_KEY = os.getenv("SECRET_KEY", "super_secret_fallback_key")

ALGORITHM = "HS256"  # JWT 서명 알고리즘
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24  # 24시간(로그인 유지 시간)

# 비밀번호 해싱 규칙 설정 (bcrypt 사용)
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def _normalize_password(password: str) -> bytes:
    # bcrypt는 내부적으로 72byte 이상을 무시하므로 잘라주는 보조 함수
    password_bytes = password.encode("utf-8")[:72]
    return password_bytes


def hash_password(password: str) -> str:
    # 비밀번호를 bcrypt에서 처리할 수 있도록 bytes로 변환
    password_bytes = password.encode("utf-8")
    print(f"password_bytes : {password_bytes}")

    # bcrypt salt 생성 (랜덤 값 → 같은 비밀번호도 해시가 항상 다름)
    salt = bcrypt.gensalt()
    print(f"salt : {salt}")

    # 비밀번호 + salt로 bcrypt 해시 생성
    # 중요: bcrypt.hashpw는 bytes를 반환하기 때문에 decode 필요
    return bcrypt.hashpw(password_bytes, salt).decode("utf-8")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    # 사용자가 입력한 비번을 해싱된 비번과 비교
    password_bytes = plain_password.encode("utf-8")
    hashed_bytes = hashed_password.encode("utf-8")

    # bcrypt.checkpw는 내부적으로 salt를 포함한 hashed_password를 사용해 검증
    return bcrypt.checkpw(password_bytes, hashed_bytes)


def create_access_token(data: dict):
    # JWT에 담을 기본 payload 복사
    to_encode = data.copy()

    # 토큰 만료시간 추가
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})

    # JWT 생성 (HS256 + SECRET_KEY)
    # 중요: 반환값은 이미 문자열(Token)이며 클라이언트로 바로 전달 가능
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
