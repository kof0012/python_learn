# Generated by Django 2.1.2 on 2018-10-29 03:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('goods', '0018_auto_20181025_1549'),
    ]

    operations = [
        migrations.CreateModel(
            name='HotWord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=128, unique=True, verbose_name='热搜词')),
                ('index', models.PositiveSmallIntegerField(default=0, verbose_name='优先级')),
            ],
            options={
                'verbose_name': '热搜词',
                'verbose_name_plural': '热搜词',
                'ordering': ('index',),
            },
        ),
    ]
