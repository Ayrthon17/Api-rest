from django.db import models

# Create your models here.
class Libro(models.Model):
    nombre = models.CharField(max_length=100)
    editorial = models.CharField(max_length=100)