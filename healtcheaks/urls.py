from . import views
from django.urls import path
app_name= 'healtcheaks'

urlpatterns = [
    #Vistas para los HC
    path('interconfiguracionATT/', views.healtcheaksInterAtt, name="healtcheaksInterAtt"),
    path('rutasInterconexion/', views.healtcheaksRutasInter, name="healtcheaksRutasInter"),
    path('interconfiguracionATT/enviar', views.envioHealtcheaksInterAtt, name="envioHealtcheaksInterAtt"),
]

