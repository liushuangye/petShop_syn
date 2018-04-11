# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-03-07 03:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GoodsInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gtitle', models.CharField(max_length=20)),
                ('gpicture', models.ImageField(upload_to='ps_goods')),
                ('gprice', models.DecimalField(decimal_places=2, max_digits=7)),
                ('isDelete', models.BooleanField(default=False)),
                ('gunit', models.CharField(default='\u4ef6', max_length=10)),
                ('gclick', models.IntegerField()),
                ('gstock', models.IntegerField()),
                ('gcontent', tinymce.models.HTMLField()),
            ],
        ),
        migrations.CreateModel(
            name='TypeInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ttitle', models.CharField(max_length=20)),
                ('isDelete', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='goodsinfo',
            name='gtype',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ps_goods.TypeInfo'),
        ),
    ]
