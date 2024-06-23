# Generated by Django 3.2 on 2024-06-22 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supplier_name', models.CharField(max_length=255, verbose_name='供应商名称')),
                ('contact_info', models.CharField(max_length=255, verbose_name='联系方式')),
            ],
            options={
                'verbose_name': '供应商',
                'verbose_name_plural': '供应商',
                'db_table': 'suppliers',
            },
        ),
    ]
