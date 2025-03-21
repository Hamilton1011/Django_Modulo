from django.db import models

# Create your models here.
class Registro(models.Model):
    fecha=models.DateTimeField(auto_now_add=True)
    tipo=models.CharField(max_length=40)
    cantidad=models.IntegerField()
    lote=models.IntegerField()
    estado=models.BooleanField(default=True)

    def __str__(self):
        return self.tipo