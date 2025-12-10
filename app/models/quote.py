from tortoise import fields
from tortoise.models import Model


class Quote(Model):
    id = fields.IntField(pk=True)
    content = fields.TextField()
    author = fields.CharField(max_length=255)

    bookmarks: fields.ManyToManyRelation["Bookmark"]

    class Meta:
        table = "quotes"
