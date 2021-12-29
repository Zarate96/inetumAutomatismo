from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

app_name= 'problema'

urlpatterns = [
	path('gp/', login_required(views.gestionProyectos.as_view()), name="proyectos"),
	path('gp/agregar/', views.crearProyectos.as_view(), name="agregar-proyecto"),
	path('gp/detalle/<int:pk>/', views.proyectoDetalle.as_view(), name="detalle-proyecto"),
	path('gp/reporte/recurrencia', views.reporteRecurrencia, name="reporte-recurrencia"),
	path('gp/reporte/bases', views.reporteBase, name="reporte-base"),
	path('gp/reporte/exportar', views.exportProyectos, name="exportar-proyectos"),
	path('hc/ri', views.reportesHcRI, name="hc-ri"),
	path('hc/apn', views.reportesHcAPN, name="hc-apn"),
	path('hc/ia', views.reportesHcIA, name="hc-ia"),
	path('ni/', views.IncidenciaMasiva.as_view(), name="ni"),
	path('ni/bot', views.IncidenciaMasivaBot.as_view(), name="ni-bot"),
	path('hc/ia/bot', views.reportesHcIABot, name="hc-ia-bot"),
	path('hc/apn/bot', views.reportesHcAPNBot, name="hc-apn-bot"),
]
