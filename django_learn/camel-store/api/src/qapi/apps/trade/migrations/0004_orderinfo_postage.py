# Generated by Django 2.0.7 on 2018-07-19 09:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('trade', '0003_auto_20180719_1609'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderinfo',
            name='postage',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=15, verbose_name='邮费'),
        ),
    ]
