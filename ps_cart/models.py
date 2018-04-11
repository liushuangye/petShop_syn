# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class CartInfo(models.Model):
    user=models.ForeignKey('ps_user.UserInfo')
    goods=models.ForeignKey('ps_goods.GoodsInfo')
    count=models.IntegerField(default=0)
