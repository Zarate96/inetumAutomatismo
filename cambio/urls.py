from . import views
from django.urls import path


app_name= 'cambio'

urlpatterns = [
	#Calendarios
	path('calendario/', views.calendario, name="calendario"),

]