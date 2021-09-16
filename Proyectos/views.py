from django.shortcuts import render

# Create your views here.
def proyectos(request):
    return render(request,"proyectos.html")

def login(request):
    return render(request,"login.html")

def registro(request):
    return render(request,"registro.html")