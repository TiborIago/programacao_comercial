from django.db import models
from Home.models import Usuario

class Cliente(models.Model):

    nome = models.CharField(max_length=150, null=False, default='')
    telefone = models.CharField(max_length=15, null=False, default='')
    endereco = models.CharField(max_length=150, null=False, default='')
    pedidos = models.ManyToManyField

class Servico(models.Model):

    tipo = models.CharField(max_length=2, null=True ,default='')
    descricao = models.CharField(max_length=150, null=True , default='')
    preco = models.DecimalField(max_digits=5,decimal_places=2, null=True, default='')
    usuario = models.ForeignKey(Usuario, related_name= 'usuario', on_delete=models.CASCADE)


class Avaliacao(models.Model):

    nota = models.DecimalField(max_digits=5, decimal_places=2, null=False,  default='')
    comentario = models.CharField(max_length=255, null=False, default='')

class Pedidos(models.Model):

    data_pedido = models.DateField(null=False, default='')
    data_atendimento = models.DateField(null=False, default='')
    local_atendimento = models.CharField(max_length=150, null=False, default='')
    cliente = models.ForeignKey(Cliente, related_name = 'cliente_servico', on_delete=models.CASCADE)
    Usuario = models.ForeignKey(Usuario, related_name= 'pedido_atendente', on_delete=models.CASCADE)
    Servico = models.ForeignKey(Servico, related_name= 'pedido_servico', on_delete=models.CASCADE)


