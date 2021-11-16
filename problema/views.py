from django.shortcuts import render, HttpResponse, get_object_or_404
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from django.views.generic import ListView, DetailView
from django.views import View

from .forms import GestionForm
from .models import Gestion

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

class reporteRecurrencia(ListView):
    model = Gestion
    template_name = "problema/reporte.html"
    context_object_name = "proyectos"
    paginate_by = 20

# class gestionProyectos(View):

#     def get(self, request):
#         form = GestionForm()
#         return render(request, "problema/problema_create.html")
    
#     def post(self, request):
#         form = GestionForm(request.POST)
    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         return context

# def problema(request):
#     gestion_form = GestionForm
#     if request.method == "POST":
#        gestion_form  = gestion_form(data=request.POST)
#        if gestion_form.is_valid():
#           pass
#     context = {
#         'form':gestion_form,
#     }
#     return render(request, "problema/problema_create.html", context)

