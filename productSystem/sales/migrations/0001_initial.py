# Generated by Django 3.2 on 2024-06-22 05:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SalesOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_date', models.DateField(auto_now=True, verbose_name='订单日期')),
                ('quantity', models.IntegerField(verbose_name='销售数量')),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='总价')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='单价')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product', verbose_name='商品')),
            ],
            options={
                'verbose_name': '销售订单',
                'verbose_name_plural': '销售订单',
                'db_table': 'sales_order',
            },
        ),
    ]
