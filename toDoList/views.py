from .models import ToDoList, ToDoItem
from django.urls import reverse
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
)

class ListListView(ListView):
    model = ToDoList
    template_name = "todolist/index.html"

class ItemListView(ListView):
    model = ToDoItem
    template_name = "todolist/to_do_list.html"

    def get_queryset(self):
        return ToDoItem.objects.filter(todo_list_id=self.kwargs["list_id"])

    def get_context_data(self):
        context = super().get_context_data()
        context["to_do_list_id"] = ToDoList.objects.get(id=self.kwargs["list_id"])
        return context

class ListCreate(CreateView):
    model = ToDoList
    fields = ["to_do_list_title"]

    def get_context_data(self):
        context = super(ListCreate, self).get_context_data()
        context["to_do_list_title"] = "Add a new list"
        return context

class ItemCreate(CreateView):
    model = ToDoItem
    fields = [
        "to_do_list_id",
        "to_do_item_title",
        "to_do_description",
        "to_do_due_date",
    ]

    def get_initial(self):
        initial_data = super(ItemCreate, self).get_initial()
        todo_list = ToDoList.objects.get(id=self.kwargs["list_id"])
        initial_data["to_do_list_id"] = todo_list
        return initial_data

    def get_context_data(self):
        context = super(ItemCreate, self).get_context_data()
        todo_list = ToDoList.objects.get(id=self.kwargs["list_id"])
        context["to_do_list_id"] = todo_list
        context["to_do_item_title"] = "Create a new item"
        return context

    def get_success_url(self):
        return reverse("list", args=[self.object.todo_list_id])

class ItemUpdate(UpdateView):
    model = ToDoItem
    fields = [
        "to_do_list_id",
        "to_do_item_title",
        "to_do_description",
        "to_do_due_date",
    ]


    def get_context_data(self):
        context = super(ItemUpdate, self).get_context_data()
        context["to_do_list_id"] = self.object.todo_list
        context["to_do_item_title"] = "Edit item"
        return context

    def get_success_url(self):
        return reverse("list", args=[self.object.todo_list_id])