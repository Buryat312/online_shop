from carts.models import Cart
from django.contrib import admin
from carts.models import Cart
# Register your models here.


class CartAdmin(admin.ModelAdmin):
    fields = ['owner', 'total_amount', ]

admin.site.register(Cart, CartAdmin)