from django.db import models

class Categoria(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    nombre = models.CharField(max_length=40)

    def __str__(self):
        return self.nombre  


class Especie(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)  
    nombre_cientifico = models.CharField(max_length=100)  
    nombre_comun = models.CharField(max_length=100)  
    ciclo_vida = models.CharField(max_length=40)
    temperatura_optima = models.CharField(max_length=40) 

    def __str__(self):
        return self.categoria.nombre
