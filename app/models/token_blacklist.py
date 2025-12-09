# from tortoise import fields
# from tortoise.models import Model
#
#
# class TokenBlacklist(Model):
#     id = fields.IntField(pk=True)
#     token = fields.CharField(max_length=512, unique=True)
#     created_at = fields.DatetimeField(auto_now_add=True)
#
#     class Meta:
#         table = "token_blacklist"
#
#     def __str__(self):
#         return self.token[:30]
#
#
# # from tortoise import fields, models
#
# # class TokenBlacklist(models.Model):
# #     id = fields.IntField(pk=True)
# #     token = fields.CharField(max_length=255, unique=True)
# #     expired_at = fields.DatetimeField(null=True)
#
# #     user = fields.ForeignKeyField(
# #         "models.User", related_name="token_blacklists"
# #     )
#
# #     class Meta:
# #         table = "token_blacklist"

from tortoise import fields
from tortoise.models import Model


class TokenBlacklist(Model):
    id = fields.IntField(pk=True)
    token = fields.CharField(max_length=255)
    expired_at = fields.DatetimeField()

    user = fields.ForeignKeyField("models.User", related_name="tokens")

    class Meta:
        table = "token_blacklist"
