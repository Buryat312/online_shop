from django.db import models
from django.db.models.deletion import SET_NULL


class Order(models.Model):
    cart = models.ForeignKey('carts.Cart', on_delete=models.SET_NULL, null=True,
                            related_name='orders')
    total_price = models.IntegerField()
    total_amount = models.IntegerField()
    product_list = models.TextField()

    
