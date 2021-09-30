from django.shortcuts import render, get_object_or_404
from .models import Proyecto

# Create your views here.


def project_detail(request,project_id):
    project=get_object_or_404(Proyecto,id=project_id)
    context={'projects':project}
    return render(request,"proyectos_detail.html",context)

def login(request):
    return render(request,"login.html")
