import random
from typing import List

from fastapi import APIRouter, Depends, HTTPException

from app.core.auth import get_current_user
from app.schemas.bookmark import BookmarkItemOut
from app.schemas.quote import QuoteOut
from app.scraping.quote_scraper import scrape_and_save_quotes

from app.models.bookmark import Bookmark
from app.models.bookmark_quote import BookmarkQuote   # 북마크와 명언을 연결하는 중간 테이블
from app.models.quote import Quote
from app.models.user import User

router = APIRouter()

# 랜덤 명언 반환
@router.get("/random", response_model=QuoteOut)
async def random_quote():
    total = await Quote.all().count()
    if total == 0:
        raise HTTPException(status_code=404, detail="등록된 명언이 없습니다.")

    # 중요: offset + limit 방식은 가장 가벼운 랜덤 레코드 조회 방식
    random_index = random.randrange(total)
    quote = await Quote.all().offset(random_index).limit(1).first()

    return quote


# 특정 명언을 북마크에 추가
@router.post("/{quote_id}/bookmark")
async def add_bookmark(quote_id: int, user: User = Depends(get_current_user)):  # 로그인한 사용자가 기준
    quote = await Quote.get_or_none(id=quote_id)
    if not quote:
        raise HTTPException(status_code=404, detail=f"Quote not found, {quote_id} 번호의 명언을 찾지 못했습니다.")

    # 사용자 북마크 가져오거나 생성 (get_or_create)
    # 중요: 북마크는 사용자당 1개만 존재
    bookmark, _ = await Bookmark.get_or_create(user=user)

    # 이미 북마크 되어 있는지 확인
    exists = await BookmarkQuote.filter(bookmark=bookmark, quote=quote).exists()
    if exists:
        raise HTTPException(status_code=400, detail="Already bookmarked")

    # 중간 테이블에 레코드 저장 → 북마크 연결
    await BookmarkQuote.create(bookmark=bookmark, quote=quote)
    return {"message": "Bookmarked successfully"}


# 북마크 목록 조회
@router.get("/bookmarks")
async def get_bookmarks(user: User = Depends(get_current_user)):
    bookmark = await Bookmark.get_or_none(user=user)
    if not bookmark:
        return []

    # 중요: prefetch_related("quote") → N+1 문제 방지 (성능 개선)
    bookmark_quotes = await BookmarkQuote.filter(bookmark=bookmark).prefetch_related("quote")

    # 연관된 명언 리스트 반환
    return [
        {
            "id": bq.quote.id,
            "content": bq.quote.content,
            "author": bq.quote.author
        }
        for bq in bookmark_quotes
    ]


# 북마크 삭제
@router.delete("/{quote_id}/bookmark")
async def remove_bookmark(quote_id: int, user: User = Depends(get_current_user)):
    bookmark = await Bookmark.get_or_none(user=user)
    if not bookmark:
        raise HTTPException(status_code=404, detail="Bookmark not found")

    quote = await Quote.get_or_none(id=quote_id)
    if not quote:
        raise HTTPException(status_code=404, detail="Quote not found")

    # 중간 테이블에서 해당 북마크 관계 삭제
    deleted = await BookmarkQuote.filter(
        bookmark=bookmark,
        quote=quote
    ).delete()

    if deleted == 0:
        raise HTTPException(status_code=404, detail="Bookmark not found")

    return {"message": "Bookmark removed successfully"}


# 명언 스크래핑 후 DB 저장
@router.post("/scrape")
async def scrape_quotes_api():
    # 중요: scrape_and_save_quotes는 max_pages만큼의 페이지를 크롤링하고 DB에 저장
    quotes = await scrape_and_save_quotes(max_pages=5)
    return {"saved": len(quotes)}
