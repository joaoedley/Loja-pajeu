from django.shortcuts import render, redirect, get_object_or_404
from produtos.models import Produto
from .carrinho import Carrinho
from .forms import AdicionarProdutoCarrinhoForm
from django.contrib import messages

def detalhe_carrinho(request):
    carrinho = Carrinho(request)
    for item in carrinho:
        item['form_quantidade'] = AdicionarProdutoCarrinhoForm(
            initial={'quantidade': item['quantidade'], 'sobrepor': True}
        )
    return render(request, 'carrinho/detalhe.html', {'carrinho': carrinho})

def adicionar_carrinho(request, produto_id):
    carrinho = Carrinho(request)
    produto = get_object_or_404(Produto, id=produto_id)
    form = AdicionarProdutoCarrinhoForm(request.POST)
    
    if form.is_valid():
        cd = form.cleaned_data
        carrinho.adicionar(
            produto=produto,
            quantidade=cd['quantidade'],
            sobrepor_quantidade=cd['sobrepor']
        )
    
    return redirect('carrinho:detalhe_carrinho')

def remover_carrinho(request, produto_id):
    carrinho = Carrinho(request)
    produto = get_object_or_404(Produto, id=produto_id)
    carrinho.remover(produto)
    return redirect('carrinho:detalhe_carrinho')

def limpar_carrinho(request):
    carrinho = Carrinho(request)
    carrinho.limpar()
    return redirect('carrinho:detalhe_carrinho')


def atualizar_carrinho(request, produto_id):
    carrinho = Carrinho(request)
    produto = get_object_or_404(Produto, id=produto_id)
    form = AdicionarProdutoCarrinhoForm(request.POST)
    
    if form.is_valid():
        cd = form.cleaned_data
        carrinho.adicionar(
            produto=produto,
            quantidade=cd['quantidade'],
            sobrepor_quantidade=cd['sobrepor']
        )
        messages.success(request, f"Quantidade de {produto.nome} atualizada no carrinho!")
    
    return redirect('carrinho:detalhe_carrinho')