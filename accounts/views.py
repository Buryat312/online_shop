from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
from rest_framework.views import APIView
from .serializers import RegistrationSerializer
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from drf_yasg.utils import swagger_auto_schema

User = get_user_model()

class RegistrationAPIView(APIView):

    @swagger_auto_schema(operations_description='Register user',
                         request_body=RegistrationSerializer)
    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = serializer.validated_data.get('username')
        password = serializer.validated_data.get('password')

        if User.objects.filter(username=username).exists():
            return Response({'message': 'user with such username is already exists'},
                             status = status.HTTP_400_BAD_REQUEST)
        
        user =User.objects.create_user(username=username, password=password)

        token, _ = Token.objects.get_or_create(user=user)

        return Response({'token': token.key}, status=status.HTTP_201_CREATED)