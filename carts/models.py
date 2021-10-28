from django.db.models.deletion import CASCADE
from products.models import Product
from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver


User = get_user_model()

class Cart(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE, related_name='cart', verbose_name='Корзина')
    total_amount = models.PositiveIntegerField(default=1, null=True)
    products = models.ManyToManyField('products.Product', through='CartProduct')
        
    def __str__(self):
        return f'Список продуктов в корзине пользовотеля {self.owner}: {self.products}. Полная стоимость:{self.total_amount}'

class CartProduct(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField(default=1, null=True)



@receiver(post_save, sender=User)
def create_cart(sender, instance, created, *args, **kwargs):
    if instance and created:
        instance.cart = Cart.objects.create(owner=instance)
        