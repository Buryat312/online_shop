from logging import exception
from rest_framework import serializers
from rest_framework import exceptions

class RegistrationSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate_password(self, value):
        if len(value) < 5:
            return exceptions.ValidationError('password is too short')
        elif len(value) >20:
            return exceptions.ValidationError('password is too long')
        return value