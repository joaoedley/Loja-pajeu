from django.db import models
from django.urls import reverse

class Categoria(models.Model):
    nome = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, unique=True)
    
    class Meta:
        ordering = ('nome',)
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'
    
    def __str__(self):
        return self.nome
    
    def get_absolute_url(self):
        return reverse('produtos:lista_produtos_por_categoria', args=[self.slug])

class Produto(models.Model):
    DESTAQUE_CHOICES = [
        ('N', 'Normal'),
        ('D', 'Destaque'),
        ('L', 'Lançamento'),
    ]
    
    categoria = models.ForeignKey(Categoria, related_name='produtos', on_delete=models.CASCADE)
    nome = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, db_index=True)
    imagem = models.ImageField(upload_to='produtos/', blank=True)
    descricao = models.CharField(max_length=255, blank=True)
    descricao_completa = models.TextField('Descrição Completa', blank=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    disponivel = models.BooleanField(default=True)
    destaque = models.CharField(max_length=1, choices=DESTAQUE_CHOICES, default='N')
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ('nome',)
        indexes = [
            models.Index(fields=['id', 'slug']),
        ]
        verbose_name = 'produto'
        verbose_name_plural = 'produtos'
    
    def __str__(self):
        return self.nome
    
    def get_absolute_url(self):
        return reverse('produtos:detalhe_produto', args=[self.id, self.slug])

class Avaliacao(models.Model):
    produto = models.ForeignKey(Produto, related_name='avaliacoes', on_delete=models.CASCADE)
    nome = models.CharField(max_length=80)
    email = models.EmailField()
    comentario = models.TextField()
    nota = models.PositiveIntegerField(choices=[(i, i) for i in range(1, 6)])
    criado_em = models.DateTimeField(auto_now_add=True)
    ativo = models.BooleanField(default=False)  # Mudado para False para moderação
    
    class Meta:
        ordering = ('-criado_em',)
        verbose_name = 'avaliação'
        verbose_name_plural = 'avaliações'
    
    def __str__(self):
        return f'Avaliação de {self.nome} para {self.produto.nome}'