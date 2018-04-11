# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
import models
from ps_goods.models import *


class TypeInfoAdmin(admin.ModelAdmin):
    list_display = ['id','ttitle']
class GoodsInfoAdmin(admin.ModelAdmin):
    list_per_page = 15
    list_display = ['id','gtitle','gprice','gunit','gstock','gcontent','gtype']
admin.site.register(TypeInfo,TypeInfoAdmin)
admin.site.register(GoodsInfo,GoodsInfoAdmin)
