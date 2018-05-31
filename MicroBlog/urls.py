"""MicroBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
import xadmin


from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView

# 处理静态文件
from django.views.static import serve
from MicroBlog.settings import MEDIA_ROOT

from user.views import LoginView, RegisterView, LogoutView, UserAttentionView, UserFanView
from operations.views import SendBlogView, AddCommentsView, AddFavView, AddPraiseView, AddAttentionView
from blog.views import BlogCommentsView, BlogListView, UserBlogListView, HotBlogView, UserPraBlogView, UserFavBlogView
from user.views import UserInfoView, UploadImageView

urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    # 登录和注册
    url('^login/$', LoginView.as_view(), name="login"),
    url('^register/$', RegisterView.as_view(), name="register"),
    url('^logout/$', LogoutView.as_view(), name="logout"),

    # 用户操作
    url('^send_blog/$', SendBlogView.as_view(), name="send_blog"),
    url('^add_comment/$', AddCommentsView.as_view(), name="add_comment"),
    url('^add_fav/$', AddFavView.as_view(), name="add_fav"),
    url('^add_praise/$', AddPraiseView.as_view(), name="add_praise"),
    url('^atten_user/$', AddAttentionView.as_view(), name="add_atten"),

    # 信息返回
    url('^atten_list/$', UserAttentionView.as_view(), name="add_list"),
    url('^fan_list/$', UserFanView.as_view(), name="fan_user"),
    url(r'^user_info/$', UserInfoView.as_view(), name="user_info"),
    url(r'^user_blog/$', UserBlogListView.as_view(), name="user_info"),
    url(r'^hot_blog/$', HotBlogView.as_view(), name="hot_blog"),
    url(r'^user_pra/$', UserPraBlogView.as_view(), name="user_pra"),
    url(r'^user_fav/$', UserFavBlogView.as_view(), name="user_fav"),

    # 微博评论页面
    url(r'^blog_list/$', BlogListView.as_view(), name="blog_list"),
    url(r'^comment_list/$', BlogCommentsView.as_view(), name="course_comment"),
    # 图片上传
    url(r'^image_upload/$', UploadImageView.as_view(), name="image_upload"),







]
