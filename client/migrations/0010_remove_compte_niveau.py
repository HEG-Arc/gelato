# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-29 12:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0009_niveau'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='compte',
            name='niveau',
        ),
    ]
