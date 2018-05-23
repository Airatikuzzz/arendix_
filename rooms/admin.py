# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *

# Register your models here.
class RoomImageInline(admin.TabularInline):
    model = RoomImage
    extra = 0


class StatusAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Status._meta.fields]

    class Meta:
        model = Status

admin.site.register(Status,StatusAdmin)

class RoomAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Room._meta.fields]
    inlines = [RoomImageInline]
    class Meta:
        model = Room

admin.site.register(Room,RoomAdmin)

class RoomImageAdmin(admin.ModelAdmin):
    list_display = [field.name for field in RoomImage._meta.fields]

    class Meta:
        model = RoomImage

admin.site.register(RoomImage,RoomImageAdmin)
