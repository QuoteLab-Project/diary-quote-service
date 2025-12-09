from tortoise import fields, models

class Quote(models.Model):
    id = fields.IntField(pk=True)
    cotent = fields.TextField()     # ERD의 'coten' 오타 그대로 따라감? → 당신 의도 확인 필요
    author = fields.CharField(max_length=255)

    bookmarks: fields.ManyToManyRelation["Bookmark"]

    class Meta:
        table = "quotes"
