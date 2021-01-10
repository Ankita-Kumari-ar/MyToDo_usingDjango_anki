from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Todo(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    text=models.CharField(max_length=254)
    date_inserted=models.DateTimeField(auto_now_add=True)


class DoneTodo(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    text=models.CharField(max_length=254)
    start_date=models.DateTimeField()
    finished_date=models.DateTimeField()
    difference=models.CharField(max_length=64, default=0)
