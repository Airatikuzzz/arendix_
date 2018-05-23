# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *

# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Order._meta.fields]

    class Meta:
        model = Order

admin.site.register(Order,OrderAdmin)

class RoomInOrderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in RoomInOrder._meta.fields]

    class Meta:
        model = RoomInOrder

admin.site.register(RoomInOrder,RoomInOrderAdmin)
