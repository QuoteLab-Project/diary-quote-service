# from tortoise import fields, models
#
# class Question(models.Model):
#     id = fields.IntField(pk=True)
#     text = fields.CharField(max_length=30)
#     category = fields.CharField(max_length=15)
#
#     class Meta:
#         table = "questions"

from tortoise import fields
from tortoise.models import Model


class Question(Model):
    id = fields.IntField(pk=True)
    text = fields.CharField(max_length=30)
    category = fields.CharField(max_length=15)

    class Meta:
        table = "questions"
