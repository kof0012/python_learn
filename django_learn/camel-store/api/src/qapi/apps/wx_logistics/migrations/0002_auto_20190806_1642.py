# Generated by Django 2.1.8 on 2019-08-06 08:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('wx_logistics', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='deliveryaccount',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='是否启用'),
        ),
        migrations.AddField(
            model_name='sender',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='是否启用'),
        ),
    ]
