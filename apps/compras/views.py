from django.shortcuts import render, redirect
from apps.compras.models import *
from apps.articulos.models import *
from apps.personas.models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse

# Create your views here.


def indexRequision(request):
    user = request.user.id
    emple = Empleado.objects.get(auth_id=user)
    requisioncreadas = RequesionCompra.objects.filter(
        id_departamento=emple.id_departamento.id, estado="Solicitado")
    contexto = {'requision': requisioncreadas,
                'emple': emple}
    return render(request, 'requision/index.html', contexto)


def generarRequision(request):
    if request.method == 'POST':
        user = request.user.id
        empleado = Empleado.objects.get(auth_id=user)

        new_requision = RequesionCompra()
        new_requision.fecha_entrega = request.POST.get('fecha_entrega')
        new_requision.fecha_pedido = request.POST.get('fecha_pedido')
        new_requision.estado = 'Solicitado'
        new_requision.comprahecha = "Sin generar"
        new_requision.id_departamento_id = empleado.id_departamento.id
        new_requision.save()
        messages.success(request, '1')
        return redirect('indexRequision')
    else:
        user = request.user.id
        empleado = Empleado.objects.get(auth_id=user)
        contexto = {'empleado': empleado
                    }
        return render(request, 'requision/generar.html', contexto)

def edit_requision(request, id_requisicion):
    user = request.user.id
    requesion = RequesionCompra.objects.get(pk=id_requisicion)
    empleado = Empleado.objects.get(auth_id=user)
    if request.method=='POST':
        fecha_pedido = request.POST.get('fecha_pedido')
        fecha_entrega = request.POST.get('fecha_entrega')

        requesion.fecha_entrega = fecha_entrega
        requesion.fecha_pedido = fecha_pedido
        requesion.estado = 'Solicitado'
        requesion.id_departamento_id = empleado.id_departamento.id
        requesion.save()
        messages.success(request, '2')
        return redirect('indexRequision')
    elif request.method == 'GET':
        contexto = {'empleado': empleado,
                    'requision': requesion
                    }                            
        return render(request, 'requision/editarReq.html', contexto)
                    

def generarRequisionArti(request, id_requisicion):
    if request.method == 'POST':
        idarticulo = request.POST.get('id_articulo')
        cantidad = request.POST.get('cantidad')

        requesion = RequesionCompra.objects.get(pk=id_requisicion)
        new_rarticulo = RequesicionArticulo()
        new_rarticulo.requisicion_id = requesion.id
        new_rarticulo.articulo_id = idarticulo
        new_rarticulo.cantidad_pedido = cantidad
        new_rarticulo.save()
        messages.success(request, '1')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        articulo = Articulo.objects.all()
        rearticulo = RequesicionArticulo.objects.filter(
            requisicion_id=id_requisicion)
        print(rearticulo)
        contexto = {'articulo': articulo,
                    'rearticulo': rearticulo
                    }
        return render(request, 'requision/agregar_articulo.html', contexto)


def AprobarRequision(request):
    user = request.user.id
    emple = Empleado.objects.get(auth_id=user)
    requisioncreadas = RequesionCompra.objects.filter(
        id_departamento=emple.id_departamento.id, estado="Solicitado" )
    contexto = {'requision': requisioncreadas,
                'emple': emple}
    return render(request, 'requision/aprobar.html', contexto)

def RequisionAprobadas(request):
    user = request.user.id
    emple = Empleado.objects.get(auth_id=user)
    requisioncreadas = RequesionCompra.objects.filter(
        id_departamento=emple.id_departamento.id, estado="Aprobado" )
    contexto = {'requision': requisioncreadas,
                'emple': emple}
    return render(request, 'requision/cancelar.html', contexto)

def detalleRequesicion(request, id_requisicion):
    requision = RequesionCompra.objects.get(pk=id_requisicion)
    rearticulo = RequesicionArticulo.objects.filter(requisicion_id=id_requisicion)
    user = request.user.id
    emple = Empleado.objects.get(auth_id=user)
    contexto = {'requision': requision,
                'rearticulo': rearticulo,
                'emple': emple}
    return render(request, 'requision/detalle2.html', contexto)

def detalleRequesicion2(request, id_requisicion):
    requision = RequesionCompra.objects.get(pk=id_requisicion)
    rearticulo = RequesicionArticulo.objects.filter(requisicion_id=id_requisicion)
    user = request.user.id
    emple = Empleado.objects.get(auth_id=user)
    contexto = {'requision': requision,
                'rearticulo': rearticulo,
                'emple': emple}
    return render(request, 'requision/detalle.html', contexto)    

def botonAprobar(request, id_requisicion):
    if request.method == 'GET':
        requi = RequesionCompra.objects.get(id=id_requisicion)
        requi.estado = "Aprobado"
        requi.save()
        messages.success(request, '1')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def botonCancelar(request, id_requisicion):
    if request.method == 'GET':
        requi = RequesionCompra.objects.get(id=id_requisicion)
        requi.estado = "Solicitado"
        requi.save()
        messages.success(request, '1')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def eliminar_articulo(request, id_rearticulo):
    if request.method == 'GET':
        requi = RequesicionArticulo.objects.get(id=id_rearticulo)
        requi.delete()
        messages.success(request, '3')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def requisicion_eliminar1(request, id_requisicion):
    if request.method == 'GET':
        requi = RequesionCompra.objects.get(id=id_requisicion)
        requi.delete()
        messages.success(request, '2')

    return redirect('aprobarRequision')



###----------------------------------ORDEN DE COMPRA-----------------------------------------------###


def indexCompras(request):
    requisioncreadas = RequesionCompra.objects.filter(estado="Aprobado", comprahecha="Sin generar")
    contexto = {'requision': requisioncreadas,
                }
    return render(request, 'compra/index.html', contexto)


def indexComprasgeneradas(request):
    requisioncreadas = RequesionCompra.objects.filter(comprahecha="Generada")
    contexto = {'requision': requisioncreadas,
                }
    return render(request, 'compra/indexgenerada.html', contexto)


def detalleRequesicion3(request, id_requisicion):
    if request.method == 'GET':
        requision = RequesionCompra.objects.get(pk=id_requisicion)
        rearticulo = RequesicionArticulo.objects.filter(requisicion_id=id_requisicion)
        oferta = Oferta.objects.all()
        contexto = {'requision': requision,
                    'rearticulo': rearticulo,
                    'oferta': oferta
                    }
        return render(request, 'compra/detalle.html', contexto) 

    elif request.method == 'POST':
        ofertas = Oferta.objects.filter(id__in = request.POST.getlist('ofertas'))       
        requi = RequesionCompra.objects.get(pk=id_requisicion)
        new_compra = ordenCompra()
        new_compra.id_requisicion_id = requi.id
        new_compra.fecha_orden = request.POST.get('fecha_orden')
        new_compra.fecha_entrega = request.POST.get('fecha_entrega')
        new_compra.precio_total = 100 #falta calcular
        new_compra.save()
        if len(ofertas) > 0:
            new_compra.ofertas.add(*ofertas)
        requi.comprahecha = "Generada"
        requi.save()
        messages.success(request,1)
        print(ofertas)
        return redirect('indexcompras')

