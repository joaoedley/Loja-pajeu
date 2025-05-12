from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.conf import settings
from .models import Pedido, ItemPedido
from .forms import PedidoForm
from carrinho.carrinho import Carrinho
from django.http import HttpResponse
from django.template.loader import render_to_string

@login_required
def criar_pedido(request):
    carrinho = Carrinho(request)
    if request.method == 'POST':
        form = PedidoForm(request.POST)
        if form.is_valid():
            pedido = form.save(commit=False)
            pedido.user = request.user
            pedido.total = carrinho.get_total()
            pedido.tipo_entrega = form.cleaned_data['tipo_entrega']
            
            # Se for retirada na loja, não precisa de endereço
            if pedido.tipo_entrega == 'retirada':
                pedido.endereco = 'Retirada na Loja'
                pedido.complemento = ''
                pedido.cep = ''
                pedido.cidade = 'Afogados da Ingazeira'
                pedido.estado = 'PE'
            
            pedido.save()
            
            for item in carrinho:
                ItemPedido.objects.create(
                    pedido=pedido,
                    produto=item['produto'],
                    preco=item['preco'],
                    quantidade=item['quantidade']
                )
            
            carrinho.limpar()
            return redirect('pedidos:sucesso')
    else:
        form = PedidoForm()
    
    return render(request, 'pedidos/criar.html', {
        'form': form,
        'carrinho': carrinho
    })

@login_required
def pedido_detalhe(request, pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id)
    if pedido.user != request.user and not request.user.is_staff:
        return redirect('core:inicio')
    return render(request, 'pedidos/detalhe.html', {'pedido': pedido})

@user_passes_test(lambda u: u.is_staff)
def admin_pedido_detalhe(request, pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id)
    return render(request, 'pedidos/admin/detalhe.html', {'pedido': pedido})

@login_required
def pedido_historico(request):
    pedidos = Pedido.objects.filter(user=request.user).order_by('-criado_em')
    return render(request, 'pedidos/historico.html', {'pedidos': pedidos})

@login_required
def pedido_pdf(request, pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id)
    if pedido.user != request.user and not request.user.is_staff:
        return redirect('core:inicio')
    
    html = render_to_string('pedidos/pdf.html', {'pedido': pedido})

    return HttpResponse(html)

def pedido_sucesso(request):
    return render(request, 'pedidos/sucesso.html')