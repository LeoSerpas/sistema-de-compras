from django.shortcuts import render, redirect
from apps.articulos.models import *
from django.contrib import messages

# Create your views here.


def indexArticulo(request):
    articulosregistrados = Articulo.objects.all()
    contexto = {'articulos': articulosregistrados}
    return render(request, 'articulos/index.html', contexto)


def articulo_create(request):
    if request.method == 'POST':
        serial = request.POST.get('serial')
        nombre = request.POST.get('nombre')
        marca = request.POST.get('marca')
        modelo = request.POST.get('modelo')
        descripcion = request.POST.get('descripcion')
        new_articulo = Articulo()
        new_articulo.serial = serial
        new_articulo.nombre = nombre
        new_articulo.marca = marca
        new_articulo.modelo = modelo
        new_articulo.descripcion = descripcion
        new_articulo.save()
        messages.success(request, '1')
        return redirect('indexArticulo')
    else:

        return render(request, 'articulos/ingresar.html')


def articulo_edit(request, id_articulo):
    articulo = Articulo.objects.get(id=id_articulo)
    if request.method == 'GET':

        contexto = {'articulo': articulo}
        return render(request, 'articulos/editar.html', contexto)

    elif request.method == 'POST':

        serial = request.POST.get('serial')
        nombre = request.POST.get('nombre')
        marca = request.POST.get('marca')
        modelo = request.POST.get('modelo')
        descripcion = request.POST.get('descripcion')

        articulo.serial = serial
        articulo.nombre = nombre
        articulo.marca = marca
        articulo.modelo = modelo
        articulo.descripcion = descripcion
        articulo.save()
        messages.success(request, '2')
        return redirect('indexArticulo')


def articulo_eliminar(request, id_articulo):
    if request.method == 'GET':
        articulo = Articulo.objects.get(id=id_articulo)
        articulo.delete()
        messages.success(request, '3')

    return redirect('indexArticulo')

#INVENTARIO

def indexInventario(request):
    inventarioArticulos = Inventario.objects.all()
    contexto = {'inventarios': inventarioArticulos}
    return render(request, 'inventario/index.html', contexto)

def indexMovimiento(request,id_inventario):
    movimientosInventario = Movimiento.objects.filter(id_inventario_id = id_inventario)
    inventario= Inventario.objects.get(id=id_inventario)
    contexto = {'movimientos': movimientosInventario,
                'inventario': inventario  }
    return render(request, 'inventario/indexMovimiento.html', contexto)

def movimiento_crear(request, id_inventario):
    inventario = Inventario.objects.get(id=id_inventario)
    if request.method == 'POST':
        cantidad = int(request.POST.get('cantidad'))
        costo = float(request.POST.get('costo_unitario'))
        tipo = int(request.POST.get('tipo'))
        fecha = request.POST.get('fecha')

        existenciaActual = inventario.existencia
        costoActual = inventario.costo_promedio

        if(tipo == 1):
            inventario.existencia = existenciaActual + cantidad
            inventario.costo_promedio = ((existenciaActual*costoActual)+(cantidad*costo))/inventario.existencia
        else:
            if(inventario.existencia - cantidad > 0 ):
                inventario.existencia = inventario.existencia - cantidad
                inventario.costo_promedio = ((existenciaActual*costoActual)-(cantidad*costo))/inventario.existencia
            else:
                messages.error(request, 'EXISTENCIA 0')
                return redirect('indexInventario')
            

        new_movimiento= Movimiento()
        new_movimiento.cantidad = cantidad
        new_movimiento.tipo = tipo
        new_movimiento.costo = costo
        new_movimiento.id_inventario_id = id_inventario
        
        new_movimiento.save()
        inventario.save()
        messages.success(request, '1')
        return redirect('indexInventario')
    elif request.method == 'GET':
        contexto = {'inventario': inventario}
        return render(request, 'inventario/ingresar.html', contexto)

def movimiento_eliminar(request, id_movimiento):
    if request.method == 'GET':
        movimiento = Movimiento.objects.get(id=id_movimiento)
        id_inventario = movimiento.id_inventario_id
        inventario = Inventario.objects.get(id=id_inventario)

        existenciaActual = inventario.existencia
        costoActual = inventario.costo_promedio

        if(movimiento.tipo == 1):
            inventario.existencia = inventario.existencia - movimiento.cantidad
            inventario.costo_promedio = ((existenciaActual*costoActual)-(movimiento.cantidad*movimiento.costo))/inventario.existencia
        else:
            if(inventario.existencia - movimiento.cantidad >= 0 ):
                inventario.existencia = inventario.existencia + movimiento.cantidad
                inventario.costo_promedio = ((existenciaActual*costoActual)+(movimiento.cantidad*movimiento.costo))/inventario.existencia
            else:
                messages.error(request, 'EXISTENCIA 0')
                return redirect('indexInventario')
        inventario.save()
        movimiento.delete()
        messages.success(request, '3')

    return redirect('indexInventario')
