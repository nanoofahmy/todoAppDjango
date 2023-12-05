import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import AsyncJsonWebsocketConsumer
from channels.generic.websocket import WebsocketConsumer
from todo.models import Todo


class ChatConsumer(WebsocketConsumer):

    def connect(self):
        # self.room_name = 'todo_room'
        self.group_name = 'todo_group'
        # self.channel = 'todo_channel'
        async_to_sync(self.channel_layer.group_add)(
             self.group_name, self.channel_name
        )
        self.accept()
        # todo = Todo.objects.all()
        # todo_test = json.loads(todo)
        # # Send a message to the WebSocket
        # self.send(text_data=json.dumps({
        #     'action': 'todo_created',
        #     'todo': todo_test
        # }))

        self.send(text_data=json.dumps({'status': 'connection success'}))

    def disconnect(self, close_code):
        self.channel_layer.group_discard(
            self.group_name, self.channel_name
        )

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        print(text_data_json)
        self.send(text_data=json.dumps({
            'result': text_data_json
        }))
        async_to_sync(self.channel_layer.group_send)(
            self.group_name,  # group name
            {
                'type': 'send_notification',
                # 'value': data
            }
        )

    def send_notification(self, event):
        print('send notification')
        print(event)
        self.send(text_data=json.dumps({
            'result': event.get('value')
        }))
        print('notification sent')  # Add this line to check if the method is reaching here

# class ChatConsumer(AsyncJsonWebsocketConsumer):
#     async def connect(self):
#         self.room_name = 'todo'
#         self.room_group_name = 'todo_group'
#         await (self.channel_layer.group_add)(
#             self.room_name, self.room_group_name
#         )
#
#         await self.accept()
#         await self.send(text_data=json.dumps({'status': 'connection success'}))
#
#     async def receive(self, text_data):
#         text_data_json = json.loads(text_data)
#         print(text_data_json)
#         action = text_data_json.get('action')
#
#         if action == 'create_todo':
#             await self.create_todo(text_data_json['title'])
#             await self.send(text_data=json.dumps({
#                 'result': text_data_json
#             }))
#
#     async def create_todo(self, title):
#         # Save the new todo item
#         todo = Todo.objects.create(title=title)
#         # Send a message to the WebSocket
#         await self.send(text_data=json.dumps({
#             'action': 'todo_created',
#             'id': todo.id,
#             'title': todo.title,
#             'completed': todo.completed,
#         }))
#
#     async def send_notification(self, event):
#         print('send notification')
#         print(event)
#         await self.send(text_data=json.dumps({
#             'result': event.get('value')
#         }))
#
#     async def disconnect(self, close_code):
#         await self.channel_layer.group_discard(
#             self.room_name, self.room_group_name
#         )
# def receive(self, text_data):
#     text_data_json = json.loads(text_data)
#     print(text_data_json)
#     expression = text_data_json['expression']
#     try:
#         result = eval(expression)
#     except Exception as e:
#         result = "Invalid Expression"
#     self.send(text_data=json.dumps({
#         'result': result
#     }))

# async def todo_created(self, event):
#     # Send the todo information to the client
#     await self.send(text_data=json.dumps({
#         'type': 'todo.created',
#         'id': event['id'],
#         'title': event['title'],
#         'description': event['description'],
#         # Add other fields as needed
#     }))
