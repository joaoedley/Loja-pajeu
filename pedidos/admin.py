from django.contrib import admin
from .models import Pedido, ItemPedido

class ItemPedidoInline(admin.TabularInline):
    model = ItemPedido
    raw_id_fields = ['produto']
    extra = 0
    fields = ['produto', 'preco', 'quantidade', 'get_custo_total']
    readonly_fields = ['get_custo_total']

    def get_custo_total(self, obj):
        if obj.preco is not None:
            return f'R$ {obj.get_custo()}'
        return 'R$ 0,00'
    get_custo_total.short_description = 'Custo Total'

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ['id', 'primeiro_nome', 'sobrenome', 'email', 'status', 'tipo_entrega', 'criado_em', 'get_total']
    list_filter = ['status', 'tipo_entrega', 'criado_em', 'pago']
    search_fields = ['primeiro_nome', 'sobrenome', 'email', 'id']
    readonly_fields = ['criado_em', 'atualizado_em']
    inlines = [ItemPedidoInline]
    fieldsets = (
        ('Informações do Cliente', {
            'fields': ('user', 'primeiro_nome', 'sobrenome', 'email', 'telefone')
        }),
        ('Endereço de Entrega', {
            'fields': ('endereco', 'complemento', 'cep', 'cidade', 'estado')
        }),
        ('Informações do Pedido', {
            'fields': ('status', 'tipo_entrega', 'metodo_pagamento', 'pago')
        }),
        ('Datas', {
            'fields': ('criado_em', 'atualizado_em'),
            'classes': ('collapse',)
        }),
    )

    def get_total(self, obj):
        return f'R$ {obj.get_total()}'
    get_total.short_description = 'Total'
