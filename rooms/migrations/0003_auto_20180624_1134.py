# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-06-24 08:34
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0002_auto_20180624_1132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='user',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
