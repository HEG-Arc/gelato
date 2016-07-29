# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-29 12:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0012_compte_modeprefere'),
    ]

    operations = [
        migrations.AddField(
            model_name='compte',
            name='niveau',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='client.Niveau', verbose_name='Niveau'),
            preserve_default=False,
        ),
    ]
