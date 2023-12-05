from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
# Create your models here.
from django.conf import settings
from django.db import models
from django.utils import timezone
from rest_framework.utils import json

from users.models import CustomUser

User = settings.AUTH_USER_MODEL


class Todo(models.Model):
    title = models.CharField(max_length=100)
    details = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(CustomUser,  on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title
    # def save(self,*args, **kwargs):
    #     channel_layer = get_channel_layer()
    #     todo_objs = Todo.objects.all().count()
    #     print(self.details)
    #     data = {'data':todo_objs , 'current_todo':self.details}
    #     # todo =
    #     print("Before group_send")
    #     async_to_sync(channel_layer.group_send)(
    #         'todo_group',  # group name
    #         {
    #             'type': 'send_notification',
    #             'value': data
    #         }
    #     )
    #     print("After group_send")
    #     print('hhhhiii')
    #     super(Todo,self).save(*args, **kwargs)


class Comment(models.Model):
    description = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(CustomUser, related_name='userComment', on_delete=models.CASCADE, null=True, blank=True)
    todos = models.ForeignKey(Todo, related_name='todos', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.description

