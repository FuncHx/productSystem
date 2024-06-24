from django.db import models

from suppliers.models import Supplier


class Product(models.Model):
    product_name = models.CharField(max_length=255, verbose_name='商品名称')
    category = models.CharField(max_length=100, verbose_name='商品类别')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='商品价格')
    spec = models.CharField(max_length=255, null=True, verbose_name="规格")
    product_img = models.CharField(max_length=128, null=True, verbose_name="商品图片")
    supplier_id = models.ForeignKey(Supplier, null=True, on_delete=models.SET_NULL, verbose_name='供应商')
    comment = models.TextField(null=True, verbose_name="备注")

    class Meta:
        db_table = 'product'
        verbose_name = '商品'
        verbose_name_plural = '商品'
