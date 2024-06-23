from django.db import models

class Supplier(models.Model):
    supplier_name = models.CharField(max_length=255, verbose_name='供应商名称')
    contact_info = models.CharField(max_length=255, verbose_name='联系方式')

    class Meta:
        db_table = 'suppliers'
        verbose_name = '供应商'
        verbose_name_plural = '供应商'

