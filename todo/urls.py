from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'todo', views.TodoViewSet)
# router.register(r'comment', views.CommentViewSet)

urlpatterns = [
    # path('', views.lobby),
    path('', include(router.urls)),
    # path('api/', include('users.urls')),
    # path('',views.todo_details),
    # path('<int:id>',views.todo_details_byId)
]
