from fastapi import APIRouter, HTTPException, Depends
from app.schemas.diary import DiaryCreate, DiaryUpdate, DiaryOut
from app.models.diary import Diary
from app.core.auth import get_current_user   # JWT 인증 후 사용자 반환
from app.models.user import User

router = APIRouter()

# 일기 생성 (로그인 사용자 기준)
@router.post("/", response_model=DiaryOut)
async def create_diary(data: DiaryCreate, current_user: User = Depends(get_current_user)):
    # 중요: user=current_user → 외래키로 사용자와 일기 연결
    diary = await Diary.create(
        user=current_user,
        title=data.title,
        text=data.text
    )
    return diary

# 일기 목록 조회 (본인 일기만 조회)
@router.get("/", response_model=list[DiaryOut])
async def get_diaries(current_user: User = Depends(get_current_user)):
    # 중요: order_by("-created_at") → 최신 순 정렬
    return await Diary.filter(user=current_user).order_by("-created_at").all()

# 단일 일기 조회
@router.get("/{diary_id}", response_model=DiaryOut)
async def get_diary(diary_id: int, current_user: User = Depends(get_current_user)):
    diary = await Diary.filter(id=diary_id, user=current_user).first()
    # 중요: user=current_user 조건으로 다른 사용자의 일기 접근 차단
    if not diary:
        raise HTTPException(status_code=404, detail="Diary not found")
    return diary

# 일기 수정
@router.put("/{diary_id}", response_model=DiaryOut)
async def update_diary(diary_id: int, data: DiaryUpdate, current_user: User = Depends(get_current_user)):
    diary = await Diary.filter(id=diary_id, user=current_user).first()
    if not diary:
        raise HTTPException(status_code=404, detail="Diary not found")

    # 변경값만 업데이트 (None일 경우 기존 값 유지)
    diary.title = data.title or diary.title
    diary.text = data.text or diary.text
    await diary.save()
    return diary

# 일기 삭제
@router.delete("/{diary_id}")
async def delete_diary(diary_id: int, current_user: User = Depends(get_current_user)):
    diary = await Diary.filter(id=diary_id, user=current_user).first()
    if not diary:
        raise HTTPException(status_code=404, detail="Diary not found")

    # 삭제 처리
    await diary.delete()
    return {"message": "Diary deleted successfully"}
