# -*- coding:utf-8 -*-
__author__ = 'brynao'
__date__ = '2018/5/15 下午7:57'
import xadmin
from xadmin import views

class GlobalSettings(object):
    site_title = "微博"
    site_footer = "微博"
    # menu_style = "accordion"   # 菜单收起

# 主题
class BaseSetting(object):
    # 打开主题
    enable_themes = True
    use_bootswatch = True


xadmin.site.register(views.CommAdminView, GlobalSettings)
xadmin.site.register(views.BaseAdminView, BaseSetting)

