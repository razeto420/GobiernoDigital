from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('proyectos/',views.proyectos,name="Proyectos"),
    path('login/',views.login,name="login"),
    path('registro/',views.registro,name="registro"),
    path('forgotpwd/',views.forgotpwd,name="forgotpwd"),
    

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)