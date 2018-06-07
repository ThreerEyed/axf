
from django.conf.urls import url
from app1 import views

urlpatterns = [
    # 首页
    url(r'^home/', views.home, name='home'),
    # 购物车
    url(r'^cart/', views.cart, name='cart'),
    # 闪购超市
    url(r'^market/$', views.market, name='market'),
    url(r'^market/(\d+)/(\d+)/(\d+)', views.use_market, name='use_market'),
    # 个人中心
    url(r'^mine/', views.mine, name='mine'),

    # 添加购物车
    url(r'^addCart/', views.add_cart, name='addCart'),
    url(r'^subCart/', views.sub_cart, name='subCart'),

    # 修改购物车中商品的选择情况
    url(r'^changeSelectStatus/', views.change_select_status, name='change'),

    # 下单
    url(r'^g_order/', views.g_order, name='g_order'),

    # 修改名单状态
    url(r'^changeOrderStatus/', views.change_order_status, name='change_order_status'),

    # 待付款订单
    url(r'^waitPay/', views.order_wait_pay, name='order_wait_pay'),

    # 付款页面
    url(r'^payMygoods/', views.pay_my_goods, name='pay_my_goods'),

    # 待收货
    url(r'^payed/', views.order_payed, name='order_payed'),

    # 总价
    url(r'^allPrice/', views.all_price, name='all_price'),

]
