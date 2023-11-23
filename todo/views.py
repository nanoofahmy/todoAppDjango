from django.shortcuts import render
from .models import Todo

# Create your views here.
def todo_details (request ):
    todoList = Todo.objects.all()
    context ={'todos':todoList}
    return render(request,template_name="../templates/todo.html",context=context)

def todo_details_byId (request , id):
    todo = Todo.objects.get(id=id)
    print(todo)
    context ={'todo':todo}
    return render(request,template_name="../templates/todo_id.html",context=context)




