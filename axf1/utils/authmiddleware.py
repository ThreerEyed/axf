from datetime import datetime

from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils.deprecation import MiddlewareMixin
from django.core.urlresolvers import reverse


# 定义中间件这个类
from user.models import UserTicketModel


class UserAuthMiddle(MiddlewareMixin):

    def process_request(self, request):
        """
        验证方法
        :param request:
        :return:
        """
        # 先验证路径是否是登录或者注册, 如果是登录注册直接返回
        path = request.path
        # 需要登录验证的, 个人中心和购物车
        path_list = ['/user/login/', '/user/register/']
        if path in path_list:
            return

        # 验证请求的COOKIE中是否有ticket
        ticket = request.COOKIES.get('ticket')
        if not ticket:
            return HttpResponseRedirect(reverse('user:login'))

        user = UserTicketModel.objects.filter(ticket=ticket).first()
        out_time = datetime.utcnow()
        if out_time > user.out_time.replace(tzinfo=None):
            UserTicketModel.objects.filter(user=user).delete()
            return HttpResponseRedirect(reverse('user:login'))
        else:
            UserTicketModel.objects.filter(Q(user_id=user.user_id) &
                                           ~Q(ticket=ticket)).delete()
        if not user:
            return HttpResponseRedirect(reverse('user:login'))

        request.user = user
        # 删除多余的信息, 从userticket 中查询当前的user 并且ticjet不等于cookie中deticket




