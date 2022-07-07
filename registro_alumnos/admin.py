from django.contrib import admin
from .models import Alumno,Funcionario,F_Inicial,F_Avanzada,F_Especializada
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# <<< REGISTRO DE CLASE ALUMNO >>>
class AlumnoAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['nombres','rut', 'apellidos','carrera']
    list_display = ('nombres', 'apellidos','rut','carrera','formacion_inicial', 'formacion_avanzada', 'formacion_especializada','fecha_registro')
    list_filter = ('formacion_inicial', 'formacion_avanzada', 'formacion_especializada','carrera','rut')
    #resource_class = AlumnoResource #Analizar logica

class AlumnoResource(resources.ModelResource):
    class Meta:
        model = Alumno
# <<< REGISTRO DE CLASE ALUMNO >>>


# <<< REGISTRO DE CLASE FUNCIONARIO >>>
class FuncionarioAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['nombres', 'apellidos','departamento']
    list_display = ('nombres', 'apellidos','departamento','correo')
    #list_filter = ('departamento')

class FuncionarioResource(resources.ModelResource):
    class Meta:
        model = Funcionario
# <<< REGISTRO DE CLASE FUNCIONARIO >>>

# <<< REGISTRO DE CLASE F_Inicial >>>
class F_InicialAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['año', 'semestre']
    list_display = ('año', 'semestre')
    list_filter = ('año', 'semestre')

class F_InicialResource(resources.ModelResource):
    class Meta:
        model = F_Inicial
# <<< REGISTRO DE CLASE F_Inicial >>>

# <<< REGISTRO DE CLASE F_Avanzada >>>
class F_AvanzadaAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['año', 'semestre']
    list_display = ('año', 'semestre')
    list_filter = ('año', 'semestre')

class F_AvanzadaResource(resources.ModelResource):
    class Meta:
        model = F_Avanzada
# <<< REGISTRO DE CLASE F_Avanzada >>>

# <<< REGISTRO DE CLASE F_Especializada >>>
class F_EspecializadaAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['año', 'semestre']
    list_display = ('año', 'semestre')
    list_filter = ('año', 'semestre')

class F_EspecializadaResource(resources.ModelResource):
    class Meta:
        model = F_Especializada
# <<< REGISTRO DE CLASE F_Especializada >>>


# <<< REGISTRO DE MODELO>>>
admin.site.register(Alumno, AlumnoAdmin)
admin.site.register(Funcionario,FuncionarioAdmin)
admin.site.register(F_Inicial,F_InicialAdmin)
admin.site.register(F_Avanzada,F_AvanzadaAdmin)
admin.site.register(F_Especializada,F_EspecializadaAdmin)

#admin.site.register(Semestre, SemestreAdmin)
# <<< REGISTRO DE MODELO>>>