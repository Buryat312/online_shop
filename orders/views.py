from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import views, generics

from orders.models import Order
from orders.serializers import OrderSerializer


class OrderListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated, ]
    queryset = Order.objects.all()
    serializer_class = OrderSerializer





# @action(methods=['post', ], detail=True)
#     def add_order(self, request, *args, **kwargs):
#         cart = request.user.cart
#         cartproducts = cart.cartproduct_set.all()
#         product_list = ''
#         total_quantity = 0
#         total_price = 0
#         for cartproduct in cartproducts:
#             product_list += f'{cartproduct.product.name}'
#             total_price += cartproduct.product.price * cartproduct.quantity
#             total_quantity += cartproduct.quantity
#         order = Order.objects.create(cart=cart, total_quantity=total_quantity, total_price=total_price, product_list=product_list)
#         cart.product.clear()
#         serializer = OrderSerializer(instance=order)
#         return Response(serializer.data)