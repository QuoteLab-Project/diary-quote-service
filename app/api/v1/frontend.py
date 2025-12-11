from fastapi import APIRouter, Request, Depends
from app.core.auth import get_current_user
from app.core.templates import templates
from app.models.user import User

router = APIRouter()

# 로그인 페이지
@router.get("/login")
async def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

# 회원가입 페이지
@router.get("/signup")
async def signup_page(request: Request):
    return templates.TemplateResponse("signup.html", {"request": request})

# 홈 화면
@router.get("/home")
async def home_page(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})


# 전체 일기 목록 페이지 : Error 고쳐야함
@router.get("/diaries")
async def diaries_page(request: Request, user: User = Depends(get_current_user)):
    return templates.TemplateResponse("diaries.html", {
        "request": request,
        "user": user
    })
