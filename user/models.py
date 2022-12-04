from django.db import models
from django.contrib.auth.models import User
from moderator.models import *
# Create your models here.

class Profile(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    university=models.ForeignKey(Universities, on_delete=models.CASCADE)
    role=models.CharField(max_length=100)
    college=models.CharField(max_length=100)
    phone=models.CharField(max_length=15)
    
    def __str__(self):
        return self.name




