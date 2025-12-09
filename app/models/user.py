from tortoise import fields
from tortoise.models import Model


class User(Model):
    id = fields.IntField(pk=True)
    email = fields.CharField(max_length=255, unique=True)
    nickname = fields.CharField(max_length=20, unique=True)  # ✅ 요청한 필드
    hashed_password = fields.CharField(max_length=128, null=False)
    is_active = fields.BooleanField(default=True)
    created_at = fields.DatetimeField(auto_now_add=True)

    diaries: fields.ReverseRelation["Diary"]
    bookmarks: fields.ReverseRelation["Bookmark"]
    tokens: fields.ReverseRelation["TokenBlacklist"]

    class Meta:
        table = "users"
