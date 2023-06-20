from django import forms
from .models import ToDoList

class ToDoListTitleForm(forms.Form):
    submitToDoListTitle = forms.CharField(label="toDoListTitle", max_length=100)

    def save(self):
        data = self.cleaned_data
        toDoList = ToDoList(to_do_list_title=data['submitToDoListTitle'])
        toDoList.save()