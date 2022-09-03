import email
from django.db import models

# Create your models here.

class usuario(models.Model):
    nombre_usuario=models.CharField(max_length=30)
    nombre=models.CharField(max_length=20)
    apellido=models.CharField(max_length=20, null=True)
    email=models.EmailField()
    curso=models.IntegerField()
    progreso=models.IntegerField()

    def __str__(self):
        return self.nombre_usuario