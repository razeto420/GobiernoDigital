from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm

# Create your views here.
def proyectos(request):
    return render(request,"proyectos.html")

def login(request):
    return render(request,"login.html")

def registro(request):
    form=UserCreationForm()
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()


    context={'form':form}
    return render(request,"registro.html",context)

def forgotpwd(request):
    return render(request,"forgot-password.html")