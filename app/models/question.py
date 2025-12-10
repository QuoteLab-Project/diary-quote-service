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

# class Category(Model):
#     id = fields.IntField(pk=True)
#     name = fields.CharField(max_length=50, unique=True)
#
#     class Meta:
#         table = "categories"

# class Question(Model):
#     id = fields.IntField(pk=True)
#     text = fields.CharField(max_length=30)
#     category = fields.CharField(max_length=15)
#     # categories: fields.ManyToManyRelation["Category"] = fields.ManyToManyField(
#     #     "models.Category",
#     #     related_name="questions",
#     #     through="question_categories"
#     # )

    # class Meta:
    #     table = "questions"
