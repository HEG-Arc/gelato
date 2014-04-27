# -*- coding: UTF-8 -*-
# models.py
#
# Copyright (C) 2014 HES-SO//HEG Arc
#
# Author(s): Cédric Gaspoz <cedric.gaspoz@he-arc.ch>
#
# This file is part of Gelato.
#
# Gelato is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Gelato is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Gelato. If not, see <http://www.gnu.org/licenses/>.

# Stdlib imports
import logging

# Core Django imports
from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _

# Third-party app imports

# Gelato imports


logger = logging.getLogger(__name__)


class Kiosk(models.Model):
    """
    A kiosk
    """
    name = models.CharField(verbose_name=_("name"), max_length=20, help_text=_("Name of the kiosk"))
    location = models.CharField(verbose_name=_("location"), max_length=100, help_text=_("Location of the kiosk"))
    created = models.DateTimeField(verbose_name=_("created"), auto_now_add=True, help_text=_("Creation date of the kiosk in the database"))
    edited = models.DateTimeField(verbose_name=_("edited"), auto_now=True, help_text=_("Last edition of the kiosk in the database"))
    editor = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_('editor'), related_name=_('kiosks'), help_text=_("Last editor of the kiosk in the database"))

    class Meta:
        verbose_name = _('kiosk')
        verbose_name_plural = _('kiosks')
        ordering = ['name']

    def __unicode__(self):
        return self.name


class KioskStorage(models.Model):
    """
    A storage location in a kiosk
    """
    tier = models.IntegerField(verbose_name=_("tier"), max_length=1, default=0, help_text=_("Tier of a kiosk"))
    tub = models.CharField(verbose_name=_("tub"), max_length=1, blank=True, default="", help_text=_("A kiosk tub on a tier"))
    kiosk = models.ForeignKey('Kiosk', verbose_name=_('kiosk'), related_name=_('storages'), help_text=_("Kiosk the storage belongs to"))
    created = models.DateTimeField(verbose_name=_("created"), auto_now_add=True, help_text=_("Creation date of the kiosk storage in the database"))
    edited = models.DateTimeField(verbose_name=_("edited"), auto_now=True, help_text=_("Last edition of the kiosk storage in the database"))
    editor = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_('editor'), related_name=_('kiosk storages'), help_text=_("Last editor of the kiosk storage in the database"))

    class Meta:
        verbose_name = _('kiosk storage')
        verbose_name_plural = _('kiosk storage')
        ordering = ['tier', 'tub']

    def __unicode__(self):
        return "%s%s" % (self.tier, self.tub)