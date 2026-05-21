from django.contrib import admin
from django.contrib import admin
from .models import Livro, Autor, Genero

@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'data_nascimento', 'data_falecimento')
    search_fields = ('nome',)

@admin.register(Genero)
class GeneroAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)

@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'ano_publicacao', 'paginas')
    list_filter = ('autor', 'generos')
    search_fields = ('titulo', 'autor__nome')