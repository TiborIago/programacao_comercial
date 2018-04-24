from django.db import models
from Home.models import Usuario

class Pedidos(models.Model):

    data_pedido = models.DateField(null=False)
    data_atendimento = models.DateField(null=False)
    local_atendimento = models.CharField(max_length=150, null=False)
    cliente = models.ForeignKey(Cliente, related_name = 'cliente_servico')
    Usuario = models.ForeignKey(Usuario, related_name= 'pedido_atendente')

class Cliente(models.Model):

    nome = models.CharField(max_length=150, null=False)
    telefone = models.CharField(max_length=15, null=False)
    endereco = models.CharField(max_length=150, null=False)
    
class Servico(models.Model):

    tipo = models.CharField(max_length=2, null=False)
    descricao = models.CharField(max_length=150, null=False)
    preco = models.DecimalField(max_digits=5, decimal_places=2,null=False)

class Avaliacao(models.Model):

    nota = models.DecimalField(max_digits=5, decimal_places=2, null=False)
    comentario = models.CharField(max_length=255, null=False)