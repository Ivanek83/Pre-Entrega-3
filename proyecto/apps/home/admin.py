from django.contrib import admin

# Register your models here.
from . import models

admin.site.register(models.Articulo)
admin.site.register(models.Autor)
admin.site.register(models.Medio)

