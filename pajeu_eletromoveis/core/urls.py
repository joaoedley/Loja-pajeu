from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('contato/', views.contato, name='contato'),
    path('login/', views.login_view, name='login'),
    path('registro/', views.registro, name='registro'),
    path('logout/', views.logout_view, name='logout'),
    path('perfil/', views.perfil, name='perfil'),
    path('meus-pedidos/', views.meus_pedidos, name='meus_pedidos'),  # Nova URL
    path('todos-produtos/', views.todos_produtos, name='todos_produtos'),
]