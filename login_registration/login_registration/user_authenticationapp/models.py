from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    full_name=models.CharField(max_length=100)
    age=models.IntegerField()


# Create your models here.