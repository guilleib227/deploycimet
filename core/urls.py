"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#Deploy
from django.conf import settings
from django.conf.urls.static import static
#Deploy

from django.contrib import admin
from django.urls import path,include
from registro_alumnos.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',inicio.as_view(),name = 'index'),
    path('alumno/', ListaAlumno.as_view(),name = 'ListaAlumno') ,
    path('funcionario/', ListaFuncionario.as_view(),name = 'ListaFuncionario'),
    path('login/', Login.as_view(),name = 'Login'),
    path('home/', Home.as_view(),name = 'Home'),
    path('formacionI/', FormacionInicial.as_view(),name = 'formacion_i'),
    path('formacionA/', FormacionAvanzada.as_view(),name = 'formacion_a'),
    path('formacionE/', FormacionEspecializada.as_view(),name = 'formacion_e'),  
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

