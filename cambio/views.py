import csv
from django.shortcuts import render
#from .models import Notificacion, Area
from django.db.models import Q
from .models import GestionPlanificada
from django.shortcuts import render, HttpResponse, get_object_or_404

# Create your views here.
def calendario(request):
    areas = Area.objects.all()
    queryset = request.GET.get('seleccionar')
    if queryset ==('Seleccione...'):
        notificaciones = Notificacion.objects.all()
    elif queryset != None:
        notificaciones = Notificacion.objects.filter(
            Q(gerente__area__name__icontains=queryset)
        ).distinct()
    else:
        notificaciones = Notificacion.objects.all()
    context={
        'notificaciones':notificaciones,
        'areas':areas,
    }
    return render(request, "cambio/calendario.html", context)

def reportePlanificadas(request):
    planificadas = GestionPlanificada.objects.all()
    print(planificadas)
    if request.method == 'POST':
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="planificadas.csv"'
        response.write(u'\ufeff'.encode('utf8'))
        
        writer = csv.writer(response)
        # writer.writerow(['Gerente','LT','Proyecto','Cumplimiento','Fecha1','Fecha2', 'Fecha3', 'Fecha4', 'Fecha5', 'Fecha6', 'Fecha7','Gestor','Comentarios','Entregables','Entregables no entregados','Estado','Detencion PP','Soporte Técnico'])
        # for proyecto in proyectos:
        #     writer.writerow([proyecto.soporte.gerente, proyecto.lider.gerente, proyecto.name_proyecto, proyecto.cumplimiento, proyecto.getFechaProxima(), '', '', '', '', '', '', proyecto.gestor, 
        #                     proyecto.comentarios_vista, proyecto.get_fechasEntregado(), proyecto.get_fechasNoEntregado(), proyecto.estatus, proyecto.detencion, proyecto.soporte.name])
        
        writer.writerow(['OM'])

        for planificada in planificadas:
            writer.writerow([planificada.om])
    
        return response

    context = {
        'planificadas' : planificadas,
    }

    return render(request, 'cambio/reportePlanificadas.html',context)