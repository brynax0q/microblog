# -*- coding:utf-8 -*-
__author__ = 'brynao'
__date__ = '2018/5/15 下午7:44'
import xadmin
from blog.models import Blog


class BlogAdmin(object):
    list_display = ['content', 'pra_num', 'comments_num', 'fav_num', 'add_time']
    ordering = ['-add_time']
    readonly_fields = ['comments_num', 'fav_num', 'pra_num']


xadmin.site.register(Blog, BlogAdmin)