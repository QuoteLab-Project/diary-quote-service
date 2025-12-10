from tortoise import fields
from tortoise.models import Model

from app.models.token_blacklist import TokenBlacklist


class User(Model):
    id = fields.IntField(pk=True)
    email = fields.CharField(max_length=255, unique=True)
    nickname = fields.CharField(max_length=20, unique=True)  # ✅ 요청한 필드
    hashed_password = fields.CharField(max_length=128, null=False)
    is_active = fields.BooleanField(default=True)
    created_at = fields.DatetimeField(auto_now_add=True)

    diaries: fields.ReverseRelation["Diary"]

    bookmarks: fields.ReverseRelation["Bookmark"]

    # bookmarks => user에 bookmarks라는 필드 이름 (컬럼 아님)
    # fields.ManyToManyField('models.Quote',...) => models 폴더 안에 Quote 라는 클래스에서 여러개를 가져올 수 있음
    # 나머지 => models폴더에 있는 Quote에서 관계이름과 through를 정함
    # bookmarks: fields.ManyToManyRelation["Quote"] = fields.ManyToManyField(
    #     "models.Quote",
    #     related_name="bookmarked_by",
    #     through="user_bookmarks"
    # )

    tokens: fields.ReverseRelation["TokenBlacklist"]

    class Meta:
        table = "users"
