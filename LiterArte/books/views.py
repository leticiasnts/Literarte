from django.shortcuts import render, get_object_or_404
from .models import Livro

# Create your views here.

def detalhe_livros(request, livro_id):
    livro = get_object_or_404(Livro, pk=livro_id)
    
    return render(request, 'livros.html', {'livro':livro})


