# Generated by Django 2.1.7 on 2019-03-13 07:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AreaInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('atitle', models.CharField(max_length=20, verbose_name='标题')),
                ('aParent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                                              to='booktest.AreaInfo')),
            ],
        ),
        migrations.CreateModel(
            name='PicTest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goods_pic', models.ImageField(upload_to='booktest')),
            ],
        ),
    ]
