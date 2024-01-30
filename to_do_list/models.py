from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Task(models.Model):
    text = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  
    completed = models.BooleanField(default=False)
    completed_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, related_name='completed_tasks')


    def __str__(self):
        return self.text

    
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    bio = models.TextField(blank=True)

    


    def __str__(self):
        return self.user.username    
    
