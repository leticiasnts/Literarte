from django.db import models
from django.contrib.auth.models import User
from books.models import Livro
# Create your models here.

class ListaLeitura(models.Model):
    STATUS_CHOICES = [
        ('QUERO_LER', 'Quero Ler'),
        ('LENDO', 'Lendo'),
        ('LIDO', 'Lido'),
    ]
    
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='minha_lista')
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE, related_name='leitores')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='QUERO_LER')
    nota = models.IntegerField(blank=True, null=True)
    favorito = models.BooleanField(default=False)
    data_atualizacao = models.DateTimeField(auto_now=True)
    
    
    class Meta:
        unique_together = ('usuario', 'livro')
        verbose_name = "Item da Lista"
        verbose_name_plural = "Itens da Lista"
        
    def __str__(self):
            return f"{self.usuario.username} - {self.livro.titulo} ({self.get_status_display()})"
        
        
    