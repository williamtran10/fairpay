from django.contrib import admin

from .models import Item, Customer, Order

models_list = [Item, Customer, Order]
admin.site.register(models_list)
