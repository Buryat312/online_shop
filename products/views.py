from carts.serializers import CartSerializer
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import serializers, status
from carts.models import CartProduct
from products.models import Product
from products.serializers import AmountSerializer, ProductSerializer

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated, ]


    @action(permission_classes = [IsAuthenticated, ], methods=['post', 'delete', ], detail=True)
    def cart(self, request, *args, **kwargs):
        product = self.get_object()
        cart = request.user.cart

        if request.method == 'POST':
            cart.products.add(product)

        elif request.method == 'DELETE':
            cart.products.remove(product)
        
        return Response({cart})


 # @action(permission_classes = [IsAuthenticated, ], 
    #         methods=['post', 'delete', ], detail=True, 
    #         serializer_classes=AmountSerializer)
    # def cart(self, request, *args, **kwargs):
    #     cart = request.user.cart
    #     product = self.get_object()
    #     if request.method == 'POST':
    #         serializer = AmountSerializer(data=request.data)

    #         serializer.is_valid(raise_exception=True)

    #         requested_amount = serializer.validated_data.get('amount')

    #         if requested_amount > product.amount:
    #             return Response({'error': 'Requested amount is larger than product amount'},
    #                             status=status.HTTP_400_BAD_REQUEST)
            
    #         product.amount -= requested_amount
    #         product.save()

    #         cart_product, created = CartProduct.objects.get_or_create(
    #             cart=cart,
    #             product=product,
    #         )
    #         if created:
    #             cart_product.amount = requested_amount
    #         else:
    #             cart_product.amount += requested_amount

    #         return Response({'success': True})

    #     elif request.method == 'DELETE':

    #         if CartProduct.objects.filter(cart=cart, product=product).exist():
    #             cart_product = CartProduct.objects.get(product=product, cart=cart)

    #             if requested_amount > cart_product.amount:
    #                 return Response({'error': 'Requested amount is larger than product amount'},
    #                             status=status.HTTP_400_BAD_REQUEST)
    #             elif requested_amount == cart_product.amount:
    #                 cart_product.delete()
    #                 return Response({'success': True})