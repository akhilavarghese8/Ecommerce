from django.contrib import admin
from store.models import Category,Products,Orders,Offers,Carts

# Register your models here.

admin.site.register(Category)
admin.site.register(Products)
admin.site.register(Offers)
