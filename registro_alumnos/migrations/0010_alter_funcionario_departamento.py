# Generated by Django 4.0.5 on 2022-06-10 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro_alumnos', '0009_alter_funcionario_departamento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcionario',
            name='departamento',
            field=models.CharField(choices=[('CIMET', 'CIMET'), ('Exito Academico', 'Exito Academico')], default='CIMET', max_length=40),
        ),
    ]
