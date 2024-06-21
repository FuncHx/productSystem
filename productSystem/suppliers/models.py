from django.db import models
from products.models import Product

class Supplier(models.Model):
    supplier_name = models.CharField(max_length=255, verbose_name='供应商名称')
    contact_info = models.CharField(max_length=255, verbose_name='联系方式')

    class Meta:
        db_table = 'suppliers'
        verbose_name = '供应商'
        verbose_name_plural = '供应商'

class SupplierProduct(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, verbose_name='供应商')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='商品')

    class Meta:
        db_table = 'supplier_products'
        verbose_name = '供应商商品'
        verbose_name_plural = '供应商商品'

