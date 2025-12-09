# from tortoise import fields, models
#
# class Bookmark(models.Model):
#     id = fields.IntField(pk=True)
#     created_at = fields.DatetimeField(auto_now_add=True)
#
#     user = fields.ForeignKeyField(
#         "models.User", related_name="bookmarks"
#     )
#
#     quotes: fields.ManyToManyRelation["Quote"] = fields.ManyToManyField(
#         "models.Quote",
#         related_name="bookmarks",
#         through="bookmarks_has_quotes"
#     )
#
#     class Meta:
#         table = "bookmarks"

from tortoise import fields
from tortoise.models import Model


class Bookmark(Model):
    id = fields.IntField(pk=True)
    created_at = fields.DatetimeField(auto_now_add=True)

    user = fields.ForeignKeyField("models.User", related_name="bookmarks")
    quotes: fields.ManyToManyRelation["Quote"] = fields.ManyToManyField(
        "models.Quote",
        related_name="bookmarks",
        through="bookmarks_has_quotes"
    )

    class Meta:
        table = "bookmarks"
