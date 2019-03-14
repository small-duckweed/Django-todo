from django.db import models

# Create your models here.


class Content(models.Model):
    text = models.CharField('内容', max_length=200)
    issue_date = models.DateTimeField('发布时间')
    finish_date = models.DateTimeField('完成时间')
    status = models.IntegerField('状态', default=0)

    def __str__(self):
        return self.text

