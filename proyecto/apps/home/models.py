from django.db import models

# Create your models here.

class Medio(models.Model):
    medio = models.CharField(max_length=100)
    genero = models.CharField(max_length=30)
    def __str__(self):
        return self.medio

    
class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    def __str__(self):
        return self.nombre
    
    
    
class Articulo(models.Model):
    titulo = models.CharField(max_length=100)
    fecha = models.DateField()
    medio_fk = models.ForeignKey(Medio, on_delete=models.SET_NULL, null=True)
    autor_fk = models.ForeignKey(Autor, on_delete=models.SET_NULL, null=True)
    articulo = models.URLField(null=True, blank=False)
    def __str__(self):
        return self.titulo
    

    