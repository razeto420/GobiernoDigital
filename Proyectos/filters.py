from django.db import models
import  django_filters  
from django import forms
from Proyectos.models import Proyecto

class ProyectFilter(django_filters.FilterSet):
    class Meta:
        model =Proyecto
        fields=["distrito"]
       
        