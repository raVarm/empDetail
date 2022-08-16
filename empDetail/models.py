from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=264, error_messages = {"required": "Enter Your name"})
    username = models.CharField(max_length=264, unique=True)
    # password = models.CharField(max_length=264)
    email = models.EmailField(max_length=264, unique=True, blank=True)
    phone = models.IntegerField( blank=True)
    department = models.CharField(max_length=264)
    role = models.CharField(max_length=264)

    def __str__(self):
        return self.username

