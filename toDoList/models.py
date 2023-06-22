from django.db import models

# Create your models here.
class ToDoList(models.Model):
    to_do_list_title = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f"{self.to_do_list_title}"

class ToDoItem(models.Model):
    to_do_item_title = models.CharField(max_length=50)
    #due date - date - cannot be empty
    to_do_due_date = models.DateTimeField(null=False)
    #submitted date - date - default and only value is when submitted
    to_do_submitted_date = models.DateTimeField(auto_now_add=True)
    #description - string - can be empty
    to_do_description = models.TextField(max_length=200, blank=True, default="no description")
    #toDoListID - int - can be empty
    to_do_list_id = models.IntegerField(blank=True, default=0)

    def __str__(self):
        return f"{self.to_do_item_title}: due {self.to_do_due_date}"

    class Meta:
        ordering = ["to_do_due_date"]