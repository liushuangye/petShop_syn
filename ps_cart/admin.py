# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from ps_cart.models import CartInfo


class CartInfoAdmin(admin.ModelAdmin):
    list_per_page = 15
    list_display = ['id','user','goods','count']
admin.site.register(CartInfo,CartInfoAdmin)

