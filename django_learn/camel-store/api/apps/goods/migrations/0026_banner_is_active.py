# Generated by Django 2.1.4 on 2018-12-18 10:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('goods', '0025_auto_20181212_1407'),
    ]

    operations = [
        migrations.AddField(
            model_name='banner',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='是否启用'),
        ),
    ]
