import requests
import asyncio
from bs4 import BeautifulSoup
from tortoise import Tortoise

from app.models.quote import Quote  # Tortoise ORM 기준

async def scrape_and_save_quotes(max_pages=10):
    all_quotes = []

    for page in range(1, max_pages + 1):
        url = f"https://saramro.com/quotes?page={page}"
        res = requests.get(url)
        if res.status_code != 200:
            print(f"Page {page} fetch failed")
            continue

        soup = BeautifulSoup(res.text, "html.parser")
        td_elements = soup.select('td[colspan="5"]')

        for td in td_elements:
            full_text = td.get_text(separator="\n").strip()
            lines = full_text.split("\n")
            if len(lines) >= 2:
                content = lines[0].strip()
                author = lines[1].lstrip("- ").strip()

                # DB에 저장 (중복 체크 포함)
                await Quote.get_or_create(content=content, author=author)

                all_quotes.append({"content": content, "author": author})

    return all_quotes

# main 함수
# async def main():
#     # Tortoise ORM 초기화
#     await Tortoise.init(
#         db_url="postgres://diary_quote_admin:1234@localhost:5432/diary_quote_database",  # DB URL, 프로젝트 DB 설정에 맞게 변경
#         modules={"models": ["app.models.quote"]}
#     )
#     await Tortoise.generate_schemas()  # 테이블 생성
#
#     quotes = await scrape_and_save_quotes(max_pages=3)
#     for q in quotes:
#         print(f"Content: {q['content']}")
#         print(f"Author: {q['author']}\n")
#
#     # DB 연결 종료
#     await Tortoise.close_connections()
#
# if __name__ == "__main__":
#     asyncio.run(main())