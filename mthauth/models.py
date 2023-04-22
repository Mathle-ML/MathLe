from django.db import models
from django.contrib.auth.models import User

class users(models.Model):
    user = models.CharField(max_length = 20)
    password = models.CharField(max_length = 50)
    email = models.EmailField()
class session(models.Model):
    userto = models.CharField(max_length = 20)
    ide = models.CharField(max_length = 15)
    state = models.CharField(max_length = 10)