from rest_framework import serializers
from todoApp import settings
from users.models import CustomUser
User = settings.AUTH_USER_MODEL

class RegisterUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password']


