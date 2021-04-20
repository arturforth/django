from django.db import models

# Create your models here.
# Representacion de una DB
class Departamento(models.Model):
    name = models.CharField('Nombre', max_length=50)
    short_name = models.CharField('Nombre Corto', max_length=20, unique=True)
    anulate = models.BooleanField('Anulado', default=False) # Campo para especificar si el departamento esta activo o no

    def __str__(self):
        return str(self.id) + ' - ' + self.name + ' - ' + self.short_name