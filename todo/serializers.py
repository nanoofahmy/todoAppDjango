from rest_framework import serializers
from todoApp import settings
from users.models import CustomUser
from .models import Todo
User = settings.AUTH_USER_MODEL

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email']

class TodoSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer(read_only=True)

    class Meta:
        model = Todo
        fields = ['user', 'id' , 'title']

