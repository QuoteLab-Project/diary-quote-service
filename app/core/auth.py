# app/core/auth.py

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt, JWTError

from app.models.user import User
from app.models.token_blacklist import TokenBlacklist
from app.core.security import SECRET_KEY, ALGORITHM  # JWT 시크릿키와 알고리즘

security = HTTPBearer()  # Authorization: Bearer <token> 헤더에서 JWT 추출


# 현재 로그인한 사용자 정보를 반환하는 의존성 함수
# 모든 보호된 API에서 Depends(get_current_user)로 사용
async def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security)
):
    token = credentials.credentials  # 클라이언트가 보낸 JWT

    # 1. 블랙리스트 체크 → 로그아웃된 토큰인지 확인
    # 중요: JWT는 서버가 상태를 저장하지 않기 때문에 블랙리스트로 무효화 구현
    token_blacklisted = await TokenBlacklist.filter(token=token).exists()
    if token_blacklisted:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token has been revoked",
        )

    try:
        # 2. JWT 복호화하여 payload 획득
        # 중요: 유효하지 않은 토큰이면 decode에서 오류 발생
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

        # payload에서 user_id 추출 (로그인 시 포함시킨 값)
        user_id: int = payload.get("user_id")
        if user_id is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token",
            )
    except JWTError:
        # 시그니처 불일치 / 만료 / 변조 등 모든 JWT 오류 처리
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
        )

    # 3. 복호화된 user_id로 실제 DB에서 사용자 확인
    # 중요: 실제 사용자는 DB에서 확인해야 안전함 (삭제된 계정일 수 있음)
    user = await User.get_or_none(id=user_id)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found",
        )

    # 최종적으로 유효한 로그인 사용자 객체 반환
    return user
