from typing import Counter
from django.db.models import query
from Proyectos.models import Distrito, Proyecto
from django.shortcuts import render
from .models import Profile
from Proyectos.filters import ProyectFilter
# Create your views here.

def home(request):
    proyectos = Proyecto.objects.all()
    distritos = Distrito.objects.all()
    myFilter=ProyectFilter(request.GET,queryset=proyectos)
    proyectos=myFilter.qs


    contador=Proyecto.objects.filter(distrito=1,estado='F').count()
    contadorProyectos=Proyecto.objects.filter(distrito=1).count()
    total=(contador/contadorProyectos)*100
    
  
    return render(request,"home.html",{'proyectos':proyectos,'distritos':distritos,'myFilter':myFilter,'total':total})

