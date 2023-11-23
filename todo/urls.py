
from django.urls import path , include
from . import  views
urlpatterns = [
    path('',views.todo_details),
    path('<int:id>',views.todo_details_byId)
]