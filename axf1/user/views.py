import random
import re

from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from user.models import UserModel, UserTicketModel


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
            msg = '请填写完所有信息'
            return render(request, 'user/user_register.html', {'msg': msg})
        if not reg1:
            msg1 = '用户名为8到12位且第一位不能为0的数字或者字母组成'
            return render(request, 'user/user_register.html', {'msg': msg1})
        if not reg2:
            msg2 = '请输入正确的邮箱账号'
            return render(request, 'user/user_register.html', {'msg': msg2})
        if password != password1:
            msg3 = '输入密码不一致 !'
            return render(request, 'user/user_register.html', {'msg': msg3})
        UserModel.objects.create(username=username, password=make_password(password),
                                 email=email, icon=icon, sex=sex)
        return HttpResponseRedirect(reverse('user:login'))


def login(request):

    if request.method == 'GET':

        return render(request, 'user/user_login.html')

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')
        user = ''
        if check_password(password, UserModel.password):

            a = UserModel.objects.filter(username=username, password=password).first()
            user = a

        if not user:
            msg = '账号或密码不正确'
            return render(request, 'user/user_login.html', {'msg': msg})

        ticket = ''
        s = 'abcdefghijkrmnopqrstuvwxyz1234567890'
        for _ in range(28):
            a = random.choice(s)
            ticket += a

        UserTicketModel.ticket = ticket
        response = HttpResponseRedirect(reverse('app1:home'))
        response.set_cookie('ticket', ticket)




def logout(request):

    if request.method == 'GET':

        return render(request, 'user/user_login.html')
