from django.shortcuts import render
from .models import EstatusInterATT,RutasInterEstatus,RutasInterComentarios,RutasInterFolioGuio, HcAPN
from django.utils import timezone
from datetime import timedelta
from task.selenium import get_hcInterATT, get_hcAPN, get_hcRutasInter
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist, PermissionDenied

# Create your views here.

@login_required
def healtcheaksInterAtt(request):
    if request.user.username == 'hcAdmin':
        estatus = EstatusInterATT.objects.all()
        hora = timezone.now() - timedelta(minutes=30)
        contexto ={
            'estatus': estatus,
            'hora':hora
        }
        return render(request, "healtcheaks/reporteHcInterBot.html", contexto )
    else:
        raise PermissionDenied()

@login_required
def healtcheaksRutasInter(request):
    if request.user.username != 'hcAdmin':
        raise PermissionDenied()

    estatus = RutasInterEstatus.objects.all()
    comentarios = RutasInterComentarios.objects.all()
    folios = RutasInterFolioGuio.objects.all()
    hora = timezone.now() - timedelta(minutes=30)
    contexto ={
        'estatus': estatus,
        'comentarios': comentarios,
        'folios': folios,
        'hora':hora
    }
    return render(request, "healtcheaks/reporteHcRutasInterBot.html", contexto )

@login_required
def healtcheaksAPN(request):
    if request.user.username != 'hcAdmin':
        raise PermissionDenied()

    data = HcAPN.objects.all()
    contexto ={
        'data': data,
    }
    return render(request, "healtcheaks/reporteHcAPNBot.html", contexto )

@login_required
def envioHealtcheaksInterAtt(request):
    if request.user.username != 'hcAdmin':
        raise PermissionDenied()

    get_hcInterATT()
    hora = timezone.now()
    contexto = {
        'hora': hora
    }
    return render(request, "healtcheaks/InterATT_confirm.html", contexto)

@login_required
def envioHealtcheaksAPN(request):
    if request.user.username != 'hcAdmin':
        raise PermissionDenied()
        
    get_hcAPN()
    hora = timezone.now()
    contexto = {
        'hora': hora
    }
    return render(request, "healtcheaks/InterATT_confirm.html", contexto)

@login_required
def envioHealtcheaksRutasInter(request):
    if request.user.username != 'hcAdmin':
        raise PermissionDenied()
        
    get_hcRutasInter()
    hora = timezone.now()
    contexto = {
        'hora': hora
    }
    return render(request, "healtcheaks/InterATT_confirm.html", contexto)
