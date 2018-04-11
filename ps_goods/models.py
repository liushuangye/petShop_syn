# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from tinymce.models import HTMLField

class TypeInfo(models.Model):
    ttitle = models.CharField(max_length=20)
    isDelete = models.BooleanField(default=False)

    def __str__(self):
        return self.ttitle.encode('utf-8')
class GoodsInfo(models.Model):
    gtitle = models.CharField(max_length=20)
    gpicture = models.ImageField(upload_to='ps_goods')
    gprice = models.DecimalField(max_digits=7,decimal_places=2)
    isDelete = models.BooleanField(default=False)
    gunit = models.CharField(max_length=10,default='件')#单位
    gclick = models.IntegerField()#点击量
    gstock = models.IntegerField()#库存
    gcontent = HTMLField()#详情
    gtype = models.ForeignKey(TypeInfo)
    def __str__(self):
        return self.gtitle.encode('utf-8')
