from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('clientes/', views.cliente_list, name='cliente_list'),
    path('produtos/', views.produto_list, name='produto_list'),
    path('vendas/', views.venda_list, name='venda_list'),
]
