# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
import models
from ps_user.models import *

# Register your models here.
class UserInfoAdmin(admin.ModelAdmin):
    list_per_page = 15
    list_display = ['id','uname','uemail','ucustomer','uaddress','uyoubian','uphone']
admin.site.register(UserInfo,UserInfoAdmin)