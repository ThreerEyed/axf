from django.shortcuts import render
# from app1.models import MainWheel, MainNav, MainMustBuy, MainShop, MainShow


def home(request):
    """
    首页视图函数
    :param request:
    :return:
    """
    if request.method == 'GET':

        mainwheels = MainWheel.objects.all()
        mainnavs = MainNav.objects.all()
        mainmustbuy = MainMustBuy.objects.all()
        mainshop = MainShop.objects.all()
        mainshow = MainShow.objects.all()
        data = {
            'title': '首页',
            'mainwheels': mainwheels,
            'mainnavs': mainnavs,
            'mainmustbuy': mainmustbuy,
            'mainshop': mainshop,
            'mainshow': mainshow,

        }

        return render(request, 'home/home.html', data)


def cart(request):
    """
    购物车视图函数
    :param request:
    :return:
    """
    if request.method == 'GET':

        return render(request, 'cart/cart.html')


def market(request):
    """
    商品列表
    :param request:
    :return:
    """
    if request.method == 'GET':
        return render(request, 'market/market.html')


def mine(request):
    """
    mine
    :param request:
    :return:
    """
    if request.method == 'GET':
        return render(request, 'mine/mine.html')


def order_info(request):
    """
    订单信息
    :param request:
    :return:
    """
    if request.method == 'GET':
        return render(request, 'order/order_info.html')


def order_list_payed(request):
    """
    已付款订单信息
    :param request:
    :return:
    """
    if request.method == 'GET':
        return render(request, 'order/order_list_payed.html')


def order_list_wait_pay(request):
    """
    已支付订单信息
    :param request:
    :return:
    """
    if request.method == 'GET':
        return render(request, 'order/order_list_wait_pay.html')


