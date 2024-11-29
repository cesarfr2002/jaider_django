from django.db import models
from django.core.validators import RegexValidator

class Provider(models.Model):
    name = models.CharField(max_length=40)
    product = models.CharField(max_length=100)  # Campo para el producto
    valor = models.IntegerField()  # Campo entero para el valor
    trash = models.BooleanField(default=False)

    def __str__(self):
        return f"Proveedor: {self.name}"
