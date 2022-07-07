from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import ListView
from registro_alumnos.models import *

# Create your views here.

class inicio(TemplateView):
    template_name = 'index.html'

class Login(TemplateView):
    template_name = 'login.html'

class Home(TemplateView):
    template_name = 'home.html'
    
class ListaAlumno (ListView):
    template_name = 'alumno.html'
    model = Alumno
    context_object_name = 'alumno'

class ListaFuncionario (ListView):
    template_name = 'funcionario.html'
    model = Funcionario
    context_object_name = 'funcionario'

class FormacionInicial (ListView):
    template_name = 'formacion_i.html'
    model = F_Inicial
    context_object_name = 'formacion_i'

class FormacionAvanzada (ListView):
    template_name = 'formacion_a.html'
    model = F_Avanzada
    context_object_name = 'formacion_a'

class FormacionEspecializada (ListView):
    template_name = 'formacion_e.html'
    model = F_Especializada
    context_object_name = 'formacion_e'

