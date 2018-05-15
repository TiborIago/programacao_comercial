from django.shortcuts import render, redirect
from Home.forms import LogarBLZ
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from dashboard.forms import AlterarSenha
from dashboard.models import Pedidos, Servico


@login_required
def get_perfil_logado(request):
    return request.user.usuario

@login_required
def dash_relatorios(request):
    return render(request, 'dash_relatorio.html')

@login_required
def dash_userdata_changepassword(request):
    return render(request, 'dash_userdata_changepassword.html')

@login_required
def dash_userdata_changedata(request):
    data = get_perfil_logado(request)
    return render(request, 'dash_userdata_changedata.html',  {'nome':data.nome, 'telefone':data.telefone, 'username':data.user.username, 'email':data.user.email})

@login_required
def logoutUser(request):
    logout(request)
    return redirect('home')

@login_required
def dash_home(request):
    if request.user.is_authenticated:
        return render(request, 'dash_home.html', )

@login_required
def dash_calendario(request):
    return render(request, 'dash_calendario.html')

@login_required
def dash_pedidos(request):
    user = get_perfil_logado(request)
    data = Pedidos.objects.filter(Usuario_id = user.id)
    print(data[0].cliente.endereco)
    
    return render(request, 'dash_pedidos.html', {'data':data})

@login_required
def dash_servicos(request):
    user = get_perfil_logado(request)
    data = Servico.objects.filter(usuario_id = user.id)
    print(data.values() )
    return render(request, 'dash_servicos.html', {'data':data})


@login_required
def alterar_senha(request):
    if request.method == "POST":
        form = AlterarSenha(request.POST)
        if form.is_valid():
            dados = form.data
            if dados['senha'] == dados['senha_confirma'] and len(dados['senha']) >= 8: 
                usuario = get_perfil_logado(request)
                usuario.user.set_password(dados['senha'])
                usuario.user.save()
                logoutUser(request)
                return redirect('loginpage')
            else:
                form.adiciona_erro(message='As senhas devem estar iguais e ter mais de 8 caracteres !')
                return render(request, 'dash_userdata_changepassword.html', {'form': form })
        else:
            form.adiciona_erro(message='Algum erro ocoreu, tente novamente !')
            return render(request, 'dash_userdata_changepassword.html', {'form': form })



def logarusuario(request):
    
    if request.method == "POST":
        form = LogarBLZ(request.POST)
        if form.is_valid():
            dados = form.data
            
            user = authenticate(username=dados['usuario'], password=dados['senha'])
            
            if user is not None:
                login(request, user)
                return redirect('dash_home')
            else:
                form.adiciona_erro(message='Usuario ou senha esta errado')
                return render(request, 'loginpage.html', {'form': form })
        else:
            return render(request, 'home.html')
    
    if request.user.is_authenticated:
        return redirect('dash_home')
    else:
        return redirect('home')

