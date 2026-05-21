from django.urls import path
from . import views

urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('meu-perfil/', views.meu_perfil, name='meu_perfil'),
    path('editar-perfil', views.editar_perfil, name='editar_perfil'),
]