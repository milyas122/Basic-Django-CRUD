from django.contrib import admin
from .models import (
    Product, Cart, Category, User
)

# Register your models here.

admin.site.register(User)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Category)


