from django.db import models
from django.contrib.auth.models import AbstractUser


class AdminUser(AbstractUser):
    username = models.CharField(max_length=255, unique=True, verbose_name="用户名")
    password = models.CharField(max_length=255, verbose_name="密码", default="123456")
    email = models.EmailField(null=True, verbose_name="邮箱")
    phone = models.CharField(max_length=32, null=True, verbose_name="手机号")
    nick_name = models.CharField(max_length=255, default="Admin", verbose_name="昵称")
    avatar = models.CharField(max_length=256, null=True, verbose_name="用户头像")
    update_time = models.DateTimeField(auto_now=True,  verbose_name="更新时间")


    class Meta:
        db_table = "admin_user"
        verbose_name = "管理员表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class UserToken(models.Model):
    user = models.OneToOneField(AdminUser, on_delete=models.CASCADE)
    refresh_token = models.TextField()


class UploadedFile(models.Model):
    file = models.FileField(upload_to='uploaded_files/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "uploaded_files"
        verbose_name = "上传文件"
        verbose_name_plural = verbose_name
