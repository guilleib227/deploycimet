# Generated by Django 4.0.5 on 2022-06-10 01:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registro_alumnos', '0005_alter_alumno_funcionario'),
    ]

    operations = [
        migrations.CreateModel(
            name='F_Avanzada',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('año', models.CharField(max_length=4, verbose_name='Año de Aprobacion')),
                ('semestre', models.CharField(choices=[('A', '10'), ('B', '20')], default='', max_length=1, verbose_name='Semestre de aprobación')),
            ],
            options={
                'verbose_name': 'Formacion Avanzada',
                'verbose_name_plural': 'Formaciones Avanzadas',
                'db_table': 'Formacion Avanzada',
            },
        ),
        migrations.CreateModel(
            name='F_Especializada',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('año', models.CharField(max_length=4, verbose_name='Año de Aprobacion')),
                ('semestre', models.CharField(choices=[('A', '10'), ('B', '20')], default='', max_length=1, verbose_name='Semestre de aprobación')),
            ],
            options={
                'verbose_name': 'Formacion Especializada',
                'verbose_name_plural': 'Formaciones Especializadas',
                'db_table': 'Formacion Especializada',
            },
        ),
        migrations.CreateModel(
            name='F_Inicial',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('año', models.CharField(max_length=4, verbose_name='Año de Aprobacion')),
                ('semestre', models.CharField(choices=[('A', '10'), ('B', '20')], default='', max_length=1, verbose_name='Semestre de aprobación')),
            ],
            options={
                'verbose_name': 'Formacion Inicial',
                'verbose_name_plural': 'Formaciones Iniciales',
                'db_table': 'Formacion Inicial',
            },
        ),
        migrations.RemoveField(
            model_name='alumno',
            name='curso1',
        ),
        migrations.RemoveField(
            model_name='alumno',
            name='curso2',
        ),
        migrations.RemoveField(
            model_name='alumno',
            name='curso3',
        ),
        migrations.RemoveField(
            model_name='alumno',
            name='fecha_curso1',
        ),
        migrations.RemoveField(
            model_name='alumno',
            name='fecha_curso2',
        ),
        migrations.RemoveField(
            model_name='alumno',
            name='fecha_curso3',
        ),
        migrations.AddField(
            model_name='alumno',
            name='formacion_avanzada',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='registro_alumnos.f_avanzada', verbose_name='Formacion Avanzada'),
        ),
        migrations.AddField(
            model_name='alumno',
            name='formacion_especializada',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='registro_alumnos.f_especializada', verbose_name='Formacion Especializada'),
        ),
        migrations.AddField(
            model_name='alumno',
            name='formacion_inicial',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='registro_alumnos.f_inicial', verbose_name='Formacion Inicial'),
        ),
    ]