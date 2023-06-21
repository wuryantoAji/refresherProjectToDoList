from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from .models import ToDoList, ToDoItem
from django.urls import reverse
import datetime


def index(request):
    allToDoList = ToDoList.objects.order_by('to_do_list_title')
    context = {
        'all_to_do_list' : allToDoList
    }
    return render(request, 'todolist/index.html',context)

def addToDoList(request):
    context = {}
    if request.method == "POST":
        toDoListTitle = request.POST['to_do_list_title']
        if toDoListTitle == "":
            context['response'] = "Please give title to the to do list"
            return render(request, 'toDoList/todolist_form.html', context)
        else:
            toDoList = ToDoList(to_do_list_title=toDoListTitle)
            toDoList.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        return render(request, 'toDoList/todolist_form.html', context)

def updateToDoList(request, toDoListId):
    context = {}
    if request.method == "POST":
        toDoListTitle = request.POST['to_do_list_title']
        if toDoListTitle == "":
            context['response'] = "Please give title to the to do list"
            return render(request, 'toDoList/todolist_update_form.html', context)
        else:
            toDoList = ToDoList.objects.get(id=toDoListId)
            toDoList.to_do_list_title = toDoListTitle
            toDoList.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        toDoList = ToDoList.objects.get(id=toDoListId)
        context = {
            'toDoList': toDoList,
        }
        return render(request, 'toDoList/todolist_update_form.html', context)
def deleteToDoList(request, toDoListId):
    if request.method == "POST":
        toDoList = get_object_or_404(ToDoList, pk=toDoListId)
        toDoList.delete()
    return HttpResponseRedirect(reverse('index'))

def allItemForTheList(request, toDoListId):
    toDoList = get_object_or_404(ToDoList, pk=toDoListId)
    toDoItem = ToDoItem.objects.filter(to_do_list_id=toDoListId)
    context = {
        'todo_list': toDoList,
        'toDoItem': toDoItem,
    }
    return render(request, 'toDoList/todo_list.html', context)

def addToDoListItem(request, toDoListId):
    toDoList = ToDoList.objects.get(id=toDoListId)
    context = {
        'toDoList': toDoList,
    }
    responseList = []
    if request.method == "POST":
        toDoListItemTitle = request.POST['to_do_list_item_title']
        toDoListItemDueDate = request.POST['to_do_list_item_due_date']
        toDoListItemDescription = request.POST['to_do_list_item_description']
        if toDoListItemTitle == "":
            responseList.append("please give title to the item")
        if toDoListItemDueDate == "":
            responseList.append("please give due date to the item")
        datetime_object = datetime.datetime.strptime(toDoListItemDueDate, '%Y-%m-%d').date()
        if datetime_object < datetime.datetime.now().date():
            responseList.append("due date must be after today")
        if len(responseList) > 0:
            context["responses"] = responseList
            return render(request, 'toDoItem/todolistitem_form.html', context)
        else:
            toDoItem = ToDoItem(
                to_do_item_title=toDoListItemTitle,
                to_do_due_date=toDoListItemDueDate,
                to_do_description=toDoListItemDescription,
                to_do_list_id=toDoListId,
            )
            toDoItem.save()
            return HttpResponseRedirect(reverse('toDoListDetail', args=[toDoListId]))
    else:
        return render(request, 'toDoItem/todolistitem_form.html', context)

def updateToDoListItem(request, toDoListId, toDoItemId):
    responseList = []
    toDoItem = get_object_or_404(ToDoItem, pk=toDoItemId)
    context = {
        'toDoItem': toDoItem,
    }
    if request.method == "POST":
        toDoListItemTitle = request.POST['to_do_list_item_title']
        toDoListItemDueDate = request.POST['to_do_list_item_due_date']
        toDoListItemDescription = request.POST['to_do_list_item_description']
        if toDoListItemTitle == "":
            responseList.append("please give title to the item")
        if toDoListItemDueDate == "":
            responseList.append("please give due date to the item")
        else:
            datetime_object = datetime.datetime.strptime(toDoListItemDueDate, '%Y-%m-%d').date()
            if datetime_object < datetime.datetime.now().date():
                responseList.append("due date must be after today")
        if len(responseList) > 0:
            context["responses"] = responseList
            return render(request, 'toDoList/todolistitemupdate_form.html', context)
        else:
            toDoItem = get_object_or_404(ToDoItem, pk=toDoItemId)
            toDoItem.to_do_item_title=toDoListItemTitle
            toDoItem.to_do_due_date=toDoListItemDueDate
            toDoItem.to_do_description=toDoListItemDescription
            toDoItem.to_do_list_id=toDoListId
            toDoItem.save()
            return HttpResponseRedirect(reverse('toDoListDetail', args=[toDoListId]))
    else:
        return render(request, 'toDoList/todolistitemupdate_form.html', context)
def deleteToDoListItem(request, toDoListId, toDoItemId):
    if request.method == "POST":
        toDoItem = get_object_or_404(ToDoItem, pk=toDoItemId)
        toDoItem.delete()
    return HttpResponseRedirect(reverse('toDoListDetail', args=[toDoListId]))