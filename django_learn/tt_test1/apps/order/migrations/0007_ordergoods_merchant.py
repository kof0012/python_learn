# Generated by Django 2.1 on 2019-05-26 07:59

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('order', '0006_orderinfo_pay_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordergoods',
            name='merchant',
            field=models.ForeignKey(default=3, limit_choices_to={'is_merchant': True},
                                    on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL,
                                    verbose_name='商家'),
            preserve_default=False,
        ),
    ]
