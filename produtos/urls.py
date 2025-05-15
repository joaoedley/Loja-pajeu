from django.urls import path
from . import views

app_name = 'produtos'

urlpatterns = [
    path('', views.lista_produtos, name='lista'),
    path('busca/', views.busca_produtos, name='busca'),
    path('<slug:categoria_slug>/', views.lista_produtos, name='lista_produtos_por_categoria'),
    path('<int:id>/<slug:slug>/', views.detalhe_produto, name='detalhe_produto'),
    path('destaques/', views.produtos_destaque, name='destaque'),
    path('lancamentos/', views.produtos_lancamento, name='lancamento'),
    path('avaliacao/<int:produto_id>/', views.adicionar_avaliacao, name='adicionar_avaliacao'),
]