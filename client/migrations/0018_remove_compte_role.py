# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-03 15:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0017_auto_20160802_1605'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='compte',
            name='role',
        ),
    ]
