from django.db import models

from user.models import UserModel


class Main(models.Model):

    # 图片字段
    img = models.CharField(max_length=200)
    # 名称字段
    name = models.CharField(max_length=100)
    # 通用id
    trackid = models.CharField(max_length=16)

    class Meta:
        abstract = True


class MainWheel(Main):

    # 轮播banner
    class Meta:
        db_table = 'axf_wheel'


class MainNav(Main):

    # 导航
    class Meta:
        db_table = 'axf_nav'


class MainMustBuy(Main):

    # 必购
    class Meta:
        db_table = 'axf_mustbuy'


class MainShop(Main):

    # 商店
    class Meta:
        db_table = 'axf_shop'


# 主要展示的商品
class MainShow(Main):

    categoryid = models.CharField(max_length=16)
    # 分类名称
    brandname = models.CharField(max_length=100)

    img1 = models.CharField(max_length=200)
    childcid1 = models.CharField(max_length=16)
    productid1 = models.CharField(max_length=16)
    # 商品名称
    longname1 = models.CharField(max_length=100)
    # 原价格
    price1 = models.FloatField(default=0)
    # 折后价格
    marketprice1 = models.FloatField(default=1)

    img2 = models.CharField(max_length=200)
    childcid2 = models.CharField(max_length=16)
    productid2 = models.CharField(max_length=16)
    # 商品名称
    longname2 = models.CharField(max_length=100)
    # 原价格
    price2 = models.FloatField(default=0)
    # 折后价格
    marketprice2 = models.FloatField(default=1)

    img3 = models.CharField(max_length=200)
    childcid3 = models.CharField(max_length=16)
    productid3 = models.CharField(max_length=16)
    # 商品名称
    longname3 = models.CharField(max_length=100)
    # 原价格
    price3 = models.FloatField(default=0)
    # 折后价格
    marketprice3 = models.FloatField(default=1)

    class Meta:
        db_table = 'axf_mainshow'


class FoodType(models.Model):
    # 分类id
    typeid = models.CharField(max_length=16)
    # 商品分类名
    typename = models.CharField(max_length=100)
    # 商品的子分类名
    childtypenames = models.CharField(max_length=200)
    # 排序
    typesort = models.IntegerField(default=1)

    class Meta:
        db_table = 'axf_foodtypes'


class Goods(models.Model):
    # 商品的id
    productid = models.CharField(max_length=16)
    # 商品的图片
    productimg = models.CharField(max_length=200)
    # 商品的名称
    productname = models.CharField(max_length=100)
    # 商品的规格名
    productlongname = models.CharField(max_length=200)
    isxf = models.IntegerField(default=1)
    pmdesc = models.CharField(max_length=200)
    # 规格
    specifics = models.CharField(max_length=100)
    # 折后价格
    price = models.FloatField(default=1)
    # 原价格
    marketprice = models.FloatField(default=1)
    # 分类id
    categoryid = models.CharField(max_length=16)
    # 子分类id
    childcid = models.CharField(max_length=16)
    # 名称
    childcidname = models.CharField(max_length=100)
    dealerid = models.CharField(max_length=16)
    # 排序
    storenums = models.IntegerField(default=1)
    # 销量排序
    productnum = models.IntegerField(default=1)

    class Meta:
        db_table = 'axf_goods'





class CartModel(models.Model):

    # 关联用户
    user = models.ForeignKey(UserModel)
    # 关联商品
    goods = models.ForeignKey(Goods)
    # 商品的个数
    c_num = models.IntegerField(default=1)
    # 商品是否被选择
    is_select = models.BooleanField(default=True)

    class Meta:
        db_table = 'axf_cart'


class OrderModel(models.Model):
    # 关联用户
    user = models.ForeignKey(UserModel)
    # 数量
    o_num = models.CharField(max_length=64)
    # 0代表已下单, 但是未付款, 1 已付款未发货 2 已付款, 已发货
    o_status = models.IntegerField(default=0)
    o_create = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'axf_order'


class OrderGoodsModel(models.Model):
    # 关联的商品
    goods = models.ForeignKey(Goods)
    # 关联的订单
    order = models.ForeignKey(OrderModel)
    # 商品的个数
    goods_num = models.IntegerField(default=1)

    class Meta:
        db_table = 'axf_order_goods'



