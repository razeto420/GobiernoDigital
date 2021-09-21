from django.db.models import query
from Proyectos.models import Distrito, Proyecto
from django.shortcuts import render
from Proyectos.models import Proyecto,Distrito
from .models import Profile
from Proyectos.filters import ProyectFilter
# Create your views here.

def home(request):
    proyectos = Proyecto.objects.all()
    distritos = Distrito.objects.all()

    myFilter=ProyectFilter(request.GET,queryset=proyectos)
    proyectos=myFilter.qs

    return render(request,"home.html",{'proyectos':proyectos,'distritos':distritos,'myFilter':myFilter})



    
def addproject(request):
    return render(request)