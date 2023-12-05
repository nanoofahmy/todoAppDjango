import json

from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import Todo, Comment
from .permissions import IsOwnerOnly
from .serializers import TodoSerializer, CommentSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

# channel_layer = get_channel_layer()


def lobby(request):
    print(request.path)
    return render(request, 'chat/lobby.html')


# Create your views here.
class TodoViewSet(viewsets.ModelViewSet):
    permission_classes = (IsOwnerOnly,)
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    # permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def perform_create(self, serializer):
        todo_instance = serializer.save(user=self.request.user)
        # Create a message with the todo data
        data = {
            # 'type': 'todo.created',
            'id': todo_instance.id,
            'title': todo_instance.title,
            'details': todo_instance.details,
            # Add other fields as needed
        }
        # print(data)
        #
        # # Send the message to the 'todo' channel
        # async_to_sync(channel_layer.group_send)(
        #     'todo_group',  # Channel name
        #     {
        #         'type': 'send_notification',
        #         'value': json.dumps(data)
        #     }
        # )

    def filter_queryset(self, queryset):
        return super().filter_queryset(queryset)
        # queryset = queryset.filter(user=self.request.user)
        # return super().filter_queryset(queryset)


class CommentViewSet(viewsets.ModelViewSet):
    permission_classes = (IsOwnerOnly,)
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    # permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def perform_create(self, serializer):
        # Get the id_todo from request data
        request_data = self.request.query_params  # Assuming it's a dictionary
        id_todo = request_data.get('id_todo')
        print(f'id_todo: {id_todo}')

        # Check if id_todo is provided
        if id_todo is None:
            return Response({'error': 'id_todo parameter is required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Get the Todo object based on id_todo
            todo = Todo.objects.get(id=id_todo)
        except Todo.DoesNotExist:
            return Response({'error': 'Todo not found'}, status=status.HTTP_404_NOT_FOUND)

        # Set the user and todo for the comment
        serializer.save(user=self.request.user, todos=todo)

    def filter_queryset(self, queryset):
        return super().filter_queryset(queryset)
        # queryset = queryset.filter(user=self.request.user)
        # return super().filter_queryset(queryset)
