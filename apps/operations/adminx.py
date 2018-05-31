# -*- coding:utf-8 -*-
__author__ = 'brynao'
__date__ = '2018/5/15 下午8:25'
import xadmin
from operations.models import *



class BlogCommentsAdmin(object):
    list_display = ['user', 'blog', 'comment', 'add_time']
    search_fields = ['user', 'blog', 'comment']
    list_filter = ['user', 'blog', 'comment', 'add_time']

class UserFavoriteAdmin(object):
    list_display = ['user', 'blog', 'add_time']
    search_fields = ['user', 'blog']
    list_filter = ['user', 'blog', 'add_time']

xadmin.site.register(BlogComments, BlogCommentsAdmin)
xadmin.site.register(UserFavorite, UserFavoriteAdmin)
