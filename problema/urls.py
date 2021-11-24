from django.urls import path
from . import views

app_name= 'problema'

urlpatterns = [
	path('', views.gestionProyectos.as_view(), name="proyectos"),
	path('agregar/', views.crearProyectos.as_view(), name="agregar-proyecto"),
	path('detalle/<int:pk>/', views.proyectoDetalle.as_view(), name="detalle-proyecto"),
	path('reporte/recurrencia', views.reporteRecurrencia, name="reporte-recurrencia"),
	path('reporte/exportar', views.exportProyectos, name="exportar-proyectos"),
]