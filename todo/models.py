from django.db import models

# Create your models here.


class Todo(models.Model):
    event = models.CharField(max_length=1024)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    is_completed = models.BooleanField(default=False)