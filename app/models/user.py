# from tortoise import fields
# from tortoise.models import Model
#
#
# class User(Model):
#     id = fields.IntField(pk=True)
#     nickname = fields.CharField(max_length=20, unique=True)
#     email = fields.CharField(max_length=255, unique=True)
#     password_hash = fields.CharField(max_length=255)
#     is_active = fields.BooleanField(default=True)
#     created_at = fields.DatetimeField(auto_now_add=True)
#
#     class Meta:
#         table = "users"
#
#     def __str__(self):
#         return self.email

from tortoise import fields
from tortoise.models import Model


class User(Model):
    id = fields.IntField(pk=True)
    email = fields.CharField(max_length=255, unique=True)
    nickname = fields.CharField(max_length=20, unique=True)  # ✅ 요청한 필드
    hashed_password = fields.CharField(max_length=45)
    is_active = fields.BooleanField(default=True)
    created_at = fields.DatetimeField(auto_now_add=True)

    diaries: fields.ReverseRelation["Diary"]
    bookmarks: fields.ReverseRelation["Bookmark"]
    tokens: fields.ReverseRelation["TokenBlacklist"]

    class Meta:
        table = "users"
