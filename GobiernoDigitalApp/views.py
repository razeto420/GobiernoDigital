from Proyectos.models import Distrito, Proyecto
from django.shortcuts import render
from Proyectos.models import Proyecto,Distrito
from .models import Profile
# Create your views here.

def home(request):
    proyectos = Proyecto.objects.all()
    distritos = Distrito.objects.all()
    return render(request,"home.html",{'proyectos':proyectos,'distritos':distritos})


def addproject(request):
    return render(request)