# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-27 06:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0004_auto_20160427_0850'),
    ]

    operations = [
        migrations.AlterField(
            model_name='demande',
            name='dateReponse',
            field=models.DateField(blank=True, null=True, verbose_name='Date de réponse'),
        ),
    ]
