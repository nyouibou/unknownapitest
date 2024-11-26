from django.contrib import admin
from .models import Product

class Product(admin.ModelAdmin):
    admin.site.register(Product)