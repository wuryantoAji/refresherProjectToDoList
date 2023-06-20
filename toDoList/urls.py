# todo_list/todo_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # path("", views.ListListView.as_view(), name="index"),
    # path("list/<int:list_id>/", views.ItemListView.as_view(), name="list"),
    # # CRUD patterns for ToDoLists
    # path("list/add/", views.ListCreate.as_view(), name="list-add"),
    # # CRUD patterns for ToDoItems
    # path(
    #     "list/<int:list_id>/item/add/",
    #     views.ItemCreate.as_view(),
    #     name="item-add",
    # ),
    # path(
    #     "list/<int:list_id>/item/<int:pk>/",
    #     views.ItemUpdate.as_view(),
    #     name="item-update",
    # ),
    path('', views.index, name='index'),
    path('addToDoList', views.addToDoList, name='addToDoList'),
    path('updateToDoList/<int:toDoListId>', views.updateToDoList, name='updateToDoList'),
    path('deleteToDoList/<int:toDoListId>', views.deleteToDoList, name='deleteToDoList'),
    path('toDoListDetail/<int:toDoListId>', views.allItemForTheList, name='toDoListDetail'),
    path('toDoListAddItem/<int:toDoListId>', views.addToDoListItem, name='addToDoListItem'),
]