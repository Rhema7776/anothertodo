from django.db import models

# Create your models here.
class Todo(models.Model):
    username = models.CharField(max_length = 100, default="")
    taskname = models.CharField(max_length=100, default="")
    due_date = models.DateField()

    def __str__(self):
        return self.username