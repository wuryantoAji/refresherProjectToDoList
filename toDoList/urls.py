# todo_list/todo_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('addToDoList', views.addToDoList, name='addToDoList'),
    path('updateToDoList/<int:toDoListId>', views.updateToDoList, name='updateToDoList'),
    path('deleteToDoList/<int:toDoListId>', views.deleteToDoList, name='deleteToDoList'),
    path('toDoListDetail/<int:toDoListId>', views.allItemForTheList, name='toDoListDetail'),
    path('toDoListAddItem/<int:toDoListId>', views.addToDoListItem, name='addToDoListItem'),
    path('toDoListUpdateItem/<int:toDoListId>/<int:toDoItemId>', views.updateToDoListItem, name='updateToDoListItem'),
    path('toDoListDeleteItem/<int:toDoListId>/<int:toDoItemId>', views.deleteToDoListItem, name='deleteToDoListItem'),
]