from django.db import models
from produtos.models import Produto

class Carrinho(models.Model):
    session_key = models.CharField(max_length=40, db_index=True)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(default=1)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    
    class Meta:
        unique_together = ('session_key', 'produto')
    
    def __str__(self):
        return f'{self.quantidade}x {self.produto.nome}'
    
    def get_total(self):
        return self.quantidade * self.produto.preco