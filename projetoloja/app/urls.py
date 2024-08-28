from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Página inicial
    path('clientes/', views.cliente_list, name='cliente_list'),  # Lista de clientes
    path('produtos/', views.lista_produtos, name='lista_produtos'),  # Lista de produtos
    path('vendas/', views.venda_list, name='venda_list'),  # Lista de vendas
]
