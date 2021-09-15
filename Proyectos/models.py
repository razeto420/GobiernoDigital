from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Provincia(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return f'Provincia de '+self.nombre

class Distrito(models.Model):
    nombre = models.CharField(max_length=50)
    provincia = models.ForeignKey(Provincia,on_delete=models.CASCADE)
    
    def __str__(self):
        return f'Distrito de '+self.nombre + ', Pronvincia de '+self.provincia.nombre


class Proyecto(models.Model):
    title = models.CharField(max_length=50)
    imagen = models.ImageField()
    descripcion = models.TextField(blank=True,null=True)
    presupuesto = models.FloatField()
    responsable = models.CharField(max_length=50)
    monto_cancelado = models.FloatField(blank=True,null=True)
    direccion = models.CharField(max_length=150)
    distrito = models.ForeignKey(Distrito,on_delete=models.CASCADE,blank=True,null=True)
    timestamp = models.DateTimeField(default=timezone.now)
    fecha_inicio = models.DateField()
    fecha_final_esperado = models.DateField()
    fecha_culminado = models.DateField(blank=True,null=True)
    adenda = models.CharField(blank=True,null=True,max_length=100)
    monto_adenda = models.FloatField(blank=True,null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='proyectos')
    
    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f'Proyecto '+self.title


class Comentario(models.Model):
    texto = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    proyecto = models.ForeignKey(Proyecto,on_delete=models.CASCADE)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f'Comentario de ' + self.user.username +' de Proyecto '+self.proyecto.title