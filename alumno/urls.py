from django.urls import path
from . import views

urlpatterns = [

    path('', views.inicio, name='inicio'),
    path('login/', views.logear, name='login'),
    path('registrarse/', views.registrarse, name='registrarse'),
    path('listado/', views.listado, name='listado'),
    path('registrar/', views.insertaralumno, name='registrar'),
    path('editar/<int:idAlumno>/', views.editar, name='editar'),
    path('eliminar/<idAlumno>/', views.eliminar, name='eliminar'),
]