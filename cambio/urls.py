from . import views
from django.urls import path
from .views import OtDetailView

app_name= 'cambio'

urlpatterns = [
	#Calendarios
	path('calendario/', views.calendario, name="calendario"),
	path('calendario/ot/<int:pk>/detail', OtDetailView.as_view(), name="ot_detail"),
	path('reporte/planificadas', views.reportePlanificadas, name='reporte-planificadas'),
	path('reporte/noplanificadas', views.reporteNoPlanificadas, name='reporte-no-planificadas'),
]