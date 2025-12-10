# 랜덤 명언 제공 + 북마크 추가/조회/삭제
import random

from fastapi import APIRouter, Depends, HTTPException
from tortoise import Tortoise

from app.core.auth import get_current_user
from app.models.bookmark import Bookmark
from app.models.quote import Quote
from app.models.user import User
from app.scraping.quote_scraper import scrape_and_save_quotes

router = APIRouter()

# quotes.json에서 읽은 리스트 중 랜덤으로 하나 반환
@router.get("/quotes/random")
async def random_quote():
    total = await Quote.all().count()
    if total == 0:
        raise HTTPException(status_code=404, detail="등록된 명언이 없습니다.")

    random_index = random.randrange(total)
    quote = await Quote.all().offset(random_index).limit(1).first()

    return quote

# 특정 명언을 북마크에 추가
@router.post("/quotes/{quote_id}/bookmark")
# Depends(get_current_user) => 현재 로그인한 유저 기준
async def add_bookmark(quote_id: int, user: User = Depends(get_current_user)):
    quote = await Quote.get_or_none(id=quote_id)
    if not quote:
        raise HTTPException(status_code=404, detail="Quote not found")

    # 사용자의 북마크 가져오기
    bookmark, _ = await Bookmark.get_or_create(user=user)

    # 이미 북마크되어 있는지 확인
    if await bookmark.quotes.filter(id=quote_id).exists():
        raise HTTPException(status_code=400, detail="Already bookmarked")

    # 북마크 추가
    await bookmark.quotes.add(quote)
    return {"message": "Bookmarked successfully"}

@router.get("/quotes/bookmarks")
async def get_bookmarks(user: User = Depends(get_current_user)):
    bookmark = await Bookmark.get_or_none(user=user)
    if not bookmark:
        return []

    quotes = await bookmark.quotes.all()
    return [{"id": q.id, "content": q.content, "author": q.author} for q in quotes]

@router.delete("/quotes/{quote_id}/bookmark")
async def remove_bookmark(quote_id: int, user: User = Depends(get_current_user)):
    bookmark = await Bookmark.get_or_none(user=user)
    if not bookmark:
        raise HTTPException(status_code=404, detail="Bookmark not found")

    quote = await Quote.get_or_none(id=quote_id)
    if not quote or not await bookmark.quotes.filter(id=quote_id).exists():
        raise HTTPException(status_code=404, detail="Bookmark not found")

    await bookmark.quotes.remove(quote)
    return {"message": "Bookmark removed successfully"}

@router.post("/quotes/scrape")
async def scrape_quotes_api():
    quotes = await scrape_and_save_quotes(max_pages=5)
    return {"saved": len(quotes)}