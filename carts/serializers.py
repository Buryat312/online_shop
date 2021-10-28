from rest_framework import serializers

from carts.models import Cart, CartProduct


class CartSerializer(serializers.ModelSerializer):
    
    total_amount = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = ['id', 'owner', 'products', 'total_amount', ]
        read_only_fields = ['owner', 'total_amount',]

    def get_total_amount(self, instance):
        total_amount = 0 
        current_products = instance.cartproduct_set.all()   #CartProduct = cartproduct_set
        for product in current_products:
            total_amount+=product.amount
        return total_amount
 



