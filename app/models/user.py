from tortoise import fields
from tortoise.models import Model

from app.models.token_blacklist import TokenBlacklist


class User(Model):
    id = fields.IntField(pk=True)
    email = fields.CharField(max_length=255, unique=True)
    password_hash = fields.CharField(max_length=255)
    is_active = fields.BooleanField(default=True)
    created_at = fields.DatetimeField(auto_now_add=True)

    diaries: fields.ReverseRelation["Diary"]
    bookmarks: fields.ReverseRelation["Bookmark"]
    tokens: fields.ReverseRelation["TokenBlacklist"]

    class Meta:
        table = "users"
