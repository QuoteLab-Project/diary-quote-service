from tortoise import fields
from tortoise.models import Model


class TokenBlacklist(Model):
    id = fields.IntField(pk=True)
    token = fields.CharField(max_length=512, unique=True)
    created_at = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "token_blacklist"

    def __str__(self):
        return self.token[:30]