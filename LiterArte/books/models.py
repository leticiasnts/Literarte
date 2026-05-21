from django.db import models

# Create your models here.

class Genero(models.Model):
    nome = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.nome
    
    
class Autor(models.Model):
    nome = models.CharField(max_length=100)
    biografia = models.TextField(blank=True, null=True)
    data_nascimento = models.DateField(blank=True, null=True)
    data_falecimento = models.DateField(blank=True, null=True)
    foto = models.ImageField(upload_to='autores/', blank=True, null=True)
    
    def __str__(self):
        return self.nome
    
    
class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name='livros')
    generos =models.ManyToManyField(Genero, related_name='livros')
    
    ano_publicacao = models.IntegerField()
    editora = models.CharField(max_length=100, blank=True, null=True)
    paginas = models.IntegerField()

    sinopse = models.TextField()
    capa = models.ImageField(upload_to='capas_livros/', blank=True, null=True)
    data_cadastro = models.DateTimeField(auto_now_add=True) 
    
    def __str__(self):
        return self.titulo