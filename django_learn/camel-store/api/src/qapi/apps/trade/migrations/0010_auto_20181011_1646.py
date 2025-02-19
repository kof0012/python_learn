# Generated by Django 2.1.2 on 2018-10-11 08:46

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('trade', '0009_orderinfo_remark'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderinfo',
            name='receive_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='收货时间'),
        ),
        migrations.AddField(
            model_name='orderinfo',
            name='send_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='发货时间'),
        ),
        migrations.AddField(
            model_name='orderinfo',
            name='share_openid',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='分享用户的openID'),
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='pay_status',
            field=models.CharField(
                choices=[('paying', '待付款'), ('sending', '待发货'), ('receiving', '待收货'), ('over', '已收货'),
                         ('close', '已关闭')], default='paying', max_length=30, verbose_name='订单状态'),
        ),
    ]
