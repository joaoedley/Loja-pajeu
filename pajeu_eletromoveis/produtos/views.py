from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Categoria, Produto, Avaliacao
from .forms import AvaliacaoForm, BuscaForm
from carrinho.carrinho import Carrinho
from django.contrib import messages

def lista_produtos(request, categoria_slug=None):
    categoria = None
    categorias = Categoria.objects.all()
    produtos = Produto.objects.filter(disponivel=True)
    
    if categoria_slug:
        categoria = get_object_or_404(Categoria, slug=categoria_slug)
        produtos = produtos.filter(categoria=categoria)
    
    paginator = Paginator(produtos, 12)
    page = request.GET.get('page')
    
    try:
        produtos = paginator.page(page)
    except PageNotAnInteger:
        produtos = paginator.page(1)
    except EmptyPage:
        produtos = paginator.page(paginator.num_pages)
    
    return render(request, 'produtos/lista.html', {
        'categoria': categoria,
        'categorias': categorias,
        'produtos': produtos,
    })

def detalhe_produto(request, id, slug):
    produto = get_object_or_404(Produto, id=id, slug=slug, disponivel=True)
    avaliacoes = produto.avaliacoes.filter(ativo=True)
    carrinho = Carrinho(request)
    
    if request.method == 'POST':
        form_avaliacao = AvaliacaoForm(data=request.POST)
        if form_avaliacao.is_valid():
            nova_avaliacao = form_avaliacao.save(commit=False)
            nova_avaliacao.produto = produto
            nova_avaliacao.ativo = True  # Agora a avaliação já nasce ativa
            nova_avaliacao.save()
            return redirect(produto.get_absolute_url())
    else:
        form_avaliacao = AvaliacaoForm()
    
    produtos_relacionados = Produto.objects.filter(
        categoria=produto.categoria,
        disponivel=True
    ).exclude(id=produto.id)[:4]
    
    return render(request, 'produtos/detalhe.html', {
        'produto': produto,
        'avaliacoes': avaliacoes,
        'form_avaliacao': form_avaliacao,
        'produtos_relacionados': produtos_relacionados,
        'carrinho': carrinho,
    })

def busca_produtos(request):
    form = BuscaForm(request.GET)
    produtos = Produto.objects.filter(disponivel=True)
    
    if form.is_valid():
        q = form.cleaned_data['q']
        produtos = produtos.filter(nome__icontains=q)
    
    return render(request, 'produtos/busca.html', {
        'form': form,
        'produtos': produtos,
        'query': q if form.is_valid() else None,
    })

def produtos_destaque(request):
    produtos = Produto.objects.filter(destaque='D', disponivel=True)
    return render(request, 'produtos/destaque.html', {'produtos': produtos})

def produtos_lancamento(request):
    produtos = Produto.objects.filter(destaque='L', disponivel=True)
    return render(request, 'produtos/lancamento.html', {'produtos': produtos})


def adicionar_avaliacao(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    
    if request.method == 'POST':
        form = AvaliacaoForm(request.POST)
        if form.is_valid():
            avaliacao = form.save(commit=False)
            avaliacao.produto = produto
            
            # Se o usuário estiver autenticado, use suas informações
            if request.user.is_authenticated:
                avaliacao.nome = request.user.get_full_name() or request.user.username
                avaliacao.email = request.user.email
            
            avaliacao.save()
            messages.success(request, 'Avaliação enviada com sucesso!')
            return redirect('produtos:detalhe_produto', id=produto.id, slug=produto.slug)
    else:
        form = AvaliacaoForm()
    
    return render(request, 'produtos/adicionar_avaliacao.html', {
        'produto': produto,
        'form': form,
    })
