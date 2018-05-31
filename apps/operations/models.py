from datetime import datetime
from django.db import models

from blog.models import Blog
from user.models import User

class BlogComments(models.Model):
    user = models.ForeignKey(User, verbose_name="用户")
    blog = models.ForeignKey(Blog, verbose_name="微博")
    comment = models.CharField(max_length=200, verbose_name="评论")
    add_time = models.DateField(default=datetime.now, verbose_name="添加时间")
    class Meta:
        verbose_name = u"用户评论"
        verbose_name_plural = verbose_name

# 用户收藏
class UserFavorite(models.Model):
    user = models.ForeignKey(User, verbose_name="用户")
    blog = models.IntegerField(default=0, verbose_name="微博")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")
    class Meta:
        verbose_name = u"用户收藏"
        verbose_name_plural = verbose_name

# 用户点赞
class UserPraise(models.Model):
    user = models.ForeignKey(User, verbose_name="用户")
    blog = models.IntegerField(default=0, verbose_name="微博")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"用户点赞"
        verbose_name_plural = verbose_name

# 用户的关注
class UserAttention(models.Model):
    user = models.ForeignKey(User, verbose_name="用户", related_name="user")
    attention_id = models.ForeignKey(User, verbose_name="用户id", related_name="atten")
    class Meta:
        verbose_name = u"用户关注"
        verbose_name_plural = verbose_name

# 用户的粉丝
class UserFan(models.Model):
    user = models.ForeignKey(User, verbose_name="用户")
    fan_id = models.IntegerField(verbose_name="用户id")
    class Meta:
        verbose_name = "用户关注"
        verbose_name_plural = verbose_name

