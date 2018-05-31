from django.db import models
from datetime import datetime
from user.models import User

class Blog(models.Model):
    user = models.IntegerField(verbose_name="用户", null=True, blank=True)
    content = models.TextField(verbose_name="微博内容")
    pra_num = models.IntegerField(default=0, verbose_name="点赞数")
    comments_num = models.IntegerField(default=0, verbose_name="评论数")
    fav_num = models.IntegerField(default=0, verbose_name="收藏数")
    add_time = models.DateField(default=datetime.now, verbose_name="发表时间")

    class Meta:
        verbose_name = u"微博"
        verbose_name_plural = verbose_name


