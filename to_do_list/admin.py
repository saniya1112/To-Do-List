from django.contrib import admin

# Register your models here.

from .models import Task

class Task(admin.ModelAdmin):
# Register the Blog model with the custom admin class
    admin.site.register(Task)