from django.db import models
from products.models import Product

class SalesOrder(models.Model):
    order_date = models.DateField(verbose_name='订单日期')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='商品')
    quantity = models.IntegerField(verbose_name='销售数量')
    total_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='总价')

    class Meta:
        db_table = 'sales_order'
        verbose_name = '销售订单'
        verbose_name_plural = '销售订单'

class SalesDetail(models.Model):
    order = models.ForeignKey(SalesOrder, on_delete=models.CASCADE, verbose_name='订单')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='商品')
    quantity = models.IntegerField(verbose_name='销售数量')
    price_per_unit = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='每单位价格')

    class Meta:
        db_table = 'sales_detail'
        verbose_name = '销售详情'
        verbose_name_plural = '销售详情'
