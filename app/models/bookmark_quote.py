from tortoise import fields
from tortoise.models import Model


class BookmarkQuote(Model):
    id = fields.IntField(pk=True)

    bookmark = fields.ForeignKeyField(
        "models.Bookmark",
        related_name="bookmark_quotes"
    )
    quote = fields.ForeignKeyField(
        "models.Quote",
        related_name="quote_bookmarks"
    )

    class Meta:
        table = "bookmarks_has_quotes"
