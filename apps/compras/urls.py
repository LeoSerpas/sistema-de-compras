from django.urls import path, include
from apps.compras.views import *

urlpatterns = [
    path('requisicion/', indexRequision, name = 'indexRequision'),
    path('requisicion/aprobar', AprobarRequision, name = 'aprobarRequision'),
    path('requisicion/generar/', generarRequision, name='generar_requisicion'),
    path('requisicion/generar/articulos/<int:id_requisicion>', generarRequisionArti, name='agregar_articulo'),
    path('requisicion/aprobar/<int:id_requisicion>/botton/', botonAprobar, name='boton_aprobar')

    ]