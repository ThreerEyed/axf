from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.shortcuts import render
from app1.models import MainWheel, MainNav, MainMustBuy, MainShop, MainShow, FoodType, Goods, CartModel, OrderModel, \
    OrderGoodsModel
from django.core.urlresolvers import reverse

from utils.functions import get_order_id


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
        # 获取用户
        user = request.user
        # 查询购物车信息
        # order =
        user_carts = CartModel.objects.filter(user=user)

        if user_carts:
            data = {
                'user_carts': user_carts
            }

            return render(request, 'cart/cart.html', data)
        return render(request, 'cart/cart.html', {'msg': '购物车是空哒'})


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

        user = request.user

        if user:
            user_cart = CartModel.objects.filter(user=user)

        else:
            user_cart = ''
        data = {
            'foodtypes': foodtypes,
            'goods': goods,
            'typeid': typeid,
            'child_list': child_list,
            'cid': cid,
            'user_cart': user_cart
        }

        return render(request, 'market/market.html', data)


def add_cart(request):
    """
    购物车添加
    :param request:
    """
    if request.method == 'POST':
        # 拿到request中的user
        user = request.user
        # 拿到商品的id
        goods_id = request.POST.get('goods_id')

        data = {
            'code': 200,
            'msg': '请求成功'
        }
        # 判断这个用户时候系统自带的还是当前的用户
        if user.id:
            user_carts = CartModel.objects.filter(user=user,
                                                  goods_id=goods_id).first()
            if user_carts:
                user_carts.c_num += 1
                user_carts.save()
                data['c_num'] = user_carts.c_num
            else:
                CartModel.objects.create(user=user,
                                         goods_id=goods_id)
                data['c_num'] = 1

            return JsonResponse(data)
        data['code'] = '403'
        data['msg'] = '当前用户没有登录, 请登录'
        return JsonResponse(data)


def sub_cart(request):
    """
    购物车减少商品对应的数量
    :param request:
    """
    if request.method == 'POST':
        user = request.user
        goods_id = request.POST.get('goods_id')


        data = {
            'code': 200,
            'msg': '请求成功'
        }
        if user.id:
            user_cart = CartModel.objects.filter(user_id=user.id,
                                                 goods_id=goods_id).first()
            if user_cart:
                if user_cart.c_num > 1:
                    user_cart.c_num -= 1
                    user_cart.save()
                    data['c_num'] = user_cart.c_num
                else:
                    user_cart.delete()
                    data['c_num'] = 0
                    if data['c_num'] == 0:
                        data = {
                            'code': 200,
                            'msg': '请求成功',
                            'c_num': 0
                        }
                        return JsonResponse(data)
                return JsonResponse(data)
        data['msg'] = '当前用户没有登录, 请前往登录'
        return JsonResponse(data)


def change_select_status(request):

    if request.method == 'POST':

        user = request.user
        cart_id = request.POST.get('cart_id')
        cart = CartModel.objects.filter(id=cart_id).first()
        if cart.is_select:
            cart.is_select = False
        else:
            cart.is_select = True
        cart.save()

        data = {
            'code': 200,
            'msg': '请求成功',
            'is_select': cart.is_select
        }
        return JsonResponse(data)


def change_all(request):

    if request.method == 'POST':

        user = request.user
        user_cart = CartModel.objects.filter(user=user)
        for cart in user_cart:
            cart.is_select = True
            cart.save()


def change_order_status(request):

    if request.method == 'POST':

        order_id = request.POST.get('order_id')

        OrderModel.objects.filter(id=order_id).update(o_status=1)

        return JsonResponse({'code': 200, 'msg': '请求成功'})


def g_order(request):
    """
    生成订单
    :param request:
    :return:
    """

    if request.method == 'GET':

        user = request.user
        user_carts = CartModel.objects.filter(user=user, is_select=True)

        if user_carts:
            order_num = get_order_id()
            # 下单
            order = OrderModel.objects.create(user=user,
                                              o_num=order_num)

            # 选择勾选的商品进行下单
            for carts in user_carts:
                # 创建商品和订单之间的关系
                OrderGoodsModel.objects.create(goods=carts.goods,
                                               order=order,
                                               goods_num=carts.c_num)
            user_carts.delete()

            return render(request, 'order/order_info.html', {'order': order})

        return render(request, 'cart/cart.html', {'msg': '购物车是空哒=.='})


def order_wait_pay(request):
    """
    等待支付
    :param request:
    :return:
    """

    if request.method == 'GET':

        user = request.user
        orders = OrderModel.objects.filter(user=user, o_status=0)
        return render(request, 'order/order_list_wait_pay.html', {'orders': orders})


def pay_my_goods(request):

    if request.method == 'GET':
        order_id = request.GET.get('order_id')
        order = OrderGoodsModel.objects.filter(order_id=order_id).first().order
        return render(request, 'order/order_info.html', {'order': order})


def order_payed(request):

    if request.method == 'GET':
        user = request.user
        orders = OrderModel.objects.filter(user=user, o_status=1)

        return render(request, 'order/order_list_payed.html', {'orders': orders})


def mine(request):
    """
    mine
    :param request:
    :return:
    """
    if request.method == 'GET':

        user = request.user
        orders = OrderModel.objects.filter(user=user)
        payed, wait_pay = 0, 0
        for order in orders:
            if order.o_status == 0:
                wait_pay += 1
            if order.o_status == 1:
                payed += 1

        data = {
            'wait_pay': wait_pay,
            'payed': payed
        }
        return render(request, 'mine/mine.html', data)


def all_price(request):

    if request.method == 'GET':
        user = request.user
        # 查询购物车信息
        user_carts = CartModel.objects.filter(user=user)
        user_cart = CartModel.objects.filter(user=user)
        t_price = 0
        for cart in user_cart:
            goods = Goods.objects.filter(id=cart.goods_id).first()
            if cart.is_select:
                t_price += cart.c_num * goods.price
                t_price = round(t_price, 3)

        data = {
            "code": 200,
            # 'user_carts': user_carts,
            't_price': t_price
        }

        return JsonResponse(data)




