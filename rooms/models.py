# coding=utf-8

from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Status(models.Model):
    status_value = models.CharField(max_length = 50,blank=True,null=True,default=None)
    status_description = models.TextField(blank=True,null=True,default=None)

    created_date = models.DateTimeField(auto_now_add=True, auto_now = False)
    updated_date = models.DateTimeField(auto_now_add=False, auto_now = True)

    def __str__(self):
        return "Статус %s" % self.status_value

    class Meta:
        verbose_name = "Статус"
        verbose_name_plural = "Статусы"


class Room(models.Model):
    name = models.CharField(max_length=50,blank=True,null=True,default=None)
    description = models.TextField(blank=True,null=True,default=None)
    square = models.IntegerField(blank=True,null=True,default=None)
    price_per_m2 = models.IntegerField(blank=True,null=True,default=None)
    price = models.IntegerField(blank=True,null=True,default=None)
    comments = models.TextField()

    status = models.ForeignKey(Status)
    user = models.ForeignKey(User, null=True)

    created_date = models.DateTimeField(auto_now_add=True, auto_now = False)
    updated_date = models.DateTimeField(auto_now_add=False, auto_now = True)

    def __str__(self):
        return "Помещение № %s status %s" % (self.id, self.status.status_value)

    class Meta:
        verbose_name = "Помещение"
        verbose_name_plural = "Помещения"

class RoomImage(models.Model):
    room = models.ForeignKey(Room,blank=True,null=True,default=None)
    image = models.ImageField()
    created_date = models.DateTimeField(auto_now_add=True, auto_now = False)
    updated_date = models.DateTimeField(auto_now_add=False, auto_now = True)

    def __str__(self):
        return "Фотография № %s для %s" % (self.id, self.room.name)

    class Meta:
        verbose_name = "Фотография"
        verbose_name_plural = "Фотографии"
