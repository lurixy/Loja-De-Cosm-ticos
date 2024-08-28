from django.contrib import admin
from .models import UF, Cidade, Cliente, Fornecedor, CategoriaProduto, Produto, Venda

admin.site.register(UF)
admin.site.register(Cidade)
admin.site.register(Cliente)
admin.site.register(Fornecedor)
admin.site.register(CategoriaProduto)
admin.site.register(Produto)
admin.site.register(Venda)