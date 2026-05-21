from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import CadastroForm, PerfilForm
from .models import Perfil
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def cadastro(request):
    if request.method == 'POST':
        form = CadastroForm(request.POST)
        
        if form.is_valid():
            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            senha = form.cleaned_data['senha']
            
            novo_usuario = User.objects.create_user(username=email, email=email, password=senha)
            novo_usuario.first_name = nome
            novo_usuario.save()
            
            Perfil.objects.create(usuario=novo_usuario)
            
            messages.success(request, 'Cadastro realizado com sucesso! Faça login.')
            return redirect('login')
        
    else:
        form = CadastroForm()
        
    return render(request, 'cadastro.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            messages.success(request, f'Bem-vindo(a), {user.first_name}!')
            return redirect('index')
        else:
            messages.error(request, 'Usuário ou senha inválidos.')
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})

def logout_view(request):
    auth_logout(request)
    messages.info(request, 'Você saiu da conta.')
    return redirect('login')



@login_required
def meu_perfil(request):
    return render(request, 'meu-perfil.html')


@login_required
def editar_perfil(request):
    perfil = request.user.perfil
    
    if request.method == 'POST':
        form = PerfilForm(request.POST, request.FILES, instance=perfil)
        novo_nome = request.POST.get('nome') 
        if form.is_valid():
            form.save()
            user = request.user
            user.first_name = novo_nome
            user.save()
            
            
            return redirect('meu_perfil')
            
    else:
        form = PerfilForm(instance=perfil)

    return render(request, 'editar-perfil.html', {'form': form})