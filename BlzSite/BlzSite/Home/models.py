from django.db import models
from django.contrib.auth.models import User

class Usuario(models.Model):
    nome = models.CharField(max_length=150, null=False)
    telefone = models.CharField(max_length=14, null=False)
    usuario_tipo = models.CharField(max_length=10, null=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="usuario")

    @property
    def email(self):
        return self.user.email
    
    @property
    def nomeusuario(self):
        return self.user.username