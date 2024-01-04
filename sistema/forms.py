from typing import Any
from django import forms
from django.contrib.auth.forms import UserCreationForm
from rolepermissions.roles import assign_role
from sistema.models import Funcionario, Usuario
from users.models import CustomUser


class GerenteForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('cpf', )

    def save(self, commit: bool = True) -> Any:
        user = self.save(commit=False)
        assign_role(user, 'gerente')
        return super().save(commit)


class UsuarioForm(UserCreationForm):
    instituicao = forms.CharField(max_length=50, required=True)

    class Meta:
        model = CustomUser
        fields = (
            'full_name', 'cpf', 'nascimento', 'telefone', 'email',
            'instituicao', 'estado', 'cidade', 'rua', 'numero'
        )

    def save(self, commit: bool = ...):
        user = self.save(commit=False)
        usuario = Usuario(user=user, instituicao=self.instituicao.clean)
        usuario.save()

        return super().save(commit=True)


class FuncionarioForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('full_name', 'cpf', 'nascimento', 'telefone',
                  'email', 'estado', 'cidade', 'rua', 'numero')

    def save(self, commit: bool = True):
        user = self.save(commit=False)
        funcionario = Funcionario(user=user)
        funcionario.save()

        return super().save(commit)
