# Generated by Django 2.2 on 2020-01-14 10:44

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('config', '0035_auto_20191211_1642'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Config',
        ),
        migrations.DeleteModel(
            name='StoreName',
        ),
        migrations.DeleteModel(
            name='StoreType',
        ),
    ]
