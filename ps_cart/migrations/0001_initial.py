# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-04-09 09:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ps_user', '0002_auto_20180307_1116'),
        ('ps_goods', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=0)),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ps_goods.GoodsInfo')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ps_user.UserInfo')),
            ],
        ),
    ]
