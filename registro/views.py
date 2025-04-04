from django.shortcuts import render,redirect,get_object_or_404
from .models import Especie, Categoria
from .forms import EspecieForm,CategoriaForm
from django.shortcuts import render


def dashboard(request):
    return render(request, 'dashboard.html')

def categorias_lista(request):
    categorias = Categoria.objects.all()
    return render(request, 'categorias_lista.html', {'categorias': categorias})

# Crear  categoría
def categorias_crear(request):
    if request.method == 'POST':
        formularios = CategoriaForm(request.POST)
        if formularios.is_valid():
            formularios.save()
            return redirect('categorias_lista')
    else:
        formularios = CategoriaForm()
    
    return render(request, 'categorias_forms.html', {'formularios': formularios})

# Editar  categoría
def categorias_editar(request, id):
    categoria = get_object_or_404(Categoria, id=id)
    if request.method == 'POST':
        formularios = CategoriaForm(request.POST, instance=categoria)
        if formularios.is_valid():
            formularios.save()
            return redirect('categorias_lista')
    else:
        formularios = CategoriaForm(instance=categoria)
    
    return render(request, 'categorias_forms.html', {'formularios': formularios})

# Eliminar  categoría
def categorias_eliminar(request, id):
    categoria = get_object_or_404(Categoria, id=id)
    if request.method == 'POST':
        categoria.delete()
        return redirect('categorias_lista')
    
    return render(request, 'categorias_confirmar.html', {'categoria': categoria})

# Listar especies
def especies_lista(request):
    especies = Especie.objects.all()
    return render(request, 'registros_lista.html', {'especies':especies})
# Crear especie
def especies_crear(request):
    if request.method == 'POST':
      formulario =  EspecieForm(request.POST)
      if formulario.is_valid():
         formulario.save()
         return redirect('especies_lista')
    else:
      formulario = EspecieForm()
      return render(request,'registros_forms.html', {'formulario':formulario})

 # Editar especie   
def especies_editar(request,id):
    especie_id =  get_object_or_404(Especie, id=id)
    if request.method == 'POST':
      formulario =  EspecieForm(request.POST, instance=especie_id)
      if formulario.is_valid():
         formulario.save()
         return redirect('especies_lista')
    else:
      formulario = EspecieForm(instance=especie_id)
      return render(request,'registros_forms.html', {'formulario':formulario})
    
#eliminar especie    
def especies_eliminar(request,id):
    especie_id =  get_object_or_404(Especie, id=id)
    if request.method == 'POST':
      especie_id.delete()
      return redirect('especies_lista')
    
    return render(request, 'registros_confirmar.html', {'registro': especie_id})
