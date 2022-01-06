from . import views
from django.urls import path
app_name= 'healtcheaks'

urlpatterns = [
    #Vistas para los HC
    path('interconfiguracionATT/', views.healtcheaksInterAtt, name="healtcheaksInterAtt"),
    path('interconfiguracionATT/enviar', views.envioHealtcheaksInterAtt, name="envioHealtcheaksInterAtt"),
]

