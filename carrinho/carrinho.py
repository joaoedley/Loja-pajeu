from django.conf import settings
from produtos.models import Produto

class Carrinho:
    def __init__(self, request):
        self.session = request.session
        carrinho = self.session.get(settings.CARRINHO_SESSION_ID)
        if not carrinho:
            carrinho = self.session[settings.CARRINHO_SESSION_ID] = {}
        self.carrinho = carrinho
    
    def __iter__(self):
        produto_ids = self.carrinho.keys()
        produtos = Produto.objects.filter(id__in=produto_ids)
        
        carrinho = self.carrinho.copy()
        for produto in produtos:
            carrinho[str(produto.id)]['produto'] = produto
        
        for item in carrinho.values():
            item['preco'] = float(item['preco'])
            item['total'] = item['preco'] * item['quantidade']
            yield item
    
    def __len__(self):
        return sum(item['quantidade'] for item in self.carrinho.values())
    
    def adicionar(self, produto, quantidade=1, sobrepor_quantidade=False):
        produto_id = str(produto.id)
        
        if produto_id not in self.carrinho:
            self.carrinho[produto_id] = {
                'quantidade': 0,
                'preco': str(produto.preco)
            }
        
        if sobrepor_quantidade:
            self.carrinho[produto_id]['quantidade'] = quantidade
        else:
            self.carrinho[produto_id]['quantidade'] += quantidade
        
        self.salvar()
    
    def salvar(self):
        self.session.modified = True
    
    def remover(self, produto):
        produto_id = str(produto.id)
        if produto_id in self.carrinho:
            del self.carrinho[produto_id]
            self.salvar()
    
    def limpar(self):
        del self.session[settings.CARRINHO_SESSION_ID]
        self.salvar()
    
    def get_total(self):
        return sum(float(item['preco']) * item['quantidade'] for item in self.carrinho.values())