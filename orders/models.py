# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from rooms.models import Room

# Create your models here.

class Order(models.Model):
    customer_name = models.CharField(max_length=50,blank=True,null=True,default=True)
    customer_email = models.EmailField(blank=True,null=True,default=True)
    customer_phone = models.CharField(max_length=30,blank=True,null=True,default=True)
    comments = models.TextField()

    created_date = models.DateTimeField(auto_now_add=True, auto_now = False)
    updated_date = models.DateTimeField(auto_now_add=False, auto_now = True)

    def __str__(self):
        return "Заказ № %s by %s" % (self.id, self.customer_name)

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"


class RoomInOrder(models.Model):
    order = models.ForeignKey(Order, blank=True,null=True,default=None)
    room = models.ForeignKey(Room, blank=True,null=True,default=None)

    customer_name = models.CharField(max_length=50,blank=True,null=True,default=True)
    customer_email = models.EmailField(blank=True,null=True,default=True)
    customer_phone = models.CharField(max_length=30,blank=True,null=True,default=True)

    created_date = models.DateTimeField(auto_now_add=True, auto_now = False)
    updated_date = models.DateTimeField(auto_now_add=False, auto_now = True)

    def __str__(self):
        return  "%s" % self.room.name

    class Meta:
        verbose_name = "Помещение  в заказе"
        verbose_name_plural = "Помещения в заказах"
