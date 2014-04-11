# -*- coding: UTF-8 -*-
# views.py
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
from django.shortcuts import render_to_response, get_object_or_404
from django.template.context import RequestContext
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.utils.translation import ugettext as _
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import ListView, DetailView
from django.db.models import Sum
from django.contrib.auth.models import User

# Third-party app imports

# Gelato imports
from transactions.models import ProductTransaction, FinancialTransaction


class UserListView(ListView):
    model = User
    # TODO: Request admin login


class UserDetail(DetailView):
    model = User
    # TODO: Request admin login

    def get_context_data(self, **kwargs):
        context = super(UserDetail, self).get_context_data(**kwargs)
        context['product_transaction_list'] = ProductTransaction.objects.all().filter(user=self.object)
        context['financial_transaction_list'] = FinancialTransaction.objects.all().filter(user=self.object)
        return context


class UserHomeDetail(DetailView):
    model = User
    # TODO: Request login


