from django.shortcuts import render
from .models import   EstatusInterATT,RutasInterEstatus,RutasInterComentarios,RutasInterFolioGuio
from django.utils import timezone
from datetime import timedelta
from task.selenium import get_hcInterATT

# Create your views here.
def healtcheaksInterAtt(request):
    estatus = EstatusInterATT.objects.all()
    hora = timezone.now() - timedelta(minutes=30)
    contexto ={
        'estatus': estatus,
        'hora':hora
    }
    return render(request, "healtcheaks/reporteHcInterBot.html", contexto )

def healtcheaksRutasInter(request):
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

def healtcheaksAPN(request):
    estatus = RutasInterEstatus.objects.all()
    contexto ={
        'estatus': estatus,
    }
    return render(request, "healtcheaks/reporteHcAPNBot.html", contexto )


def envioHealtcheaksInterAtt(request):
    get_hcInterATT()
    hora = timezone.now()
    contexto = {
        'hora': hora
    }
    return render(request, "healtcheaks/InterATT_confirm.html", contexto)

