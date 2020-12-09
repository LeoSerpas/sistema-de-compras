from django.db import models
from apps.personas.models import EmpresaProvedora


# Create your models here.
class Articulo(models.Model):
    #id default
    serial = models.CharField(max_length=20)
    nombre = models.CharField(max_length=25) # cambiar dice articulo
    marca = models.CharField(max_length=25)
    modelo = models.CharField(max_length=25)
    descripcion = models.CharField(max_length=100)

    class Meta:
        db_table = 'Articulo'
        verbose_name = 'Articulo'
        verbose_name_plural = 'Articulos'
        default_permissions = []

    def __str__(self):
        return '%s' % (self.nombre)

class Oferta(models.Model):
    #id default
    precio = models.FloatField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    periodo_gracia = models.IntegerField() #arreglar diagrama
    descuento = models.IntegerField()    #arreglar diagrama
    tipo_entrega = models.CharField(max_length=25)
    id_articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE, db_column= 'id_articulos')
    id_provedora = models.ForeignKey(EmpresaProvedora, on_delete=models.CASCADE, db_column= 'id_provedora')
    
    
    class Meta:
        db_table = 'Oferta'
        verbose_name = 'Oferta'
        verbose_name_plural = 'Ofertas'
        default_permissions = []

    def __str__(self):
        return '%s' % (self.id_articulo)

class Inventario(models.Model):
    #id default
    existencia = models.IntegerField()
    costo_promedio = models.FloatField(default=None)
    id_articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE, db_column= 'id_articulos')

    class Meta:
        db_table = 'Inventario'
        verbose_name = 'Inventario'
        verbose_name_plural = 'Inventario'
        default_permissions = []

    def __str__(self):
        return '%s' % (self.id_articulo)

class Movimiento(models.Model):
    #id default
    cantidad = models.IntegerField()
    tipo = models.BooleanField()
    costo = models.FloatField(default=None)
    fecha = models.DateTimeField(auto_now_add=True)
    id_inventario = models.ForeignKey(Inventario, on_delete= models.CASCADE, db_column='id_inventario')    

    class Meta:
        db_table = 'Movimiento'
        verbose_name = 'Movimiento'
        verbose_name_plural = 'Movimiento'
        default_permissions = []

    def __str__(self):
        return '%s' % (self.id_inventario)

