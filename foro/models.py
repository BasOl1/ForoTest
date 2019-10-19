from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=40, null=False)
    email = models.EmailField(max_length=50, null=False)
    contrasena = models.CharField(max_length=50, null=False)
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return self.nombre
