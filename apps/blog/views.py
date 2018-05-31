from django.shortcuts import render
from django.views.generic.base import View
from django.http import HttpResponse

from blog.models import Blog
from operations.models import BlogComments, UserAttention, UserPraise, UserFavorite
from user.models import User
from django.core import serializers
import json
from django.http import JsonResponse


class BlogListView(View):
    def get(self, request):
        if not request.user.is_authenticated():
            return HttpResponse('{"status": "fail", "msg":"用户未登陆"}', content_type='application/json')
        user_id = request.GET.get("user_id", "")
        user = User.objects.get(id=int(user_id))
        # 用户的关注列表
        atten_list = []
        all_atten = UserAttention.objects.filter(user=user)
        for user in all_atten:
            atten_list.append(user.attention_id_id)
        all_blog = Blog.objects.filter(user__in=atten_list)
        response = {}
        response['list'] = json.loads(serializers.serialize("json",all_blog))
        response['msg'] = 'success'
        return JsonResponse(response)

#  显示所有评论
class BlogCommentsView(View):
    def get(self, request):
        if not request.user.is_authenticated():
            return HttpResponse('{"status": "fail", "msg":"用户未登陆"}', content_type='application/json')
        blog_id = request.GET.get("blog_id", "")
        comments = BlogComments.objects.filter(blog_id=blog_id)
        response = {}
        response['list'] = json.loads(serializers.serialize("json", comments))
        response['msg'] = 'success'
        return JsonResponse(response)

# 用户自己微博
class UserBlogListView(View):
    def get(self, request):
        if not request.user.is_authenticated():
            return HttpResponse('{"status": "fail", "msg":"用户未登陆"}', content_type='application/json')

        response = {}
        user_id = request.GET.get("user_id", "")
        blog = Blog.objects.filter(user=user_id)
        response['list'] = json.loads(serializers.serialize("json", blog))
        response['msg'] = 'success'
        return JsonResponse(response)

class HotBlogView(View):
    def get(self, request):
        response = {}
        blog = Blog.objects.all().order_by("-pra_num")
        response['list'] = json.loads(serializers.serialize("json", blog))
        response['msg'] = 'success'
        return JsonResponse(response)

class UserPraBlogView(View):
    def get(self, request):
        user_id = request.GET.get("user_id", "")
        pra_list = []
        user = User.objects.filter(id=int(user_id))
        user_pra = UserPraise.objects.filter(user=user)

        for blog in user_pra:
            pra_list.append(blog.id)

        blog = Blog.objects.filter(id__in=user_pra)
        response = {}
        response['list'] = json.loads(serializers.serialize("json", blog))
        response['msg'] = 'success'
        return JsonResponse(response)


class UserFavBlogView(View):
    def get(self, request):
        user_id = request.GET.get("user_id", "")
        fav_list = []
        user = User.objects.filter(id=int(user_id))
        user_fav = UserFavorite.objects.filter(user=user)

        for blog in user_fav:
            fav_list.append(blog.id)

        blog = Blog.objects.filter(id__in=user_fav)
        response = {}
        response['list'] = json.loads(serializers.serialize("json", blog))
        response['msg'] = 'success'
        return JsonResponse(response)