from django.db import models
from django.contrib.auth import get_user_model
from produtos.models import Produto

User = get_user_model()

class Pedido(models.Model):
    STATUS_CHOICES = [
        ('pendente', 'Pendente'),
        ('pago', 'Pago'),
        ('enviado', 'Enviado'),
        ('entregue', 'Entregue'),
        ('cancelado', 'Cancelado'),
    ]
    
    METODO_PAGAMENTO_CHOICES = [
        ('pix', 'PIX'),
        ('cartao', 'Cartão de Crédito'),
        ('boleto', 'Boleto'),
    ]

    TIPO_ENTREGA_CHOICES = [
        ('retirada', 'Retirar na Loja'),
        ('envio', 'Envio para Endereço'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    primeiro_nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50)
    email = models.EmailField()
    endereco = models.CharField(max_length=250)
    complemento = models.CharField(max_length=100, blank=True)
    cep = models.CharField(max_length=10)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=2)
    telefone = models.CharField(max_length=20)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    pago = models.BooleanField(default=False)
    metodo_pagamento = models.CharField(max_length=10, choices=METODO_PAGAMENTO_CHOICES, default='pix')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pendente')
    tipo_entrega = models.CharField(max_length=10, choices=TIPO_ENTREGA_CHOICES, default='envio')
    
    class Meta:
        ordering = ('-criado_em',)
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'
    
    def __str__(self):
        return f'Pedido {self.id} - {self.primeiro_nome} {self.sobrenome}'
    
    def get_total(self):
        return sum(item.get_custo() for item in self.itens.all())

class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, related_name='itens', on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, related_name='itens_pedido', on_delete=models.CASCADE)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade = models.PositiveIntegerField(default=1)
    
    def __str__(self):
        return str(self.id)
    
    def get_custo(self):
        return self.preco * self.quantidade