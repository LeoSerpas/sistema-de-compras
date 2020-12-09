from django.urls import path, include
from apps.compras.views import *

urlpatterns = [
    path('requisicion/', indexRequision, name = 'indexRequision'),
    path('requisicion/aprobar/', AprobarRequision, name = 'aprobarRequision'),
    path('requisicion/cancelar/', RequisionAprobadas, name = 'cancelarRequision'),
    path('requisicion/generar/', generarRequision, name='generar_requisicion'),
    path('requisicion/editar/<int:id_requisicion>/', edit_requision, name='edit_requision'),
    path('requisicion/generar/articulos/<int:id_requisicion>/', generarRequisionArti, name='agregar_articulo'),
    path('requisicion/generar/articulos/<int:id_requisicion>/eliminar/', eliminar_articulo, name='eliminar_articulo'),
    path('requisicion/detalle/articulos/<int:id_requisicion>/', detalleRequesicion, name='detalle_requisicion'),
    path('requisicion/detalle2/articulos/<int:id_requisicion>/', detalleRequesicion2, name='detalle_requisicion2'),
    path('requisicion/aprobar/<int:id_requisicion>/botton/', botonAprobar, name='boton_aprobar'),
    path('requisicion/cancelar/<int:id_requisicion>/botton/', botonCancelar, name='boton_cancelar'),
    path('requisicion/aprobar/<int:id_requisicion>/eliminar/', requisicion_eliminar1, name='eliminar1'),
    ###------------------Compras-----------------------------##
    path('ordencompra/', indexCompras, name = 'indexcompras'),
    path('ordencompra/generada/', indexComprasgeneradas, name = 'indexgeneradas'),
    path('ordencompra/detalle/articulos/<int:id_requisicion>/', detalleRequesicion3, name='detalle_requisicion3'),
    ]