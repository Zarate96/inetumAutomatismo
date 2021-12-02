from django.urls import path
from . import views

app_name= 'problema'

urlpatterns = [
	path('gp/', views.gestionProyectos.as_view(), name="proyectos"),
	path('gp/agregar/', views.crearProyectos.as_view(), name="agregar-proyecto"),
	path('gp/detalle/<int:pk>/', views.proyectoDetalle.as_view(), name="detalle-proyecto"),
	path('gp/reporte/recurrencia', views.reporteRecurrencia, name="reporte-recurrencia"),
	path('gp/reporte/bases', views.reporteBase, name="reporte-base"),
	path('gp/reporte/exportar', views.exportProyectos, name="exportar-proyectos"),
	path('hc/interconfiguracionatt', views.reportesHc, name="hc-interconfiguracion-att"),
]