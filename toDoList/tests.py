from django.test import TestCase
from .models import ToDoList, ToDoItem
from django.urls import reverse
from .views import index, addToDoList, updateToDoList, deleteToDoList, \
    allItemForTheList, addToDoListItem, updateToDoListItem, deleteToDoListItem
from django.test.client import RequestFactory
from datetime import timedelta
import datetime

# Create your tests here.
class ToDoTestCase(TestCase):

    def setUpToDoItem(self):
        ToDoList.objects.create(to_do_list_title="test1")
        ToDoItem.objects.create(to_do_item_title="testItem1",
                                to_do_due_date=datetime.datetime.now().date()+timedelta(days=10),
                                to_do_submitted_date=datetime.datetime.now().date(),
                                to_do_description="lorem ipsum",
                                to_do_list_id=1)

    def setUpWrongToDoItem(self):
        ToDoList.objects.create(to_do_list_title="test1")
        ToDoItem.objects.create(to_do_item_title="",
                                to_do_due_date=datetime.datetime.now().date()-timedelta(days=10),
                                to_do_submitted_date=datetime.datetime.now().date(),
                                to_do_description="lorem ipsum",
                                to_do_list_id=1)

    def setUpWrongToDoItemNoDate(self):
        ToDoList.objects.create(to_do_list_title="test1")
        ToDoItem.objects.create(to_do_item_title="",
                                to_do_submitted_date=datetime.datetime.now().date(),
                                to_do_description="lorem ipsum",
                                to_do_list_id=1)

    def testIndex(self):
        ToDoList.objects.create(to_do_list_title="test1")
        url = reverse('index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todolist/index.html')
        self.assertContains(response, 'test1')

    def testAddToDoListGet(self):
        url = reverse('addToDoList')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'toDoList/todolist_form.html')

    def testAddToDoListPost(self):
        url = reverse('addToDoList')
        data = {
            'to_do_list_title' : 'test1'
        }
        request = self.client.post(url, data)
        self.assertEqual(request.status_code, 302)
        # self.assertTemplateUsed(request, 'todolist/index.html')
        # self.assertContains(request, 'test1')

    def testFailedAddToDoListPost(self):
        url = reverse('addToDoList')
        data = {
            'to_do_list_title' : ''
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'toDoList/todolist_form.html')
        self.assertContains(response, 'Please give title to the to do list')

    def testUpdateToDoListGet(self):
        ToDoList.objects.create(to_do_list_title="test1")
        url = reverse('updateToDoList', args=[1])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'toDoList/todolist_update_form.html')
        self.assertContains(response, 'test1')

    def testUpdateToDoListPost(self):
        ToDoList.objects.create(to_do_list_title="test1")
        url = reverse('updateToDoList', args=[1])
        data = {
            'to_do_list_title': 'test2'
        }
        request = self.client.post(url, data)
        self.assertEqual(request.status_code, 302)
        # self.assertTemplateUsed(request, 'todolist/index.html')
        # self.assertContains(request, 'test1')

    def testFailedUpdateToDoListPost(self):
        ToDoList.objects.create(to_do_list_title="test1")
        url = reverse('updateToDoList', args=[1])
        data = {
            'to_do_list_title' : ''
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'toDoList/todolist_update_form.html')
        self.assertContains(response, 'Please give title to the to do list')

    def testDeleteToDoListPost(self):
        ToDoList.objects.create(to_do_list_title="test1")
        url = reverse('deleteToDoList', args=[1])
        request = self.client.post(url)
        self.assertEqual(request.status_code, 302)
        # self.assertTemplateUsed(request, 'todolist/index.html')
        # self.assertNotContains(request, 'test1')

    def testAllItemForTheList(self):
        self.setUpToDoItem()
        url = reverse('toDoListDetail', args=[1])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'toDoList/todo_list.html')

    def testAddToDoListItemGet(self):
        ToDoList.objects.create(to_do_list_title="test1")
        url = reverse('addToDoListItem', args=[1])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'toDoItem/todolistitem_form.html')

    def testAddToDoListItemPost(self):
        ToDoList.objects.create(to_do_list_title="test1")
        url = reverse('addToDoListItem', args=[1])
        data = {
            'to_do_list_item_title': 'testItem1',
            'to_do_list_item_due_date': datetime.datetime.now().date()+timedelta(days=10),
            'to_do_list_item_description': 'loremIpsum',
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)
        # self.assertTemplateUsed(response, 'toDoItem/todolistitem_form.html')

    def testFailedNoTitleNoDateAddToDoListItemPost(self):
        ToDoList.objects.create(to_do_list_title="test1")
        url = reverse('addToDoListItem', args=[1])
        data = {
            'to_do_list_item_title': '',
            'to_do_list_item_due_date': '',
            'to_do_list_item_description': 'loremIpsum',
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'toDoItem/todolistitem_form.html')
        self.assertContains(response, 'please give title to the item')
        self.assertContains(response, 'please give due date to the item')

    def testFailedFalseDateAddToDoListItemPost(self):
        ToDoList.objects.create(to_do_list_title="test1")
        url = reverse('addToDoListItem', args=[1])
        data = {
            'to_do_list_item_title': 'testItem1',
            'to_do_list_item_due_date': datetime.datetime.now().date()-timedelta(days=10),
            'to_do_list_item_description': 'loremIpsum',
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'toDoItem/todolistitem_form.html')
        self.assertContains(response, 'due date must be after today')

    def testUpdateToDoListItemGet(self):
        self.setUpToDoItem()
        url = reverse('updateToDoListItem', args=[1,1])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'toDoList/todolistitemupdate_form.html')

    def testUpdateToDoListItemPost(self):
        self.setUpToDoItem()
        url = reverse('updateToDoListItem', args=[1, 1])
        data = {
            'to_do_list_item_title': 'testItem2',
            'to_do_list_item_due_date': datetime.datetime.now().date()+timedelta(days=20),
            'to_do_list_item_description': 'loremIpsum2',
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)
        # self.assertTemplateUsed(response, 'toDoItem/todolistitem_form.html')

    def testFailedNoTitleNoDateUpdateToDoListItemPost(self):
        self.setUpToDoItem()
        url = reverse('updateToDoListItem', args=[1, 1])
        data = {
            'to_do_list_item_title': '',
            'to_do_list_item_due_date': '',
            'to_do_list_item_description': 'loremIpsum2',
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'toDoList/todolistitemupdate_form.html')
        self.assertContains(response, 'please give title to the item')
        self.assertContains(response, 'please give due date to the item')

    def testFailedFalseDateAddToDoListItemPost(self):
        self.setUpToDoItem()
        url = reverse('updateToDoListItem', args=[1, 1])
        data = {
            'to_do_list_item_title': 'testItem2',
            'to_do_list_item_due_date': datetime.datetime.now().date()-timedelta(days=100),
            'to_do_list_item_description': 'loremIpsum3',
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'toDoList/todolistitemupdate_form.html')
        self.assertContains(response, 'due date must be after today')