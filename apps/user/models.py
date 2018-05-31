from __future__ import unicode_literals
from datetime import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    user_name = models.CharField(max_length=50, verbose_name=u"昵称", default="")
    gender = models.CharField(max_length=6, choices=(("male", u"男"), ("female", u"女")), default="female")
    fan_nums = models.IntegerField(default=0, verbose_name="粉丝数量")
    atten_nums = models.IntegerField(default=0, verbose_name="关注数量")
    # 头像， upload_to 指定上传目录
    image = models.ImageField(upload_to="image/%Y/%m", default=u"image/default.png", max_length=100)

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

    # 重载为了打印自定义的字符串
    def __str__(self):
        return self.user_name

        # 获取用户的未读消息的数量
        # def unread_nums(self):
        #     from operation.models import UserMessage
        #     return UserMessage.objects.filter(user=self.id, has_read=False).count()
