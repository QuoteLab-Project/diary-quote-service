from fastapi import APIRouter, HTTPException, Depends
from app.schemas.diary import DiaryCreate, DiaryUpdate, DiaryOut
from app.models.diary import Diary
from app.core.auth import get_current_user
from app.models.user import User

router = APIRouter()

# Create
@router.post("/", response_model=DiaryOut)
async def create_diary(data: DiaryCreate, current_user: User = Depends(get_current_user)):
    diary = await Diary.create(
        user=current_user,
        title=data.title,
        text=data.text
    )
    return diary


# Read – list
@router.get("/", response_model=list[DiaryOut])
async def get_diaries(current_user: User = Depends(get_current_user)):
    diaries = await Diary.filter(user=current_user).order_by("-created_at").all()
    return diaries


# Read – single
@router.get("/{diary_id}", response_model=DiaryOut)
async def get_diary(diary_id: int, current_user: User = Depends(get_current_user)):
    diary = await Diary.filter(id=diary_id, user=current_user).first()
    if not diary:
        raise HTTPException(status_code=404, detail="Diary not found")
    return diary


# Update
@router.put("/{diary_id}", response_model=DiaryOut)
async def update_diary(diary_id: int, data: DiaryUpdate, current_user: User = Depends(get_current_user)):
    diary = await Diary.filter(id=diary_id, user=current_user).first()
    if not diary:
        raise HTTPException(status_code=404, detail="Diary not found")

    diary.title = data.title or diary.title
    diary.text = data.text or diary.text
    await diary.save()

    return diary


# Delete
@router.delete("/{diary_id}")
async def delete_diary(diary_id: int, current_user: User = Depends(get_current_user)):
    diary = await Diary.filter(id=diary_id, user=current_user).first()
    if not diary:
        raise HTTPException(status_code=404, detail="Diary not found")

    await diary.delete()
    return {"message": "Diary deleted successfully"}
