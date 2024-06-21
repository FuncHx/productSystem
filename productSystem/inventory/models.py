from django.db import models
from products.models import Product

class Inventory(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, verbose_name='商品')
    stock_quantity = models.IntegerField(verbose_name='库存量')
    last_updated = models.DateTimeField(auto_now=True, verbose_name='最后更新时间')

    class Meta:
        db_table = 'inventory'
        verbose_name = '库存'
        verbose_name_plural = '库存'
