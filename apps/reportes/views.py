#from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import View
from xhtml2pdf import pisa
from django.db.models.aggregates import Sum
from django.db.models import Sum

from django.template.loader import get_template
# Create your views here.
from apps.personas.models import Departamento
from apps.personas.models import Empleado
from apps.articulos.models import Articulo
from django.db import connection

from datetime import datetime


class reporteArtDepto(View):
    def get(self, request, *args, **kwargs):
        
            template = get_template('reportes/reportes.html')
            context = {
            'titulo': 'esto es un pdf',
            }
            requisiciones = Articulo.objects.raw('SELECT ID_DEPARTAMENTO AS ID, NOMBRE,SUM( CANTIDAD_PEDIDO  ) pedido FROM SISTEMACOMPRAS.REQUISICION INNER JOIN SISTEMACOMPRAS.COMPRAS_REQUESICIONARTICULO ON SISTEMACOMPRAS.COMPRAS_REQUESICIONARTICULO.REQUISICION_ID=SISTEMACOMPRAS.REQUISICION.ID INNER JOIN SISTEMACOMPRAS.DEPARTAMENTO ON SISTEMACOMPRAS.DEPARTAMENTO.ID=SISTEMACOMPRAS.REQUISICION.ID_DEPARTAMENTO GROUP BY ID_DEPARTAMENTO, NOMBRE ORDER BY pedido DESC')
            context = {'requisicion': requisiciones
                       }
            html = template.render(context)
            response: HttpResponse = HttpResponse(content_type='application/pdf')
            pisa_status = pisa.CreatePDF(html, dest=response)
            return response


class reporteArtEmple(View):
    def get(self, request, *args, **kwargs):
        try:
            template = get_template('reportes/reporte2.html')
            context = {
            'titulo': 'esto es un pdf',

            }
            #con django
            articulos_solicitados = Departamento.objects.all()
            #cursor = connection.cursor()
            #cursor.execute('''SELECT * FROM departamento''')
            #cursor.execute('''SELECT count(*) FROM people_person''')
            #articulos_solicitados = cursor.fetchone()
            context = {'articulos': articulos_solicitados}
            html = template.render(context)
            response: HttpResponse = HttpResponse(content_type='application/pdf')
            #response['Content-Disposition'] = 'attachment; filename="reporte1.pdf"'
            pisa_status = pisa.CreatePDF(html, dest=response)
            return response
        except:
            pass
            return HttpResponseRedirect(reverse_lazy('home'))


class reporteArtProvee(View):
    def get(self, request, *args, **kwargs):
            template = get_template('reportes/reporte3.html')
            context = {
            'titulo': 'esto es un pdf',
            }
            
            articulos = Art.objects.raw('SELECT a.ID AS ID, ep.NOMBRE, a.nombre AS articulos, o.FECHA_FIN, o.FECHA_INICIO, a.marca,a.modelo, o.PRECIO FROM OFERTA o, ARTICULO a, "EMPRESA PROVEEDORA" ep WHERE o.ID_ARTICULOS=a.ID AND o.ID_PROVEDORA=ep.ID')
            fechas = datetime.now()
            context = {'articulo': articulos, 'fecha': fechas}
            html = template.render(context)
            response: HttpResponse = HttpResponse(content_type='application/pdf')
            #response['Content-Disposition'] = 'attachment; filename="reporte1.pdf"'
            pisa_status = pisa.CreatePDF(html, dest=response)
            return response

class reporteOrdenCompra(View):
    def get(self, request, *args, **kwargs):
        try:
            template = get_template('reportes/reporte4.html')
            context = {
            'titulo': 'esto es un pdf',

            }
            #con django
            articulos_solicitados = Departamento.objects.all()
            #cursor = connection.cursor()
            #cursor.execute('''SELECT * FROM departamento''')
            #cursor.execute('''SELECT count(*) FROM people_person''')
            #articulos_solicitados = cursor.fetchone()
            context = {'articulos': articulos_solicitados}
            html = template.render(context)
            response: HttpResponse = HttpResponse(content_type='application/pdf')
            #response['Content-Disposition'] = 'attachment; filename="reporte1.pdf"'
            pisa_status = pisa.CreatePDF(html, dest=response)
            return response
        except:
            pass
            return HttpResponseRedirect(reverse_lazy('home'))

class reporteStock(View):
    def get(self, request, *args, **kwargs):
        try:
            template = get_template('reportes/reporte5.html')
            context = {
            'titulo': 'esto es un pdf',

            }
            #con django
            articulos_solicitados = Departamento.objects.all()
            #cursor = connection.cursor()
            #cursor.execute('''SELECT * FROM departamento''')
            #cursor.execute('''SELECT count(*) FROM people_person''')
            #articulos_solicitados = cursor.fetchone()
            context = {'articulos': articulos_solicitados}
            html = template.render(context)
            response: HttpResponse = HttpResponse(content_type='application/pdf')
            #response['Content-Disposition'] = 'attachment; filename="reporte1.pdf"'
            pisa_status = pisa.CreatePDF(html, dest=response)
            return response
        except:
            pass
            return HttpResponseRedirect(reverse_lazy('home'))

class reporteInventario(View):
    def get(self, request, *args, **kwargs):
        try:
            template = get_template('reportes/reporte6.html')
            context = {
            'titulo': 'esto es un pdf',

            }
            #con django
            articulos_solicitados = Departamento.objects.all()
            #cursor = connection.cursor()
            #cursor.execute('''SELECT * FROM departamento''')
            #cursor.execute('''SELECT count(*) FROM people_person''')
            #articulos_solicitados = cursor.fetchone()
            context = {'articulos': articulos_solicitados}
            html = template.render(context)
            response: HttpResponse = HttpResponse(content_type='application/pdf')
            #response['Content-Disposition'] = 'attachment; filename="reporte1.pdf"'
            pisa_status = pisa.CreatePDF(html, dest=response)
            return response
        except:
            pass
            return HttpResponseRedirect(reverse_lazy('home'))