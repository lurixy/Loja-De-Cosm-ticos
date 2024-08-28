from django.db import models

class UF(models.Model):
    sigla = models.CharField(max_length=2)

    class Meta:
        verbose_name_plural = "UF"

    def __str__(self):
        return self.sigla

class Cidade(models.Model):
    nome = models.CharField(max_length=100)
    uf = models.ForeignKey(UF, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Cidades"

    def __str__(self):
        return self.nome

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)
    rg = models.CharField(max_length=9)
    data_nascimento = models.DateField()
    email = models.EmailField()
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Clientes"

    def __str__(self):
        return self.nome

class Fornecedor(models.Model):
    nome = models.CharField(max_length=100)
    contato = models.CharField(max_length=100)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)
    telefone = models.CharField(max_length=15)

    class Meta:
        verbose_name_plural = "Fornecedores"

    def __str__(self):
        return self.nome

class CategoriaProduto(models.Model):
    nome = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Categorias de Produtos"

    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.IntegerField()
    categoria = models.ForeignKey(CategoriaProduto, on_delete=models.CASCADE)
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Produtos"

    def __str__(self):
        return self.nome

class Venda(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)
    data_venda = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Vendas"

    def __str__(self):
        return f"Venda {self.id} - {self.cliente.nome}"
