from django.shortcuts import render
from .forms import CadastrarNovoUsuario, LogarBLZ
from .models import Usuario
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout

def home(request):
    return render(request, 'home.html')
    
def cadastro(request):
    return render(request, 'cadastro.html')

def cadastrarusuario(request):
    if request.method == "POST":
        form = CadastrarNovoUsuario(request.POST)

        if form.is_valid():
            dados = form.data
            
            novo_user = User.objects.create_user(dados['usuario'],dados['email'],dados['senha'])
            novo_usuario = Usuario(nome=dados['nome'], telefone=dados['telefone'], usuario_tipo=dados['usuario_tipo'], user=novo_user)
            novo_usuario.save()
            return HttpResponse('O cadastro foi feito !')
        else:
            return render(request, 'cadastro.html', {'form': form })

def loginpage(request):
    return render(request, 'loginpage.html')

def logarusuario(request):
    if request.method == "POST":
        form = LogarBLZ(request.POST)
        if form.is_valid():
            dados = form.data
            user = authenticate(username=dados['usuario'], password=dados['senha'])
            if user is not None:
                login(request, user)
                return HttpResponse('O novo usuario esta logado no sistema .')
            else:
                form.adiciona_erro(message='Usuario ou senha esta errado')
                return render(request, 'loginpage.html', {'form': form })
        else:
            return render(request, 'home.html')
