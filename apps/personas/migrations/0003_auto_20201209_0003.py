# Generated by Django 2.2 on 2020-12-09 06:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0002_auto_20201204_2032'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='empleado',
            options={'permissions': [('usuarios_control', 'Manejo de los usuarios'), ('permisos_control', 'Manejo de los permisos')], 'verbose_name': 'Empleado', 'verbose_name_plural': 'Empleados'},
        ),
    ]