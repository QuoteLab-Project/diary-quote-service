# from tortoise import fields, models
#
# class Diary(models.Model):
#     id = fields.IntField(pk=True)
#     title = fields.CharField(max_length=50)
#     text = fields.TextField()
#     created_at = fields.DatetimeField(auto_now_add=True)
#     updated_at = fields.DatetimeField(auto_now=True)
#
#     user = fields.ForeignKeyField(
#         "models.User", related_name="diaries"
#     )
#
#     class Meta:
#         table = "diaries"

from tortoise import fields
from tortoise.models import Model


class Diary(Model):
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=50)
    text = fields.TextField()
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    user = fields.ForeignKeyField("models.User", related_name="diaries")

    class Meta:
        table = "diaries"
