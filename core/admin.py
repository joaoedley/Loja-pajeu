from django.contrib import admin
from .models import Contato, SiteConfig, SobreSite

@admin.register(SobreSite)
class SobreSiteAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'atualizado_em']
    search_fields = ['titulo', 'texto']
    readonly_fields = ['atualizado_em']

@admin.register(SiteConfig)
class SiteConfigAdmin(admin.ModelAdmin):
    list_display = ['logo', 'atualizado_em']
    def has_add_permission(self, request):
        # Permite apenas um registro de configuração
        return not SiteConfig.objects.exists()

@admin.register(Contato)
class ContatoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'email', 'assunto', 'criado_em', 'user']
    search_fields = ['nome', 'email', 'assunto', 'mensagem']
    list_filter = ['criado_em']
    readonly_fields = ['nome', 'email', 'assunto', 'mensagem', 'user', 'criado_em']
