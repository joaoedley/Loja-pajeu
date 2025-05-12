from django.contrib import admin
from .models import Banner

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'tipo', 'ativo', 'data_criacao')
    list_filter = ('tipo', 'ativo')
    search_fields = ('titulo',)
    list_editable = ('ativo',)
    ordering = ('-data_criacao',)