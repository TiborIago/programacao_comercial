from django.urls import path
from . import views


urlpatterns = [
    path('', views.logarusuario, name='dash_login'),
    path('calendario/', views.dash_calendario, name='dash_calendario'),
    path('pedidos/', views.dash_pedidos, name='dash_pedidos'),
    path('home/', views.dash_home, name='dash_home'),
    path('relatorios/', views.dash_relatorios, name='dash_relatorios'),
    path('servicos/', views.dash_servicos, name='dash_servicos'),
    path('logout/', views.logoutUser, name='logout_user'),
    path('user/atualizardados/', views.dash_userdata_changedata, name='user_changedata'),
    path('user/atualizarsenha/', views.dash_userdata_changepassword, name='user_changepassword'),
    path('user/atualizarnovasenha/', views.alterar_senha, name='user_changenewpassword')

]