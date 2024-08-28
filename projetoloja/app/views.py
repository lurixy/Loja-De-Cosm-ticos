from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Cliente, Produto, Venda

class IndexView(TemplateView):
    template_name = 'index.html'  # Altere para o nome do seu template

def index(request):
    return render(request, 'index.html')

def cliente_list(request):
    clientes = Cliente.objects.all()
    return render(request, 'cliente_list.html', {'clientes': clientes})

def produto_list(request):
    produtos = Produto.objects.all()
    return render(request, 'produto_list.html', {'produtos': produtos})

def venda_list(request):
    vendas = Venda.objects.all()
    return render(request, 'venda_list.html', {'vendas': vendas})

def lista_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'produtos.html', {'produtos': produtos})

def home(request):
    return render(request, 'home.html')  # Substitua 'home.html' pelo nome do seu template para a página inicial
