from tortoise import fields
from tortoise.models import Model


class BookmarkQuote(Model):
    # 중간 테이블의 기본 키 (자동 증가)
    id = fields.IntField(pk=True)

    # Bookmark ↔ Quote 를 연결하는 외래키
    # 중요: 다대다(Many-to-Many) 관계를 구현하기 위한 중간 테이블 역할
    bookmark = fields.ForeignKeyField(
        "models.Bookmark",
        related_name="bookmark_quotes"  # 북마크 객체에서 연결된 Quote 목록 접근 가능
    )

    quote = fields.ForeignKeyField(
        "models.Quote",
        related_name="quote_bookmarks"  # 명언 객체에서 연결된 Bookmark 목록 접근 가능
    )

    class Meta:
        table = "bookmarks_has_quotes"  # 실제 DB 테이블명 지정
