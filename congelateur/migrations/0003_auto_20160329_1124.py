# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-29 09:24
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('congelateur', '0002_auto_20160329_1115'),
    ]

    operations = [
        migrations.AddField(
            model_name='glace',
            name='datePeremption',
            field=models.DateField(auto_now=True, default=datetime.datetime(2016, 3, 29, 9, 24, 29, 157927, tzinfo=utc), verbose_name='Date de péremption'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bac',
            name='code',
            field=models.CharField(max_length=5, unique=True, verbose_name='Code'),
        ),
        migrations.AlterField(
            model_name='bac',
            name='libelle',
            field=models.CharField(max_length=100, verbose_name='Libellé'),
        ),
        migrations.AlterField(
            model_name='bac',
            name='tiroir',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='congelateur.Tiroir', verbose_name='Tiroir'),
        ),
        migrations.AlterField(
            model_name='categorie',
            name='code',
            field=models.CharField(max_length=5, unique=True, verbose_name='Code'),
        ),
        migrations.AlterField(
            model_name='categorie',
            name='libelle',
            field=models.CharField(max_length=100, verbose_name='Libellé'),
        ),
        migrations.AlterField(
            model_name='categorie',
            name='sousCategorie',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='congelateur.Categorie', verbose_name='Catégorie'),
        ),
        migrations.AlterField(
            model_name='congelateur',
            name='code',
            field=models.CharField(max_length=5, unique=True, verbose_name='Code'),
        ),
        migrations.AlterField(
            model_name='congelateur',
            name='emplacement',
            field=models.CharField(max_length=50, verbose_name='Emplacement du congélateur'),
        ),
        migrations.AlterField(
            model_name='congelateur',
            name='libelle',
            field=models.CharField(max_length=100, verbose_name='Libellé'),
        ),
        migrations.AlterField(
            model_name='glace',
            name='calories',
            field=models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Callories'),
        ),
        migrations.AlterField(
            model_name='glace',
            name='fournisseur',
            field=models.CharField(choices=[('AD', 'Admin')], default='AD', max_length=50, verbose_name='Fournisseur'),
        ),
        migrations.AlterField(
            model_name='glace',
            name='libelle',
            field=models.CharField(max_length=100, verbose_name='Libellé'),
        ),
        migrations.AlterField(
            model_name='glace',
            name='prixVente',
            field=models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Prix de vente'),
        ),
        migrations.AlterField(
            model_name='tiroir',
            name='code',
            field=models.CharField(max_length=5, unique=True, verbose_name='Code'),
        ),
        migrations.AlterField(
            model_name='tiroir',
            name='congelateur',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='congelateur.Congelateur', verbose_name='Congélateur'),
        ),
    ]