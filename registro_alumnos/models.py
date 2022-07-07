from tabnanny import verbose
from tkinter import CASCADE
from django.db import models


#<<< MODELO FUNCIONARIO >>>
class Funcionario(models.Model):
    id_funcionario = models.AutoField(primary_key=True)
    nombres = models.CharField('Nombres', max_length=100, null=False, blank=False)
    apellidos = models.CharField('Apellidos', max_length=100, null=False, blank=False)
    departamento = (('CIMET','CIMET'),('Exito Academico','Exito Academico'))
    departamento = models.CharField(max_length=40,choices=departamento,default='CIMET',blank=False)
    correo = models.EmailField('Correo Electronico Institucional', blank=False, null=True)

    def funcionario(self):
        return"{} {} {}".format(self.nombres,self.apellidos,self.departamento)
    def __str__(self):
        return self.funcionario()

    class Meta:
        verbose_name = 'Funcionario'
        verbose_name_plural = 'Funcionarios'
        db_table='Funcionarios'

#<<< MODELO FUNCIONARIO >>>


#<<< MODELO FORMACION INICIAL >>>
class F_Inicial(models.Model):
    id = models.AutoField(primary_key=True)
    #Alumno_F_Inicial = models.ManyToManyField(Alumno,null=True,blank=False,on_delete=models.SET_NULL,verbose_name='Alumno: ')
    año = models.CharField('Año de Aprobacion',max_length=4,blank=False,null=False)
    semestre = (('10','10'),('20','20'))
    semestre = models.CharField('Semestre de aprobación',max_length=2,choices=semestre,default='',blank=False)

    def F_Inicial(self):
        return"{} {}".format(self.año,self.semestre)
    def __str__(self):
        return self.F_Inicial()

    class Meta:
        verbose_name = 'Formacion Inicial'
        verbose_name_plural = 'Formaciones Iniciales'
        db_table='Formacion Inicial'
#<<< MODELO FORMACION INICIAL >>>


#<<< MODELO FORMACION AVANZADA >>>
class F_Avanzada(models.Model):
    id = models.AutoField(primary_key=True)
    #Alumno_F_Avanzada = models.ManyToManyField(Alumno,null=True,blank=False,on_delete=models.SET_NULL,verbose_name='Alumno: ')
    año = models.CharField('Año de Aprobacion',max_length=4,blank=False,null=False)
    semestre = (('10','10'),('20','20'))
    semestre = models.CharField('Semestre de aprobación',max_length=2,choices=semestre,default='',blank=False)

    def F_Avanzada(self):
        return"{} {}".format(self.año,self.semestre)
    def __str__(self):
        return self.F_Avanzada()

    class Meta:
        verbose_name = 'Formacion Avanzada'
        verbose_name_plural = 'Formaciones Avanzadas'
        db_table='Formacion Avanzada'
#<<< MODELO FORMACION AVANZADA >>>


#<<< MODELO FORMACION ESPECIALIZADA >>>
class F_Especializada(models.Model):
    id = models.AutoField(primary_key=True)
    #Alumno_F_Especializada = models.ManyToManyField(Alumno,null=True,blank=False,on_delete=models.SET_NULL,verbose_name='Alumno: ')
    año = models.CharField('Año de Aprobacion',max_length=4,blank=False,null=False)
    semestre = (('10','10'),('20','20'))
    semestre = models.CharField('Semestre de aprobación',max_length=2,choices=semestre,default='',blank=False)

    def F_Especializada(self):
        return"{} {}".format(self.año,self.semestre)
    def __str__(self):
        return self.F_Especializada()

    class Meta:
        verbose_name = 'Formacion Especializada'
        verbose_name_plural = 'Formaciones Especializadas'
        db_table='Formacion Especializada'
#<<< MODELO FORMACION ESPECIALIZADA >>>


#<<< MODELO ALUMNO >>>
class Alumno(models.Model):
    id = models.AutoField(primary_key=True)
    rut = models.CharField('RUN',max_length=12,null=False,blank=False)
    nombres = models.CharField('Nombres', max_length=100, null=False, blank=False)
    apellidos = models.CharField('Apellidos', max_length=100, null=False, blank=False)
    fecha_nacimiento=models.DateField('Fecha de Nacimiento',null=False,blank=False)
    sexo= (('F','Femenino'),('M','Masculino'),('N','No Informa'))
    sexo=models.CharField(max_length=1,choices=sexo,default='',blank=True)
    carrera= (('A','Ingeniería en Información y Control de Gestión'),
    ('B','Ingeniería en Prevención de Riesgos y Medioambiente'),('C','Biología Marina'),
    ('D','Ingeniería en Acuicultura'),('E','Ingeniería Comercial'),('F','Derecho'),
    ('G','Ingeniería Civil Industrial'),('H','Pedagogía en Filosofía y Religión'),
    ('I','Pedagogía en Educación Diferencial con Mención en Desarrollo Emocional y Cognitivo'),
    ('J','Enfermería'),('K','Kinesiología'),('L','Medicina'),('M','Nutrición y Dietética'),
    ('N','Ingeniería Civil en Computación e Informática'),('O','Ingeniería en Tecnologías de Información'),
    ('P','Licenciatura en Ciencias Religiosas'))
    carrera=models.CharField(max_length=1,choices=carrera,default='A',blank=False)
    correo = models.EmailField('Correo Electronico Institucional', blank=False, null=False)
    correo2 = models.EmailField('Correo Electronico Alternativo', blank=True, null=True)
    aprobacion= (('A','Aprobado'),('R','Reprobado'))
    #curso1=models.CharField(verbose_name='Curso Basico:', max_length=1,choices=aprobacion,default='',blank=True)
    formacion_inicial = models.ForeignKey(F_Inicial,null=True,blank=True,on_delete=models.SET_NULL,verbose_name='Formacion Inicial')
    formacion_avanzada = models.ForeignKey(F_Avanzada,null=True,blank=True,on_delete=models.SET_NULL,verbose_name='Formacion Avanzada')
    formacion_especializada = models.ForeignKey(F_Especializada,null=True,blank=True,on_delete=models.SET_NULL,verbose_name='Formacion Especializada')

    #fecha_curso1=models.CharField('Aprobacion Curso Básico',max_length=6,blank=True,null=True)
    #curso2=models.CharField(verbose_name='Curso Intermedio:', max_length=1,choices=aprobacion,default='',blank=True)
    #fecha_curso2=models.CharField('Aprobacion Curso Intermedio', max_length=6,blank=True,null=True)
    #curso3=models.CharField(verbose_name='Curso Avanzado:', max_length=1,choices=aprobacion,default='',blank=True)
    #fecha_curso3=models.CharField('Aprobacion Curso Avanzado', max_length=6,blank=True,null=True)
    funcionario = models.ForeignKey(Funcionario,null=True,blank=False,on_delete=models.SET_NULL,verbose_name='Funcionario')

    #Fecha de registro del alumno en la plataforma (registro en la plataforma y no permite modificación, por seguridad)
    fecha_registro = models.DateField('Fecha de Registro', auto_now=False, auto_now_add=True)

    def alumno(self):
        return"{} {} {}".format(self.nombres,self.apellidos)
    def __str__(self):
        return self.alumno()

    class Meta:
        verbose_name = 'Alumno'
        verbose_name_plural = 'Alumnos'
        db_table='Alumnos'
#<<< MODELO ALUMNO >>>