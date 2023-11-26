
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
    user = models.ForeignKey(CustomUser, related_name='users', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title
