from django.db import models
from django.contrib.auth.models import User

class Todo(models.Model):
    owner=models.ForeignKey(User,on_delete=models.CASCADE,related_name="todo_owner")
    content=models.CharField(max_length=100)
    deadline=models.DateField(auto_now=False)
    