from django.db import models
from django.utils import timezone

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self):
         return self.nombre

class PlatoTipico(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=255)
    ingredientes = models.CharField(max_length=255)
    stock = models.IntegerField()
    puntaje = models.FloatField()
    creado_en = models.DateTimeField(default=timezone.now)

    def __str__(self):
         return self.nombre