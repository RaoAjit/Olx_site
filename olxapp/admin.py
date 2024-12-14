from django.contrib import admin
from .models import Product,Cart,delivery

# Register your models here.
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(delivery)