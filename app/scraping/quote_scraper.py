import requests
import asyncio
from bs4 import BeautifulSoup
from tortoise import Tortoise

from app.models.quote import Quote  # 명언 모델 (Tortoise ORM)

async def scrape_and_save_quotes(max_pages=10):
    # 반환 용도: 스크래핑한 명언 전체 리스트
    all_quotes = []

    # 1페이지부터 max_pages까지 반복해서 스크래핑
    for page in range(1, max_pages + 1):
        url = f"https://saramro.com/quotes?page={page}"
        res = requests.get(url)

        # HTTP 요청 실패 시 해당 페이지 건너뜀
        if res.status_code != 200:
            print(f"Page {page} fetch failed")
            continue

        # HTML 파싱
        soup = BeautifulSoup(res.text, "html.parser")

        # 명언이 들어 있는 <td colspan="5"> 요소 선택
        td_elements = soup.select('td[colspan="5"]')

        for td in td_elements:
            # 줄바꿈을 기준으로 명언과 저자를 분리
            full_text = td.get_text(separator="\n").strip()
            lines = full_text.split("\n")

            # 최소 2줄(내용 + 저자)일 때만 처리
            if len(lines) >= 2:
                content = lines[0].strip()               # 명언 내용
                author = lines[1].lstrip("- ").strip()   # 앞의 "- " 제거 후 저자 이름

                # 중요: DB 저장 시 get_or_create 사용 → 중복 명언 방지
                await Quote.get_or_create(content=content, author=author)

                # 결과 리스트에 추가
                all_quotes.append({"content": content, "author": author})

    # 스크래핑 완료 후 전체 명언 반환
    return all_quotes
