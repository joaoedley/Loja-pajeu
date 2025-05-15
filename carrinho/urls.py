from django.urls import path
from . import views

app_name = 'carrinho'

urlpatterns = [
    path('', views.detalhe_carrinho, name='detalhe_carrinho'),
    path('adicionar/<int:produto_id>/', views.adicionar_carrinho, name='adicionar_carrinho'),
    path('remover/<int:produto_id>/', views.remover_carrinho, name='remover_carrinho'),
    path('limpar/', views.limpar_carrinho, name='limpar_carrinho'),
    path('atualizar/<int:produto_id>/', views.atualizar_carrinho, name='atualizar_carrinho'),
]