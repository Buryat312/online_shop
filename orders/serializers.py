from rest_framework import serializers

from orders.models import Order


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['cart', 'total_price', 'total_amount', 'product_list',]
        read_only_fields = ['total_price', 'total_amount', ]
