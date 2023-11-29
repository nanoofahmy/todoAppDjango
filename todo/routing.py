
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/some_path/', consumers.MyConsumer.as_asgi()),
    # Add more WebSocket paths if needed
]

application = ProtocolTypeRouter({
    'websocket': URLRouter(websocket_urlpatterns),
})