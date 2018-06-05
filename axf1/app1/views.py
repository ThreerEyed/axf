from django.http import HttpResponseRedirect
from django.shortcuts import render
from app1.models import MainWheel, MainNav, MainMustBuy, MainShop, MainShow, FoodType, Goods
from django.core.urlresolvers import reverse


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
        return HttpResponseRedirect(reverse('app1:use_market', args=('104749', '0', '0')))


def use_market(request, typeid, cid, sid):
    """
    :param request:
    :param typeid:  分类id
    :param cid:  子分类id
    :param sid:  排序id
    """
    if request.method == 'GET':

        foodtypes = FoodType.objects.all()
        # 获取某分类下的商品
        if cid == '0':
            goods = Goods.objects.filter(categoryid=typeid)
        else:
            goods = Goods.objects.filter(categoryid=typeid,
                                         childcid=cid)
        # 重新组装全部分类的参数
        # 组装结果为[['全部分类', '0'], ['酒类', '13550']...]
        # 拿到所有的typeid=typeid   foodtypes 的对象
        foodtypes_current = foodtypes.filter(typeid=typeid).first()
        #  使用split 函数 拿到我们要的结果, 并且将其放在一个列表当中
        if foodtypes_current:

            childtypes = foodtypes_current.childtypenames
            childtypenames = childtypes.split('#')
            child_list = []
            for childtypename in childtypenames:
                child_type_info = childtypename.split(':')
                child_list.append(child_type_info)

        # 排序
        if sid == '0':
            pass
        if sid == '1':
            # 按销量排列
            goods = Goods.objects.order_by('productnum')
        if sid == '2':
            # 降序排列
            goods = Goods.objects.order_by('-price')
        if sid == '3':
            # 升序排列
            goods = Goods.objects.order_by('price')

        data = {
            'foodtypes': foodtypes,
            'goods': goods,
            'typeid': typeid,
            'child_list': child_list,
            'cid': cid
        }

        return render(request, 'market/market.html', data)


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


