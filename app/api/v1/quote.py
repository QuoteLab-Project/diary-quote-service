# # 랜덤 명언 제공 + 북마크 추가/조회/삭제
# from fastapi import APIRouter, Depends, HTTPException
# from app.models.quote import Quote
# from app.models.bookmark import Bookmark
# from app.models.user import User
# from app.core.auth import get_current_user
# import random
# import os
# import json
#
# router = APIRouter()
#
# # 프로젝트 루트 기준 경로
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# QUOTES_FILE = os.path.join(BASE_DIR, "data", "quotes.json")
#
# # quotes.json 읽기
# with open(QUOTES_FILE, "r", encoding="utf-8") as f:
#     quotes = json.load(f)
#
# def get_random_quote():
#     return random.choice(quotes)
#
# # quotes.json에서 읽은 리스트 중 랜덤으로 하나 반환
# @router.get("/quotes/random")
# async def random_quote():
#     quote = get_random_quote()
#     return {"id": quote["id"], "content": quote["content"], "author": quote["author"]}
#
# # 북마크 추가
# @router.post("/quotes/{quote_id}/bookmark")
#
# # Depends(get_current_user) => 현재 로그인한 유저 기준
# async def add_bookmark(quote_id: int, user: User = Depends(get_current_user)):
#     quote = await Quote.get_or_none(id=quote_id)
#     if not quote:
#         raise HTTPException(status_code=404, detail="Quote not found")
#
#     # 사용자의 북마크 가져오기
#     bookmark, _ = await Bookmark.get_or_create(user=user)
#
#     # 이미 북마크되어 있는지 확인
#     if await bookmark.quotes.filter(id=quote_id).exists():
#         raise HTTPException(status_code=400, detail="Already bookmarked")
#
#     # 북마크 추가
#     await bookmark.quotes.add(quote)
#     return {"message": "Bookmarked successfully"}
#
# @router.get("/quotes/bookmarks")
# async def get_bookmarks(user: User = Depends(get_current_user)):
#     bookmark = await Bookmark.get_or_none(user=user)
#     if not bookmark:
#         return []
#
#     quotes = await bookmark.quotes.all()
#     return [{"id": q.id, "content": q.content, "author": q.author} for q in quotes]
#
# @router.delete("/quotes/{quote_id}/bookmark")
# async def remove_bookmark(quote_id: int, user: User = Depends(get_current_user)):
#     bookmark = await Bookmark.get_or_none(user=user)
#     if not bookmark:
#         raise HTTPException(status_code=404, detail="Bookmark not found")
#
#     quote = await Quote.get_or_none(id=quote_id)
#     if not quote or not await bookmark.quotes.filter(id=quote_id).exists():
#         raise HTTPException(status_code=404, detail="Bookmark not found")
#
#     await bookmark.quotes.remove(quote)
#     return {"message": "Bookmark removed successfully"}
#
# quotes_router = router
