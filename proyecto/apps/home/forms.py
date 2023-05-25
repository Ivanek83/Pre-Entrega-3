from django import forms
from . import models

class ArticuloForm(forms.ModelForm):
    class Meta:
        model = models.Articulo
        fields = '__all__'

class AutorForm(forms.ModelForm):
    class Meta:
        model = models.Autor
        fields = '__all__'

class MedioForm(forms.ModelForm):
    class Meta:
        model = models.Medio
        fields = '__all__'