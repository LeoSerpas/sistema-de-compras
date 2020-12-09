from django.db import models
from apps.articulos.models import Articulo, Oferta
from apps.personas.models import Departamento, EmpresaProvedora
# Create your models here.

class RequesionCompra(models.Model):
    #Id default
    articulos = models.ManyToManyField(Articulo, through='RequesicionArticulo')
    id_departamento = models.ForeignKey(Departamento, on_delete= models.CASCADE, db_column='id_departamento')
    fecha_pedido = models.DateField()
    fecha_entrega = models.DateField()
    estado = models.CharField(max_length=30)
    comprahecha = models.CharField(max_length=30)

    class Meta:
        db_table = 'Requisicion'
        verbose_name = 'Requsicion'
        verbose_name_plural = 'Requisicion'
        default_permissions = []

    def __str__(self):
        return '%s' % (self.id_articulo)      

class RequesicionArticulo(models.Model):  
    #id_default
    articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE)
    requisicion = models.ForeignKey(RequesionCompra, on_delete=models.CASCADE)
    cantidad_pedido = models.IntegerField()

class ordenCompra(models.Model):
    #Id default
    id_requisicion = models.ForeignKey(RequesionCompra, on_delete= models.CASCADE, db_column='id_requisicion')
    ofertas = models.ManyToManyField(Oferta)
    precio_total = models.FloatField()
    fecha_orden = models.DateField()
    fecha_entrega = models.DateField()

    class Meta:
        db_table = 'orden de compra'
        verbose_name = 'orden de compra'
        verbose_name_plural = 'ordenes de compra'
        default_permissions = []

    def __str__(self):
        return '%s' % (self.id_requisicion)      


class NotaRemision(models.Model):
    #id default
    id_orden = models.ForeignKey(ordenCompra, on_delete= models.CASCADE, db_column='id_orden')
    id_proveedor = models.ForeignKey(EmpresaProvedora, on_delete= models.CASCADE, db_column='id_proveedor')
    #quitar usuario
    precio_total = models.FloatField()

    class Meta:
        db_table = 'Nota remision'
        verbose_name = 'Nota remision'
        verbose_name_plural = 'Notas remision'
        default_permissions = []

    def __str__(self):
        return '%s' % (self.id_orden)      

