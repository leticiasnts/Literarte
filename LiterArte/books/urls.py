from django.urls import path
from . import views

urlpatterns = [
    path('livro/<int:livro_id>/', views.detalhe_livros, name='detalhe_livro')
]