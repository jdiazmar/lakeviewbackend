from unittest.util import _MAX_LENGTH
from django.db import models
from authentication.models import User

# Create your models here.


class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    grade = models.CharField(max_length=255)
    school = models.CharField(max_length=255)
    age = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)