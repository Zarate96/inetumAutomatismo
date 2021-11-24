import csv
from django.core.paginator import Paginator
from django.shortcuts import render, HttpResponse, get_object_or_404
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from django.views.generic import ListView, DetailView
from django.views import View

from .forms import GestionForm
from .models import Gestion
from .filters import GestionFilter

class gestionProyectos(ListView):
    template_name = "problema/proyectos_list.html"
    model = Gestion
    context_object_name = "proyectos"

class proyectoDetalle(DetailView):
    template_name = "problema/proyecto_detalle.html"
    model = Gestion
    context_object_name = "proyecto"

class crearProyectos(FormView):
    form_class = GestionForm
    template_name = "problema/problema_create.html"
    
def reporteRecurrencia(request):
    proyectos = Gestion.objects.all()
    paginator = Paginator(proyectos, 25) 
    filter = GestionFilter(request.GET, queryset=proyectos)
    proyectos = filter.qs
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if request.method == 'POST':
        response = HttpResponse(content_type='text/csv')
        
        writer = csv.writer(response)
        writer.writerow(['Gerente','LT','Proyecto','Cumplimiento','Fecha1','Fecha2', 'Fecha3', 'Fecha4', 'Fecha5', 'Fecha6', 'Fecha7','Gestor','Comentarios','Entregables','Estado','Detencion PP'])
        for proyecto in proyectos:
            writer.writerow([proyecto.soporte.gerente, proyecto.lider.gerente, proyecto.name_proyecto, proyecto.cumplimiento, proyecto.getFechaProxima(), '', '', '', '', '', '', proyecto.gestor, 
                            proyecto.comentarios_vista, proyecto.getEntregables(), proyecto.estatus, proyecto.detencion])
        
        response['Content-Disposition'] = 'attachment; filename="reporte.csv"'

        return response

    context = {
        'proyectos' : proyectos,
        'filter': filter,
        'page_obj': page_obj,
    }
    return render(request, 'problema/reporte.html',context)

def exportProyectos(request):
    proyectos = Gestion.objects.all()

    response = HttpResponse(content_type='text/csv')
    
    writer = csv.writer(response)
    writer.writerow(['ID','Nombre','Tipo de Proyecto','Estatus','Gestor','Líder Técnico','Grupos','Area de ingeniería','Soporte Técnico','Nombre del PMO','Catálogo'
                    ,'Orden de trabajo','Comentarios','Cumplimiento','BL'])
    for proyecto in proyectos:

        for grupo in proyecto.grupo.all():
            grupos = []
            grupos.append(grupo.name)
        
        for catalogo in proyecto.catalogo.all():
            catalogos = []
            catalogos.append(catalogo.name)
        
        for ot in proyecto.ot.all():
            ots = []
            ots.append(ot.name)


        writer.writerow([proyecto.id_proyecto, proyecto.name_proyecto, proyecto.tipoProyecto, proyecto.estatus, proyecto.gestor, proyecto.lider, grupos, proyecto.area, 
        proyecto.soporte, proyecto.pmo, catalogos, ots, proyecto.comentarios_vista, proyecto.cumplimiento, proyecto.backlog])
    
    response['Content-Disposition'] = 'attachment; filename="proyectos.csv"'

    return response
    
    # writer.writerow(['Username', 'First name', 'Last name', 'Email address'])


