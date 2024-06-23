# Generated by Django 3.2 on 2024-06-22 05:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('suppliers', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=255, verbose_name='商品名称')),
                ('category', models.CharField(max_length=100, verbose_name='商品类别')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='商品价格')),
                ('spec', models.CharField(max_length=255, null=True, verbose_name='规格')),
                ('product_img', models.CharField(max_length=128, verbose_name='商品图片')),
                ('comment', models.TextField(null=True, verbose_name='备注')),
                ('supplier_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='suppliers.supplier', verbose_name='供应商')),
            ],
            options={
                'verbose_name': '商品',
                'verbose_name_plural': '商品',
                'db_table': 'product',
            },
        ),
    ]
