# Generated by Django 2.1.7 on 2019-02-28 10:07

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('goods', '0044_auto_20190220_1653'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='goods',
            options={'ordering': ('status', 'index', 'id'), 'permissions': (('create_template', '创建商品模板'),),
                     'verbose_name': '商品', 'verbose_name_plural': '商品'},
        ),
    ]
