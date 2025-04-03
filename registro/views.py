from django.shortcuts import render,redirect,get_object_or_404
from .models import Especie
from .forms import EspecieForm

# Create your views here.
def especies_lista(request):
    especies = Especie.objects.all()
    return render(request, 'registros_lista.html', {'especies':especies})

def especies_crear(request):
    if request.method == 'POST':
      formulario =  EspecieForm(request.POST)
      if formulario.is_valid():
         formulario.save()
         return redirect('especies_lista')
    else:
      formulario = EspecieForm()
      return render(request,'registros_forms.html', {'formulario':formulario})
    
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
    
def especies_eliminar(request,id):
    especie_id =  get_object_or_404(Especie, id=id)
    if request.method == 'POST':
      especie_id.delete()
      return redirect('especies_lista')
    
    return render(request, 'registros_confirmar.html', {'registro': especie_id})
