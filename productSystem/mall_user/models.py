from django.db import models


class MallUser(models.Model):
    u_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=128, null=False, verbose_name="用户名")
    password = models.CharField(max_length=128, null=False, verbose_name="密码")
    nick_name = models.CharField(max_length=256, null=True, default="user", verbose_name="用户名称")
    phone = models.CharField(max_length=32, null=True, verbose_name="手机号")
    sex = models.BooleanField(null=True, verbose_name="性别")
    avatar = models.CharField(max_length=256, null=True, verbose_name="用户头像")

    class Meta:
        db_table = 'mall_user'
        verbose_name = '商城用户'
        verbose_name_plural = '商城用户'