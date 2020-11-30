from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.decorators.http import require_POST

from .models import TodoApp

from .forms import TodoListForm

def index(request):
    return render(request,'index.html')

def aboutme(request):
    return render(request,'aboutme.html')

def specifications(request):
    return render(request,'specifications.html')

def google(request):
    return redirect("https://www.google.co.in")    

def todopage(request):
    todo_items = TodoApp.objects.order_by('id')
    form = TodoListForm
    text = {'todo_items' : todo_items, 'form' : form}
    return render(request,'Todopage.html', text)

@require_POST
def addTodoItem(request):
    new_todo = TodoApp(text=request.POST['text'])
    new_todo.save()
    return redirect('todo')

def completedTodo(request, todo_id):
    todo = TodoApp.objects.get(pk=todo_id)
    todo.completed = True
    todo.save()
    return redirect('todo')

def deletecompleted(request):
    TodoApp.objects.filter(completed=True).delete()
    return redirect('todo')

def deleteall(request):
    TodoApp.objects.all().delete()
    return redirect('todo')

