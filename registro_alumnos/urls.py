from unicodedata import name
from django.urls import path,include

from .views import *
from registro_alumnos import views

urlpatterns = [
    path('',inicio, name = 'index')  
]

urlpatterns = [
    path('alumnos/', views.ListaAlumno.as_view(), name = 'ListaAlumno'),
    path('formacionI/', views.FormacionInicial.as_view(), name = 'formacion_i'),
    path('formacionA/', views.FormacionAvanzada.as_view(), name = 'formacion_a'),
    path('formacionE/', views.FormacionEspecializada.as_view(), name = 'formacion_e'),
]

urlpatterns = [
    path('funcionario/', views.ListaFuncionario.as_view(), name = 'ListaFuncionario'),
    path('home/', Home, name = 'Home'),
    path('login/', Login, name = 'Login'),
]