from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('proyectos_detail/<int:project_id>/',views.project_detail,name="proyectos_detail"),
    path('login/',views.login,name="login"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)