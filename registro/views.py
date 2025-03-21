from django.shortcuts import render,redirect,get_object_or_404
from .models import Registro
from .forms import RegistroForm

# Create your views here.
def registros_lista(request):
    registro = Registro.objects.all()
    return render(request, 'registros_lista.html', {'registro':registro})

def registros_crear(request):
    if request.method == 'POST':
      formulario =  RegistroForm(request.POST)
      if formulario.is_valid():
         formulario.save()
         return redirect('registros_lista')
    else:
      formulario = RegistroForm()
      return render(request,'registros_forms.html', {'formulario':formulario})
    
def registros_editar(request,id):
    registro_id =  get_object_or_404(Registro, id=id)
    if request.method == 'POST':
      formulario =  RegistroForm(request.POST, instance=registro_id)
      if formulario.is_valid():
         formulario.save()
         return redirect('registros_lista')
    else:
      formulario = RegistroForm(instance=registro_id)
      return render(request,'registros_forms.html', {'formulario':formulario})
    
def registros_eliminar(request,id):
    registro_id =  get_object_or_404(Registro, id=id)
    if request.method == 'POST':
      registro_id.delete()
      return redirect('registros_lista')
    
    return render(request, 'registros_confirmar.html', {'registro': registro_id})
