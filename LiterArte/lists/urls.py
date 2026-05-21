from django.urls import path
from . import views

urlpatterns = [
    path('adicionar/<int:livro_id>/', views.adicionar_na_lista, name='adicionar_na_lista'),
    path('meus-livros/', views.pagina_minha_lista, name='minha_lista'),
    path('atualizar-status/<int:item_id>/', views.atualizar_status, name='atualizar_status'),
    path('remover/<int:item_id>/', views.remover_da_lista, name='remover_da_lista'),
]