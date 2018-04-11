# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class UserInfo(models.Model):
    uname = models.CharField(max_length=20)
    upwd = models.CharField(max_length=40)
    uemail = models.CharField(max_length=30)
    ucustomer = models.CharField(max_length=20,default='')#收货人
    uaddress = models.CharField(max_length=100,default='')
    uyoubian = models.CharField(max_length=10,default='')
    uphone = models.CharField(max_length=11,default='')
    def __str__(self):
        return self.uname# .encode('utf-8')