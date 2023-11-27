from rest_framework import serializers
from todoApp import settings
from users.models import CustomUser
from .models import Todo, Comment

User = settings.AUTH_USER_MODEL


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email']


class TodoSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer(read_only=True)

    class Meta:
        model = Todo
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer(read_only=True)
    todos = TodoSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = "__all__"
