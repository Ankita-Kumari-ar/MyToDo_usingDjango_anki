from django.contrib import admin
from .models import Todo, DoneTodo
# Register your models here.
admin.site.register(Todo)
admin.site.register(DoneTodo)

