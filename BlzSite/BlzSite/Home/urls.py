from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('cadastrar/', views.cadastrarusuario, name='cadastrar'),
    path('login/', views.loginpage, name='loginpage'),
    path('logar/',views.logarusuario, name='logar')
]