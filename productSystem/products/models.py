from django.db import models

class Product(models.Model):
    product_name = models.CharField(max_length=255, verbose_name='商品名称')
    category = models.CharField(max_length=100, verbose_name='商品类别')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='商品价格')
    stock_quantity = models.IntegerField(verbose_name='库存量')

    class Meta:
        db_table = 'product'
        verbose_name = '商品'
        verbose_name_plural = '商品'
