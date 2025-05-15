from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class SiteConfig(models.Model):
    logo = models.ImageField(upload_to='logo/', verbose_name='Logo do Site')
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Configuração do Site'
        verbose_name_plural = 'Configurações do Site'

    def __str__(self):
        return 'Configuração do Site'

class Contato(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Usuário')
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    assunto = models.CharField(max_length=150)
    mensagem = models.TextField()
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Mensagem de Contato'
        verbose_name_plural = 'Mensagens de Contato'
        ordering = ['-criado_em']

    def __str__(self):
        return f'{self.nome} - {self.assunto} ({self.criado_em:%d/%m/%Y %H:%M})'

class SobreSite(models.Model):
    titulo = models.CharField('Título', max_length=200, default='Sobre Nós')
    texto = models.TextField('Texto', blank=True)
    imagem = models.ImageField('Imagem da Loja', upload_to='sobre/', blank=True, null=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Sobre o Site'
        verbose_name_plural = 'Sobre o Site'

    def __str__(self):
        return self.titulo
