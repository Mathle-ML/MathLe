from django.db import models
from django.contrib.auth.models import User

class users(models.Model):
    nivel = models.IntegerField(default=0)
    tema = models.CharField(max_length = 30, default="")
    actividad = models.CharField(max_length= 30, default="")
    porcentaje = models.IntegerField(default=0)