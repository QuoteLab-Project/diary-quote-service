from tortoise import fields
from tortoise.models import Model


class Quote(Model):
    id = fields.IntField(pk=True)
    content = fields.TextField()
    author = fields.CharField(max_length=255)

    quote_bookmarks: fields.ReverseRelation["BookmarkQuote"]

    class Meta:
        table = "quotes"
