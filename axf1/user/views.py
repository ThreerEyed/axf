
import re
from datetime import datetime, timedelta

from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
# 手动导入
from django.core.urlresolvers import reverse

from user.models import UserModel, UserTicketModel
from utils.functions import get_ticket


def register(request):
    """
    注册用户
    :param request:
    :return:
    """
    if request.method == 'GET':

        return render(request, 'user/user_register.html')

    if request.method == 'POST':

        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password1 = request.POST.get('password1')
        sex = request.POST.get('sex')
        icon = request.FILES.get('icon')

        reg1 = re.match(r'[1-9A-Za-z\u4e00-\u9fa5]{2,12}', username)
        reg2 = re.match(r'[1-9A-Za-z]\w{6,12}@\w{2,5}.[a-z]{3}', email)
        if not all([username, email, password, password1, icon]):
            # 用户信息没输入完全, 提示错误并返回页面错误提示
            msg = '请填写完所有信息'
            return render(request, 'user/user_register.html', {'msg': msg})
        if not reg1:
            # 用户名正则未匹配正确, 返回页面错误提示
            msg1 = '用户名为8到12位且第一位不能为0的数字或者字母组成'
            return render(request, 'user/user_register.html', {'msg': msg1})
        if not reg2:
            # 邮箱匹配不正确, 返回页面错误提示
            msg2 = '请输入正确的邮箱账号'
            return render(request, 'user/user_register.html', {'msg': msg2})
        if password != password1:
            # 密码不一致, 返回页面错误提示
            msg3 = '输入密码不一致 !'
            return render(request, 'user/user_register.html', {'msg': msg3})
        # 保存所有用户信息, 并返回到登录页面
        UserModel.objects.create(username=username, password=make_password(password),
                                 email=email, icon=icon, sex=sex)
        return HttpResponseRedirect(reverse('user:login'))


def login(request):
    """
    登录
    :param request:
    :return:
    """
    # GET请求返回登录页面
    if request.method == 'GET':

        return render(request, 'user/user_login.html')

    if request.method == 'POST':
        # 先验证是否有这个用户
        if UserModel.objects.filter(username=request.POST.get('username')).exists():
            # 得到这个user
            user = UserModel.objects.filter(username=request.POST.get('username')).first()
            # 验证密码
            if check_password(request.POST.get('password'), user.password):
                # 在ticket 在客户端和服务端
                ticket = get_ticket()
                # 绑定cookies 的ticket
                response = HttpResponseRedirect(reverse('app1:home'))
                out_time = datetime.utcnow() + timedelta(hours=8)
                response.set_cookie('ticket', ticket, expires=out_time)
                UserTicketModel.objects.create(user_id=user.id, ticket=ticket, out_time=out_time)
                return response
            return render(request, 'user/user_login.html', {'msg': '用户名或密码错误'})
        else:
            return render(request, 'user/user_login.html', {'msg': '用户名或密码错误'})


def logout(request):

    if request.method == 'GET':
        response = HttpResponseRedirect(reverse('user:login'))
        response.delete_cookie('ticket')

        return response

