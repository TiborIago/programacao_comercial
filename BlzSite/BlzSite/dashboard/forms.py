from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
    
class AlterarSenha(forms.Form):
    
    senha = forms.CharField(required=True)
    senha_confirma = forms.CharField(required=True)
    
    def is_valid(self):
        valid = True

        if not super(AlterarSenha, self).is_valid():
            self.adiciona_erro('Dados incorretos')
            valid = False

        return valid

    def adiciona_erro(self, message):  
        error = self._errors.setdefault(forms.forms.NON_FIELD_ERRORS, forms.utils.ErrorList())
        error.append(message)