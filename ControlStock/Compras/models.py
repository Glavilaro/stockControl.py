from django.db import models

# Create your models here.
class Productos(models.Model):

    nombre = models.CharField(max_length=30)
    precio = models.FloatField()
    descripcion = models.CharField(max_length=200)


