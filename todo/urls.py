from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'todo', views.TodoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path('',views.todo_details),
    # path('<int:id>',views.todo_details_byId)
]
