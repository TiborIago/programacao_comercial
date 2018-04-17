from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class CadastrarNovoUsuario(forms.Form):

    nome = forms.CharField(required=True)
    usuario = forms.CharField(required=True)
    email = forms.CharField(required=True)
    senha = forms.CharField(required=True)
    usuario_tipo = forms.CharField(required=True)
    telefone = forms.CharField(required=True)

    def is_valid(self):
        valid = True
        if not super(CadastrarNovoUsuario, self).is_valid():
            self.adiciona_erro('Dados incorretos !')
            valid = False
        
        user_exists = User.objects.filter(username=self.data['nome']).exists()

        if user_exists:
            self.adiciona_erro("Usuario ja existe")
            valid = False

        return valid

    def adiciona_erro(self, message):
        error = self._errors.setdefault(forms.forms.NON_FIELD_ERRORS, forms.utils.ErrorList())
        error.append(message)


class LogarBLZ(forms.Form):
    
    usuario = forms.CharField(required=True)
    senha = forms.CharField(required=True)

    def is_valid(self):
        valid = True

        if not super(LogarBLZ, self).is_valid():
            self.adiciona_erro('Dados incorretos')
            valid = False
   
        return valid

    def adiciona_erro(self, message):  
        error = self._errors.setdefault(forms.forms.NON_FIELD_ERRORS, forms.utils.ErrorList())
        error.append(message)

