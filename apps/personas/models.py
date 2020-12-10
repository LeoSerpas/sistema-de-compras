from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Depa(models.Model):
    # id default
    nombreDepartamento = models.CharField(max_length=250)


    class Meta:
        db_table = 'Depa'
        verbose_name = 'Depa'
        verbose_name_plural = 'Depas'
        default_permissions = []



        def _str_(self):
            return '%s' % (self.concepto)

class Municipio(models.Model):
    # id default
    departamento_id = models.ForeignKey(Depa, on_delete=models.CASCADE)
    nombreMunicipio = models.CharField(max_length=250)

    class Meta:
        db_table = 'Municipio'
        verbose_name = 'Municipio'
        verbose_name_plural = 'Municipios'
        default_permissions = []



        def _str_(self):
            return '%s' % (self.concepto)


class Departamento(models.Model):
    #id default
    codigo = models.CharField(max_length=50) # no va ser el id arreglar
    nombre = models.CharField(max_length=50)

    class Meta:
        db_table = 'Departamento'
        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamentos'
        default_permissions = []

    def __str__(self):
        return '%s' % (self.codigo)


class Empleado(models.Model):
    #id default 
    primer_nombre = models.CharField(max_length=50)
    segundo_nombre = models.CharField(max_length=50)
    primer_apellido = models.CharField(max_length=50)
    segundo_apellido = models.CharField(max_length=50)
    genero = models.CharField(max_length=25)
    fecha_nacimiento = models.DateField()
    fecha_contratacion = models.DateField()
    direccion = models.TextField()
    dui = models.CharField(max_length=10)
    nit = models.CharField(max_length=17)
    telefono = models.CharField(max_length=25)
    auth_id = models.OneToOneField(User, on_delete = models.CASCADE, default=0)
    id_departamento = models.ForeignKey(Departamento, on_delete= models.CASCADE, db_column='id_departamento')
    depa_id = models.ForeignKey(Depa, on_delete=models.CASCADE, default = 0, db_column='id_depa')
    municipio_id = models.ForeignKey(Municipio, on_delete=models.CASCADE, default = 0, db_column='id_municipio')
    
    class Meta:
        db_table = 'Empleado'
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
        permissions = [
            ('usuarios_control', 'Manejo de los usuarios'),
            ('permisos_control', 'Manejo de los permisos')
        ]


    def __str__(self):
        return '%s' % (self.primer_nombre)

class EmpresaProvedora(models.Model):
    #id default
    nombre = models.CharField(max_length= 25)
    telefono = models.CharField(max_length=25)
    direccion = models.TextField()
    auth_id = models.OneToOneField(User, on_delete= models.CASCADE)
    depa_id = models.ForeignKey(Depa, on_delete=models.CASCADE, default = 0, db_column='id_depa')
    municipio_id = models.ForeignKey(Municipio, on_delete=models.CASCADE, default = 0, db_column='id_municipio')

    class Meta:
        db_table = 'Empresa Proveedora'
        verbose_name = 'Empresa Provedora'
        verbose_name_plural = 'Empresa Proveedora'
        default_permissions = []

    def __str__(self):
        return '%s' % (self.nombre)



     



