
from django.conf.urls import url
from app1 import views

urlpatterns = [
    # 首页
    url(r'^home/', views.home, name='home'),
    # 购物车
    url(r'^cart/', views.cart, name='cart'),
    # 超市
    url(r'^market/', views.market, name='market'),
    # mine
    url(r'^mine/', views.mine, name='mine'),
    # 用户订单
    url(r'^order_info/', views.order_info, name='order_info'),
    url(r'^order_list_payed/', views.order_list_payed, name='order_list_payed'),
    url(r'^order_list_wait_pay/', views.order_list_wait_pay, name='order_list_wait_pay')
    # 关于用户
]
