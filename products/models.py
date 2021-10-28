from django.db import models
from django.contrib.auth import get_user_model



User = get_user_model()

class Product(models.Model):
    category = models.ForeignKey('categories.Category', on_delete=models.PROTECT, related_name='products', verbose_name='Категория')
    name = models.CharField(max_length=200, verbose_name='Название')
    quantity = models.PositiveIntegerField(verbose_name='Колличество', null=True)
    price = models.DecimalField(max_digits=15, decimal_places=2, verbose_name='Цена')
    rating = models.PositiveIntegerField(default=0)   #how to create rating logic  ----- think!!!
    

    class Meta:
        ordering = ('rating',)
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        
    def __str__(self):
        return self.name

    # class Rating(models.Model):
    #     author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ratings')
    #     post = models.ForeignKey()              