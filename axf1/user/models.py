from django.db import models


class UserModel(models.Model):
    # 用户名
    username = models.CharField(max_length=32, unique=True)
    # 密码
    password = models.CharField(max_length=256)
    email = models.CharField(max_length=64, unique=True)
    # 性别  False 代表女
    sex = models.BooleanField(default=False)
    # 头像
    icon = models.ImageField(upload_to='icons')
    # 是否删除
    is_delete = models.BooleanField(default=False)

    class Meta:
        db_table = 'axf_users'


class UserTicketModel(models.Model):
    # 关联用户
    user = models.ForeignKey(UserModel)
    # 密码
    ticket = models.CharField(max_length=256)
    # 过期时间
    out_time = models.DateTimeField()

    class Meta:
        db_table = 'axf_users_ticket'
