import  django_filters  
from Proyectos.models import Proyecto

class ProyectFilter(django_filters.FilterSet):
    class Meta:
        model =Proyecto
        fields=['distrito']
        