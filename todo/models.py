
# Create your models here.
from django.conf import settings
from django.db import models
from django.utils import timezone

from users.models import CustomUser

User = settings.AUTH_USER_MODEL


class Todo(models.Model):
    title = models.CharField(max_length=100)
    details = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(CustomUser,  on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    description = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(CustomUser, related_name='userComment', on_delete=models.CASCADE, null=True, blank=True)
    todos = models.ForeignKey(Todo, related_name='todos', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.description

