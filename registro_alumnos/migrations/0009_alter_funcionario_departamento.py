# Generated by Django 4.0.5 on 2022-06-10 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro_alumnos', '0008_alter_f_avanzada_semestre_alter_f_inicial_semestre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcionario',
            name='departamento',
            field=models.CharField(choices=[('CIMET', 'CIMET'), ('Exelencia Academica', 'Exelencia Academica')], default='CIMET', max_length=40),
        ),
    ]
