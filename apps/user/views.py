from django.shortcuts import render
from django.views.generic.base import View  # 继承View 完成基于类的用户登陆
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password  # 对明文加密
from django.core import serializers
import json
from django.http import JsonResponse


from operations.models import UserAttention
from user.models import User

# 基于类做用户登陆
class LoginView(View):
    # 会根据 method 调用 post或者get方法
    def post(self, request):
        # 从POST中取出用户名和密码
        user_name = request.POST.get("username", "")
        pass_word = request.POST.get("password", "")
        # 使用django.contrib.auth中authenticate方法验证用户名和密码
        user = authenticate(username=user_name, password=pass_word)
        if user is not None:      # 如果成功返回 对象，失败返回 None
            login(request, user)  # 调用login方法登陆账号

            return HttpResponse('{"msg": "成功","status": 0}', content_type='application/json')
        else:
            return HttpResponse('{"msg": "用户名或密码错误","status": 1}', content_type='application/json')


class RegisterView(View):
    def get(self, request):
        return render(request, "register.html")

    def post(self, request):
        user_name = request.POST.get("username", "")
        if User.objects.filter(username=user_name):
            # return render(request, "register.html", {"msg": "用户已经存在"})
            return HttpResponse('{"msg": "该用户名已经存在","status": 1}', content_type='application/json')
        pass_word = request.POST.get("password", "")
        # 实例化用户，然后赋值
        user_profile = User()
        user_profile.username = user_name
        # 将明文转换为密文赋给password
        user_profile.password = make_password(pass_word)
        user_profile.save()  # 保存到数据库
        return HttpResponse('{"msg": "注册成功","status": 0}', content_type='application/json')

class LogoutView(View):
    """
    用户登出
    """
    def get(self, request):
        logout(request)
        return HttpResponse('{"msg": "退出登录","status": 0}', content_type='application/json')


# 用户关注列表
class UserAttentionView(View):
    def get(self, request):
        response = {}
        # 用户关注的用户id列表
        user_id = request.GET.get("user_id","")
        user = User.objects.get(id=int(user_id))

        atten_list = []
        all_atten = UserAttention.objects.filter(user=user)
        for user in all_atten:
            atten_list.append(user.attention_id_id)

        # 筛选出被关注用户信息
        all_atten = User.objects.filter(id__in=atten_list)
        response['list'] = json.loads(serializers.serialize("json", all_atten))
        response['msg'] = "success"
        return JsonResponse(response)

# 用户粉丝列表
class UserFanView(View):
    def get(self, request):
        response = {}
        fan_list = []
        user_id = request.GET.get("user_id", "")
        all_fan = UserAttention.objects.filter(attention_id=user_id)
        for user in all_fan:
            fan_list.append(user.user_id)

        all_fan = User.objects.filter(id__in=fan_list)
        response['list'] = json.loads(serializers.serialize("json", all_fan))
        response['msg'] = "success"
        return JsonResponse(response)

class UserInfoView(View):
    def get(self, request):
        response = {}
        user_id = request.GET.get('user_id', '')
        user = User.objects.filter(id=user_id)
        response['User'] = json.loads(serializers.serialize("json", user))
        response['msg'] = 'success'
        return JsonResponse(response)

class UploadImageView(View):
    def post(self, request):
        user = request.user
        user.image = request.FILES.get("img")
        user.save()
        return HttpResponse('{"msg": "图片上传成功","status": 0}', content_type='application/json')







