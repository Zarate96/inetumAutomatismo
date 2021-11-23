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
    context = {
        'proyectos' : proyectos,
        'filter': filter,
        'page_obj': page_obj,
    }
    return render(request, 'problema/reporte.html',context)

def export_report(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="users.csv"'
    writer = csv.writer(response)
    writer.writerow(['Username', 'First name', 'Last name', 'Email address'])

# class reporteRecurrencia(ListView):
#     model = Gestion
#     template_name = "problema/reporte.html"
#     context_object_name = "proyectos"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['myFilter'] = GestionFilter() 
#         return context
    
    #paginate_by = 20

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

