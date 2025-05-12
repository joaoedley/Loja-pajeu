from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from produtos.models import Produto
from django.contrib.auth.decorators import login_required
from pedidos.models import Pedido
from banners.models import Banner
from .models import Contato

def inicio(request):
    """View para a página inicial"""
    produtos_destaque = Produto.objects.filter(destaque='D', disponivel=True)[:4]
    produtos_lancamento = Produto.objects.filter(destaque='L', disponivel=True)[:4]
    banners_desktop = Banner.objects.filter(ativo=True, tipo='desktop')
    banners_mobile = Banner.objects.filter(ativo=True, tipo='mobile')

    context = {
        'produtos_destaque': produtos_destaque,
        'produtos_lancamento': produtos_lancamento,
        'banners_desktop': banners_desktop,
        'banners_mobile': banners_mobile,
    }
    return render(request, 'core/inicio.html', context)

def todos_produtos(request):
    """View para listar todos os produtos"""
    produtos = Produto.objects.filter(disponivel=True).order_by('-criado_em')
    return render(request, 'produtos/lista.html', {'produtos': produtos})

def contato(request):
    """View para a página de contato"""
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        assunto = request.POST.get('assunto')
        mensagem = request.POST.get('mensagem')
        user = request.user if request.user.is_authenticated else None
        Contato.objects.create(
            user=user,
            nome=nome,
            email=email,
            assunto=assunto,
            mensagem=mensagem
        )
        messages.success(request, 'Sua mensagem foi enviada com sucesso!')
        return redirect('core:contato')
    return render(request, 'core/contato.html')

def login_view(request):
    """View para login de usuários"""
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Bem-vindo(a), {username}!')
                return redirect('core:inicio')
        messages.error(request, 'Usuário ou senha inválidos.')
    else:
        form = AuthenticationForm()
    
    return render(request, 'core/login.html', {'form': form})

def registro(request):
    """View para registro de novos usuários"""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registro realizado com sucesso!')
            return redirect('core:inicio')
    else:
        form = UserCreationForm()
    
    return render(request, 'core/registro.html', {'form': form})

def logout_view(request):
    """View para logout de usuários"""
    logout(request)
    messages.info(request, 'Você saiu da sua conta.')
    return redirect('core:inicio')

def perfil(request):
    """View para exibir e editar perfil do usuário"""
    if not request.user.is_authenticated:
        messages.warning(request, 'Por favor, faça login para acessar seu perfil.')
        return redirect('core:login')

    if request.method == 'POST':
        first_name = request.POST.get('first_name', '').strip()
        last_name = request.POST.get('last_name', '').strip()
        email = request.POST.get('email', '').strip()
        user = request.user
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.save()
        messages.success(request, 'Perfil atualizado com sucesso!')
        return redirect('core:perfil')

    return render(request, 'core/perfil.html')

@login_required
def meus_pedidos(request):
    """View para listar os pedidos do usuário"""
    pedidos = Pedido.objects.filter(user=request.user).order_by('-criado_em')
    return render(request, 'core/meus_pedidos.html', {'pedidos': pedidos})