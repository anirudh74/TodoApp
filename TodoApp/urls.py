from django.urls import path,include
from django.conf.urls import url
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('aboutme/',views.aboutme,name="aboutme"),
    path('specifications/',views.specifications,name="specifications"),
    path('google/',views.google,name="google"),
    path('todo/',views.todopage,name="todo"),
    path('addnew/',views.addTodoItem,name="addnew"),
    path('completed/<todo_id>',views.completedTodo,name="completed"),
    path('delete/',views.deletecompleted,name="delete"),
    path('deleteall/',views.deleteall,name="deleteall"),
]
