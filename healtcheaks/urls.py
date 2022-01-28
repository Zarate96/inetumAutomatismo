from . import views
from django.urls import path
app_name= 'healtcheaks'

urlpatterns = [
    #Vistas para los HC
    path('interconfiguracionATT/', views.healtcheaksInterAtt, name="healtcheaksInterAtt"),
    path('rutasInterconexion/', views.healtcheaksRutasInter, name="healtcheaksRutasInter"),
    path('APN/', views.healtcheaksAPN, name="healtcheaksAPN"),
    path('interconfiguracionATT/enviar', views.envioHealtcheaksInterAtt, name="envioHealtcheaksInterAtt"),
    path('APN/enviar', views.envioHealtcheaksAPN, name="envioHealtcheaksAPN"),
    path('rutasInterconexion/enviar', views.envioHealtcheaksRutasInter, name="envioHealtcheaksRutasInter"),
]

