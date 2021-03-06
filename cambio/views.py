import csv
from django.shortcuts import render
#from .models import Notificacion, Area
from django.db.models import Q
from .models import GestionPlanificada, GestionNoPlanificada
from django.shortcuts import render, HttpResponse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic.detail import DetailView

# Create your views here.
def calendario(request):
    ots_aprobadas = GestionPlanificada.objects.filter(estatus='APROBADA')
    queryset = request.GET.get('seleccionar')


    if queryset:
        if queryset ==('Seleccione...'):
            ots_aprobadas = GestionPlanificada.objects.filter(estatus='APROBADA')
        else:
            ots_aprobadas =  GestionPlanificada.objects.filter(estatus='APROBADA').filter(
                Q(area=queryset)
            ).distinct()
    print(ots_aprobadas)
    context = {
        'ots_aprobadas': ots_aprobadas,
    }
    return render(request, "cambio/calendario.html", context)

#CAMBIO UNA ORDEN DE TRABAJO
class OtDetailView(DetailView):
    model = GestionPlanificada
    template_name = "cambio/ot_detail.html"

@login_required
def reportePlanificadas(request):
    planificadas = GestionPlanificada.objects.all()
    if request.method == 'POST':
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="planificadas.csv"'
        response.write(u'\ufeff'.encode('utf8'))

        writer = csv.writer(response)
        # writer.writerow(['Gerente','LT','Proyecto','Cumplimiento','Fecha1','Fecha2', 'Fecha3', 'Fecha4', 'Fecha5', 'Fecha6', 'Fecha7','Gestor','Comentarios','Entregables','Entregables no entregados','Estado','Detencion PP','Soporte Técnico'])
        # for proyecto in proyectos:
        #     writer.writerow([proyecto.soporte.gerente, proyecto.lider.gerente, proyecto.name_proyecto, proyecto.cumplimiento, proyecto.getFechaProxima(), '', '', '', '', '', '', proyecto.gestor,
        #                     proyecto.comentarios_vista, proyecto.get_fechasEntregado(), proyecto.get_fechasNoEntregado(), proyecto.estatus, proyecto.detencion, proyecto.soporte.name])

        writer.writerow(['GERENTE RESPONSABLE','Autor','Categoria','OM','TÍTULO','DESCRIPCIÓN','Afectación (B2B o B2C)', 'CRITICIDAD DEL CAMBIO', 'IMPACTO', 'TIEMPO DE EJECUCIÓN', 'TIEMPO DE ROLLBACK',
                        'TIEMPO DE AFECTACIÓN', 'FECHA Y HORA ASIGNADAS PARA LA EJECUCIÓN', 'Afectación', 'HORARIO Afectación', 'Gestor','tareas'])

        for planificada in planificadas:
            writer.writerow([planificada.gerente,planificada.autor, planificada.categoria, planificada.om, planificada.titulo, planificada.descripcion, planificada.afectacion_b2b_b2c, planificada.criticidad,
            planificada.impacto, planificada.durationEjecucion(), planificada.durationRollback(), planificada.durationAfectacion(), planificada.getFecHorAsignadas(),
            planificada.afectacion, planificada.horarioAfectacion(),planificada.gestor,planificada.comentarios_fechas])
#agregue planificada.gestor()
        return response

    context = {
        'planificadas' : planificadas,
    }

    return render(request, 'cambio/reportePlanificadas.html',context)

@login_required
def reporteNoPlanificadas(request):
    no_planificadas = GestionNoPlanificada.objects.all()
    print(no_planificadas)
    if request.method == 'POST':
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="no_planificadas.csv"'
        response.write(u'\ufeff'.encode('utf8'))

        writer = csv.writer(response)
        # writer.writerow(['Gerente','LT','Proyecto','Cumplimiento','Fecha1','Fecha2', 'Fecha3', 'Fecha4', 'Fecha5', 'Fecha6', 'Fecha7','Gestor','Comentarios','Entregables','Entregables no entregados','Estado','Detencion PP','Soporte Técnico'])
        # for proyecto in proyectos:
        #     writer.writerow([proyecto.soporte.gerente, proyecto.lider.gerente, proyecto.name_proyecto, proyecto.cumplimiento, proyecto.getFechaProxima(), '', '', '', '', '', '', proyecto.gestor,
        #                     proyecto.comentarios_vista, proyecto.get_fechasEntregado(), proyecto.get_fechasNoEntregado(), proyecto.estatus, proyecto.detencion, proyecto.soporte.name])

        writer.writerow(['GERENTE RESPONSABLE','Categoria','OM','TÍTULO','DESCRIPCIÓN','Afectación (B2B o B2C)', 'CRITICIDAD DEL CAMBIO', 'IMPACTO', 'TIEMPO DE EJECUCIÓN', 'TIEMPO DE ROLLBACK',
                        'FECHA Y HORA ASIGNADAS PARA LA EJECUCIÓN', 'Afectación', 'HORARIO Afectación', 'Gestor'])

        for planificada in no_planificadas:
            writer.writerow([planificada.gerente, planificada.categoria, planificada.om, planificada.titulo, planificada.descripcion, planificada.afectacion_b2b_b2c, planificada.criticidad,
            planificada.impacto, planificada.tiempo_ejecucion, planificada.tiempo_rollback, planificada.tiempo_afectacion, planificada.getFecHorAsignadas(),
            planificada.afectacion, planificada.horario])

        return response

    context = {
        'no_planificadas' : no_planificadas,
    }

    return render(request, 'cambio/reporteNoPlanificadas.html',context)