from django.db import models
from django.core.validators import RegexValidator, MinValueValidator

class Client(models.Model):
    name = models.CharField(max_length=30)
    card = models.CharField(
        max_length=10,  # Limitado a 10 caracteres
        validators=[
            RegexValidator(regex='^\d{10}$', message='La cédula debe contener exactamente 10 números')
        ]
    )
    phone = models.CharField(
        max_length=10,  # Limitado a 10 caracteres
        validators=[
            RegexValidator(regex='^\d{10}$', message='El teléfono debe contener exactamente 10 números')
        ]
    )
    date = models.DateField()
    medical_prescription = models.CharField(max_length=200)
    valor = models.IntegerField(null=True) 
    trash = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Nombre: {self.name}"
