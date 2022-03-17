from . import views
from django.urls import path


app_name= 'cambio'

urlpatterns = [
	#Calendarios
	path('calendario/', views.calendario, name="calendario"),
	path('reporte/planificadas', views.reportePlanificadas, name='reporte-planificadas'),

]