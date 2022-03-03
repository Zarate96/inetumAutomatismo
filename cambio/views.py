from django.shortcuts import render
from .models import Notificacion, Area
from django.db.models import Q

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