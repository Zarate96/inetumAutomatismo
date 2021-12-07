from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

#crea tus urls de la app

app_name= 'core'
urlpatterns = [
	path('', views.home, name="home"),
	path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='core/logout.html'), name='logout'),
]