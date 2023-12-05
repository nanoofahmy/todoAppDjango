from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Todo, Comment
channel_layer = get_channel_layer()

@receiver(post_save, sender=Todo)
def send_todo_notification(sender, instance, **kwargs):
    print("hiiiiiii from signals")
    data = {
        'type': 'todo.created' if kwargs['created'] else 'todo.updated',
        'id': instance.id,
        'title': instance.title,
        'details': instance.details,
        # Add other fields as needed
    }

    async_to_sync(channel_layer.group_send)(
        'todo_group',  # group name
        {
            'type': 'send_notification',
            'value': data
        }
    )

@receiver(post_save, sender=Comment)
def send_comment_notification(sender, instance, **kwargs):
    print("hiiiiiii from signals comment")
    data = {
        'type': 'comment.created' if kwargs['created'] else 'comment.updated',
        'id': instance.id,
        'description': instance.description,
        # Add other fields as needed
    }

    async_to_sync(channel_layer.group_send)(
        'todo_group',  # group name
        {
            'type': 'send_notification',
            'value': data
        }
    )