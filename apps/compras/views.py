from django.shortcuts import render, redirect
from apps.compras.models import *
from apps.articulos.models import *
from apps.personas.models import *
from django.contrib.auth.models import User

# Create your views here.
def indexRequision(request):
    user = request.user.id
    emple = Empleado.objects.get(auth_id=user)
    requisioncreadas = RequesionCompra.objects.filter(id_departamento=emple.id_departamento.id, estado="Solicitado")#valorar si hacer una relacion con empleado para ver solo el que el usuario crea
    contexto = {'requision': requisioncreadas}
    return render(request,'requision/index.html', contexto)

def generarRequision(request):
    if request.method == 'POST':
        user = request.user.id
        empleado = Empleado.objects.get(auth_id=user)
    
        new_requision = RequesionCompra()
        new_requision.fecha_entrega = request.POST.get('fecha_entrega')
        new_requision.fecha_pedido = request.POST.get('fecha_pedido')
        new_requision.estado = 'Solicitado'
        new_requision.id_departamento_id = empleado.id_departamento.id
        new_requision.save()
        return redirect('indexRequision')
    else:
        user = request.user.id
        empleado = Empleado.objects.get(auth_id=user)
        contexto = {'empleado': empleado
                    }
        return render(request, 'requision/generar.html', contexto) 

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
        return redirect('indexRequision')
    else:
        articulo = Articulo.objects.all()
        rearticulo = RequesicionArticulo.objects.filter(requisicion_id= id_requisicion)
        print(rearticulo)
        contexto = {'articulo': articulo,
                    'rearticulo': rearticulo
                    }
        return render(request,'requision/agregar_articulo.html', contexto)

def AprobarRequision(request):
    user = request.user.id
    emple = Empleado.objects.get(auth_id=user)
    requisioncreadas = RequesionCompra.objects.filter(id_departamento=emple.id_departamento.id)#valorar si hacer una relacion con empleado para ver solo el que el usuario crea
    contexto = {'requision': requisioncreadas}
    return render(request,'requision/aprobar.html',contexto)

def botonAprobar(request,id_requisicion):
    if request.method =='GET':
        requi = RequesionCompra.objects.get(id=id_requisicion)
        requi.estado = "Aprobado"
        requi.save()
        return redirect('aprobarRequision')

    




