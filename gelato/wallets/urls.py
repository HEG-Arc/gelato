# -*- coding: UTF-8 -*-
# urls.py
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

# Core Django imports
from django.conf.urls import patterns, url, include

# Third-party app imports

# Gelato imports
from .views import UserListView, UserDetail, UserHomeDetail, dashboard, create_account, activation_form, activate_account, wallet_add_money_paypal, wallet_add_money_cash, rfid_scan

urlpatterns = patterns('',
    url(r'^user/(?P<pk>\d+)/$', UserDetail.as_view(), name='user_detail'),
    url(r'^rfid/(?P<kiosk_id>\d+)/(?P<rfid>\d+)/$', rfid_scan, name='rfid_scan'),
    url(r'^rfid/(?P<kiosk_id>\d+)/ESC/$', rfid_scan, {'rfid': 'ESC'}, name='rfid_scan'),
    url(r'^dashboard/$', dashboard, name='dashboard'),
    url(r'^dashboard/$', dashboard, name='paypal-return'),
    url(r'^dashboard/$', dashboard, name='paypal-cancel'),
    url(r'^create_account/$', create_account, name='create_account'),
    url(r'^activation_form/$', activation_form, name='activation_form'),
    url(r'^activate_account/$', activate_account, name='activate_account'),
    url(r'^add_money/$', wallet_add_money_paypal, name='add_money'),
    url(r'^refill/$', wallet_add_money_cash, name='add_cash'),
    url(r'$', UserListView.as_view(), name='users'),
)