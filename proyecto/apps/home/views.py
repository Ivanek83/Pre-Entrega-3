from django.shortcuts import render, redirect
# Create your views here.
from . import forms


def index(request):
    return render(request, 'home/index.html')

def subir_articulo(request):
    if request.method == 'POST':
        form = forms.ArticuloForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home:index')
    else:
        form = forms.ArticuloForm()
        contexto = {'form': form }
        return render(request, 'home/subir_articulo.html', context=contexto)

def cargar_autor(request):
    if request.method == 'POST':
        form = forms.AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home:index')
    else:
        form = forms.AutorForm()
        contexto = {'form': form }
        return render(request, 'home/cargar_autor.html', context=contexto)
    

def identificar_medio(request):
    if request.method == 'POST':
        form = forms.MedioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home:index')
    else:
        form = forms.MedioForm()
        contexto = {'form': form }
        return render(request, 'home/cargar_autor.html', context=contexto)    
