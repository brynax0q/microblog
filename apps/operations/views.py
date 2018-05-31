from django.shortcuts import render
from django.views.generic.base import View
from django.http import HttpResponse



from blog.models import Blog
from user.models import User
from operations.models import BlogComments, UserFavorite, UserPraise, UserAttention, UserFan


# 发送微博
class SendBlogView(View):
    def post(self, request):
        if not request.user.is_authenticated:
            return HttpResponse('{"status": "fail", "msg":"用户未登陆"}', content_type='application/json')
        else:
            content = request.POST.get("content", "none")
            blog = Blog()
            blog.user = request.user
            blog.content = content
            blog.save()
            return HttpResponse('{"status": "success", "msg": "发表成功"}', content_type='application/json')


# 给微博添加评论
class AddCommentsView(View):
    def post(self, request):
        if not request.user.is_authenticated:
            return HttpResponse('{"status": "fail", "msg":"用户未登陆"}', content_type='application/json')

        blog_id = request.POST.get("blog_id", 0)
        comments = request.POST.get("comments")
        if comments:
            blog_comments = BlogComments()
            blog = Blog.objects.get(id=int(blog_id))
            blog_comments.user = request.user
            blog_comments.blog = blog
            blog_comments.comment = comments
            blog_comments.save()
            return HttpResponse('{"status": "success", "mag": "添加成功"}', content_type='application/json')
        else:
            return HttpResponse('{"status": "fail", "mag": "评论不能为空"}', content_type='application/json')

# 收藏
class AddFavView(View):
    def post(self, request):
        # blog_id
        blog_id = request.POST.get('blog_id', "")

        # 判断用户是否登陆
        if not request.user.is_authenticated():
            return HttpResponse('{"status": "fail", "msg":"用户未登陆"}', content_type='application/json')

        exist_records = UserFavorite.objects.filter(user=request.user, blog=int(blog_id))
        if exist_records:
            # 如果记录已经存在， 则表示用户取消收藏
            exist_records.delete()
            # 取消收藏 收藏数减一
            blog = Blog.objects.get(id=int(blog_id))
            blog.fav_num -= 1
            if blog.fav_num <= 0:
                blog.fav_num = 0
            blog.save()
            return HttpResponse('{"status": "success", "msg":"取消收藏成功"}', content_type='application/json')
        else:
            # 否则用户收藏 收藏数加一
            user_fav = UserFavorite()
            user_fav.user = request.user
            user_fav.blog = blog_id
            user_fav.save()
            blog = Blog.objects.get(id=int(blog_id))
            blog.fav_num += 1
            blog.save()
            return HttpResponse('{"status": "success", "msg":"收藏成功"}', content_type='application/json')

# 点赞
class AddPraiseView(View):
    def post(self, request):
        # blog_id
        blog_id = request.POST.get('blog_id', "")

        # 判断用户是否登陆
        if not request.user.is_authenticated():
            return HttpResponse('{"status": "fail", "msg":"用户未登陆"}', content_type='application/json')

        exist_records = UserPraise.objects.filter(user=request.user, blog=int(blog_id))
        if exist_records:
            # 如果记录已经存在， 则表示用户取消点赞
            exist_records.delete()
            # 取消点赞 点赞数减一
            blog = Blog.objects.get(id=int(blog_id))
            blog.pra_num -= 1
            if blog.pra_num <= 0:
                blog.pra_num = 0
            blog.save()
            return HttpResponse('{"status": "success", "msg":"取消点赞成功"}', content_type='application/json')
        else:
            # 否则用户收藏 收藏数加一
            user_fav = UserPraise()
            user_fav.user = request.user
            user_fav.blog = blog_id
            user_fav.save()
            blog = Blog.objects.get(id=int(blog_id))
            blog.pra_num += 1
            blog.save()
            return HttpResponse('{"status": "success", "msg":"点赞成功"}', content_type='application/json')

# 用户添加关注
class AddAttentionView(View):
    def post(self, request):
        # blog_id
        user_id = request.POST.get('user_id', "")

        # 判断用户是否登陆
        if not request.user.is_authenticated():
            return HttpResponse('{"status": "fail", "msg":"用户未登陆"}', content_type='application/json')

        exist_records = UserAttention.objects.filter(user=request.user, attention_id=int(user_id))
        if exist_records:
            # 如果记录已经存在， 则表示用户取消关注
            exist_records.delete()
            # 取消关注 关注数减一 被关注粉丝减一
            user = request.user
            user1 = User.objects.get(id=int(user_id))

            user.atten_nums -= 1
            user1.fan_nums -= 1
            if user.atten_nums <= 0:
                user.atten_nums = 0

            if user.fan_nums <= 0:
                user1.fan_nums = 0
            user.save()
            user1.save()
            return HttpResponse('{"status": "success", "msg":"取消关注成功"}', content_type='application/json')
        else:
            # 否则用户关注 关注数加一  被关注粉丝加一
            user_atten = UserAttention()
            user_atten.user = request.user
            user_atten.attention_id = User.objects.get(id=int(user_id))
            user_atten.save()
            user = request.user
            user.atten_nums += 1
            user.save()
            user1 = User.objects.get(id=user_id)
            user1.fan_nums += 1
            user1.save()
            return HttpResponse('{"status": "success", "msg":"已关注"}', content_type='application/json')
















