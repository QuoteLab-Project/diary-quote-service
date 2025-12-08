from tortoise import fields
from tortoise.models import Model


class Diary(Model):
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=200)
    content = fields.TextField()
    created_at = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "diary"

    def __str__(self):
        return self.title
