from django.db import models

# Create your models here.

class Articulo(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=300)
    fecha = models.DateField()
    def __str__(self):
        return self.titulo
    
class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    def __str__(self):
        return self.nombre
    
    
class Medio(models.Model):
    medio = models.CharField(max_length=100)
    genero = models.CharField(max_length=30)
    def __str__(self):
        return self.medio
    

    