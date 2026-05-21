from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil')
    livro_favorito = models.CharField(max_length=200, blank=True, null=True)
    generos_favoritos = models.CharField(max_length=200, blank=True, null=True)
    autores_favoritos = models.CharField(max_length=200, blank=True, null=True)
    
    def __str__(self):
        return f"Perfil de {self.usuario.username}"
    
    