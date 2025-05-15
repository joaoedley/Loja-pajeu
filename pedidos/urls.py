from django.urls import path
from . import views

app_name = 'pedidos'

urlpatterns = [
    path('criar/', views.criar_pedido, name='criar'),
    path('admin/pedido/<int:pedido_id>/', views.admin_pedido_detalhe, name='admin_pedido_detalhe'),
    path('historico/', views.pedido_historico, name='pedido_historico'),
    path('<int:pedido_id>/', views.pedido_detalhe, name='pedido_detalhe'),
    path('<int:pedido_id>/pdf/', views.pedido_pdf, name='pedido_pdf'),
    path('sucesso/', views.pedido_sucesso, name='sucesso'),
]