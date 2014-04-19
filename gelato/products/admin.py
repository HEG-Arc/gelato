# -*- coding: UTF-8 -*-
# admin.py
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
from django.contrib import admin

# Third-party app imports

# Gelato imports
from .models import Product, ProductCategory, ProductBrand, ProductSupplier


class ProductSupplierAdmin(admin.ModelAdmin):
    pass


class ProductBrandAdmin(admin.ModelAdmin):
    pass


class ProductCategoryAdmin(admin.ModelAdmin):
    pass


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'category', 'weight', 'calorie', 'tu', 'price', 'supplier')
    list_filter = ('brand', 'category', 'supplier')


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductCategory, ProductCategoryAdmin)
admin.site.register(ProductSupplier, ProductSupplierAdmin)
admin.site.register(ProductBrand, ProductBrandAdmin)
