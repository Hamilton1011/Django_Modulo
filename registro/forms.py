from django import forms
from .models import Especie, Categoria

class EspecieForm(forms.ModelForm):
    class Meta:
        model = Especie
        fields = [ 'categoria', 'nombre_cientifico', 'nombre_comun', 'ciclo_vida', 'temperatura_optima']
        widgets = {
            'categoria': forms.Select(attrs={'class': 'form-control'}),  
        }

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre']
