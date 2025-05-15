from django.contrib import admin
from .models import Categoria, Produto, Avaliacao

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'slug')
    prepopulated_fields = {'slug': ('nome',)}
    search_fields = ['nome']

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'categoria', 'preco', 'disponivel', 'destaque', 'criado_em')
    list_filter = ('categoria', 'disponivel', 'destaque')
    list_editable = ('preco', 'disponivel', 'destaque')
    search_fields = ('nome', 'descricao', 'descricao_completa')
    prepopulated_fields = {'slug': ('nome',)}
    ordering = ('-criado_em',)
    fieldsets = (
        (None, {
            'fields': ('nome', 'slug', 'categoria', 'imagem', 'preco', 'disponivel')
        }),
        ('Descrição', {
            'fields': ('descricao', 'descricao_completa')
        }),
    )

@admin.register(Avaliacao)
class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = ('produto', 'nome', 'nota', 'ativo', 'criado_em')
    list_filter = ('ativo', 'nota')
    search_fields = ('produto__nome', 'nome', 'email')
    list_editable = ('ativo',)
    ordering = ('-criado_em',)
    actions = ['aprovar_avaliacoes']

    def aprovar_avaliacoes(self, request, queryset):
        queryset.update(ativo=True)
    aprovar_avaliacoes.short_description = 'Aprovar avaliações selecionadas'