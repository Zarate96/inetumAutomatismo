from django.shortcuts import render
from .models import   EstatusInterATT
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
    estatus = EstatusInterATT.objects.all()
    hora = timezone.now() - timedelta(minutes=30)
    contexto ={
        'estatus': estatus,
        'hora':hora
    }
    return render(request, "healtcheaks/reporteHcRutasInterBot.html", contexto )


def envioHealtcheaksInterAtt(request):
    get_hcInterATT()
    hora = timezone.now()
    contexto = {
        'hora': hora
    }
    return render(request, "healtcheaks/InterATT_confirm.html", contexto)

