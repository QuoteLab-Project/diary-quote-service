from tortoise import fields, models

class BookmarkQuote(models.Model):
    bookmark = fields.ForeignKeyField(
        "models.Bookmark",
        related_name="bookmark_quotes",
        pk=True
    )
    quote = fields.ForeignKeyField(
        "models.Quote",
        related_name="quote_bookmarks",
        pk=True
    )

    class Meta:
        table = "bookmarks_has_quotes"
